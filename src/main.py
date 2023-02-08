from rich import print
from rich.progress import track
from rich.prompt import FloatPrompt
from rich.prompt import IntPrompt
import time


def pretty_print(rows, delay: float = 0):
    last_row_len = len(rows[-1])
    print_rows = []
    for row in track(rows, description="Formatting output..."):
        text = ""
        spaces = (last_row_len - len(row)) // 2
        text += spaces * "  "
        for item in row:
            if item == 0:
                text += "  "
            else:
                text += "[#ffffff]⬛[/]"
        text += spaces * "  "
        print_rows.append(text)

    for row in print_rows:
        print(row)
        time.sleep(delay)


def main():
    #autopep8: off
    rows = [
            [0, 1, 0]
        ]
    #autopep8: on

    runs = IntPrompt.ask("Wie viele Durchläufe?", default=10)
    delay = FloatPrompt.ask(
        "Wie lange soll zwischen den Durchläufen gewartet werden? (in Millisekunden)", default=0) / 1000

    for _ in track(range(runs), description="Generating..."):
        row = rows[-1]

        new_row = []
        new_row.append(0)
        for idx in range(len(row)):
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

            xOR = left ^ right

            new_row.append(xOR)

        new_row.append(0)
        rows.append(new_row)

    pretty_print(rows, delay)


if __name__ == "__main__":
    main()
