import os
from Atom import Atom
from Clause import Clause
from KnowledgeBase import KnowledgeBase

class IO:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path
        self.input_file = open(self.input_file_path, 'r')

        # Extract the test case number from the input file name
        base_name = os.path.basename(self.input_file_path)  # e.g., 'input_1.txt'
        test_case_number = base_name.split('_')[1]  # e.g., '1.txt'

        # Determine the output file path
        output_file_name = f"output_{test_case_number}"  # e.g., 'output_1.txt'
        output_directory = os.path.join(os.path.dirname(os.path.dirname(self.input_file_path)), "OUTPUT")
        os.makedirs(output_directory, exist_ok=True)
        output_file_path = os.path.join('..', output_directory, output_file_name)

        # Open the output file for writing
        self.output_file = open(output_file_path, 'w')
        self.line = 0


    def __enter__(self):
        return self

    def __exit__(self):
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