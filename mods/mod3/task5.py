"""
Дан список слов. Составить из последних букв каждого слова новое.
"""

def main():
    n = [n[len(n) - 1] for n in input().split()]
    print("".join(n))

if __name__ == '__main__':
    main()