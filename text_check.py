def capitalize_text(text):

    # Make the first letter capital
    if text != "":
        text = text[0].upper() + text[1:]

    return text


def count_punctuation(text):

    count = 0

    for letter in text:
        if letter == ".":
            count = count + 1
        elif letter == ",":
            count = count + 1
        elif letter == "!":
            count = count + 1
        elif letter == "?":
            count = count + 1

    return count


def check_text(text):

    if text == "":
        return "You did not enter any text."

    last = text[-1]

    if last == ".":
        return "Sentence ends correctly."
    elif last == "!":
        return "Sentence ends correctly."
    elif last == "?":
        return "Sentence ends correctly."
    else:
        return "Sentence needs punctuation at the end."
