"""https://www.codewars.com/kata/67fbd1c105b5721c8011d44b"""


def is_row_winner(table) -> bool:
    """Check if row is winner """
    for i in range(0, len(table), 3):
        row = "".join(table[i:i+3])
        # print(row)
        if row in ("XXX", "OOO"):
            print(f"{row[0]} is winner by row!")
            return True
    return False


is_row_winner(["X", "X", "X", "O", "O", ".", ".", ".", "."])  # True
is_row_winner(["X", "O", "X", "O", "O", "O", "X", ".", "X"])  # True
is_row_winner(["X", "O", ".", ".", "X", "O", ".", ".", "X"])  # False


def is_col_winner(table) -> bool:
    """Check if column is winner """
    for i in range(3):
        col = "".join([table[j] for j in (i, i+3, i+6)])
        # print(col)
        if col in ("XXX", "OOO"):
            print(f"{col[0]} is winner by column!")
            return True
    return False


is_col_winner(["X", "X", "X", "O", "O", ".", ".", ".", "."])  # False
is_col_winner(["X", "O", "X", "O", "O", "O", "X", ".", "X"])  # False
is_col_winner(["X", "O", ".", ".", "X", "O", ".", ".", "X"])  # False


def print_table(table):
    """Prints the board in a pretty tic tac toe format"""

    def cell(val):
        if val == "X":
            return "  ❌ "
        if val == "O":
            return "  ⭕️ "
        return "     "

    print()
    print("     |     |     ")
    print(f"{cell(table[0])}|{cell(table[1])}|{cell(table[2])}")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"{cell(table[3])}|{cell(table[4])}|{cell(table[5])}")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"{cell(table[6])}|{cell(table[7])}|{cell(table[8])}")
    print("     |     |     ")


print_table(["X", "X", "X", "O", "O", ".", ".", ".", "."])
print_table(["X", "O", "X", "O", "O", "O", "X", ".", "X"])
print_table(["X", "O", ".", ".", "X", "O", ".", ".", "X"])


def is_diag_winner(table) -> bool:
    """Check if diagonal is winner """
    diag1 = "".join([table[i] for i in (0, 4, 8)])
    # print(diag1)
    diag2 = "".join([table[i] for i in (2, 4, 6)])
    # print(diag2)

    if diag1 in ("XXX", "OOO"):
        print(f"{diag1[0]} is winner by diagonal!")
        return True
    if diag2 in ("XXX", "OOO"):
        print(f"{diag2[0]} is winner by diagonal!")
        return True

    return False


is_diag_winner(["X", "X", "X", "O", "O", ".", ".", ".", "."])  # False
is_diag_winner(["X", "O", "X", "O", "O", "O", "X", ".", "X"])  # False
is_diag_winner(["X", "O", ".", ".", "X", "O", ".", ".", "X"])  # True


def is_winner(table) -> bool:
    """Check if table is winner"""

    print_table(table)

    row = is_row_winner(table)
    if row:
        return row
    col = is_col_winner(table)
    if col:
        return col
    diag = is_diag_winner(table)
    if diag:
        return diag

    return False


is_winner(["X", "X", "X", "O", "O", ".", ".", ".", "."])  # X is winner by row!
is_winner(["X", "O", "X", "O", "O", "O", "X", ".", "X"])  # O is winner by row!
is_winner(["X", "O", ".", ".", "X", "O", ".", ".", "X"])  # X is winner by diagonal!
is_winner(["O", "X", ".", "O", ".", "X", "O", ".", "."])  # O is winner by column!
