import yt_dlp
import os
from datetime import datetime
from urllib.parse import urlparse

def download_video(url):
    """
    Download video from URL and return the local file path.
    Videos are saved in mp4/[domain]/[YYYYMMDD]/ directory.
    """
    try:
        # Extract domain from URL
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.replace('www.', '')

        # Get current date in YYYYMMDD format
        date_str = datetime.now().strftime('%Y%m%d')

        # Create output directory structure: mp4/[domain]/[YYYYMMDD]/
        output_dir = os.path.join('mp4', domain, date_str)
        os.makedirs(output_dir, exist_ok=True)

        ydl_opts = {
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
            'format': 'best',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info)
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None