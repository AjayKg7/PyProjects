word = input()                  # Reading input from STDIN
toggle_str=""
for i in word:
    if i.isupper():
        toggle_str+=i.lower()
    else:
        toggle_str+=i.upper()

print(toggle_str)