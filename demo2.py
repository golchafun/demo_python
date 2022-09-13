# membuat list_a dari 1-15
list_a = [*range(1,16)]
print("list_a:",list_a)

# membuat list genap dari list_a
list_b = [x for x in list_a if x%2 == 0]
print("list_b:",list_b)