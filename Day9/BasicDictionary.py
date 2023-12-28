#Define a dictionary

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

#Add new key called satish and value called Data engineer solution Architect
programming_dictionary["satish"]="Data engineer solution Architect"
print(programming_dictionary)

#Edit an current item
programming_dictionary["Function"] = "New Year 2024"

#print the keys and values in the dictionary
for key, value in programming_dictionary.items():
    print(key)
    print(value)

captials = {
    "usa" : "Washington",
    "india": "Delhi"
}

#Nested Dictinoary in a Dictionray
# Key would have list or dictionaries
travel_log={
    "France": {"citiesvisited2024":["Paris", "lile", "bhot"]},
    "India": {"citiesvisited2023":["chennai", "Delhi", "ooty"]}
}
#Nested Dictionary in a list
travel_log = [
    {"country": "france",
     "citiesvisited2024":
         ["Paris", "lile", "bhot"]
     },
    {"country": "India",
     "citiesvisited2024":
         ["chennai", "Delhi", "Maduria"]}
]