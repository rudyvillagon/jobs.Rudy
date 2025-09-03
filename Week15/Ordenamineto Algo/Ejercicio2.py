def Bubble_Sort(list_to_sort):

    n= len(list_of_numbers)

    for out_index in range(n - 1):
        made_changes = False
        for index in range(n - 1, out_index, -1 ):
            current_num = list_to_sort[index]
            next_num = list_to_sort[index - 1]

            print(f"Iterable: {out_index}, {index} Current Number: {current_num} Next Number: {next_num}")


            if current_num < next_num :
                print("The current number in higher, Accommodating it on the list.... ")
                list_to_sort[index], list_to_sort[index - 1] = next_num, current_num
                made_changes = True


    if not made_changes:
        return
            
list_of_numbers = [12,56,32,-2,56,11,76,-12]
Bubble_Sort(list_of_numbers)

print(list_of_numbers)
