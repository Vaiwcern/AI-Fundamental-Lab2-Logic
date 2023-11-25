from typing import List
from Clause import Clause

class KnowledgeBase: 
    def __init__(self, list_clause: List[Clause]) -> None:
        self.list_clause = list_clause

    def __str__(self) -> str:
        return "\n".join(str(clause) for clause in self.list_clause)

    def getLen(self) -> int: 
        return len(self.list_clause)

    def PL_resolution(self, alpha: 'Clause'): 
        # insert the negative alpha into list of clauses
        clause_map = {clause.key(): clause for clause in self.list_clause}
        for atom in alpha.list_Atom: 
            atom.getOpposite()
            clause_map[Clause([atom]).key()] = Clause([atom])
        
        lst_KB = []
        collision_found = False
        while True: 
            resolvents = {}
            
            found_new = False
            for key1, C1 in clause_map.items(): 
                for key2, C2 in clause_map.items():
                    if key1 < key2: 
                        res = C1.PL_resolve(C2)
                        if res[0] == True:
                            if res[1].isEmpty(): 
                                    collision_found = True
                                
                            if (res[1].key() not in clause_map
                                and res[1].key() not in resolvents): 
                                resolvents[res[1].key()] = res[1]
                                found_new = True

            lst_KB.append(KnowledgeBase(resolvents.values()))
            for key, value in resolvents.items(): 
                clause_map[key] = value

            if collision_found or not found_new: 
                break

        if collision_found: 
            return ["YES", lst_KB]
        return ["NO", lst_KB]