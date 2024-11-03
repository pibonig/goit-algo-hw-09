import time


def find_coins_greedy(amount, coins):
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count

    return result


def find_min_coins(amount, coins):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


def compare_algorithms(amount, coins):
    start_time = time.time()
    greedy_result = find_coins_greedy(amount, coins)
    greedy_time = time.time() - start_time

    start_time = time.time()
    dp_result = find_min_coins(amount, coins)
    dp_time = time.time() - start_time

    print(f"Greedy algorithm result: {greedy_result}, time taken: {greedy_time:.6f} seconds")
    print(f"Dynamic programming result: {dp_result}, time taken: {dp_time:.6f} seconds")

    return greedy_time, dp_time


def generate_readme(greedy_time, dp_time):
    with open("readme.md", "w") as file:
        file.write("# Порівняння ефективності жадібного алгоритму та алгоритму динамічного програмування\n\n")
        file.write("## Жадібний алгоритм\n")
        file.write(f"Час виконання жадібного алгоритму: {greedy_time:.6f} секунд\n\n")
        file.write(
            "Жадібний алгоритм працює дуже швидко, оскільки він просто вибирає найбільші доступні номінали монет, доки не сформує потрібну суму. Його складність становить O(N), де N - кількість номіналів монет. Однак жадібний алгоритм не завжди гарантує мінімальну кількість монет, особливо коли набір номіналів не оптимальний.\n\n")
        file.write("## Алгоритм динамічного програмування\n")
        file.write(f"Час виконання алгоритму динамічного програмування: {dp_time:.6f} секунд\n\n")
        file.write(
            "Алгоритм динамічного програмування гарантує мінімальну кількість монет для формування заданої суми. Його складність становить O(N * M), де N - кількість номіналів монет, а M - сума, яку потрібно видати. Хоча алгоритм динамічного програмування може працювати повільніше, ніж жадібний алгоритм, він забезпечує оптимальний результат.\n\n")
        file.write("## Висновок\n")
        file.write(
            "Жадібний алгоритм підходить для швидкого знаходження рішення, коли набір номіналів монет оптимальний, і ми не потребуємо гарантії мінімальної кількості монет. Алгоритм динамічного програмування є більш надійним, оскільки він завжди знаходить оптимальне рішення, але може вимагати більше часу для обчислення, особливо при великих сумах. У конкретних ситуаціях вибір алгоритму залежить від вимог до точності та швидкості.\n")


if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    amount = 113
    greedy_time, dp_time = compare_algorithms(amount, coins)
    generate_readme(greedy_time, dp_time)
