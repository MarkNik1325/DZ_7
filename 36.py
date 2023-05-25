def print_operation_table(operation, num_rows=8, num_columns=8):
    for x in range (1, num_columns+1):
        for y in range (1, num_rows +1):
            print (*list(map (operation, [x], [y])), end = "  ")
        print ()

print_operation_table(lambda x, y: x * y)