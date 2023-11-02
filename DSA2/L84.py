def find_rightmost_set_bit_position(n):
    if n == 0:
        return 0

    position = 1  
    while n & 1 == 0:
        n >>= 1  
        position += 1

    return position

n = int(input("n: "))


position = find_rightmost_set_bit_position(n)


print("output :", position)