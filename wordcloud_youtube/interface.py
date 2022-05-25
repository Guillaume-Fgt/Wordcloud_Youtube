import re
from typing import Callable
import streamlit as st
import sys
from streamlit import cli as stcli


interface_input = Callable[[], str]
interface_output = Callable[[str], None]


def CLI_input() -> str:
    """Implement Command Line Interface Input"""
    url = input("Enter the youtube video URL:")
    while not re.search(r"^https:.+=.{3,}$", url):
        url = input("Enter the youtube video URL:")
    return url


def CLI_output(filename: str) -> None:
    """Implement Command Line Interface Output"""
    print(f"Wordcloud saved as {filename}")


def streamlit_input() -> str:
    """Implement Streamlit Interface Input"""
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
    """Implement Streamlit Interface Output"""
    st.write(f"Done. Wordcloud saved as {filename}")
    st.image(filename)
