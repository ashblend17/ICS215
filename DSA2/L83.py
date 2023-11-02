def count_set_bits(n):
    count = 0
    while n > 0:
        count += n & 1  
        n >>= 1  
    return count

n = int(input("n=: "))

set_bits_count = count_set_bits(n)

print("Count of set bits =", set_bits_count)
