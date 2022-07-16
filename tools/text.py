from re import sub


def remove_html(text):
    return sub(r"<\/?\s*\w+\s*>", " ", text)


def remove_dashes(text):
    return sub(r"-+", "", text)


def remove_urls(text):
    return sub(r"(https?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", "", text)


def remove_newlines(text):
    return sub(r"\s*\n+\s*\n*", "\n", text)


def remove_newlines_completely(text):
    return sub(r"\n+", " ", text)


def remove_spaces(text):
    return sub(r"\s+", " ", text)


def remove_digits(text):
    return sub(r"\d+", "", text)


def remove_spec_chars(text):
    return sub(r"[_|@#$.,;<>+?:&`\"\'\/\\\[\]()]", " ", text)
