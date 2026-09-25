my_list = [ 4 ,3 ,6 ,1 ,7 ]

last_deleted = my_list.pop()
firts_deleted = my_list.pop(0)

my_list.append(firts_deleted)
my_list.insert(0,last_deleted)

print(my_list)