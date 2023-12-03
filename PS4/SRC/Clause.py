from typing import List
from Literal import Literal

class Clause: 
    def __init__(self, list_Atom: List[Literal]) -> None:
        self.list_Atom = list_Atom

    def __str__(self) -> str:
        if self.isEmpty(): 
            return "{}"
        return " OR ".join(str(atom) for atom in self.list_Atom)
    
    def __eq__(self, other):
        if not isinstance(other, Clause):
            return False
        return self.list_Atom == other.list_Atom

    def sort(self) -> None:
        self.list_Atom = sorted(self.list_Atom, key=lambda atom: atom.value[-1])

    def isEmpty(self) -> bool: 
        return len(self.list_Atom) == 0
    
    def key(self) -> str: 
        return ' '.join(str(atom) for atom in self.list_Atom)

    def PL_resolve(self, other : 'Clause'): 
        pos = [False for _ in range(26)]
        neg = [False for _ in range(26)]

        cnt_complementary = 0
        totalClause = self.list_Atom + other.list_Atom
        for atom in totalClause:
            num = atom.getNum()
            if atom.isNegative(): 
                neg[num] = True
            else: 
                pos[num] = True
            if neg[num] and pos[num]: 
                cnt_complementary += 1
        
        if cnt_complementary != 1: 
            return [False, []]

        newList = []
        for i in range(26): 
            if pos[i] != neg[i]: 
                atom = chr(ord('A') + i)
                if neg[i]: 
                    atom = '-' + atom
                newList.append(Literal(atom))

        return [True, Clause(newList)]
            