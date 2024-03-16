"""
На вход подается последовательность целых чисел. Требуется определить, присутствуют
ли в этой последовательности одинаковые числа. Результат вернуть в формате Boolean.
"""

def main():
    numbers = [int(x) for x in input().split()]
    b = False
    for i in range(len(numbers)):
        if (numbers.count(numbers[i]) > 1):
            b = True
            break
    print(b)

if __name__ == '__main__':
    main()
