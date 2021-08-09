from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    chunks = [names[i:i + cols] for i in range(0, len(names), cols)]

    for row in chunks:
        output = ["| " + row[0].ljust(10)]
        for col in row[1:]:
            output.append("| " + col.ljust(10))
        print(''.join(output))