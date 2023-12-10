""" 
magic values:

[[replace_player]] replace this with the player name/id
[[replace_default]] replace this with the default option
[[replace_throwed_number]] replace this with the throwed number
[[replace_new_position]] replace this with the new position

"""
from pathlib import Path
from std.src import Result,ok,err,ErrorKind
import json

def get_supported_langs(file_path:Path) -> Result:
    '''
    return: Result with ok value list[str]

    reads the translations.json file and gets the names of the languages present in the file  
    '''

    if file_path.exists() is False:
        return err(ErrorKind.FileDoesNotExist,"given file for the map parser does not exist")
    
    with open(file_path, 'r') as file:
        try:
            input_data = json.load(file)
        except Exception as error:
            return err(ErrorKind.Other,error)
        
    if type(input_data) != dict:
        return err(ErrorKind.Other,f"json file contents differs from the expected contents. Must be dict is {type(input_data)}")

    
    return ok(list(input_data.keys()))


def get_lang_data(file_path:Path,lang:str) -> Result:
    '''
    Opens the translations json file and loads it.
    Returns Result<Dict,str>
    '''
    if file_path.exists() is False:
        return err(ErrorKind.FileDoesNotExist,"given file for the map parser does not exist")

    with open(file_path, 'r') as file:
        try:
            input_data = json.load(file)
        except Exception as error:
            return err(ErrorKind.Other,error)
        
    if type(input_data) != dict:
        return err(ErrorKind.Other,f"json file contents differs from the expected contents. Must be dict is {type(input_data)}")
    
    if input_data.get(lang) is None:
        return err(ErrorKind.Other,f"json file contents differs from the expected contents. {lang} does not exist")
    
    return ok(input_data.get(lang))



def replace_magic_values(msg: str, throwed_number="", player="", default="",new_position="") -> str:
    return msg.replace("[[replace_throwed_number]]", str(throwed_number))\
            .replace("[[replace_player]]", str(player))\
            .replace("[[replace_default]]", str(default))\
            .replace("[[replace_new_position]]", str(new_position))





# A badly named class to map functions to the messages
class Language:
    def __init__(self,file_path:Path,lang:str):
        self.lang_data = get_lang_data(file_path,lang).unwrap()

    def ask_if_player_wants_to_throw_dice_or_stop(self, player_name: str) -> str:
        return replace_magic_values(self.lang_data["Ask_if_player_wants_to_throw_dice_or_stop"],player=player_name)

    def double_square(self) -> str:
        return self.lang_data["Double_square"]

    def well_square(self) -> str:
        return self.lang_data["Well_square"]

    def thornbush_square(self) -> str:
        return self.lang_data["ThornBush_square"]

    def cannot_move_stuck_in_well(self, player_name: str) -> str:
        return replace_magic_values(self.lang_data["Cannot_move_stuck_in_well"],player=player_name)

    def ask_for_how_many_dices(self, default: str) -> str:
        return replace_magic_values(self.lang_data["Ask_for_how_many_dices"],default=default)

    def ask_for_how_many_sides_on_dices(self, default: str) -> str:
        return replace_magic_values(self.lang_data["Ask_for_how_many_sides_on_dices"],default=default)

    def ask_for_player_name(self, player_name: str) -> str:
        return replace_magic_values(self.lang_data["Ask_for_player_name"],player=player_name)

    def report_throwed_number(self, throwed_number: int) -> str:
        return replace_magic_values(self.lang_data["Report_throwed_number"],throwed_number=throwed_number)

    def names_under_3_long_are_not_allowed(self) -> str:
        return self.lang_data["Names_under_3_long_are_not_allowed"]

    def other_player_has_same_name(self) -> str:
        return self.lang_data["Other_player_has_same_name"]

    def must_be_at_least_two_players(self) -> str:
        return self.lang_data["Must_be_at_least_two_players"]

    def throw_dices_input(self) -> str:
        return self.lang_data["Throw_dices_input"]

    def stop_input(self) -> str:
        return self.lang_data["Stop_input"]

    def did_not_input_throw_dices_or_stop(self) -> str:
        return self.lang_data["Did_not_input_throw_dices_or_stop"]

    def input_is_wrong(self) -> str:
        return self.lang_data["Input_is_wrong"]

    def player_gave_up(self, player_name: str) -> str:
        return replace_magic_values(self.lang_data["Player_gave_up"],player=player_name)

    def player_won(self, player_name: str) -> str:
        return replace_magic_values(self.lang_data["Player_won"],player=player_name)
    
    def landed_on_double(self) -> str:
        return self.lang_data["Landed_on_Double"]

    def landed_on_well(self) -> str:
        return self.lang_data["Landed_on_Well"]

    def landed_on_thornbush(self, new_position: str) -> str:
        return replace_magic_values(self.lang_data["Landed_on_ThornBush"], new_position=new_position)

    def player_was_skipped_because_stuck_in_well(self, player_name: str) -> str:
        return replace_magic_values(self.lang_data["Player_was_skipped_because_stuck_in_well"], player=player_name)

    def ask_for_how_many_squares(self) -> str:
        return self.lang_data["Ask_for_how_many_squares"]

    def error_must_be_at_least_ten_squares(self) -> str:
        return self.lang_data["Error_must_be_at_leats_ten_squares"]

    def ask_generate_or_load_map(self) -> str:
        return self.lang_data["Ask_generate_or_load_map"]
    
    def generate_map_input(self) -> str:
        return self.lang_data["Generate_map_input"]
    
    def load_map_input(self) -> str:
        return self.lang_data["Load_map_input"]
