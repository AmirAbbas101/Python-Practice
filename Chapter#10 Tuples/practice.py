a = {'one':1,'two':2,'three':3,'four':4,'five':5}
# for key in a:
#     print(key,' ',a[key])
# l = list()
# for i in a.items():
#     l.append(i)
# l.sort()
# print(l)
# ll = list()
# for k,v in l:
#     ll.append((v,k))
# print(ll)
# ll.sort()
# print(ll)

li = list()
for k,v in a.items():
    li.append((v,k))
li.sort()
maximum = max(li)
minimum = min(li)
print(li)

le = list()
for v,k in li:
    le.append((k,v))
print(le)
print(maximum)
print(minimum)