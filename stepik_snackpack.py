def calculate(W, items):

    items.sort(key=lambda x: round(x[0]/x[1], 3), reverse=True)
    best_cost = 0

    while W and items:
        item_cost, item_weight = items[0]
        if W-item_weight >= 0:
            W -= item_weight
            best_cost += item_cost
        else:
            part_cost = W * round(item_cost/item_weight,8)
            best_cost += part_cost
            W = 0
        items = items[1:]

    print(f"{best_cost:.3f}")


if __name__ == "__main__":
    n, W = map(int, input().split())

    items = []
    for _ in range(n):
        items.append(tuple(map(int, input().split())))

    calculate(W, items)

# answers:
# Passed test #1. 180.000
# Passed test #2. 500.000
# Passed test #3. 166.667
# Passed test #4. 0.000
# Passed test #5. 0.000
# Passed test #6. 7777.731
# Passed test #7. 66152.572
# Passed test #8. 239607.438
# Passed test #9. 200232.681
# Passed test #10. 1232251.000
# Passed test #11. 1232251.000

