book=dict() #add new hash table: fruit prices ''

book["apple"]=0.99
book["pear"]=1.49
book["banana"]=0.55

print(book)
print(book["banana"])

phoneBook={} #add new hash table

phoneBook["katie"]=2123334455
phoneBook['emergency']=911
phoneBook["erva"]=2167773344

val=phoneBook.get("cem")
print(val)

contacts={} #add new hash table

def checkName(name):
	if contacts.get(name):
		print("In the list!")
	else:
		contacts[name]=True
		print("Added to the list!")
		
checkName("Erva")
checkName("Erva")

#Breadth-first Search Example
#Find the apple seller whose name ends with k
graph = {}
graph["you"] = ["erva","katie","jane"]
graph["erva"]=["jack","adam"]
graph["jane"]=["matt","alif"]
graph["katie"]=[]
graph["matt"]=[]
graph["jack"]=[]
graph["adam"]=[]
graph["alif"]=[]


def person_is_seller(name):
    return name[-1] == 'k'
    
from collections import deque
search_queue = deque()
search_queue += graph["you"]
searched=[]
    
while search_queue:
	person=search_queue.popleft()
	if not person in searched:
		if person_is_seller(person):
			print(person+" is a apple seller!")
		else:
			search_queue += graph[person]
			searched.append(person)
print(searched)
