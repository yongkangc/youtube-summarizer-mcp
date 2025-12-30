#!/usr/bin/env python3

from mcp.server.fastmcp import FastMCP
from mcp.server.models import InitializationOptions
import mcp.types as types
from main import get_youtube_transcript, extract_video_id
from typing import Any, Dict
from pathlib import Path
import subprocess
import os
import re

# Create MCP server
mcp = FastMCP("YouTube Transcript MCP Server")

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.resolve()
PROMPTS_DIR = SCRIPT_DIR / "prompts"
SUMMARIES_DIR = SCRIPT_DIR / "summaries"

def _load_summarize_prompt() -> str:
    """Load the summarize prompt template from file."""
    prompt_file = PROMPTS_DIR / "summarize_prompt.md"
    if prompt_file.exists():
        return prompt_file.read_text()
    return "Please provide a comprehensive summary of this video transcript."


def _run_claude_cli(prompt: str, input_text: str) -> str:
    """Run claude CLI with the given prompt and input text."""
    result = subprocess.run(
        ["claude", "-p", prompt],
        input=input_text,
        capture_output=True,
        text=True,
        timeout=120
    )
    if result.returncode != 0:
        raise RuntimeError(f"Claude CLI failed: {result.stderr}")
    return result.stdout.strip()


def _generate_filename(summary: str) -> str:
    """Generate a clean filename from the summary using Claude CLI."""
    prompt = (
        "Based on this video summary, generate a concise, descriptive filename "
        "(without .md extension). Use lowercase letters, numbers, and underscores only. "
        "Make it descriptive but not too long (max 60 chars). Only output the filename, nothing else."
    )
    filename = _run_claude_cli(prompt, summary)
    # Clean the filename: only allow lowercase, numbers, underscores
    filename = re.sub(r'[^a-z0-9_]', '_', filename.lower())
    filename = re.sub(r'_+', '_', filename)  # collapse multiple underscores
    filename = filename.strip('_')
    return f"{filename}.md"


def _classify_category(summary: str) -> str:
    """Classify the summary into a category using Claude CLI."""
    prompt = (
        "Based on this video summary, classify it into exactly ONE of these categories: "
        "ai, trading, self-help, career, programming. Only output the single category word, nothing else."
    )
    category = _run_claude_cli(prompt, summary).lower().strip()

    # Validate category
    valid_categories = {"ai", "trading", "self-help", "career", "programming"}
    if category not in valid_categories:
        category = "misc"
    return category


def _extract_title(summary: str) -> str:
    """Extract title from summary (first markdown header)."""
    for line in summary.split('\n'):
        if line.startswith('#'):
            # Remove # prefix and strip
            return line.lstrip('#').strip()
    return "Video Summary"


def _git_push_summary(category: str, filename: str, title: str) -> str:
    """Commit and push the summary to git, return GitHub URL."""
    # Change to summaries directory
    os.chdir(SUMMARIES_DIR)

    # Git operations
    file_path = f"{category}/{filename}"
    subprocess.run(["git", "add", file_path], check=True)
    subprocess.run(["git", "commit", "-m", f"Add summary: {title}"], check=True)
    subprocess.run(["git", "pull", "--rebase"], check=True)
    subprocess.run(["git", "push"], check=True)

    # Generate GitHub URL
    result = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        capture_output=True, text=True, check=True
    )
    remote_url = result.stdout.strip()

    # Extract owner/repo from git URL (handles both SSH and HTTPS)
    match = re.search(r'github\.com[:/](.+?)(?:\.git)?$', remote_url)
    repo_path = match.group(1) if match else remote_url

    result = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        capture_output=True, text=True, check=True
    )
    branch = result.stdout.strip()

    return f"https://github.com/{repo_path}/blob/{branch}/summaries/{category}/{filename}"


@mcp.tool()
def get_transcript_for_summary(url: str) -> Dict[str, Any]:
    """
    Get transcript and prompt template for summarizing a YouTube video.

    Use this tool to fetch a video transcript along with the summarization prompt.
    After receiving the response, generate a comprehensive summary following the prompt,
    then call publish_summary with the result.

    Args:
        url: YouTube video URL

    Returns:
        Dictionary containing transcript, prompt template, and video URL
    """
    # Get transcript
    result = get_youtube_transcript(url)

    if not result.get('success'):
        return {
            "success": False,
            "error": result.get('error', 'Failed to fetch transcript'),
            "video_url": url
        }

    # Load prompt template
    prompt = _load_summarize_prompt()

    return {
        "success": True,
        "video_url": url,
        "transcript": result['transcript']['formatted'],
        "prompt": prompt,
        "instructions": (
            "Please generate a comprehensive summary following the prompt template above. "
            "After generating the summary, call publish_summary with the summary content and video URL."
        )
    }


@mcp.tool()
def publish_summary(summary: str, video_url: str) -> Dict[str, Any]:
    """
    Publish a video summary to GitHub.

    This tool takes a generated summary, classifies it, generates a filename,
    saves it to the appropriate category folder, and pushes to GitHub.

    Args:
        summary: The generated summary content (markdown format)
        video_url: The original YouTube video URL

    Returns:
        Dictionary with GitHub URL, filename, and category
    """
    try:
        # Generate filename using Claude CLI
        filename = _generate_filename(summary)

        # Classify category using Claude CLI
        category = _classify_category(summary)

        # Extract title for commit message
        title = _extract_title(summary)

        # Create category directory if needed
        category_dir = SUMMARIES_DIR / category
        category_dir.mkdir(parents=True, exist_ok=True)

        # Save summary to file
        file_path = category_dir / filename
        file_path.write_text(summary)

        # Git commit and push
        github_url = _git_push_summary(category, filename, title)

        return {
            "success": True,
            "github_url": github_url,
            "filename": filename,
            "category": category,
            "file_path": str(file_path)
        }
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "Claude CLI timed out"
        }
    except subprocess.CalledProcessError as e:
        return {
            "success": False,
            "error": f"Git operation failed: {e}"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


@mcp.tool()
def get_transcript(url: str, languages: str = "en", include_timestamps: bool = True) -> Dict[str, Any]:
    """
    Get transcript from YouTube video URL.
    
    Args:
        url: YouTube video URL
        languages: Comma-separated list of preferred languages (default: "en")
        include_timestamps: Whether to include timing information
    
    Returns:
        Dictionary containing transcript data and metadata
    """
    # Convert comma-separated languages to list
    languages_list = [lang.strip() for lang in languages.split(',') if lang.strip()]
    
    # Get transcript using our main function
    result = get_youtube_transcript(url, languages_list)
    
    # If timestamps not requested, remove them from structured data
    if not include_timestamps and result.get('success'):
        if result['transcript'] and result['transcript'].get('structured'):
            for segment in result['transcript']['structured']:
                segment.pop('start', None)
                segment.pop('duration', None)
    
    return result

@mcp.tool()
def extract_video_id_tool(url: str) -> Dict[str, Any]:
    """
    Extract YouTube video ID from URL.
    
    Args:
        url: YouTube video URL
        
    Returns:
        Dictionary with success status and video ID
    """
    video_id = extract_video_id(url)
    if video_id:
        return {"success": True, "video_id": video_id, "url": url}
    else:
        return {"success": False, "error": "Invalid YouTube URL format", "url": url}

@mcp.resource("youtube://transcript/{video_id}")
def get_transcript_resource(video_id: str) -> str:
    """
    Get transcript as a resource using video ID.
    
    Args:
        video_id: YouTube video ID
        
    Returns:
        Formatted transcript text
    """
    # Construct YouTube URL from video ID
    url = f"https://www.youtube.com/watch?v={video_id}"
    
    result = get_youtube_transcript(url)
    
    if result['success']:
        return result['transcript']['formatted']
    else:
        return f"Error: {result['error']}"

@mcp.resource("youtube://metadata/{video_id}")
def get_transcript_metadata(video_id: str) -> str:
    """
    Get transcript metadata as a resource using video ID.
    
    Args:
        video_id: YouTube video ID
        
    Returns:
        JSON string with transcript metadata
    """
    import json
    
    # Construct YouTube URL from video ID
    url = f"https://www.youtube.com/watch?v={video_id}"
    
    result = get_youtube_transcript(url)
    
    if result['success']:
        metadata = {
            "video_id": result['video_id'],
            "video_url": result['video_url'],
            "total_segments": result['transcript']['total_segments'],
            "languages_used": result['languages_used']
        }
        return json.dumps(metadata, indent=2)
    else:
        return json.dumps({"error": result['error']}, indent=2)

@mcp.prompt()
def analyze_transcript(video_url: str) -> str:
    """
    Create a prompt for analyzing YouTube video transcript.
    
    Args:
        video_url: YouTube video URL
        
    Returns:
        Formatted prompt for transcript analysis
    """
    return f"""Please analyze the transcript from this YouTube video: {video_url}

Use the get_transcript tool to fetch the video transcript, then provide:

1. **Summary**: A brief overview of the main topics discussed
2. **Key Points**: The most important information or insights
3. **Themes**: Major themes or subjects covered
4. **Structure**: How the content is organized
5. **Notable Quotes**: Any particularly interesting or important statements

Please be thorough and provide actionable insights from the transcript."""

@mcp.prompt()
def summarize_transcript(video_url: str, length: str = "medium") -> str:
    """
    Create a prompt for summarizing YouTube video transcript.
    
    Args:
        video_url: YouTube video URL
        length: Summary length (short, medium, long)
        
    Returns:
        Formatted prompt for transcript summarization
    """
    length_instructions = {
        "short": "Provide a concise 2-3 sentence summary.",
        "medium": "Provide a comprehensive paragraph summary (4-6 sentences).",
        "long": "Provide a detailed summary with multiple paragraphs covering all major points."
    }
    
    instruction = length_instructions.get(length, length_instructions["medium"])
    
    return f"""Please summarize the transcript from this YouTube video: {video_url}

Use the get_transcript tool to fetch the video transcript, then {instruction}

Focus on:
- Main topic and purpose of the video
- Key insights or information presented
- Important conclusions or takeaways
- Any actionable advice or recommendations

Make the summary clear, engaging, and useful for someone who hasn't watched the video."""

if __name__ == "__main__":
    mcp.run() 