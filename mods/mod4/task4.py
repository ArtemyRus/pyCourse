"""
На вход подается строка. Напишите функцию для
реализации: если из слова можно составить
палиндром, то составить его и вывести на экран.
"""

def foo(n :str):
    l = []
    oddCount = 0
    d = dict()
    for i in range(len(n)):
        if n[i] not in d:
            d[n[i]] = n.count(n[i])
            if n.count(n[i]) % 2 != 0:
                oddCount += 1
    if oddCount > 1:
        print("Палиндром не существует")
        return
    for i in d.items():
        if i[1] % 2 == 0:
            for j in range(i[1] // 2):
                l.insert(0, i[0])
                l.append(i[0])
        else:
            for j in range(i[1]):
                l.insert(len(l) // 2, i[0])
    return "".join(l)

def main():
    n = str(input())
    print(foo(n))

if __name__ == '__main__':
    main()