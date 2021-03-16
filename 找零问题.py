# coding:utf-8
# 递归方式
def rec_mc(coin_value_list, change):
    min_coins = change
    if change in coin_value_list:
        return 1
    else:
        for i in [c for c in coin_value_list if c <= change]:  # 在小于找零金额面值的硬币寻找
            num_coins = 1 + rec_mc(coin_value_list, change - i)  # 总归分解递归，子金额的找零问题
            if num_coins < min_coins:  # 记录要找的最小硬币数量
                min_coins = num_coins
        return min_coins


# 递归方式，加入记录表
def rec_dc(coin_value_list, change, known_results):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + rec_dc(coin_value_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[change] = min_coins
    return min_coins


# 动态规划方式
def dp_make_change(coin_value_list, change, min_coins):
    for cents in range(change + 1):
        coin_count = cents
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
            min_coins[cents] = coin_count
    # print(min_coins)
    return min_coins[change]


# 修改后的动态规划方式
def dp_make_changes(coin_value_list, change, min_coins, coins_used):
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
            min_coins[cents] = coin_count
            coins_used[cents] = new_coin
    return min_coins[change]


def print_coins(coin_used, change):
    coin = change
    while coin > 0:
        this_coin = coin_used[coin]
        print(this_coin, end=' ')
        coin -= this_coin


if __name__ == '__main__':
    change = 33
    known_results = [0] * (change + 1)
    min_coins = [0] * (change + 1)
    coins_used = [0] * (change + 1)
    value_list = [1, 5, 8, 10, 25]
    # start_time = time.time()
    # print(rec_mc(value_list, change))
    # end_time = time.time()
    # print("cost time: {}s".format(end_time - start_time))

    # print(rec_dc(value_list, change, known_results))
    # print(dp_make_change(value_list, 63, min_coins))
    print(dp_make_changes(value_list, change, min_coins, coins_used))
    print_coins(coins_used, change)
