"""
На вход подается два числа через пробел: a, b.
Напишите функцию для реализации рекурсивного
алгоритма Евклида поиска наибольшего общего
делителя.
"""

def foo(a, b):
    if a == 0 or b == 0:
        return a + b
    if a > b:
        return foo(a % b, b)
    return foo(a, b % a)

def main():
    a, b = [int(x) for x in input().split()]
    print(foo(a,b))

if __name__ == '__main__':
    main()