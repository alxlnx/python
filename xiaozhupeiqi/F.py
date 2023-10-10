N, M = 0, 0
m = []
ms = []
# with open('in.txt') as f:
#     lines = f.readlines()
#     lines = [l.rstrip('\n') for l in lines]
#     N, M = [int(ch) for ch in lines[0].split(' ')]

#     for i in range(1, M+1):
#         m.append([int(x) for x in lines[i].split()])

#     K = int(lines[M+1])
#     for i in range(K):
#         ms.append([int(x) for x in lines[M+2+i].split()])

N, M = [int(ch) for ch in input().rstrip('\n').split()]
for i in range(M):
    m.append([int(x) for x in input().rstrip('\n').split()])

K = int(input().rstrip('\n'))
for i in range(K):
    ms.append([int(x) for x in input().rstrip('\n').split()])

# print(N, M)
# print(*m, sep='\n')
# print(K)
# print(ms)

res = 0
for miner in ms:
    d = miner[2]
    m_x, m_y = miner[0], miner[1]
    for dy in range(-d, +d+1):
        y = m_y + dy 
        if (y < 0 or y > M-1):
            pass
        else:
            for dx in range(-d, +d+1):
                x = m_x + dx
                if (x < 0 or x > N-1):
                    pass
                else:
                    # this (x,y) is on the field
                    if (m[y][x] != -1):
                        res += m[y][x]
                        m[y][x] = -1
                    
print(res)

