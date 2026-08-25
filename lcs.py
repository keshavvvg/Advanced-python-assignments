str1=input("Enter first sequence: ")
str2=input("Enter second sequence: ")
m=len(str1)
n=len(str2)
dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if str1[i-1]==str2[j-i]:
            dp[i][j]=dp[i-1][j-1] + 1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])
i=m
j=n
lcs=""
while i>0 and j>0:
    if str1[i-1]==str2[j-1]:
        lcs=str1[i-1]+lcs
        i-=1
        j-=1
    elif dp[i-1][j]>dp[i][j-1]:
        i-=1
    else:
        j-=1
print("Longest common subsequence among the given strings ",str1," and ",str2," is: ",lcs)
print("Length of Longest common subsequence: ",len(lcs))


#OUTPUT

'''
Enter first sequence: abcde
Enter second sequence: cdefgh
Longest common subsequence among the given strings  abcde  and  cdefgh  is:  cde
Length of Longest common subsequence:  3
'''
