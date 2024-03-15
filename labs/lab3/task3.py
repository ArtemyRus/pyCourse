"""
На вход подается доменное имя сайта. Необходимо вывести все домены по порядку
начиная с домена первого уровня.
"""

def main():
    domain = input().split(".")
    for i in range(len(domain)):
        print(domain[-i - 1])

if __name__ == '__main__':
    main()