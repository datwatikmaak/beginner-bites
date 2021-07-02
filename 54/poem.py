INDENTS = 4

rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """


def print_hanging_indents(poem):
    lines = poem.strip().split("\n")
    lines = map(str.strip, lines)

    formatted_poem = ""
    is_first_line = True
    indent = " " * INDENTS

    for line in lines:
        if line == "":
            is_first_line = True
            continue
        if is_first_line:
            formatted_poem += line + "\n"
            is_first_line = False
        else:
            formatted_poem += indent + line + "\n"

    print(formatted_poem)


print_hanging_indents(rosetti_unformatted)
