N=int(input())
삼육구=list(map(str,list(range(1,N+1))))

result=[]
for num in 삼육구:
    threecnt=num.count('3')
    sixcnt=num.count('6')
    ninecnt=num.count('9')

    if threecnt+sixcnt+ninecnt>=1:
        result.append('-'*(threecnt+sixcnt+ninecnt))
    
    else:
        result.append(num)

    resstr = " ".join(result)

print(resstr)