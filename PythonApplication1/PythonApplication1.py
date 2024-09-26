
import random as r

#list와 내장함수

b=list()
#print(b)

a=[1,2,3,4,5]
#print(a)
#print(a[0])

b=list(range(1,11))
#print(b)

c=a+b
#print(c)

print(a)
a.append(6)
print(a)

a.insert(3,7)
print(a)

a.pop()
print(a)

a.pop(3) #3번 index pop
print(a)

a.remove(4) #4라는 값 삭제
print(a)

print(a.index(5)) #5라는 값의 index num print

#초기화
a=list(range(1,11))
print(a)
print(sum(a))
print(max(a))
print(min(7,5))
r.shuffle(a)
print(a)
a.sort(reverse=True)
print(a)
a.clear()
print(a)