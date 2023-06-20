def alignedPrint(A, B):
    # simple utility function to print two lists aligned
    print(
        "A: [",
        ", ".join(map(lambda x: "{:2d}".format(x), A)),
        "]\nL: [",
        ", ".join(map(lambda x: "{:2d}".format(x), B)),
        "]", 
    sep="")

def firstLeftNaive(A):
    L = [0] * len(A)

    for i in range(1, len(A)):
        j = i - 1

        while A[j] > A[i]: j -= 1
        L[i] = j

def firstLeft(A):
    L = [0] * len(A)

    for i in range(1, len(A)):
        j = i - 1

        while A[j] > A[i]: j = L[j]
        L[i] = j

    return L

def firstLeftAlt(A):
    L = [0] * len(A)
    s = [0]

    for i in range(len(A)):
        while A[s[-1]] > A[i]: s.pop()
        L[i] = s[-1]
        
        s.append(i)
    
    return L

if __name__ == "__main__":
    # array of size of input 
    # with random values from 0 to 100, but always starting with 0
    import random
    A = [0] + [random.randint(0, 100) for _ in range(int(input()))]

    alignedPrint(A, firstLeft(A))
    # print()
    # alignedPrint(A, firstLeftAlt(A))