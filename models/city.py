#!/usr/bin/python3
""" City Model | inherites from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class """
    state_id = ''
    name = ''
