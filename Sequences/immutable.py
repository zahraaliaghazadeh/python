# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
# # Both have the same id because both have the value of True
#
#
# result = False
# print(id(result))

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))



result += "ish"
print(id(result))
print(id(another_result))