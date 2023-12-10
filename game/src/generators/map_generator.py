import structures.map_structs as map_structs

import random

def map_generater(amount_squares:int) -> map_structs.GameMap:
    # the index(not position) of special squares


    output_map = [map_structs.NormalSquare(i+1)  for i in range(amount_squares)]


    # generate the random positions. random.sample should not pick the same value twice
    special_squares = random.sample(range(amount_squares), 3)

    for index, index_position in enumerate(special_squares):

        match index:
            case 0:
                output_map[index_position] = map_structs.WellSquare(index_position+1)
            case 1:
                output_map[index_position] = map_structs.DoubleSquare(index_position+1)

            case 2:
                output_map[index_position] = map_structs.thornbush(index_position+1)
    

    return map_structs.GameMap(output_map)

    