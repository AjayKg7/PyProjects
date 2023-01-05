T = int(input())  # Reading input from STDIN

for test in range(T):
    print("running this loop for __ times :", test)
    R, C = map(int, input().split())
    matrix = []
    blacks_in_row = 0
    blacks_in_col = 0
    for row in range(R):
        x = []
        hashes = 0
        for val in input():
            if val == "#":
                hashes += 1
                x.append(val)
            else:
                if hashes > blacks_in_row:
                    blacks_in_row = hashes

                hashes = 0
                x.append(val)

        matrix.append(x)
    if blacks_in_row < R:
        for cell in range(C):
            col_val = 0
            for each in range(R):
                if matrix[each][cell] == "#":
                    col_val+=1
                else:
                    if col_val > blacks_in_col:
                        blacks_in_col = col_val
                    col_val = 0

    if blacks_in_row > blacks_in_col:
        print(blacks_in_row)
    else:
        blacks_in_col
