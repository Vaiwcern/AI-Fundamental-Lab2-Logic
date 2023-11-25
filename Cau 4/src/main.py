import sys
from Atom import Atom
from Clause import Clause
from IO import IO  
from KnowledgeBase import KnowledgeBase

def main(file_path):
    # input/output manager
    myClerk = IO(file_path)

    # read input
    alpha = myClerk.readClause()
    KB = myClerk.readKB()
    
    # PL-Resolution
    result = KB.PL_resolution(alpha)

    # write output
    myClerk.writeRes(result)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
