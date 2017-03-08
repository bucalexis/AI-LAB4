import fileinput
from Node import Node 
from Query import Query
from sets import Set

class InputReader():

    def searchNode(self, name, nodes):
        for node in nodes:
            if name in node.name:
                return  node;
        return False

    def read(self):
        nodes = []
        queries = []
        input = fileinput.input()
        state = ""

        for line in input:
            line = "".join(line.split())
            if "Nodes" in line:
                line = ""
                state = "readNode"
            if "Probabilities" in line:
                line = ""
                state = "readProb"
            if "Queries" in line:
                line = ""
                state = "readQuery"

            if  state == "readNode" and line:
                nodeNames = line.split(",")
                for name in nodeNames:
                    nodes.append(Node(name))

            if  state == "readProb" and line:
                if "|" in line:
                    nodeName, other = line.split("|")
                    childNode = self.searchNode(nodeName[1:], nodes)
                    evidence, probability = other.split("=")
                    parents = evidence.split(",")
                    tableRow = Set([])
                    for parent in parents:
                        parentNode = self.searchNode(parent[1:], nodes)
                        childNode.parents.add(parentNode)
                        parentNode.childs.add(childNode.name)
                        tableRow.add(parent)

                    childNode.table.append([tableRow,probability])
                else:
                    nodeName, probability = line.split("=")
                    tableRow = Set([])
                    node = self.searchNode(nodeName[1:], nodes)
                    tableRow.add(nodeName[0])
                    node.table.append([tableRow,probability])

            if  state == "readQuery" and line:
                if "|" in line:
                    query = Query()
                    queryNodes, evidenceNodes = line.split("|")
                    for node in queryNodes.split(","):
                        query.queries.append(node)
                    for node in evidenceNodes.split(","):
                        query.evidence.append(node)
                    queries.append(query);
                else:
                    query = Query()
                    for node in line.split(","):
                        query.queries.append(node)
                    queries.append(query)

        return nodes, queries

