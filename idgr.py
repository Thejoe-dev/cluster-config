from random import randint

class RandomSet:

    def __init__(self):
        self.values = []
        self.values_idx = {}

    def insert(self,val: int) -> bool:
        if val in self.values:
            return False
        self.values.insert(val)
        self.values_idx[val] = len(self.values)
        return True

    # Code I would actually write
    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False
        self.values.remove(val)
        del self.values_idx[val]
        return True

    # Code I would not write as its overly complicated to read and maintain for the future. There is a tradeoff here you have
    # to make sometimes in the real world between speed and readability/maintainability. And thats a decision you make as a team
    def remove_alt(self, val: int) -> bool:
        if val not in self.values:
            return False
        val_idx = self.values_idx[val]
        last_val = self.values[-1]
        self.values_idx[last_val] = val_idx
        self.values[val_idx] = last_val
        self.values.pop()
        del self.values_idx[val]
        return True

    def get_random(self) -> int :
        rand_val: int = randint(0, len(self.values)-1)
        return self.values[rand_val]