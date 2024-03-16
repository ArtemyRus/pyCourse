"""
На вход подается список чисел через пробел.
Напишите функцию выводящую сообщение для
списка чисел:
1) Все числа равны
2) Все числа разные
3) Есть равные и неравные числа
"""

def foo(n):
    countList = []
    valuesList = []
    for i in range(len(n)):
        if(n[i] not in valuesList):
            valuesList.append(n[i])
            countList.append(n.count(n[i]))
    if (len(countList) == 1):
        print("Все числа равны")
        return
    if(max(countList) == 1):
        print("Все числа разные")
        return
    print("Есть равные и неравные числа")

def main():
    n = [int(x) for x in input().split()]
    foo(n)

if __name__ == '__main__':
    main()