import os


def _write_title(writer, title):
    writer.write(f"# {title}" + "\n\n")


def _write_disclaimer(writer):
    writer.write(
        "This md document is generated programatically from https://github.com/gsweene2/garrett-learns-python/blob/master/convert-to-md.py\n\n"
    )


with open(
    "/Users/garrettsweeney/git/garrett-mkdocs/docs/python.md", "w", newline=""
) as writer:
    _write_title(writer, "Python")
    _write_disclaimer(writer)

    close_code = False

    with open("pytest_python_utilities.py") as reader:
        for line in reader.readlines():
            if '"""' in line:
                if close_code:
                    writer.write("```\n")
                # Clean the line of python comment
                cleaned_line = line.replace('"', "").strip()
                # Write the cleaned line
                if "Test" in cleaned_line:
                    writer.write("### " + cleaned_line + "\n")
                else:
                    writer.write("## " + cleaned_line + "\n")
                # Code block for code-to-follow
                writer.write("```python")
                close_code = True
            else:
                writer.write(line)
        writer.write("```\n")
