Wordcloud Youtube creates a wordcloud of a youtube video based on the subtitles (english ones).
You will have to provide a URL of the video and it will create a png file, using a youtube logo as canvas.

Two interfaces are avalaible: CLI (Command Line Interface) and Streamlit. To change which one the program uses, you have to edit the main function in main.py. CLI_input/CLI_output or streamlit_input/streamlit_output.
With the streamlit version, you will have a direct vizualisation of the wordcloud generated.


install using poetry:
`poetry install`


run:
`python -m wordcloud_youtube.main`


run tests:
`coverage -m run pytest`

Example of a generated wordcloud:
![transcript_wordcloud](https://user-images.githubusercontent.com/66461774/170279073-c557ce92-fbe8-42eb-ab80-b563cd2ba7bd.png)
