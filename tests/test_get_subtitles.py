import os
from wordcloud_youtube.get_subtitles import (
    download_transcript,
    format_transcript_text,
    write_to_text_file,
    get_video_id,
)
from youtube_transcript_api import TranscriptsDisabled
import pytest

# Pj-h6MEgE7I valid URL
# S1ZOW6HVLJ0 no subtitles URL


def test_get_video_id() -> None:
    id = get_video_id("https://www.youtube.com/watch?v=Pj-h6MEgE7I")
    assert id == "Pj-h6MEgE7I"


def test_download_transcript_invalid() -> None:
    """Should raise custom error if video id is invalid or subtitles disabled for
    the video"""
    invalid_id = "12345"
    with pytest.raises(TranscriptsDisabled):
        download_transcript(invalid_id)


def test_download_transcript_valid() -> None:
    """test if a valid video id with subtitles returns a list"""
    valid_id = "Pj-h6MEgE7I"
    assert type(download_transcript(valid_id) is list)


def test_format_transcript_text() -> None:
    """test if only text is returned when providing a dict with different
    keys"""
    transcript = [
        {"text": "Hey there", "start": 7.58, "duration": 6.13},
    ]
    text_formatted = format_transcript_text(transcript)
    assert text_formatted == "Hey there"


def test_write_to_text_file() -> None:
    text = "test"
    filename = "test.txt"
    write_to_text_file(text, filename)
    with open(filename) as text_file:
        assert text_file.read() == "test"
    os.remove(filename)


def test_write_to_text_file_extension() -> None:
    """test if a wrong file extension is provided"""
    text = "test"
    filename = "test.json"
    with pytest.raises(ValueError):
        write_to_text_file(text, filename)
