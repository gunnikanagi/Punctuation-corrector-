def fix_spaces(text):

    text = text.replace(" ,", ",")
    text = text.replace(" .", ".")
    text = text.replace(" !", "!")
    text = text.replace(" ?", "?")

    while "  " in text:
        text = text.replace("  ", " ")

    return text


def fix_punctuation(text):

    text = fix_spaces(text)

    new_text = ""

    for i in range(len(text)):
        new_text = new_text + text[i]

        if text[i] == "," or text[i] == "." or text[i] == "!" or text[i] == "?":
            if i + 1 < len(text):
                if text[i + 1] != " " and text[i + 1] != "." and text[i + 1] != "," and text[i + 1] != "!" and text[i + 1] != "?":
                    new_text = new_text + " "

    return new_text.strip()


def remove_extra_marks(text):

    new_text = ""

    for letter in text:

        if new_text != "":
            if letter == new_text[-1]:
                if letter == "." or letter == "!" or letter == "?":
                    continue

        new_text = new_text + letter

    return new_text


def add_full_stop(text):

    if text != "":
        last = text[-1]

        if last != "." and last != "!" and last != "?":
            text = text + "."

    return text
