# N = int(input())

result = []
def binary(N):
    if N % 2 == 0:
        result.append('0')
    else:
        result.append('1')
    if N // 2 == 1:
        result.append('1')
        return '1'
    
    binary(N//2)

binary(999)
result.reverse()
print(''.join(result))