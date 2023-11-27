def binary_search(number: int) -> int:
    left, right = 0, number
    while left <= right:
        mid = (right + left) // 2
        
        sq_mid = mid ** 2
        if sq_mid < number:
            left = mid + 1
            result = mid
        elif sq_mid > number:
            right = mid - 1
        elif sq_mid == number:
            result = mid
            break
            
    return result

with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(binary_search(int(line)))