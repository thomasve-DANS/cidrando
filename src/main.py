from typing import List, Optional
from fastapi import FastAPI, Response
import random
import copy

from pydantic import BaseModel

class Data(BaseModel):
    leaders: List[str]
    players: List[str] 
    amount_per_player: int = 1

class Result(BaseModel):
    leaders: List[str]
    players: List[str] 
    amount_per_player: int = 1
    choices: dict
    message: Optional[str]

app = FastAPI()

@app.post("/randomize")
def randomize(input_data: Data, response: Response):
    results = {}
    temp_list = copy.copy(input_data.leaders)
    for player in input_data.players:
        choices = []
        for x in range(0, input_data.amount_per_player):
            random.shuffle(temp_list)
            try:
                choices.append(temp_list.pop())
            except IndexError:
                response.status_code = 400
                return Result(
                    leaders=input_data.leaders,
                    players=input_data.players,
                    amount_per_player=input_data.amount_per_player,
                    choices=[],
                    message="Ran out of leaders, try decreasing amount per player",
                )
        results[player] = sorted(choices)
    return results

    
