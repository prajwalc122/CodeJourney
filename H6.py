n = int(input("Enter value of n: "))

for i in range(n):
    j = 1
    print(f"\nOuter loop i = {i}")
    
    while j < n:
        print("j =", j)
        j *= 2
