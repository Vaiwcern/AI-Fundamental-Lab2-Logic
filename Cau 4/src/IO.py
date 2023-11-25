import os
from Atom import Atom
from Clause import Clause
from KnowledgeBase import KnowledgeBase

class IO:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path
        self.input_file = open(self.input_file_path, 'r')

        # Determine the output file path and open it
        output_file_path = self.input_file_path.replace("input", "output")
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        self.output_file = open(output_file_path, 'w')  # Open for appending
        self.line = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self.input_file.close()
        self.output_file.close()

    def readLine(self):
        self.line += 1
        return self.input_file.readline()
    
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
        self.output_file.write(str(KB.getLen()) + '\n')
        if (KB.getLen() > 0): 
            self.output_file.write(str(KB) + '\n')
    
    def writeRes(self, result): 
        for KB in result[1]:
            self.writeKB(KB)    
        self.output_file.write(result[0] + '\n')