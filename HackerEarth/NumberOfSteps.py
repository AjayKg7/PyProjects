N = int(input())                  # Reading input from STDIN
series_a = list(map(int,input().split()))
series_b = list(map(int,input().split()))
steps = 0
min_val = min(series_a)
min_ind = series_a.index(min_val)
possible = False

while series_a[min_ind]>= series_b[min_ind]:
    all_eq = 0

    for i in range(N):
        if series_a[i] != series_a[min_ind]:
            if (series_a[i] - series_a[min_ind])%series_b[i] != 0:
                possible = False
                break

            else:
                steps += (series_a[i] - series_a[min_ind]) // series_b[i]

        all_eq += 1

    if all_eq == N:
        possible = True
        break
    steps+=1
    series_a[min_ind]-=series_b[min_ind]
if not possible:
    print(-1)
else:
    print(steps)




#print('Hi, %s.' % name)         # Writing output to STDOUT