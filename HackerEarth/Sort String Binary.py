
class BinSort:

    def checksortedstring(self,S):
        val = True
        for ch in range(len(S)):
            if S[ch] == "1":
                for i in S[ch:]:
                    if i == "0":
                        val = False
                        break
                # print("is it infinite loop!!")
                break
        return val

    def itersort(self,S,attempts):
        ones = S.count('1')
        zeros = S.count('0')
        if len(S) == 2:
            S = S[-1::-1]
            attempts+=1
        elif ones == 2:
            attempts += 1
            for i in S:
                if i == "1":
                    S[S.index(i)] = "0"

        elif zeros == 2:
            attempts += 1
            for i in S:
                if i == "0":
                    S[S.index(i)] = "1"

        elif ones == 1 and zeros>2:
            S[S.index("1")] = "0"
            S[-1] = "1"
            attempts+=1
        elif ones >=2 and zeros == 1:
            S[S.index("0")] = "1"
            S[0] = "0"
            attempts += 1

        else:
            way = self.eitherway(S)
            revs = S[-1::-1]
            if way == "osway":
                cdn = True
                cnt = 0
                attempts+=1
                for i in range(2):
                    if cnt <2:
                        for j in range(len(S)):
                            if S[j] == "0" and cdn == True:
                                pass
                            elif cdn == False:
                                cnt = 2
                                break
                            elif S[j] == "1":
                                cdn = False
                                if S[j:].count("0") >=2:
                                    val=0
                                    for k in S[j:]:
                                        if k == "0" and val<2:
                                            # print("Now I am Here")
                                            S[S[j:].index(k)+j] = "1"
                                            val+=1
                                        elif val == 2:
                                            break
                                elif S[j:].count("0")==1:
                                    S[S[j:].index("0") + j ] = "1"
                                    S[j] = "0"
                                    cnt =2
                                    # print(S,"You r in right place")
                                    break

            else:
                S=S[-1::-1]
                cdn = True
                cnt = 0
                attempts += 1
                for i in range(2):
                    if cnt < 2:
                        for j in range(len(S)):
                            if S[j] == "1" and cdn == True:
                                pass
                            elif cdn == False:
                                cnt = 2
                                break
                            elif S[j] == "0":
                                cdn = False
                                if S[j:].count("1") >= 2:
                                    val = 0
                                    for k in S[j:]:
                                        if k == "1" and val < 2:
                                            # print("Now I am in onesway")
                                            S[S[j:].index(k) + j] = "0"
                                            val += 1
                                            # print(type(S))
                                        elif val == 2:
                                            break
                                elif S[j:].count("1") == 1:
                                    S[S[j:].index("1") + j] = "0"
                                    S[j] = "1"
                                    cnt = 2
                                    # print(S, "You r in right place")
                                    break

                S=S[-1::-1]
        return S, attempts
    # print('Hi, %s.' % name)         # Writing output to STDOUT

    def eitherway(self,S):
        revs = S[-1::-1]
        onesway = True
        osway = 0
        for j in range(len(S)):
            if S[j] == "1":
                osway = S[j:].count("0")
                break

        for j in range(len(revs)):
            if revs[j] == "0":
                onesway = revs[j:].count("1")
                break
        if onesway > osway:
            return "osway"
        return "onesway"

T = int(input())  # Reading input from STDIN

for i in range(T):
    N = int(input())
    S1 = input()
    S = [i for i in S1]
    attempts = 0
    ret = BinSort()
    srted = ret.checksortedstring(S)
    while srted == False:
        S,attempts = ret.itersort(S,attempts)
        srted = ret.checksortedstring(S)

    print(attempts)

