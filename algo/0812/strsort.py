import sys

sys.stdin=open("GNS_test_input.txt")

T=int(input())

def count(a,k):                  
    cnt=0
    for i in a:
        if i==k:
            cnt+=1

    return cnt

for t in range(1,T+1):
    test_case,test_length=input().split()
    numlist=list((input().rstrip()).split(" "))        

    slist=["ZRO","ONE","TWO","THR","FOR","FIV","SIX","SVN","EGT","NIN"]

    print(test_case)
    for i in slist:
        print(f"{i} "*count(numlist,i))

    


    






#    for i in range(len(numlist)):
#        if numlist[i]=="ZRO":
#            numlist[i]='0'+numlist[i]
#        elif numlist[i]=="ONE":
#            numlist[i]='1'+numlist[i]
#        elif numlist[i]=="TWO":
#            numlist[i]='2'+numlist[i]
#        elif numlist[i]=="THR":
#            numlist[i]='3'+numlist[i]
#        elif numlist[i]=="FOR":
#            numlist[i]='4'+numlist[i]
#        elif numlist[i]=="FIV":
#            numlist[i]='5'+numlist[i]
#        elif numlist[i]=="SIX":
#            numlist[i]='6'+numlist[i]
#        elif numlist[i]=="SVN":
#            numlist[i]='7'+numlist[i]
#        elif numlist[i]=="EGT":
#            numlist[i]='8'+numlist[i]
#        elif numlist[i]=="NIN":
#            numlist[i]='9'+numlist[i]
#
#    slist=sorted(numlist)
#    rlist=[0]*len(numlist)
#    for i in range(len(numlist)):
#        rlist[i]=slist[i][1:]
#
#    print(test_case)
#    print(" ".join(rlist))