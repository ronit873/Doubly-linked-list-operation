class Solution:
    def josephus(self,n,k):
        def fun(a,k,i):
            if len(a)==1:
                return a[0]
            n=k
            while n-1:
                i+=1
                n-=1
                if i>=len(a):
                    i=0
            a.pop(i)
            if i>=len(a):
                i=0
            return fun(a,k,i)
        a=[]
        for i in range(1,n+1):
            a.append(i)
        return fun(a,k,0)