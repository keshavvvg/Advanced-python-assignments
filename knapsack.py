def knapsack(val, wts, w):
    # wts=[1,3,7,2,4]
    # val=[40,23,60,100,0]
    n = len(wts)
    dp = [[0 for _ in range(0, w + 1)] for _ in range(0, n + 1)]
    for i in range(1, n + 1):
        for w in range(1, w + 1):
            if wts[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], val[i - 1] + dp[i - 1][w - wts[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    included_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            # i = i - 1
            included_items.append(i)
            w = w - wts[i - 1]
    included_items.reverse()
    return dp[n][w], included_items, dp

n = int(input("Enter the number of items: "))
w = int(input("Enter the maximum capacity of the knapsack: "))
val = []
wts = []
items = []
print("Enter values and weights of each item: ")
for i in range(0, n):
    value = int(input("value of item "))
    wt = int(input("weight of item "))
    val.append(value)
    wts.append(wt)
max, items, dp_table = knapsack(val, wts, w)
print("Items included in the sack of maximum capacity = ", w, " are: ", items)


#OUTPUT:

'''
Enter the number of items: 3
Enter the maximum capacity of the knapsack: 5
Enter values and weights of each item: 
value of item 1
weight of item 1
value of item 2
weight of item 2
value of item 3
weight of item 3
Items included in the sack of maximum capacity =  5  are:  [2, 3]
'''
