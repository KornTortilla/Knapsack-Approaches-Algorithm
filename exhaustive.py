from util import run_problems

def exhaustive(input):
    num = input[0]
    stocks = input[1]
    amount = input[2]

    best = None
    for candinate in generate_combinations(stocks):
        if verify_combination(candinate, amount):
            if best is None or total_stocks(candinate) > total_stocks(best):
                best = candinate

    if best is None:
        return 0
    else:
        return total_stocks(best)

def generate_combinations(stocks):
    result = []
    if not stocks:
        return [[]]
    for i in generate_combinations(stocks[1:]):
        result.append(i)
        result.append([stocks[0]] + i)
    return result

def verify_combination(candinate, amount):
    total_amount = 0
    for i in range(len(candinate)):
        total_amount += candinate[i][1]

    if total_amount > amount:
        return False
    else:
        return True

def total_stocks(candinate):
    total_stocks = 0
    for i in range(len(candinate)):
        total_stocks += candinate[i][0]

    return total_stocks

run_problems(exhaustive)