# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Model Context Protocol (MCP) server that fetches YouTube video transcripts and provides summarization capabilities. It can run as an MCP server (for AI assistants), a FastAPI HTTP server, or be used via command-line scripts.

## Development Commands

### Setup
```bash
# Install dependencies using uv
uv sync
```

### Testing & Development
```bash
# Test basic transcript fetcher (prints transcript to stdout)
uv run python main.py "https://www.youtube.com/watch?v=VIDEO_ID"

# Run MCP server in development mode
uv run mcp dev mcp_server.py

# Run FastAPI server with hot reload
uv run uvicorn api_server:app --reload
```

### CLI Scripts
```bash
# Fetch transcript and copy to clipboard (macOS/Linux)
./scripts/yt "https://www.youtube.com/watch?v=VIDEO_ID"

# Fetch transcript and generate AI summary (requires Claude CLI)
./scripts/yt-summarize "https://www.youtube.com/watch?v=VIDEO_ID"
```

## Architecture

### Core Components

**main.py** - Core transcript fetching logic
- `extract_video_id()`: Extracts video ID from various YouTube URL formats
- `get_youtube_transcript()`: Fetches transcript using youtube-transcript-api, returns structured data with both formatted text and timestamped segments

**mcp_server.py** - MCP server implementation using FastMCP
- Tools: `get_transcript`, `extract_video_id_tool`
- Resources: `youtube://transcript/{video_id}`, `youtube://metadata/{video_id}`
- Prompts: `analyze_transcript`, `summarize_transcript`

**scripts/** - Bash utilities
- `yt`: Cross-platform script that fetches transcript and copies to clipboard (handles dependency installation)
- `yt-summarize`: Fetches transcript and generates AI summary using Claude CLI

### Data Flow

1. YouTube URL → `extract_video_id()` → Video ID
2. Video ID → `YouTubeTranscriptApi.fetch()` → Raw transcript segments
3. Raw segments → Processing → Both formatted text (plain) and structured data (with timestamps)
4. Output via MCP tools/resources, HTTP API, or CLI scripts

### MCP Protocol Support

The server implements three MCP primitives:
- **Tools**: Function calls for fetching transcripts
- **Resources**: URI-based access to transcript content
- **Prompts**: Pre-configured analysis/summary templates

## Key Implementation Details

### URL Pattern Matching
The `extract_video_id()` function handles multiple YouTube URL formats:
- `youtube.com/watch?v=...`
- `youtu.be/...`
- `youtube.com/embed/...`
- `youtube.com/v/...`

### Transcript Data Structure
Transcripts are returned with two formats:
- `formatted`: Plain text, one line per segment
- `structured`: Array of objects with `text`, `start`, `duration` fields

### Language Support
Default language is English (`en`), but supports comma-separated language codes for fallback (e.g., `"en,es,fr"`).

## Deployment

### Local Development
Uses `uv` for Python dependency management (pyproject.toml).

### Smithery Deployment
Configured via `smithery.yaml`:
- Docker container runtime
- HTTP-based MCP protocol
- Configurable rate limiting and default settings
- See smithery.yaml for full schema

## Dependencies

Core dependencies (from pyproject.toml):
- youtube-transcript-api (≥1.1.0) - Transcript fetching
- fastmcp (≥2.8.0) - MCP server framework
- fastapi (≥0.115.12) + uvicorn - HTTP API server
- Python ≥3.11 required

## Summaries Directory

The `summaries/` directory contains saved video summaries generated using the `yt-summarize` script. Summaries follow a structured format defined in `prompts/summarize_prompt.md`.
