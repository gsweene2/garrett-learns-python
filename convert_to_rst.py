with open(
    "/Users/garrettsweeney/git/garrett-docs/languages/python.rst", "w", newline=""
) as writer:
    # Write Python rst header
    writer.write("Python\n======\n.. meta::\n   :description lang=en: Python docs\n\n")
    # Note about programatic generation
    writer.write(".. warning::\n\n")
    writer.write(
        "    This rst document is generated programatically from https://github.com/gsweene2/garrett-learns-python/blob/master/pytest_python_utilities.py\n\n"
    )
    # Write description and prepare code block for import lines to follow
    writer.write(
        "Import statements for all examples\n\n.. code-block:: python\n  :linenos:\n\n"
    )

    with open("pytest_python_utilities.py") as reader:
        for line in reader.readlines():
            if '"""' in line:
                # Clean the line of python comment
                cleaned_line = line.replace('"', "").strip()
                # Write the cleaned line
                writer.write("\n" + cleaned_line + "\n")
                """
                If the cleaned line does not include 'test'
                - write the cleaned line as a header
                - add Example subneader underneath
                else
                - write the cleaned line as a subheader
                """
                writer.write(
                    "-" * len(cleaned_line) + "\nExample\n" + "*" * len("Example")
                ) if "test" not in cleaned_line.lower() else writer.write(
                    "*" * len(cleaned_line)
                )
                # Code block for code-to-follow
                writer.write("\n.. code-block:: python\n  :linenos:\n")
            else:
                writer.write("  " + line)
