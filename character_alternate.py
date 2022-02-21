def characterAlternete(s):
    res = 0
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            res += 1
    return res


if __name__ == '__main__':
    print("Please Enter your Number : ")
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = characterAlternete(s)

        print(str(result))