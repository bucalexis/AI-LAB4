from sets import Set

class Node():
    def __init__(self, name):
    	self.name = name
    	self.parents = Set([])
    	self.childs = Set([])
    	self.table = []

    