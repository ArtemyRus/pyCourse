"""
Строка состоит из 0 и 1 Выведите ‘yes’, если количество единиц совпадает с
количеством нулей. И ‘no’ в противном случае.
"""

def main():
    n = [int(x) for x in input()]
    print("yes") if n.count(0) == len(n) // 2 else print("no")

if __name__ == '__main__':
    main()