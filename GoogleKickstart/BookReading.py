# Google Kickstart 2019 Round H Problem No.1

tests = int(input())
for test_case in range(1, tests+1):
    N, M, Q = [int(s) for s in input().split()]
    P = [s for s in range(1,N+1)]
    TP = [int(s) for s in input().split()]
    R = [int(s) for s in input().split()]
    pages_read = 0
    for reader in range(Q):
        pages_read += len([p for p in P if p not in TP and p%R[reader]==0])
    print("Case #%d: %d" %(test_case, pages_read))

