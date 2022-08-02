def display_message():
    print("i am learning about functions")
display_message()    

def favorite_book(tittle):
    print(f"One of my favorit book is {tittle.title()}")
favorite_book('alice')

def make_shirt(size, text):
    print(f"\ni need an {size.title()}")
    print(f"\nThe {size.title()} should have a {text.title} message written on it ")

make_shirt('extra large', 'happy birthday')
make_shirt('size', 'i love python')


def describe_city(city, country="germany"):
    print (f"{city.title()} is a beautiful city")
    print(f"it is found in {country.title()}")

describe_city(city='berlin')
describe_city(city="younde", country="cameroon")
describe_city("los angeles", "america")

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician=get_formatted_name('jimi', 'hendrix')
print(musician)

def buld_person(first_name, last_name):
    person ={'first': first_name, 'last': last_name}
    return person
me = buld_person("Ngwa", "Jude")
print(me)

def get_formateed(first, last):
    full_name = f"{first} {last}"
    return full_name.title()
    
while True:
        print("\n enter your name: ")
        print ("enter 'p' to end")
        first =input("first name ")
        last = input("last name ")
        if first == 'p':
            break
        if last =='p':
            break


def city_country(city , country):
    place=f"{city} {country}"
    return place.title()
place_1=print(city_country('younde', 'cameroon'))
place_2=print(city_country('new york', 'america'))
place_3=print(city_country('paris', 'france'))

def make_album(artist, album):
    musician={'Artist': artist, 'album': album}
    return musician
musician =print(make_album("Micheal-learns", "to rock, killed, love, death"))