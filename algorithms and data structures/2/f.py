'''ARRAY = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 
         365596, 2279184, 14772512, 95815104, 666090624, 4968057848,
         39029188884, 314666222712, 2691008701644, 24233937684440,
         227514171973736, 2207893435808352, 22317699616364044, 234907967154122528]
'''

def queens(n: int) -> int:
    diagonal_a, diagonal_b = [], []
    columns = []
    
    return row_iteration(n, diagonal_a, diagonal_b, columns, 0)

def row_iteration(n: int, diagonal_a: list, diagonal_b: list, columns: list, row: int) -> int:
    if n == row:
        return 1
    
    counter = 0
    for column in range(n):
        a, b = row + column, row - column
        if not (a in diagonal_a or b in diagonal_b or column in columns):
            diagonal_a.append(a)
            diagonal_b.append(b)
            columns.add(column)
            
            counter += row_iteration(n, diagonal_a, diagonal_b, columns, row + 1)

            diagonal_a.remove(a)
            diagonal_b.remove(b)
            columns.remove(column)
    
    return counter

print(queens(int(input())))