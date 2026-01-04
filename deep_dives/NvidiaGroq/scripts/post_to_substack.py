#!/usr/bin/env python3
"""
Post the Nvidia-Groq article to Substack as a draft.

Usage:
    uvx --from python-substack python post_to_substack.py

Requires environment variables:
    SUBSTACK_EMAIL - Your Substack email
    SUBSTACK_PASSWORD - Your Substack password
    SUBSTACK_PUBLICATION_URL - Your publication URL (e.g., https://yourname.substack.com)
"""

import os
import sys
from pathlib import Path

def load_env():
    """Load .env file from project root."""
    env_path = Path(__file__).parent.parent.parent.parent / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ.setdefault(key.strip(), value.strip())

def main():
    # Load .env file
    load_env()

    try:
        from substack import Api
        from substack.post import Post
    except ImportError:
        print("Error: python-substack not installed.")
        print("Run: uvx --from python-substack python post_to_substack.py")
        sys.exit(1)

    # Get credentials from environment
    email = os.getenv("SUBSTACK_EMAIL")
    password = os.getenv("SUBSTACK_PASSWORD")
    publication_url = os.getenv("SUBSTACK_PUBLICATION_URL")
    cookies_string = os.getenv("SUBSTACK_COOKIES")

    if not cookies_string and (not email or not password):
        print("Error: Missing credentials.")
        print("Set environment variables:")
        print("  SUBSTACK_EMAIL='your_email@example.com'")
        print("  SUBSTACK_PASSWORD='your_password'")
        print("  SUBSTACK_PUBLICATION_URL='https://yourname.substack.com'")
        print()
        print("OR use cookie-based auth (bypasses captcha):")
        print("  SUBSTACK_COOKIES='your_cookie_string'")
        print()
        print("To get cookies: Sign in to Substack in browser, open DevTools (F12),")
        print("go to Network tab, refresh, find any request, right-click -> Copy as cURL,")
        print("and extract the cookie string from the 'cookie:' header.")
        sys.exit(1)

    # Read the article
    script_dir = Path(__file__).parent
    article_path = script_dir.parent / "SUBSTACK_POST.md"

    if not article_path.exists():
        print(f"Error: Article not found at {article_path}")
        sys.exit(1)

    content = article_path.read_text()

    # Extract title from first line (# Title)
    lines = content.split('\n')
    title = lines[0].lstrip('# ').strip()

    # Extract subtitle from italicized line after title
    subtitle = ""
    for line in lines[1:5]:
        if line.startswith('*') and line.endswith('*'):
            subtitle = line.strip('*').strip()
            break

    # Remove title and subtitle from content for body
    body_start = content.find('---')
    if body_start > 0:
        body_content = content[body_start:]
    else:
        body_content = '\n'.join(lines[3:])

    print(f"Title: {title}")
    print(f"Subtitle: {subtitle}")
    print(f"Content length: {len(body_content)} chars")
    print()

    # Authenticate
    print("Authenticating with Substack...")
    if cookies_string:
        print("Using cookie-based authentication...")
        api = Api(
            cookies_string=cookies_string,
            publication_url=publication_url,
        )
    else:
        print("Using email/password authentication...")
        api = Api(
            email=email,
            password=password,
            publication_url=publication_url,
        )

    user_id = api.get_user_id()
    print(f"Authenticated as user ID: {user_id}")

    # Create post
    print("Creating draft post...")
    post = Post(
        title=title,
        subtitle=subtitle,
        user_id=user_id,
        audience="everyone",
        write_comment_permissions="everyone"
    )

    # Convert markdown content to Substack format
    post.from_markdown(body_content, api=api)

    # Create draft (not publish)
    draft = api.post_draft(post.get_draft())
    draft_id = draft.get("id")

    print(f"\nDraft created successfully!")
    print(f"Draft ID: {draft_id}")
    print(f"\nView your draft at: {publication_url}/publish/post/{draft_id}")
    print("\nTo publish, run prepublish and publish manually in Substack dashboard.")

if __name__ == "__main__":
    main()
