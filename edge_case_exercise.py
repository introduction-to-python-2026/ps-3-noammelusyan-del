def move(my_list, direction):
    my_list [0, 0, 1, 0]
    index = my_list[2]
    
    if direction == "left":
        if index > 0:
            my_list[index], my_list[index - 1] = 0, 1

    elif direction == "right":
        if index < len(my_list) - 1:
            my_list[index], my_list[index + 1] = 0, 1
    return my_list
