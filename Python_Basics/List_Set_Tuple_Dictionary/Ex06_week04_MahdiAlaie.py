cities = {
    "Karaj": "Alborz", 
    "Tehran": "Tehran", 
    "Fardis": "Alborz", 
    "Damavand":"Tehran"
    }

states={
    
}



for city,state in cities.items():
    if state not in states:
        states[state]=[]
    states[state].append(city)

print(states)