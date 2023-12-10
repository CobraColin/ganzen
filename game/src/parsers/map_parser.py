import structures.map_structs as map_structs
from pathlib import Path
import json


from std.src import Result,ok,err,ErrorKind

def json_map_parser(file_path:Path) -> Result:
    '''
    return: Result with ok map_structs.GameMap.

    reads a file with json turns it into a python dict and processes that dict.

    
    input_data = [
        {"type": "start", "place": 1},
        {"type": "double", "place": 2},
    ]

    and turns it into a list
    output_data = [
        {"type": class_StartSquare, "place": 1},
        {"type": class_DoubleSquare, "place": 2},
    ]
    '''

    if file_path.exists() is False:
        return err(ErrorKind.FileDoesNotExist,"given file for the map parser does not exist")
    
    with open(file_path, 'r') as file:
        try:
            input_data = json.load(file)
        except Exception as error:
            return err(ErrorKind.Other,error)

     
    output = list()

    for square_data in input_data:
        square_type = square_data.get("type")
        position = square_data.get("place")


        match square_type:
            case "normal":
                output.append(map_structs.NormalSquare(position))
            case "well":
                output.append(map_structs.WellSquare(position))
            case "double":
                output.append(map_structs.DoubleSquare(position))
            case "thorn_bush":
                output.append(map_structs.thornbush(position))
            case _:
                output.append(map_structs.NormalSquare(position))
        


    return ok(map_structs.GameMap(output))