shopping_list = ["milk","pasta","eggs","spam","bread","rice"]

item_to_find = "spam"
# use None when does not have a value
found_at = None
# last value in range is not included
for index in range(len(shopping_list)):
    # len is length
    if shopping_list[index] == item_to_find
        found_at = index