
def Bubble_Sort(list_to_sort):


    for out_index in range(0,len(list_to_sort)-1):
        made_changes = False
        for index in range(0,len(list_to_sort)-1 - out_index ):
            current_num = list_to_sort[index]
            next_num = list_to_sort[index + 1]

            print(f"Iterable: {out_index}, {index} Current Number: {current_num} Next Number: {next_num}")


            if current_num > next_num :
                print("The current number in higher, Accommodating it on the list.... ")
                list_to_sort[index] = next_num
                list_to_sort[index + 1] = current_num
                made_changes = True


        if not made_changes:
            break
            
    return list_to_sort