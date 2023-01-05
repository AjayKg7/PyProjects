

N=int(input())
Girl = []
Menot = []
for i in range(N):
    chat = input()
    if chat[0] == "G":
        val = chat.split()

        for ch in val:
            if any(ch.isdigit()):
                Girl.append(int(ch))
    else:
        val = chat.split()

        for ch in val:
            if any(ch.isdigit()):
                Menot.append(int(ch))
onenine = Girl.count(19) - Menot.count(19)
twozero = Girl.count(20) - Menot.count(20)





