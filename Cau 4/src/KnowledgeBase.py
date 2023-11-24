from Clause import Clause
from typing import List

class KnowledgeBase: 
    def __init__(self, list_clause: List[Clause]) -> None:
        self.list_clause = list_clause

    def __str__(self) -> str:
        return "\n".join(str(clause) for clause in self.list_clause)

    def getLen(self) -> int: 
        return len(self.list_clause)

    def PL_resolution(self, alpha: 'Clause'): 
        # insert the negative alpha into list of clauses
        lst_clause_tmp = self.list_clause
        for atom in alpha.list_Atom: 
            atom.getOpposite()
            lst_clause_tmp.append(Clause([atom]))
        
        lst_KB = []
        collision_found = False
        while True: 
            resolvents = []
            
            found_new = False
            for i in range(0, len(lst_clause_tmp)):
                for j in range(i + 1, len(lst_clause_tmp)):
                    # print(i, j)
                    C1 = lst_clause_tmp[i]
                    C2 = lst_clause_tmp[j]

                    # print(C1)
                    # print(C2)
                    # print()
                    res = C1.PL_resolve(C2)
                    if res[0] == True:
                        # print(res[1])
                        if res[1].isEmpty(): 
                                collision_found = True
                            
                        if (res[1] not in lst_clause_tmp
                            and res[1] not in resolvents): 
                            resolvents.append(res[1])
                            print(C1, "|", C2, "|", res[1])
                            found_new = True

            if not found_new: 
                break

            lst_KB.append(KnowledgeBase(resolvents))
            for clause in resolvents: 
                lst_clause_tmp.append(clause)

            if collision_found: 
                break

        if collision_found: 
            return [True, lst_KB]
        return [False, []]