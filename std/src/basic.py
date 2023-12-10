'''
I do not like the error system of python so i will try to use the error system of rust instead.

So the result of a function is structured like this:

Result<ok,Error>

with ok being the value returned if the function succeeded.
'''

import sys
from enum import Enum

class ErrorKind(Enum):
    Other = 1
    NotFound = 2
    NotJson = 3
    FileDoesNotExist = 4
    SquareDoesNotExist = 5

class Error:
    def __init__(self, err_type:ErrorKind, msg):
        if type(err_type) is not ErrorKind or msg is None:
            raise ValueError("Both vars must not be None and type must be ErrorKind")
        self.type = err_type
        self.msg = msg

    def __str__(self):
        return f"Error<{self.type},{self.msg}>"
    
    def __repr__(self):
        return f"Error<{self.type},{self.msg}>"





class ResultEnum(Enum):
    Ok = 1
    Err = 2
    

class Result:
    def __init__(self, type:ResultEnum, value):
        self.type = type
        self._value = value

    def __str__(self) -> str:
        return f"Result<{self.type},{self._value }>"
    
    # def __repr__(self):
    #     return f"Result<{self.type},{self._value }>"

    def __eq__(self,other) -> bool:
        if self.type == other:
            return True
        return False

    def unwrap(self):
        match self.type:
            case ResultEnum.Ok:
                return self._value
            case ResultEnum.Err:
                raise ValueError("Tried to call unwrap on a result error.")
            
    def is_ok(self) -> bool:
        return self.type == ResultEnum.Ok
    
    def is_err(self) -> bool:
        return self.type == ResultEnum.Err
    
    def unwrap_err(self) -> Error:
        if self.is_err():
            return self._value
        else:
            raise ValueError("Tried to call unwrap_err is a result OK")




def err(err_type:ErrorKind,msg:str) -> Result:
    if err_type is None or msg is None:
        raise ValueError("Both vars must not be None")
    error = Error(err_type,msg)
    result_err = Result(ResultEnum.Err,error)

    return result_err


def ok(value) -> Result:
    ok_result = Result(ResultEnum.Ok,value)
    return ok_result