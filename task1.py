# explicitly defined variables
item_1 = 10
item_2 = 20
item_3 = 30
budget = 100

total_cost = item_1 + item_2 + item_3
difference = budget - total_cost

print(total_cost)
print(difference)


# compare items against budget?
if total_cost <= budget:
    print("within budget")
else:
    print("over budget")


