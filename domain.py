from pydantic import BaseModel


class Car(BaseModel):
    id: int
    name: str



class NativeWorld(BaseModel):
    id: int
    name: str

class Film(BaseModel):
    id: int
    name: str


class BiologicalSpecies(BaseModel):
    id: int
    name: str



class Personal(BaseModel):
    id: int
    name: str
    age: int
    height: int
    hair_color: str
    eyes_color: str
    year_of_birth: int
    gender: str
    car: Car
    nativeworld: NativeWorld
    film: Film
    biologicalspecies: BiologicalSpecies

