import os,sys
import sys

CURRENT_DIR = os.getcwd()
sys.path.append(CURRENT_DIR)

import json
import std.src as std
import std.src.terminal_utils as terminal_utils
import parsers.map_parser as map_parser
import parsers.input_parser as input_parser
import structures.input_structures as input_structures
import parsers.translations_parser as translations_parser

from generators.map_generator import map_generater

import game_logic.game_loop as game_loop

import os.path 
from pathlib import Path
import time





    


if __name__ == "__main__":
    map_file_path = os.path.join(CURRENT_DIR,"a_game_files","map.json")
    translations_file_path = os.path.join(CURRENT_DIR,"a_game_files","translations.json")

    


    

    result_of_parsing_translations = translations_parser.get_supported_langs(Path(translations_file_path))

    if result_of_parsing_translations.is_err():
        print("error while loading translations: {}",result_of_parsing_translations.unwrap_err())


    [print(f"{i+1} : {lang}") for i, lang in enumerate(result_of_parsing_translations.unwrap())]
    
    chosen_lang = int(input("choose language: "))
    chosen_lang = result_of_parsing_translations.unwrap()[chosen_lang-1]

    messages = translations_parser.Language(Path(translations_file_path),chosen_lang)
    input_smt_object = input_parser.InputSomething(messages)
    

    match input_smt_object.ask_generated_or_load_map():
        case input_structures.MapChoises.Load:
            result_of_parsing_game_map = map_parser.json_map_parser(file_path=Path(map_file_path))

            
            if result_of_parsing_game_map.is_err():
                print("error while loading game map: {}",result_of_parsing_game_map.unwrap_err())
                sys.exit()

            game_map = result_of_parsing_game_map.unwrap()

        case input_structures.MapChoises.Generated:
            squares = input_smt_object.ask_for_amount_of_squares()

            game_map = map_generater(squares)







    amount_of_dices = input_smt_object.ask_for_amount_of_dices(1)
    dice_sides = input_smt_object.ask_for_amount_of_sides_on_dices(6)
    players = input_smt_object.ask_for_player_names()
    game_loop.run(game_map,players_list=players,dice_sides=dice_sides,amount_of_dices=amount_of_dices,input_parser=input_smt_object,messages=messages)
    
    
    






