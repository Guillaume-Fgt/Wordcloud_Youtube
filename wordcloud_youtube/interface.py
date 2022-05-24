from typing import Callable
import get_subtitles
import generate_wordcloud

interface_input = Callable[[], str]
interface_output = Callable[[str], None]


def CLI_input() -> str:
    url = input("Enter the youtube video URL:")
    return url


def CLI_output(filename: str) -> None:
    print(f"Wordcloud saved as {filename}")


def use_interface(
    interface_input: interface_input, interface_output: interface_output
):  # noqa: E501
    url = interface_input
    # get subtitles of a youtube video from the URL
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
