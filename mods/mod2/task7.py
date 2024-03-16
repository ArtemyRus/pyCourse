"""
На вход подается строка s и символ i. Необходимо найти количество символов i,
расположенных в начале строки.
"""

def foo(s :str, c) -> int:
    count = 0
    for i in range(len(s)):
        if(s[i] == c):
            while(i < len(s) and s[i] == c):
                i += 1
                count += 1
            break
    return count

def main():
    inputStr = str(input())
    symb = str(input())
    print(foo(inputStr, symb))

if __name__ == '__main__':
    main()