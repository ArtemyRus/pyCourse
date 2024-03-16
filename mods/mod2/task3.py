"""
В единственной строке записаны три целых числа
a, b, c (−1000≤a,b,c≤1000), числа разделены одиночными пробелами.
Выведите число, которое будет стоять между двумя другими после упорядочивания.
"""

def main():
    a = int(input())
    b = int(input())
    c = int(input())

    if (a >= b):
        if (b >= c): print(b)
        print(c)
    elif (c >= b):
        print(b)
    elif (a >= c):
        print(a)
    else:
        print(c)

if __name__ == '__main__':
    main()


