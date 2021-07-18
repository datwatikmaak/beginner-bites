IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    filtered_names = []
    for name in names:

        if name.startswith(QUIT_CHAR) or len(filtered_names) == MAX_NAMES:
            break

        if name.startswith(IGNORE_CHAR) or not name.isalpha():
            continue

        else:
            filtered_names.append(name)

    return filtered_names
