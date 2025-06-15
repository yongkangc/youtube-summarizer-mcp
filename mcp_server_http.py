#!/usr/bin/env python3

import os
import json
import logging
from urllib.parse import parse_qs
from mcp.server.fastmcp import FastMCP
from main import get_youtube_transcript, extract_video_id
from typing import Any, Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create MCP server with Streamable HTTP support
mcp = FastMCP("YouTube Transcript MCP Server", stateless_http=True)

def parse_config_from_query(query_params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Parse Smithery configuration from query parameters using dot-notation.
    Example: server.host=localhost&server.port=8080&apiKey=secret123
    """
    config = {}
    
    for key, values in query_params.items():
        value = values[0] if isinstance(values, list) else values
        
        # Handle dot-notation (e.g., "server.host" -> {"server": {"host": value}})
        keys = key.split('.')
        current = config
        
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        current[keys[-1]] = value
    
    return config

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
    try:
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
        
        logger.info(f"Successfully processed transcript for URL: {url}")
        return result
        
    except Exception as e:
        logger.error(f"Error getting transcript for {url}: {str(e)}")
        return {
            "success": False,
            "error": str(e),
            "video_id": None,
            "transcript": None
        }

@mcp.tool()
def extract_video_id_tool(url: str) -> Dict[str, Any]:
    """
    Extract YouTube video ID from URL.
    
    Args:
        url: YouTube video URL
        
    Returns:
        Dictionary with success status and video ID
    """
    try:
        video_id = extract_video_id(url)
        if video_id:
            logger.info(f"Successfully extracted video ID: {video_id}")
            return {"success": True, "video_id": video_id, "url": url}
        else:
            logger.warning(f"Failed to extract video ID from URL: {url}")
            return {"success": False, "error": "Invalid YouTube URL format", "url": url}
    except Exception as e:
        logger.error(f"Error extracting video ID from {url}: {str(e)}")
        return {"success": False, "error": str(e), "url": url}

@mcp.resource("youtube://transcript/{video_id}")
def get_transcript_resource(video_id: str) -> str:
    """
    Get transcript as a resource using video ID.
    
    Args:
        video_id: YouTube video ID
        
    Returns:
        Formatted transcript text
    """
    try:
        # Construct YouTube URL from video ID
        url = f"https://www.youtube.com/watch?v={video_id}"
        
        result = get_youtube_transcript(url)
        
        if result['success']:
            return result['transcript']['formatted']
        else:
            return f"Error: {result['error']}"
    except Exception as e:
        logger.error(f"Error getting transcript resource for video ID {video_id}: {str(e)}")
        return f"Error: {str(e)}"

@mcp.resource("youtube://metadata/{video_id}")
def get_transcript_metadata(video_id: str) -> str:
    """
    Get transcript metadata as a resource using video ID.
    
    Args:
        video_id: YouTube video ID
        
    Returns:
        JSON string with transcript metadata
    """
    try:
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
    except Exception as e:
        logger.error(f"Error getting metadata for video ID {video_id}: {str(e)}")
        return json.dumps({"error": str(e)}, indent=2)

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
    # Get port from environment variable (Smithery requirement)
    port = int(os.environ.get("PORT", 8000))
    
    logger.info(f"Starting YouTube Transcript MCP Server on port {port}")
    logger.info("Available tools: get_transcript, extract_video_id_tool")
    logger.info("Available resources: youtube://transcript/{video_id}, youtube://metadata/{video_id}")
    logger.info("Available prompts: analyze_transcript, summarize_transcript")
    logger.info("Server will be accessible at /mcp endpoint (Smithery requirement)")
    
    # Run with Streamable HTTP transport (automatically handles /mcp endpoint)
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port) 