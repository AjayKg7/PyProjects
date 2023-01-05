def MinimizeCount(K, array):
    min_sum = 0
    count = 0
    val = K

    for i in array:

        if (i >= 0):
            count += 1
            min_sum += i
            val = K
        else:
            if (count == 0):
                return abs(sum(array) + i)

            else:
                val -= 1
                if (val < 0):
                    min_sum += abs(i)

                else:
                    min_sum += i

    return abs(min_sum)


N, K = map(int, input().split())            # Reading input from STDIN
array = list(map(int, input().split()))

finalval = MinimizeCount(K, array)
print(finalval)
