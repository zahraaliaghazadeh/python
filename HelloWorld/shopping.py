shopping_list = ["milk","pasta","eggs","spam","bread","rice"]

# code 1
# for item in shopping_list:
#     if item != "spam":
#     print("Buy " + item)

# code 2
# for item in shopping_list:
#     if item == "spam":
#         # continue causes everything else in the loop to be ignored
#         # you ll never have to use this continue
#         # some good examples of using continue on stack overflow
#         continue
#     print("Buy " + item)
#     # the print should be as same as if in terms of indentation


# code 3
for item in shopping_list:
    if item == "spam":
        # stop looking when you find what you are looking for
        break
    print("Buy " + item)


