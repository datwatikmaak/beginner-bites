def get_index_different_char(chars):
    chars = ["-" if char == "" else char for char in chars]
    string_of_chars = ''.join(str(char).strip() for char in chars)

    alpha = ""
    non_alpha = ""
    for char in string_of_chars:
        if char.isalpha() or char.isdigit():
            alpha += char
        elif char == "":
            non_alpha += "*"
        else:
            non_alpha += char

    if len(alpha) == 1:
        return string_of_chars.index(alpha)
    if len(non_alpha) == 1:
        return string_of_chars.index(non_alpha)


get_index_different_char(['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'])
