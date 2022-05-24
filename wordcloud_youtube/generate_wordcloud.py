import numpy as np
from PIL import Image
from wordcloud import STOPWORDS
from wordcloud import WordCloud
import re


def read_sub_file(path: str) -> str:
    """open a text file and return its text"""
    with open(path) as subtitle:
        text = subtitle.read()
    return text


def read_mask_image(path: str) -> np.ndarray:
    """open an image and return it as a numpy array"""
    with Image.open(path) as image:
        mask = np.array(image)
    return mask


def generate_stopwords_set(path: str) -> set[str]:
    """add words contained in a text file to default wordcloud stopwords"""
    with open(path) as file:
        stop_words = set(STOPWORDS)
        stop_words.update(file.read().splitlines())
    return stop_words


def generate_wordcloud(
    text: str, stopwords: set[str] = None, mask: np.ndarray = None
) -> WordCloud:
    """generate a wordcloud from a text"""
    wordcloud = WordCloud(
        stopwords=stopwords,
        max_words=200,
        color_func=lambda *args, **kwargs: (255, 255, 255),
        mask=mask,
        include_numbers=True,
    ).generate(text)
    return wordcloud


def save_wordcloud(wordcloud: WordCloud, filename: str) -> None:
    """save the wordcloud to image file"""
    if not (
        re.search(r"^\w+.jpg", filename) or re.search(r"^\w+.png", filename)
    ):  # noqa: E501
        raise ValueError(
            f"Invalid filename: {filename} must finish with .jpg or .png"
        )  # noqa: E501
    wordcloud.to_file(filename)
