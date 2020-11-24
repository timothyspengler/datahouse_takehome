# Timothy Spengler
# DataHouse Take Home Assignment
# November 24, 2020

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from util import score_applicants

app = FastAPI()

class Attributes(BaseModel):
    intelligence: int
    strength: int
    endurance: int
    spicyFoodTolerance: int

class Person(BaseModel):
    name: str
    attributes: List[Attributes]

class Group(BaseModel):
    team: List[Person] = None
    applicants: List[Person] = None


@app.get("/")
def read_root():
    return {"Timothy Spengler": "DataHouse Assignment"}

# Parameters: team and applicant information in json format
# Output: Applicant Scores in json
@app.post("/score/")
async def score_members(group: Group):
    scoredApplicants = {'scoredApplicants': score_applicants(group.team,group.applicants)}

    return scoredApplicants