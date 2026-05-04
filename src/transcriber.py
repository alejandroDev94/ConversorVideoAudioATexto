import whisper

def audio_to_text(audio_path):
    """
    Transcribe audio file to text using Whisper.

    :param audio_path: Path to the input audio file.
    :return: Transcribed text.
    """
    model = whisper.load_model("base")  # You can choose 'tiny', 'base', 'small', 'medium', 'large'
    result = model.transcribe(audio_path)
    return result["text"]
