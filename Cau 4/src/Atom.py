class Atom: 
    def __init__(self, value) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return self.value

    # def sameElement(self, other) -> bool: 
    #     return self.value[-1] == other.value[-1]
    
    # def isOpposite(self, other) -> bool: 
    #     return (len(self.value) + len(other.value) == 3 
    #             and self.sameElement(other))
    
    def getOpposite(self): 
        if self.value[0] == '-': 
            self.value = self.value[1:]
        else:
            self.value = '-' + self.value

    def getNum(self) -> int: 
        return ord(self.value[-1]) - ord('A')
    
    def isNegative(self) -> bool: 
        return self.value[0] == '-'