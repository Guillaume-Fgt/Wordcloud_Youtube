import get_subtitles
import generate_wordcloud


def main():

    # get subtitles from the video id
    transcript = get_subtitles.download_transcript("Pj-h6MEgE7I")
    formatted_text = get_subtitles.format_transcript_text(transcript)
    filename = "transcript.txt"
    get_subtitles.write_to_text_file(formatted_text, filename)

    # generate the wordcloud
    text = generate_wordcloud.read_sub_file(filename)
    wordcloud = generate_wordcloud.generate_wordcloud(text)
    generate_wordcloud.save_wordcloud(wordcloud)


if __name__ == "__main__":
    main()
