N = int(input())
array  = list(map(int, input().split()))
X = int(input())
index = 0 

if N == len(array):
    min = abs(X - array[0])
    index = 0
    for i in range(1, N):
        count = abs(X - array[i])
        if count < min:
            min = count
            index = i
print(f'{array[index]}')