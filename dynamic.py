from util import run_problems

def dynamic(input):
    num = input[0]
    stocks = input[1]
    amount = input[2]

    dp = [[0]*(amount + 1) for i in range(num + 1)]

    for i in range(num + 1):
        for j in range(amount + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif stocks[i - 1][1] <= j:
                dp[i][j] = max(stocks[i-1][0] + dp[i-1][j-stocks[i - 1][1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]

run_problems(dynamic)