import os

def test_files_exist():
    assert os.path.exists("index.html")
    assert os.path.exists("README.md")
    assert os.path.exists("script.js")
    assert os.path.exists("style.css")

def test_no_empty_files():

    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
        assert len(content.strip()) > 0

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
        assert len(content.strip()) > 0

    with open("script.js", "r", encoding="utf-8") as f:
        content = f.read()
        content = content.replace("alert('Hello World'", "alert('Hello World')")
        assert len(content.strip()) > 0

    with open("style.css", "r", encoding="utf-8") as f:
        content = f.read()
        assert len(content.strip()) > 0