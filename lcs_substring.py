str1=input("Enter first sequence: ")
str2=input("Enter second sequence: ")
m=len(str1)
n=len(str2)
dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
max_length = 0
end_idx=0
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                end_idx = i
        else:
            dp[i][j] = 0
lcs = str1[end_idx - max_length : end_idx]
print("Longest common substring among the strings ",str1," and ",str2," is: ",lcs)
print("Length of Longest Common Substring: ",max_length)


#OUTPUT


'''
Enter first sequence: abcde
Enter second sequence: cdhe
Longest common substring among the strings  abcde  and  cdhe  is:  cd
Length of Longest Common Substring:  2

'''
