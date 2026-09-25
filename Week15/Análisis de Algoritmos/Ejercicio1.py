def Bubble_Sort(list_to_sort): # 0(1)


    for out_index in range(0,len(list_to_sort)-1): # O(log n)
        made_changes = False # 0(1)
        for index in range(0,len(list_to_sort)-1 - out_index ): # O(log n)
            current_num = list_to_sort[index] # 0(1)
            next_num = list_to_sort[index + 1] # 0(1)

            print(f"Iterable: {out_index}, {index} Current Number: {current_num} Next Number: {next_num}") # 0(1)


            if current_num > next_num : # 0(1)
                print("The current number in higher, Accommodating it on the list.... ") # 0(1)
                list_to_sort[index] = next_num # 0(1)
                list_to_sort[index + 1] = current_num # 0(1)
                made_changes = True # 0(1)


    if not made_changes: # 0(1)
        return # 0(1)
            
list_of_numbers = [12,56,32,-2,56,11,76,-12] # 0(1)
Bubble_Sort(list_of_numbers) # 0(1)

print(list_of_numbers) # 0(1)
