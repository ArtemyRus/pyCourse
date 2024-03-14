"""
Дан список слов. Составить из последних букв каждого слова новое.
"""

if __name__ == '__main__':
    inputStr = input().split()
    s = ""
    for i in range(len(inputStr)):
        s += inputStr[i][len(inputStr[i]) - 1]
    print(s)