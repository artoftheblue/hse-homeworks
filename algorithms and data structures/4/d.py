ERROR = 10 ** (-9)

def polynomial(a, b, c, d):
    return lambda x: a * x ** 3 + b * x ** 2 + c * x + d

def binary_search(poly, error_margin=ERROR) -> str:
    # find borders
    right = 1
    while poly(right) * poly(-right) >= 0:
        right = right * 2
    left = -right
    
    # binary search itself
    while right - left >= error_margin:
        mid = (right + left) / 2
        if poly(mid) * poly(right) > 0:
            right = mid
        else:
            left = mid
    return left

print(binary_search(polynomial(*map(int, input().split()))))

'''def ternary_search(poly, left: float, right: float, error_margin=ERROR):
    while abs(left - right) >= error_margin:
        diff = (right - left) / 3
        left_third = left + diff
        right_third = right - diff
        
        if poly(left_third) < poly(right_third):
            left = left_third 
        else:
            right = right_third
            
    return (left + right) / 2'''
    
