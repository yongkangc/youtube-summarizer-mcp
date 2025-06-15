#!/usr/bin/env python3

import requests
import json

def test_mcp_server():
    """Test the MCP server with the YouTube URL"""
    url = 'http://localhost:8000/mcp'
    payload = {
        'jsonrpc': '2.0',
        'id': 1,
        'method': 'tools/call',
        'params': {
            'name': 'get_transcript',
            'arguments': {
                'url': 'https://www.youtube.com/watch?v=NLBXgSmRBgU&ab_channel=neurotrader'
            }
        }
    }

    try:
        print("Testing MCP server with YouTube URL...")
        response = requests.post(url, json=payload, timeout=30)
        print(f'Status: {response.status_code}')
        
        if response.status_code == 200:
            result = response.json()
            print(f'Response: {json.dumps(result, indent=2)}')
            
            # Check if we got a successful transcript
            if 'result' in result and 'content' in result['result']:
                content = result['result']['content'][0]
                if 'text' in content:
                    data = json.loads(content['text'])
                    if data.get('success'):
                        print(f"\n✅ SUCCESS! Got transcript for video: {data.get('video_id')}")
                        print(f"Total segments: {data['transcript']['total_segments']}")
                        print(f"Languages used: {data['languages_used']}")
                        print(f"First few words: {data['transcript']['formatted'][:100]}...")
                    else:
                        print(f"\n❌ FAILED: {data.get('error')}")
        else:
            print(f'Error response: {response.text}')
            
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    test_mcp_server() 