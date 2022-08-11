from pprint import pprint

mat=[['0' for _ in range(10)] for _ in range(10)]
pprint(mat)

mat[0][0]=mat[0][0]+'a'
pprint(mat)