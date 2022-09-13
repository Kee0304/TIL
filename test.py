def find_root(V):
    for i in range(1, V+1):
        if par[i]==0:
            return i

def preorder(n):
    if n:
        print(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):
    if n:
        inorder(ch1[n])
        print(n)
        inorder(ch2[n])

def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)


E=int(input())
arr=list(map(int,input().split()))
print(arr)
V=E+1
ch1=[0]*(V)
ch2=[0]*(V)
par=[0]*(V)
for i in range(E-1):
    p,c=arr[i*2],arr[(i*2)+1]
    if ch1[p]==0:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c]=p

print(par)
print(ch1)
print(ch2)
a=find_root(V)
print(a)
preorder(a)
#inorder(a)
#postorder(a)