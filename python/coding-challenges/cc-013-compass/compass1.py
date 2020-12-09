def final_direction(startpoint, rotations):
    directions = ["N", "E", "S", "W"]     
    counter = 0
    for i in rotations: 
        if i == "R":
            counter += 1
        else:
            counter -= 1
    index_number = (counter + directions.index(startpoint)) % 4
    endpoint = directions[index_number]
    return endpoint 

print(final_direction("N", ["R", "R", "R", "L"]))