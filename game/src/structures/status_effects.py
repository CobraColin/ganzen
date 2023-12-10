from parsers import translations_parser


'''
Status affects should immediately be applied when a player steps on a square 

The status effect process is called before is_able_to_throw.  
'''

class StatusEffect:
    def __init__(self,activated_time:int) -> None:
        self.activated_time = activated_time
    def __repr__(self) -> str:
        return f"{type(self).__name__}"

    def __str__(self) -> str:
        return f"{type(self).__name__}"

    def process(self,player,current_time,messages:translations_parser.Language,**kwargs):
        pass

    def is_able_to_throw(self,player,current_time,messages:translations_parser.Language,**kwargs) -> bool:
        return True




class WellStatus(StatusEffect):
    def process(self,player,current_time,**kwargs):
        if current_time > self.activated_time+1:
            player.remove_status_effect(self)

    def is_able_to_throw(self,player,current_time,messages:translations_parser.Language,**kwargs) -> bool:
        if current_time > self.activated_time+1:
            return True
        else:
            print(messages.player_was_skipped_because_stuck_in_well(player.name))
            return False