def solve(s, K):
    # Write your code here
    S = [i for i in s]  # converted to list for re-assignment
    dup_in_substr = 0

    # iterating through all possible substring
    for i in range(len(S) - (K - 1)):

        x = S[i:i + K]  # substring & dict for duplicates

        dict_lower = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                      'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                      'y': 0, 'z': 0}

        for j in range(len(x)):  # count duplicates & replace
            if x[j] != "#":
                dict_lower[x[j]] += 1
                if dict_lower[x[j]] > 1:
                    S[i + j] = '#'
                    dup_in_substr += 1
                    dict_lower[x[j]] -= 1

    return dup_in_substr


S = input()
K = int(input())

out_ = solve(S, K)
print(out_)