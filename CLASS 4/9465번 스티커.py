import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    for i in range(1,N):
        if i == 1:
            sticker[0][i] += sticker[1][i-1]
            sticker[1][i] += sticker[0][i-1]

        else:
            sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2])
            sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])

    print(max(sticker[0][N-1], sticker[1][N-1]))