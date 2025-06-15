#!/usr/bin/env python3

from main import get_youtube_transcript
import sys

if len(sys.argv) != 2:
    print("Usage: python get_full_transcript.py <youtube_url>")
    sys.exit(1)

url = sys.argv[1]
result = get_youtube_transcript(url)

if result['success']:
    print('Full Transcript:')
    print('=' * 50)
    print(result['transcript']['formatted'])
    print('=' * 50)
    print(f"Total segments: {result['transcript']['total_segments']}")
else:
    print('Error:', result['error']) 