
"""

We have n units of a resource to be allocated to r projects. n and r are
integers and resource allocation is in integer units only. If j, 0<=j<=n, units of
the resource are allocated to project i, then the resulting net profit is P (i,j).
Design an algorithm to allocate the resource to the r projects so as to
maximize the total net profit. Analyze its time complexity.

Input:Adjacency matrix representing the profit gained by providing j resorces to i'th project.
Output:The number of resources to be allocated to each project inorder to get maximum profit.
Providing extra Resources to a project will result in a no extra profit.(optional)

"""

"""
Constraints Faced
+The same number of resources cannot be allocated two two projects except in the case of no resources at all.
"""
def Remduplicates(d): 
    f=[]
    for i in d: 
        if i not in f: 
            f.append(i) 
    return f

# Python function to print permutations of a given list 
def permutation(permutations): 
    if len(permutations) == 0: 
        return []  
    if len(permutations) == 1: 
        return [permutations] 
    l = []  
    for i in range(len(permutations)): 
       m = permutations[i] 
       rempermutations = permutations[:i] + permutations[i+1:] 
       for p in permutation(rempermutations): 
           l.append([m] + p) 
    return l 
"""
def split(x, n): 
    if(x < n):  
        return -1 
    elif (x % n == 0): 
        for i in range(n): 
            print(x//n, end =" ") 
    else: 
        # upto n-(x % n) the values  
        # will be x / n  
        # after that the values  
        # will be x / n + 1 
        zp = n - (x % n) 
        pp = x//n 
        for i in range(n): 
            if(i>= zp): 
                print(pp + 1, end =" ") 
            else: 
                print(pp, end =" ")
"""
def getPossibilities(res,m,n):
    l=len(res)
    for i in res:
        for k in range(m):
            if (len(i)<(m)):
                i.append(0)
            else:
                break       
    #print(res)
    p=[]
    for i in res:
        for k in permutation(i):
            p.append(k)
    return p
  
def getAllSubsetsRec(arr, n, v, sum,res) :  
    if (sum == 0) : 
        #print(v)
        res.append(v)
        return 
    if (n == 0): 
        return 
    getAllSubsetsRec(arr, n - 1, v, sum,res) 
    v1 = [] + v 
    v1.append(arr[n - 1]) 
    getAllSubsetsRec(arr, n-1, v1, sum - arr[n - 1],res) 
  
 
def getAllSubsets(arr, n, sum,res): 
    v = [] 
    getAllSubsetsRec(arr, n, v, sum,res)
""" 
def extraCases(x,n,m):
    arr=[u for u in range(n)]
    s=[]
    k=1
    if (n==m):
        t=[1 for i in range(m-1)]
        t.append(0)
        x.append(t)
        for i in range(m):
            s=[arr[k] for i in range(m-(k+1))]
            s.append(arr[k+1])
        while (len(s)<m-1):
            s.append(0)
            print(s)
        tsum=0
        for i in range(len(s)):
            tsum+=s[i]
        if (tsum==(n-1)):
            x.append(s)
        s=[]
    return x
 """       
            
            
    
            
    
            
        
    
def getMaxProfit(JR,res,m,n):
    #res=extraCases(res,n,m)
    x=getPossibilities(res,m,n)
    #extraCases(x,n,m)
    x=Remduplicates(x)
    #print(x)
    maximum=0
    maxpath=[]
    print("Possible Ways of allocating Resources are:")
    k=0
    a=[]
    for i in x:
        tot=0
        a=[]
        for j in range(m):
            tot+=JR[j][i[j]]
            a.append(JR[j][i[j]])
            #print(JR[j][i[j]],end="")
            print(i[j],end="")
            print("->",end="")
        print("=",tot)
        print()
        if (tot>maximum):
            maxpath=[]
            maximum=tot
            maxpath=i
    return maxpath

#Main Function    
#JR=[[100,150,175,175,175,175],[120,135,140,147,147,147],[80,105,105,105,105,105]]
path=input("Enter Input File Name:");
fpath="Input/"+path+".txt"
with open(fpath) as textFile:
    lines = [line.split() for line in textFile]

JR=[]
for line in lines:
    JR.append([int(l) for l in line])

#print(JR)


#arr = [0,1,2,3,4,5]
m=len(JR)
#print(m)
n=len(JR[0])
arr=[u for u in range(n)]
#print(arr)
#sum = 5
sum=n-1
res=[]
n = len(arr) 
getAllSubsets(arr, n, sum,res)
#print(res)
result=getMaxProfit(JR,res,m,n)
#print(result)
print("The Method of allocating resources which gives the maximum profit is ")
for i in result:
    print(i,end="")
    print("->",end="")
fin=0
#print(JR)
for j in range(m):
    fin+=JR[j][result[j]]
    #i+=1
    #print(fin)
print(fin)

