import fileinput
import operator
import copy
import sys
from Node import Node 
from inputReader import  InputReader
from sets import Set
import math

nodes = []
queries = []
def searchNode(name):
	global nodes
	if "+" in name:
		name = name[1:]
	if "-" in name:
		name = name[1:]

	for node in nodes:
		if name in node.name:
			return  node;
	return False

def getRelevants(joint):
	jointNoSigns = []

	for element in joint:
		jointNoSigns.append(element[1:])

	relevants = Set([])
	visited = []
	toExpand = copy.copy(jointNoSigns)

	while toExpand:
		node = toExpand.pop(0) 
		if node not in visited:
			node = searchNode(node)
			for parent in node.parents:
				if parent.name not in jointNoSigns:
					relevants.add(parent.name)
				toExpand.append(parent.name)
			visited.append(node)
	return list(relevants)



def combinateRelevants(relevants):
	combinations = []
	if relevants:
		counter = 2
		numberElement = 1
		n = int(math.pow(2, len(relevants)))
		combinations = [[] for _ in range(n)]
		for element in relevants:
			index = 0
			for x in range(0, numberElement):
				for j in range(0, int(n / counter)):
					combinations[index].append("+" + element)
					index += 1
				for j in range(0, int(n / counter)):
					combinations[index].append("-" + element)
					index += 1
			numberElement *= 2
			counter *= 2

	return combinations


def getNodesWithoutChilds(nodes):
	nodesNoSigns = []
	withoutChilds = []
	for name in nodes:
		if "+" in name:
			name = name[1:]
		if "-" in name:
			name = name[1:]
		nodesNoSigns.append(name)

	for name in nodes:
		node = searchNode(name)
		flag = True
		for child in node.childs:
			if child in nodesNoSigns:
				flag = False
		if flag:
			withoutChilds.append(name)

	return withoutChilds




def chain(fullList):
		prob = 1.0
		probs = []
		while fullList:
			noChilds = getNodesWithoutChilds(fullList)
			for element in noChilds:
				mark = element[0]
				fullList.remove(element)
				node = searchNode(element)
				depending = copy.copy(fullList)
				erase = []
				
				parentNames = []
				for parent in node.parents:
					parentNames.append(parent.name)
				for dep in depending:
					if dep[1:] not in parentNames:
						erase.append(dep)
				for er in erase:
					depending.remove(er)
				depending = set(depending)
				if not depending:
					depending.add("+")
				for row in node.table:
					res = row[0].symmetric_difference(depending)
					if not res:
						if "+" in mark:
							prob *= float(row[1])
							probs.append(float(row[1]))
						if "-" in mark:
							prob *= 1 - float(row[1])
							probs.append(1-float(row[1]))
		mult = 1.0
		for n in probs:
			mult *= n
		return mult



def convertToJoinProb(query):
	
	numerator = copy.copy(query.queries) + copy.copy(query.evidence)
	denominator = copy.copy(query.evidence)
	relevants = getRelevants(numerator)
	combinations = combinateRelevants(relevants)

	acum = 0.0
	if combinations:
		for combination in combinations:
			fullList = numerator + combination
			acum += chain(fullList)
	else:
		fullList = numerator
		acum += chain(fullList)
	
	acumAux = 0.0
	if not denominator:
		acumAux = 1.0
	if denominator:
		relevants = getRelevants(denominator)
		combinations = combinateRelevants(relevants)
		if combinations:
			for combination in combinations:
				fullList = denominator+ combination
				acumAux += chain(fullList)
		else:
			fullList = denominator
			acumAux += chain(fullList)

	result = round(acum/acumAux,7)
	print (result)


reader = InputReader()
nodes, queries = reader.read()
for query in queries:
	convertToJoinProb(query)

#noChilds= getNodesWithoutChilds(["-Alarm", "+JohnCalls","-Earthquake", "-MaryCalls", "+Burglary"])
#noChilds= getNodesWithoutChilds(["-Earthquake", "-Alarm", "+Burglary"])
#noChilds= getNodesWithoutChilds(["-Earthquake",  "+Burglary"])



