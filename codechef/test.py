T = int(input())
for _ in range(T):
    N = int(input())
    question=[]
    score=[]
    for _ in range(N):


    for i in range(0,N):
        for j in range(i,N):
            if (i!=j):
                if(A[i]+A[j] == A[i]*A[j]):
                    count = count+1
    print(count)
