# 1 - misol
faktorial = lambda n: 1 if n <= 1 else n * faktorial(n-1)

son = int(input("Son kiriting: "))
print(f"{son}! = {faktorial(son)}")

# 2 - misol
palindrom = lambda s: all(s[i].lower() == s[-i-1].lower() for i in range(len(s)//2))

satr = input("Satr kiriting: ").replace(" ", "")
print("Palindrom!" if palindrom(satr) else "Palindrom emas.")

# 3 - misol
royxat = list(map(int, input("Ro'yxatni kiriting: ").split()))
tartiblangan = sorted(royxat)
print(f"Kichik: {tartiblangan[0]}, Katta: {tartiblangan[-1]}")

# 4 - misol
satr = input("Satr kiriting: ")
unli_soni = sum(1 for x in satr.lower() if x in 'aeiouy')
print(f"Unli harflar: {unli_soni}")

# 5 - misol
def tubmi(n):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

son = int(input("Son kiriting: "))
print(f"{son} → {'tub' if tubmi(son) else 'tub emas'}")
