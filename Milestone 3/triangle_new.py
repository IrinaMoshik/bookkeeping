import sys

def get_triangle(n):
    triangle = []
    for i in range(n):
        temp_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(temp_list)
    return triangle

def print_triangle(triangle):
    max_width = len(str(triangle[-1][-1]))
    for i, row in enumerate(triangle):
        padding = " " * (max_width - len(str(row[0])))
        print(padding, end="")
        print("  " * (len(triangle) - i - 1), end="")
        print("  ".join(str(num).rjust(max_width) for num in row))

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python triangle.py <number_of_rows>")
            sys.exit(1)

        try:
            n = int(sys.argv[1])
        except ValueError:
            print("Invalid input. Please provide a valid integer for the number of rows.")
            sys.exit(1)

triangle = get_triangle(5)
print_triangle(triangle)