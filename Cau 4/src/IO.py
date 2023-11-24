from Atom import Atom
from Clause import Clause
from KnowledgeBase import KnowledgeBase

class IO:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(self.file_path, 'r')
        self.line = 0

    def __enter__(self):
        return self

    def __exit__(self):
        self.close()

    def close(self):
        self.file.close()

    def readLine(self):
        self.line += 1
        return self.file.readline()
    
    def readClause(self) -> Clause:     
        nxtLine = self.readLine()
        lst = nxtLine.split()
        list_Atom = []
        for str in lst: 
            if str != "OR": 
                list_Atom.append(Atom(str))
        return Clause(list_Atom)
    
    def readKB(self) -> KnowledgeBase: 
        numLine = int(self.readLine().split()[0])
        list_clause = []
        for i in range(numLine): 
            list_clause.append(self.readClause())
        return KnowledgeBase(list_clause)
    
    def writeKB(self, KB: 'KnowledgeBase'): 
        print(KB.getLen())
        print(KB)
    