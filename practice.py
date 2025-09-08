list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("first: " + str(list[0]))
print("last: " + str(list[-1]))
print("middle: " + str(list[4]))
list.append(11)
list[2] = 99
for i in list:
    if(i%2 == 0):
        print(i)


capitals = {
    "Afghanistan": "Kabul",
    "Italy": "Rome",
    "USA": "Washington DC",
    "Mexico": "Mexico City",
    "Japan": "Tokyo"
}
print(capitals["Afghanistan"])
print(capitals["Mexico"])
capitals["Afghanistan"] = "Afghanistan City"
for i in capitals:
    print(capitals[i])



fruits1 = {"dragonfruit", "banana", "kiwi", "lemon", "lime"}
fruits2 = {"dragonfruit", "apple", "mango", "lemon", "lime"}
print(fruits1.intersection(fruits2))
newSet = fruits1.symmetric_difference(fruits2)
for i in newSet.copy():
    if(i in fruits2):
        newSet.remove(i)
print(newSet)
