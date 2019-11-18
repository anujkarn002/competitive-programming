# Google Kickstart Round H Problem No. 3

from itertools import permutations
T = int(input())
for t in range(1, T+1):
    numbers = [int(s) for s in input().split()]
    num = []
    for n in range(len(numbers)):
        if numbers[n] !=0:
            for i in range(1, numbers[n]+1):
                num.append(n+1)
    perm = permutations(num)
    s = False
    for p in perm:
        p = list(p)
        for i in range(len(num)//2):
            p[i] = p[i]*-1
        sm = sum(p)
        if sm == 0 or sm % 11 == 0:
            s = True
            break
    if s == False:
      print("Case #{}: NO".format(t))
    else:
      print("Case #{}: YES".format(t))
