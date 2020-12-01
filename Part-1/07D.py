def make_exchange(money, coins):
    if money == 0:
        return 1
    if len(coins) == 0 or min(coins) > money or money < 0:
        return 0
    x = coins[len(coins)-1]
    b = coins[0:len(coins)-1]
    return (make_exchange(money, b) + make_exchange(money-x, coins))
