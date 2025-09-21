import re
import sys
from typing import Optional, List, Dict, Any
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


def extract_video_id(url: str) -> Optional[str]:
    """
    Extract YouTube video ID from various YouTube URL formats.
    
    Args:
        url: YouTube URL in various formats
        
    Returns:
        Video ID string or None if not found
    """
    patterns = [
        r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([^&\n?#]+)',
        r'(?:https?://)?(?:www\.)?youtube\.com/embed/([^&\n?#]+)',
        r'(?:https?://)?(?:www\.)?youtube\.com/v/([^&\n?#]+)',
        r'(?:https?://)?youtu\.be/([^&\n?#]+)',
        r'(?:https?://)?(?:www\.)?youtube\.com/watch\?.*v=([^&\n?#]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None


def get_youtube_transcript(url: str, languages: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Get transcript from YouTube video URL.
    
    Args:
        url: YouTube video URL
        languages: List of preferred languages (default: ['en'])
        
    Returns:
        Dictionary containing transcript data and metadata
    """
    if languages is None:
        languages = ['en']
    
    try:
        # Extract video ID
        video_id = extract_video_id(url)
        if not video_id:
            return {
                'success': False,
                'error': 'Invalid YouTube URL format',
                'video_id': None,
                'transcript': None
            }
        
        # Get transcript
        api = YouTubeTranscriptApi()
        fetched_transcript = api.fetch(
            video_id, 
            languages=languages
        )
        
        # Convert to list of dictionaries
        transcript_list = fetched_transcript.to_raw_data()
        
        # Format transcript - create simple text version
        formatted_transcript = '\n'.join([entry['text'] for entry in transcript_list])
        
        # Also provide structured data
        structured_transcript = []
        for entry in transcript_list:
            structured_transcript.append({
                'text': entry.get('text', ''),
                'start': entry.get('start', 0),
                'duration': entry.get('duration', 0)
            })
        
        return {
            'success': True,
            'video_id': video_id,
            'video_url': url,
            'transcript': {
                'formatted': formatted_transcript,
                'structured': structured_transcript,
                'total_segments': len(transcript_list)
            },
            'languages_used': languages,
            'error': None
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'video_id': video_id if 'video_id' in locals() else None,
            'transcript': None
        }


def main():
    """Main function for testing the transcript fetcher."""
    if len(sys.argv) != 2:
        print("Usage: python main.py <youtube_url>", file=sys.stderr)
        print("Example: python main.py 'https://www.youtube.com/watch?v=LBn0eAxQpb8'", file=sys.stderr)
        sys.exit(1)
    
    url = sys.argv[1]
    
    result = get_youtube_transcript(url)
    
    if result['success']:
        # Output full transcript without any decorations for easy clipboard copying
        print(result['transcript']['formatted'])
    else:
        print(f"Error: {result['error']}", file=sys.stderr)
        if result['video_id']:
            print(f"Video ID extracted: {result['video_id']}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
