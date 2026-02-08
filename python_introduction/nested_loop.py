rows = 5
current_row = 1

while current_row <= rows:
    # Print spaces
    space_count = rows - current_row
    while space_count > 0:
        print(" ", end="")
        space_count -= 1

    # Print stars
    star_count = (2 * current_row) - 1
    while star_count > 0:
        print("*", end="")
        star_count -= 1

    # Move to next line
    print()
    current_row += 1