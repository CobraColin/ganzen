import structures.players as players
import structures.status_effects as status_effects
import parsers.input_parser as input_parser
import parsers.translations_parser as translations_parser
import sys,os
from . import dice_logic

import platform
from structures.input_structures import *

from structures.map_structs import *

from typing import List, Dict


import std.src.terminal_utils as terminal_utils

import time

def players_to_str(position:int,players:List[Player]) -> str:
    '''
    Gets all the players that are on the position and creates a string that has all the
    players names that are on the specified position seperated by a dash
    '''
    out_str = ""
    
    first = True
    for index, player in enumerate(players):
        if player.position != position:
            continue
        if first is False:
            out_str+= " - "

        out_str+= f"{player.name}"
        
        first = False
    return out_str


def print_map(map:GameMap,players:List[Player],current_player:Player):
    '''
    Print a the map with focus on a player.
    '''
    
    begin = current_player.position - 10
    end = current_player.position + 10

    # make sure we don't show not exsisting squares.
    if begin > 5:
        begin = begin - 5
    elif begin > 1:
        begin = begin - (begin-1)
    elif begin < 1:
        begin = 1
    

    

    for i in range(begin,end+1):
        square:Result = map.get_square(i)
        if square.is_ok():
            square:Square = square.unwrap()
            place = square.position
            if square == NormalSquare: 
                print(f"{place}: {players_to_str(place,players)}")
            else:
                print(f"{place}: ({square}) {players_to_str(place,players)}")
            time.sleep(0.045)










def run(map:GameMap,players_list:List[Player],dice_sides:int,amount_of_dices:int,messages:translations_parser.Language,input_parser:input_parser.InputSomething):
    game_time = 0
    


    
    while True:
        
        game_time += 1
        print(f"game time {game_time}")
        for player in players_list:
            terminal_utils.clear_terminal()



            # process the status effects
            
            allowed_to_continue = True
            for status_effect in player.status_effects:
                # call both process and is is_able_to_throw to make sure the status effect gets processed 
                status_effect.process(player=player,current_time=game_time,messages=messages)
                
                temp_is_allowed_to_continue = status_effect.is_able_to_throw(player=player,current_time=game_time,messages=messages)
                                
                if allowed_to_continue: 
                    allowed_to_continue = temp_is_allowed_to_continue   


            if allowed_to_continue is False:
                time.sleep(3)
                continue

            print_map(map,players_list,current_player=player)
            move = input_parser.ask_throw_dice_or_stop(player.name)
            if move == ThrowDiceOrStop.Stop:
                print(messages.player_gave_up(player.name))
                players_list.remove(player)
                # check if there is only 1 player in the player list
                # if it so. then that player has won 
                if len(players_list) == 1:
                    print(messages.player_won(players_list[0].name))
                    sys.exit()
                continue


            move = dice_logic.throw(amount_of_dices,dice_sides)

            print(messages.report_throwed_number(move))
            time.sleep(1.5)



                
            ## check if the position is in the map.
            if player.position + move <= map.length:
                square:Square = map.get_square(player.position+move).unwrap()
            else:
                # bounce back the player
                new_corrected_position =  map.length-(player.position+move-map.length)
                if new_corrected_position < 1:
                    new_corrected_position = 1
                player.position = new_corrected_position
                
                square:Square = map.get_square(player.position).unwrap()
                # process the walk. But because the player already bounced we dont the player to move so number_thown is 0.
                square.process_walk(number_thrown=0,player=player,time=game_time,players=players_list,map=map,messages=messages)
                continue

            
            # normal walk
            square.process_walk(number_thrown=move,player=player,time=game_time,players=players_list,map=map,messages=messages)


            # this is here because if you land on doubler it may be out of bounds.
            if player.position > map.length:
                player.position =  map.length-(player.position+move-map.length)
                continue
            
            
            
            
            # check if the player has reached the end of the map.
            if player.position == map.length:
                print(messages.player_won(player.name))
                sys.exit()



                    
        

        




