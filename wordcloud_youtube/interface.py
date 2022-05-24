import re
from typing import Callable
import get_subtitles
import generate_wordcloud
import streamlit as st
import sys
from streamlit import cli as stcli


interface_input = Callable[[], str]
interface_output = Callable[[str], None]


def CLI_input() -> str:
    url = input("Enter the youtube video URL:")
    while not re.search(r"^https:.+=.{3,}$", url):
        url = input("Enter the youtube video URL:")
    return url


def CLI_output(filename: str) -> None:
    print(f"Wordcloud saved as {filename}")


def streamlit_input() -> str:
    if st._is_running_with_streamlit:
        st.title("Generate a Wordcloud from a youtube video")
        url = st.text_input("Enter the youtube video URL")
        if not re.search(r"^https:.+=.{3,}$", url):
            st.write("Enter a youtube video URL")
        else:
            st.write("Processing")
            return url
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())


def streamlit_output(filename: str) -> None:
    st.write(f"Done. Wordcloud saved as {filename}")
    st.image(filename)


def use_interface(
    interface_input: interface_input, interface_output: interface_output
):  # noqa: E501
    url = interface_input()
    # get subtitles of a youtube video from the URL
    if not url:
        return
    video_id = get_subtitles.get_video_id(url)
    transcript = get_subtitles.download_transcript(video_id)
    formatted_text = get_subtitles.format_transcript_text(transcript)
    filename = "transcript.txt"
    get_subtitles.write_to_text_file(formatted_text, filename)

    # generate the wordcloud
    text = generate_wordcloud.read_sub_file(filename)
    mask = generate_wordcloud.read_mask_image("thumbnail.png")
    wordcloud = generate_wordcloud.generate_wordcloud(text, mask=mask)
    image_output = "transcript_wordcloud.png"
    generate_wordcloud.save_wordcloud(wordcloud, image_output)
    interface_output(image_output)
