immutable_var = 1, "hello", 3.01, True
print("Immutable tuple:", immutable_var)
mutable_list = [2, "Hi", 4.5, True]
mutable_list[0] = 42
mutable_list[1] = "bye"
mutable_list.append("Transformed")
mutable_list.extend([False, 0, 1])
print("Mutable list:", mutable_list)