"""
Строка состоит из 0 и 1 Выведите ‘yes’, если количество единиц совпадает с
количеством нулей. И ‘no’ в противном случае.
"""

def main():
    n = str(input())
    if (len(n) % 2 != 0):
        print("no")
        exit()
    count = 0
    for i in range(len(n)):
        if n[i] == "0":
            count += 1
    if (count == (len(n) // 2)):
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()