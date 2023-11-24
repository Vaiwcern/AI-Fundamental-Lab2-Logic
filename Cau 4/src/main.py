import sys
from Atom import Atom
from Clause import Clause
from IO import IO  
from KnowledgeBase import KnowledgeBase

def main(file_path):
    records_main = IO(file_path)

    alpha = records_main.readClause()
    KB = records_main.readKB()
    result = KB.PL_resolution(alpha)

    if (result[0] == True):
        for x in result[1]: 
            records_main.writeKB(x)
    print(result[0])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
