from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import re


def download_transcript(video_id: str) -> list[dict]:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return transcript


def format_transcript_text(transcript: list[dict]) -> str:
    formatter = TextFormatter()
    text_formatted = formatter.format_transcript(transcript)
    return text_formatted


def write_to_text_file(text: str, filename: str) -> None:
    if not re.search(r"^\w+.txt", filename):
        raise ValueError(f"Invalid filename: {filename}.Must finish with .txt")
    with open(filename, "w", encoding="utf-8") as text_file:
        text_file.write(text)
