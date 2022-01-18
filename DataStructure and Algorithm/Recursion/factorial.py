# n = int(input())

# def factorial(n):
#     if n == 1 or n==0:
#         return 1
#     return n * factorial(n-1)

# print(factorial(n))



N, r = map(int, input().split())

jarisu = len(str(N)) - r

until_find = True

N = list(str(N))
N = list(map(int, N))

res = []
cur_max = 0


lst = N[:]
FIND = True

first_jari = 0
first_jari_index = 0

while FIND:
    cur_max = max(lst)
    print('현재 cur_max: ', cur_max)
    cur_idx = lst.index(cur_max)
    print('현재 cur_idx: ', cur_idx)

    if len(N[cur_idx:]) >= jarisu and len(N[:cur_idx]) <= r:
        first_jari = cur_max
        first_jari_index = cur_idx
        FIND = False
    else:
        lst.remove(cur_max)
        print("지울게", cur_max)
        print('지우고 난 뒤: ', lst)


res_lst = N[first_jari_index:]
    
r = r - len(lst[:first_jari_index])

for _ in range(r):
    min_val = min(res_lst)
    res_lst.remove(min_val)

print(''.join(str(_) for _ in res_lst))
