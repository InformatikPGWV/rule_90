from rich import print


def pretty_print(rows):
    text = ""
    last_row_len = len(rows[-1])
    for row in rows:
        spaces = (last_row_len - len(row)) // 2
        text += spaces * "  "
        # text += spaces * "☐"
        for item in row:
            if item == 0:
                text += "[#0000ff]⬛[/]"
                # text += "⬛"
            else:
                text += "[#ff0000]⬛[/]"
                # text += "⬜"
        # text += spaces * "[#000000]⬛[/]"
        # text += spaces * "☐"
        text += "\n"
    print(text)


def find_digit(row, idx):
    left = None
    right = None

    # find left
    if idx == 0:
        left = 0
    else:
        left = row[idx-1]

    # find right
    if idx == len(row)-1:
        right = 0
    else:
        right = row[idx+1]

    return left, right


def main():
    #autopep8: off
    rows = [
            [0, 1, 0]
        ]
    #autopep8: on

    for i in range(25):  # ? ROW DURCHLÄUFE
        row = rows[-1]

        new_row = []
        new_row.append(0)
        for idx, digit in zip(range(len(row)), row):
            left = None
            right = None

            left, right = find_digit(row, idx)

            # print(left, digit, right)

            xOR = left ^ right
            # print(xOR)

            new_row.append(xOR)

        # print(new_row)
        new_row.append(0)
        rows.append(new_row)

    pretty_print(rows)


if __name__ == "__main__":
    main()
