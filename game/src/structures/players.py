import random

from .status_effects import *
from std.src import Result,ok,err,ErrorKind


class Player:
    def __init__(self,name:str):
        self.id = random.randint(1,99999999999)
        self.name = name
        self.position = 1
        self.status_effects:list[StatusEffect] = list()

    def __str__(self) -> str:
        return f"Player<{self.id},{self.name},{self.position},{self.status_effects}>"

    def __repr__(self) -> str:
        return f"Player<{self.id},{self.name},{self.position},{self.status_effects}>"
    
    
    def remove_status_effect(self,status_effect:StatusEffect) -> Result:
        # give the current status_effect object to remove
        if status_effect in self.status_effects:
            self.status_effects.remove(status_effect)
            return ok(f"removed status effect: {status_effect}")
        else:
            return err(ErrorKind.NotFound,"status effect not in status_effect list.")

    def add_status_effect(self,status_effect) -> Result:
        if status_effect in self.status_effects:
            return err(ErrorKind.NotFound,"status effect not in status_effect list.")
        else:
            self.status_effects.append(status_effect)
            return ok("success")
        
