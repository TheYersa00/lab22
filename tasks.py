# 1.
a = int(input("Бірінші санды енгізіңіз: "))
b = int(input("Екінші санды енгізіңіз: "))
if a < b:
    print("Кіші сан:", a)
else:
    print("Кіші сан:", b)


# 2.
n = int(input("Сан енгізіңіз: "))
if n % 2 == 0:
    print("Жұп сан")
else:
    print("Тақ сан")


# 3.
N = int(input("N санын енгізіңіз: "))
total = 0
for i in range(1, N + 1):
    total += i
print("Қосынды:", total)


# 4.
N = int(input("N санын енгізіңіз (көбейту кестесі үшін): "))
for i in range(1, 11):
    print(N, "*", i, "=", N * i)


# 5. 
N = int(input("Факториал үшін N санын енгізіңіз: "))
fact = 1
for i in range(1, N + 1):
    fact *= i
print("Факториал:", fact)


# 6. 
text = input("Жол енгізіңіз: ")
vowels = "аеёиоуыэюяAEIOUYaeiouyӘәІіӨөҮүҰұҚқҒғ"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Дауысты әріптер саны:", count)


# 7. 
text = input("Жол енгізіңіз: ")
print("Кері жол:", text[::-1])


# 8. 
arr = list(map(int, input("Массив элементтерін енгізіңіз (бос орын арқылы): ").split()))
print("Максимум:", max(arr))


# 9.
arr = list(map(int, input("Массив енгізіңіз (бос орын арқылы): ").split()))
print("Элементтер қосындысы:", sum(arr))


# 10.
arr = list(map(int, input("Массив енгізіңіз (бос орын арқылы): ").split()))
x = int(input("Іздейтін санды енгізіңіз: "))
if x in arr:
    print(x, "массивте бар")
else:
    print(x, "массивте жоқ")
