import interface
import get_subtitles
import generate_wordcloud


def use_interface(
    interface_input: interface.interface_input,
    interface_output: interface.interface_output,
):  # noqa: E501
    """Define how a generic interface must be used"""
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


def main() -> None:
    use_interface(interface.streamlit_input, interface.streamlit_output)  # noqa: E501


if __name__ == "__main__":
    main()
