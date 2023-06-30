N = int(input())
array  = list(map(int, input().split()))
X = int(input())
i =0 
j =0 
if N == len(array):

    for i in range(N):
        if X == array[i]:
            j += 1
        

print(f'{j}')

