from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import re


def get_video_id(url: str) -> str:
    """return video id from a youtube URL"""
    id = url.split("=")[-1]
    return id


def download_transcript(video_id: str) -> list[dict]:
    """download subtitles of a youtube video (english)"""
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return transcript


def format_transcript_text(transcript: list[dict]) -> str:
    """convert youtube subtitles format to plain text"""
    formatter = TextFormatter()
    text_formatted = formatter.format_transcript(transcript)
    return text_formatted


def write_to_text_file(text: str, filename: str) -> None:
    """write text to a .txt file"""
    if not re.search(r"^\w+.txt", filename):
        raise ValueError(f"Invalid filename: {filename}.Must finish with .txt")
    with open(filename, "w", encoding="utf-8") as text_file:
        text_file.write(text)
