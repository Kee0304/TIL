#from pprint import pprint
#
#
#T=int(input())
#
#for test_case in range(1, T+1):
#    N=int(input())
#    b_height_list=list(map(int,(input().rstrip(" ")).split(' ')))
#
#    
#    mat=[]
#    cnt=0
#
#    
#    for i in range(0,N):
#        mat.append([0*N]*255)
#
#    for m in range(0,N):
#        for n in range(N-1,-1,-1):
#            if 
#
#    pprint(mat)
#
#    
#    for n in range(N-1,-1,-1):
#        for m in range(2, N-2):
#            if mat[n][m]==1:
#                if mat[n][m-1]==mat[n][m-2]==mat[n][m+1]==mat[n][m+2]==0:
#                    cnt+=1
#    
#    print(f"#{test_case} {cnt}")

T=int(input())

def BubbleSort(a):
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    
    return a


for test_case in range(1, T+1):
    test_length=int(input())
    b_height_list=list(map(int,(input().rstrip(' ')).split(' ')))
    cnt=0
    idx=2
    while idx<len(b_height_list)-2:
        if BubbleSort([b_height_list[idx-2],b_height_list[idx-1],b_height_list[idx],b_height_list[idx+1],b_height_list[idx+2]])[4]==b_height_list[idx]:
            cnt+=b_height_list[idx]-BubbleSort([b_height_list[idx-2],b_height_list[idx-1],b_height_list[idx],b_height_list[idx+1],b_height_list[idx+2]])[3]
            idx+=3
        else:
            idx+=1
    
    print (f'#{test_case} {cnt}')