def find (ordered_list, element_to_find):
    for element in ordered_list:
        if element == element_to_find:
            return True
        return False
        
x = [1,2,3,4,5]

print(find(x, 1))
print(find(x, 6))
