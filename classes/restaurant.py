from os import PRIO_PGRP
from pydoc import describe


class Restuarant:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def describe_restuarant(self):
        print(f"welcome to {self.name.upper()} restuarant" )
        print(f"we have {self.type.title()} cusine available for today")

    def open_restuarant(self):
        print("we open our doord everydayu from 8am to 5pm")

big_restaurant =Restuarant("philip_lounge", "frech")

big_restaurant.describe_restuarant()
big_restaurant.open_restuarant()
