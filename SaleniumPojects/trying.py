from abc import ABC

a=10
b=15
# x=lambda y:a>b or b>a
# print(x(10))
x=[a,b]
x.sort()
print(x[-1])