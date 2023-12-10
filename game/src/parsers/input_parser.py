import std.src as std
import std.src.terminal_utils as terminal_utils
import parsers.translations_parser as translations_parser

from structures import players
from structures import input_structures
import time

def contains_numbers(string:str) -> bool:
    for char in string:
        if char.isdigit():
            return True
    return False

def contains_non_numbers(string:str) -> bool:
    for char in string:
        if char.isdigit() is False:
            return True
    
    return False

def remove_whitespace(input_string) -> str:
    return input_string.replace(" ", "").replace("\n", "").replace("\t", "")


'''
ask the player for input.
Uses the Language class to get the text to ask.

'''
    
class InputSomething:
    def __init__(self,messages:translations_parser.Language) -> None:
        self.messages = messages

    def ask_for_player_names(self) -> list[players.Player]:
        '''
        Asks the player for a name.
        name must be longer than two long.
        There must be two names provided.
         
        '''
        while True:
            output = list()
            current_player = 1
            
            while True:
                player_name = input(self.messages.ask_for_player_name(current_player)).strip()
                
                if len(player_name) == 0:
                    break
                
                if len(player_name) < 3:
                    print(self.messages.names_under_3_long_are_not_allowed())
                    time.sleep(1)
                    continue

                # This is a poor check. It can be easily bypassed
                if player_name in output:
                    print(self.messages.other_player_has_same_name())
                    time.sleep(1) 
                    continue

                new_player = players.Player(player_name)
                
                output.append(new_player)
                
                current_player += 1
            
            if len(output) < 2:
                print(self.messages.must_be_at_least_two_players())
                time.sleep(2)
                terminal_utils.clear_terminal()
            else:
                return output
            
    def ask_for_amount_of_dices(self,default:int) -> int:
        while True:
            number_of_dices = input(self.messages.ask_for_how_many_dices(default))
            number_of_dices = remove_whitespace(number_of_dices)
            if len(number_of_dices) == 0:
                return default
            
            if contains_non_numbers(number_of_dices) is True:
                print(self.messages.input_is_wrong())
                time.sleep(2.5)
                terminal_utils.clear_terminal()
                continue
            
            number_of_dices = int(number_of_dices)
            if number_of_dices == 0:
                print(self.messages.input_is_wrong())
                time.sleep(2.5)
                terminal_utils.clear_terminal()
                continue

            return number_of_dices
            
    def ask_for_amount_of_sides_on_dices(self,default:int) -> int:
        while True:
            amount_of_sides = input(self.messages.ask_for_how_many_sides_on_dices(default))
            amount_of_sides = remove_whitespace(amount_of_sides)
            if len(amount_of_sides) == 0:
                return default
            
            if contains_non_numbers(amount_of_sides) is True:
                print(self.messages.input_is_wrong())
                time.sleep(2.5)
                terminal_utils.clear_terminal()
                continue
            
            amount_of_sides = int(amount_of_sides)
            if amount_of_sides == 0:
                print(self.messages.input_is_wrong())
                time.sleep(2.5)
                terminal_utils.clear_terminal()
                continue

            return amount_of_sides
        
    def ask_throw_dice_or_stop(self,player_name) -> input_structures.ThrowDiceOrStop:
        '''
        Asks the player to throw dice or stop.
        returns either
        input_structures.ThrowDiceOrStop.Stop or input_structures.ThrowDiceOrStop.Throw
        '''
        while True:
            throw_or_stop = input(self.messages.ask_if_player_wants_to_throw_dice_or_stop(player_name))
            throw_or_stop = remove_whitespace(throw_or_stop)
            throw_or_stop = throw_or_stop.lower()
            if throw_or_stop == self.messages.throw_dices_input():
                return input_structures.ThrowDiceOrStop.Throw
            elif throw_or_stop == self.messages.stop_input():
                return input_structures.ThrowDiceOrStop.Stop
            else:
                print(self.messages.did_not_input_throw_dices_or_stop())
                time.sleep(1.5)


    def ask_generated_or_load_map(self) -> input_structures.MapChoises:
        '''
        '''
        while True:
            load_or_gen_map = input(self.messages.ask_generate_or_load_map())
            load_or_gen_map = remove_whitespace(load_or_gen_map)
            load_or_gen_map = load_or_gen_map.lower()

            if load_or_gen_map == self.messages.generate_map_input():
                return input_structures.MapChoises.Generated
            elif load_or_gen_map == self.messages.load_map_input():
                return input_structures.MapChoises.Load
            else:
                print(self.messages.input_is_wrong())
                time.sleep(1.5)


    def ask_for_amount_of_squares(self) -> int:
        '''
        '''
        while True:
            amount_of_sides = input(self.messages.ask_for_how_many_squares())
            amount_of_sides = remove_whitespace(amount_of_sides)
        
        
            if contains_non_numbers(amount_of_sides) is True or len(amount_of_sides) == 0:
                print(self.messages.input_is_wrong())
                time.sleep(2.5)
                terminal_utils.clear_terminal()
                continue
            
            amount_of_sides = int(amount_of_sides)
            if amount_of_sides < 10:
                print(self.messages.error_must_be_at_least_ten_squares())
                time.sleep(2.5)
                terminal_utils.clear_terminal()
                continue

            return amount_of_sides

        
                
