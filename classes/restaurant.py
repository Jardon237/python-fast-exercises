class Restuarant:

    def __init__(self,name,type,):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restuarant(self):
        print(f"welcome to {self.name.upper()} restuarant" )
        print(f"we have {self.type.title()} cusine available for today")

    def open_restuarant(self):
        print("we open our door everydayu from 8am to 5pm")

    def restuarant(self):
        print(f"number of customers serverd are{self.number_served}")
        
    def increment_number_served(self, plus):
        self.number_served += plus


big_restaurant =Restuarant("philip_lounge", "frech")
small_restaurant=Restuarant("janna", "affrican")
big_restaurant.describe_restuarant()
big_restaurant.open_restuarant()
small_restaurant.describe_restuarant()
big_restaurant.number_served = 6
big_restaurant.restuarant()
big_restaurant.increment_number_served(6)

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"This is {self.first_name.title()} {self.last_name.title()}  a 15 years old and is in good heathcondition")
    def greet_user(self):
        print(f"Hi {self.first_name.title()} {self.last_name.title()}")

user_1=User("ngwa", "jude")
user_2=User('nfon', 'andrew')
user_3=User('ankini', "muso")
user_4= User('me', 'you')

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user
user_3.describe_user()
user_3.greet_user()
user_4.describe_user()
user_4.greet_user()