my_list = (0, 0, 1, 0)

def move(my_list, direction):
    index = my_list[2]
    
    if direction == "left":
        if index > 0:
            my_list[index], my_list[index - 1] = 0, 1
            index = my_list[1]
            if index > 0:
                my_list[index], my_list[index - 1] = 1
             return my_list
