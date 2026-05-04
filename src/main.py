import argparse
from converter import video_to_audio
from transcriber import audio_to_text
import os
import sys
from downloaderVideo import download_video
from utils import is_url


def main():
    parser = argparse.ArgumentParser(description="Convert video to audio and transcribe to text.")
    parser.add_argument("video_path", help="Path to the input video file or URL.")
    args = parser.parse_args()

    video_path = args.video_path

    # Check if it's a URL
    if is_url(video_path):
        print("Downloading video from URL...")
        downloaded_path = download_video(video_path)
        if downloaded_path is None:
            return
        video_path = downloaded_path

    if not os.path.exists(video_path):
        print(f"Error: Video file '{video_path}' does not exist.")
        return

    print("Converting video to audio...")
    try:
        audio_path = video_to_audio(video_path)
    except Exception as e:
        print(f"Error converting video to audio: {e}")
        return

    print("Transcribing audio to text...")
    try:
        text = audio_to_text(audio_path)
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        print("\nFFmpeg is required for audio processing.")
        print("Run: python install_dependencies.py")
        return

    print("Transcription:")
    print(text)

    # Optionally, save text to file
    text_path = os.path.splitext(video_path)[0] + '.txt'
    with open(text_path, 'w') as f:
        f.write(text)
    print(f"Text saved to {text_path}")

if __name__ == "__main__":
    main()
