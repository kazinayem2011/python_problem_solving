def stringConstruction(s):
    return len(set(s))

if __name__ == '__main__':
    print("Please Enter an Input : ")
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        print("Number of Unique Value: ",str(result) + '\n')