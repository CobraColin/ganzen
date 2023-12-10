import std.src as std
from std.src import Result,ok,err,ErrorKind
from .players import Player

from parsers import translations_parser
from .status_effects import *
import random


import time

class GameMap:
    def __init__(self,map_squares:list) -> Result: 
        '''
        this function expects a a list with squares 
        like this index:square_object
        '''
        self.squares = map_squares

        self.length = len(map_squares)

    def get_square(self,index:int) -> Result:
        '''
        index starts at 1
        '''
        if index > self.length or index < 1:
            return err(ErrorKind.SquareDoesNotExist,"index is out of bounds")

        return ok(self.squares[index-1])
    





class Square:
    def __init__(self,position:int) -> None:
        self.position = position

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

    def __str__(self) -> str:
        return f"{type(self).__name__}"
    
    def __eq__(self, other: object) -> bool:
        if type(self) == other:
            return True
        return False

    def process_walk(self,number_thrown:int,player:Player,messages=translations_parser.Language,**kwargs) -> None:
        pass

class NormalSquare(Square):
    def process_walk(self,number_thrown:int,player:Player,**kwargs) -> None:
        player.position += number_thrown
    


class WellSquare(Square):
    def process_walk(self,number_thrown:int,player:Player,time:int,players:list[Player],**kwargs) -> None:
        for lplayer in players:
            if lplayer == player:
                continue

            for effect in lplayer.status_effects:
                if type(effect) == WellStatus:
                    lplayer.remove_status_effect(effect) 


        player.position += number_thrown
        player.add_status_effect(WellStatus(time))
    

class DoubleSquare(Square):
    def process_walk(self,number_thrown:int,player:Player,**kwargs) -> None:
        player.position += number_thrown*2

class thornbush(Square):
    def process_walk(self,number_thrown:int,player:Player,map:GameMap,messages=translations_parser.Language,**kwargs) -> None:
        random_player_position = random.randint(1,player.position)
        player.position = random_player_position
        print(messages.landed_on_thornbush(new_position=player.position))
        time.sleep(3)



