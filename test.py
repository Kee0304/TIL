a=[1,0,0,1,0,0,1,1]

zerocnt=a.count(0)

for _ in range(zerocnt):
    a.remove(0)

print(a)