choice = int(input())
n = int(input())
if choice == 1:
    parity = 0
    x=n
    while n > 0:
        parity = ~(parity)
        n = n & (n - 1)
    print(bin(x)[2:])
    if parity:
        print("odd")
    else:
        print("even")
else:
    table = [0, 1, 1, 0, 1, 0, 0, 1]
    print(bin(n)[2:])
    if table[n & 7]:
        print("even")
    else:
        print("odd")