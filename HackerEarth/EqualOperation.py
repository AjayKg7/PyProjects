T = int(input())                  # Reading input from STDIN
for test in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    count = 0
    minx = min(A)
    rem=0
    for i in A:
        if i%minx != 0:
            rem = i%minx
            count = 0
            break
        else:
            if i != minx:
                count += ((i/minx)-1)
    attempt3 = False
    if rem != 0:
        while attempt3 == False:
            # print("the rem is:", rem)
            for j in A:
                if j%rem != 0:
                    attempt3 = False
                    rem = j%rem
                    count=0
                    break
                else:
                    if j != rem:
                        count += ((j / rem) - 1)
                        attempt3 = True

    print(int(count))





#print('Hi, %s.' % name)         # Writing output to STDOUT