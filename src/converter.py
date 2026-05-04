from moviepy import VideoFileClip
import os

def video_to_audio(video_path, audio_path=None):
    """
    Extract audio from a video file and save it as an audio file.

    :param video_path: Path to the input video file.
    :param audio_path: Path to save the output audio file. If None, uses video_path with .wav extension.
    :return: Path to the output audio file.
    """
    if audio_path is None:
        base, _ = os.path.splitext(video_path)
        audio_path = base + '.wav'

    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)
    video.close()

    return audio_path
