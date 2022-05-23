import numpy as np
from wordcloud import WordCloud
from wordcloud_youtube.generate_wordcloud import (
    read_sub_file,
    read_mask_image,
    generate_stopwords_set,
    generate_wordcloud,
    save_wordcloud,
)
import pytest
import os
from PIL import Image


@pytest.fixture
def textfile():
    file = "test.txt"
    with open(file, "w", encoding="utf-8") as text_file:
        text_file.write("test")
    yield file
    os.remove(file)


def test_read_sub_file(textfile) -> None:
    assert read_sub_file(textfile) == "test"


@pytest.fixture
def create_image():
    image_file = "test.jpg"
    matrix = np.array([[255] * 50 for _ in range(8)], dtype="uint8")
    im = Image.fromarray(matrix, mode="L")
    im.save(image_file)
    yield image_file
    os.remove(image_file)


def test_read_mask_image(create_image) -> None:
    mask = read_mask_image(create_image)
    assert type(mask) is np.ndarray


@pytest.fixture
def stopwordsfile():
    file = "stopwords.txt"
    with open(file, "w", encoding="utf-8") as stopwords_file:
        stopwords_file.write("test")
    yield file
    os.remove(file)


def test_generate_stopwords_set(stopwordsfile) -> None:
    stopwords_set = generate_stopwords_set(stopwordsfile)
    assert "test" in stopwords_set


def test_generate_wordcloud(textfile) -> None:
    text = read_sub_file(textfile)
    wordcloud = generate_wordcloud(text)
    assert type(wordcloud) is WordCloud


def test_generate_wordcloud_allwordstopped(textfile, stopwordsfile) -> None:
    """provide a stopword list containing all the words of the text file"""
    text = read_sub_file(textfile)
    stopwords = generate_stopwords_set(stopwordsfile)
    with pytest.raises(ValueError):
        generate_wordcloud(text, stopwords)


def test_save_wordcloud(textfile) -> None:
    text = read_sub_file(textfile)
    wordcloud = generate_wordcloud(text)
    save_wordcloud(wordcloud)
    assert os.path.isfile("transcript_wordcloud.png")
