#working with varaibles
message="you are useless"

message="reall use less"
print(message)

#working with strings
first_name="ada lovelace"
last_name ="Jude"
print(first_name.title()) #using the .title methiod to change the case of the case
print(first_name.upper()) #changinr the entire first_name to upper case
print(first_name.lower()) #Changing all to lowe case

print(f"{first_name} {last_name.title()}") #using formated string 

print("languages: Python \n java \n c\n R") #Using the escape character \n to move to a new line

from email.policy import strict


name ="Eric"
print(f"Hello {name} would you like to learn some python today?")
print(name.title())
print(name.upper())
print(name.lower()) 

famous_person = "Albert Einstein"
print(f"{famous_person} once said, 'A person who never made a mistake never tried anything new'")
stripping =" Jude "
print(f"name:\n {stripping}")
print(stripping.rstrip())
print(stripping.strip())
print(stripping.lstrip())
