import get_subtitles
import generate_wordcloud


def main():

    # get subtitles of a youtube video from the URL
    video_id = get_subtitles.get_video_id(
        "https://www.youtube.com/watch?v=Pj-h6MEgE7I"
    )  # noqa: E501
    transcript = get_subtitles.download_transcript(video_id)
    formatted_text = get_subtitles.format_transcript_text(transcript)
    filename = "transcript.txt"
    get_subtitles.write_to_text_file(formatted_text, filename)

    # generate the wordcloud
    text = generate_wordcloud.read_sub_file(filename)
    mask = generate_wordcloud.read_mask_image("thumbnail.png")
    wordcloud = generate_wordcloud.generate_wordcloud(text, mask=mask)
    generate_wordcloud.save_wordcloud(wordcloud, "transcript_wordcloud.png")


if __name__ == "__main__":
    main()
