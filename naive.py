import sys
line = sys.stdin.readline().split()
n = int(line[0])
m = int(line[1])

data = []
for i in range(n):
    line = sys.stdin.readline().rstrip()
    data.append([int(x) for x in line.split()])


def maxsub():
    subsum  = []
    for i in range(n):
        subsum.append(range(m))
        if i == 0:
            subsum[i][0] = data[i][0]
        else:
            subsum[i][0] = subsum[i-1][0] + data[i][0]
        for j in xrange(1, m):
            psum = 0       
            for k in range(i+1):
                psum += data[k][j]
            subsum[i][j] = subsum[i][j-1] + psum
    
    max = -99999999;
    for i in range(n):
        for j in range(m):
            for k in xrange(i, n):
                for l in xrange(j, m):
                    if i>0 and j>0:
                        s_i1_j1 = subsum[i-1][j-1]
                    else:
                        s_i1_j1 = 0
                    if i > 0:
                        s_i1_l = subsum[i-1][l]
                    else:
                        s_i1_l = 0
                    if j>0:
                        s_k_j1 = subsum[k][j-1]
                    else:
                        s_k_j1 = 0
                    sum = subsum[k][l] -(s_i1_l + s_k_j1 - s_i1_j1)
                    if sum > max:
                        max = sum
                        print i,j,k,l,sum
    return max
def test():
    sum = 0
    for i in range(n):
        for j in range(m):
            sum += data[i][j]
    return sum
    
print maxsub()