# https://www.codechef.com/COOK112B/problems/DIET

# cook your dish here
T = int(input())
for t in range(1, T+1):
  N, K = [int(s) for s in input().split()]
  pbd = [int(s) for s in input().split()]
  P = 0
  day = 0
  for i in range(N):
    P += pbd[i]  # buys pbd[i] protein on ith day
    if P < K:
      day = i+1
      print("NO {}".format(day))
      break
    P -=K  # ate 5 proteins
    day = i+1
    if day == N:
      print("YES")

