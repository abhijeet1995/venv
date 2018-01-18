def check(A, pos):
	    if (A[pos]+pos)>=(len(A)-1):
	        return True
	    if A[pos]==0:
	        return False
	    res=False
	    i=pos+1
	    while i<=pos+A[pos]:
	        res = res or check(A,i)
            i+=1
		return result

def canJump(A):
	    if len(A)==1:
	        return 1
	    if check(A,0,A[0]):
	        return 1
	    else:
	        return 0

canJump([3,2,1,0,4])
