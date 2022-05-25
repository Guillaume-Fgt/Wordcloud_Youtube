from wordcloud_youtube.interface import CLI_input, CLI_output
from pytest import MonkeyPatch


def test_CLI_input(monkeypatch: MonkeyPatch) -> None:
    """test with incorrect first input and correct second one"""
    inputs = ["aaa", "https://www.youtube.com/watch?v=Pj-h6MEgE7I"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    url = CLI_input()
    assert url == "https://www.youtube.com/watch?v=Pj-h6MEgE7I"


def test_CLI_output(capsys) -> None:
    CLI_output("testfile.png")
    captured = capsys.readouterr()
    assert captured.out == "Wordcloud saved as testfile.png\n"
