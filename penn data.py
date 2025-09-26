import pandas as pd
import random
fNames = ["tom", "danny", "chris", "matt", "mathew", "gorbino", "donald", "benedict", "richard", "andrew", "joe", "john", "james", "noah", "owen", "dave", "maddy", "angelina", "jenny", "madson", "patty", "marge"]
lNames = ["putman", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "li", "gi", "smith", "smells", "like", "handover", "riso", "wisseaux", "jacqueline", "dav", "lamar", "smithers", "elvis", "presley", "president", "king", "cobain", "kurt", "jackson", "friedmann", "fripp"]
years = ["freshman", "sophmore", "junior", "senior", "super senior", "super duper senior", "uncommon senior", "rare senior", "epic senior", "legendary senior"]
pathways = ["early college", "engineering", "CS", "business", "marketing", "early childhood education", "culinary", "criminal justice", "construction", "biomed", "evil", "batman", "mud", "shovel", "quantum dentistry", "geologic morphology of squid ink within the martian cerebellum due", "dumb", "watergate", "mario", "luigi", "bowser", "applesauce", "amazon", "a", "b", "aa", "aaaa", "kendrick lamar", "stupid dumb idiot supid dumb"]
names = []
for i in range(200):
    names.append(f"{random.choice(fNames)} {random.choice(lNames)}")
print(names)

data = {
    "name": names,
    "age": [random.randint(14, 92500000000000000000000000000000000000000000000000000000000000000000000000000000000000002) for _ in names],
    "gpa": [round(random.uniform(0.0, 100000.0),2) for _ in names],
    "credits completed": [random.randint(0, 1000000000000000) for _ in names],
    "year":  [random.choice(years) for _ in names],
    "pathway": [random.choice(pathways) for _ in names]
}
print(data)
pennData = pd.DataFrame(data)
print(pennData)
pennData.to_csv('dataFrame.csv', index=False)
readableData = pennData.describe()
print(readableData)