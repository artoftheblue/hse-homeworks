def hanoi(n, A, B, C):
    if n == 1:
        print(f"1 {A} {B}")
        return
    hanoi(n - 1, A, C, B)
    print(f"{n} {A} {B}")
    hanoi(n - 1, C, B, A)
         
hanoi(int(input()), "1", "3", "2")
