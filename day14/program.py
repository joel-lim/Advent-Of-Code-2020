from abc import ABC, abstractmethod


class Program(ABC):
    def execute(self, instruction):
        if instruction[:4] == 'mask':
            bitmask = instruction[instruction.index('=') + 2:]
            self.change_bitmask(bitmask)
        else:
            idx = int(instruction[instruction.index(
                '[') + 1:instruction.index(']')])
            val = int(instruction[instruction.index('=') + 2:])
            self.write_mem(idx, val)

    def get_sum(self):
        return sum(self.mem.values())

    @abstractmethod
    def change_bitmask(self, bitmask):
        pass

    @abstractmethod
    def write_mem(self, idx, val):
        pass


class ProgramV1(Program):
    def __init__(self):
        self.bitmask_and = None
        self.bitmask_or = None
        self.mem = {}

    def change_bitmask(self, bitmask):
        self.bitmask_and = int(bitmask.replace('X', '1'), 2)
        self.bitmask_or = int(bitmask.replace('X', '0'), 2)

    def write_mem(self, idx, val):
        self.mem[idx] = self.apply_bitmask(val)

    def apply_bitmask(self, val):
        new_val = val & self.bitmask_and | self.bitmask_or
        return new_val


class ProgramV2(Program):
    def __init__(self):
        self.bitmask_or = None
        self.x_pos = []
        self.mem = {}

    def change_bitmask(self, bitmask):
        self.bitmask_or = int(bitmask.replace('X', '0'), 2)
        self.x_pos = [35 - i for i, char in enumerate(bitmask) if char == 'X']

    def write_mem(self, idx, val):
        idxes = self.apply_bitmask(idx)
        for idx in idxes:
            self.mem[idx] = val

    def apply_bitmask(self, idx):
        new_idx = idx | self.bitmask_or
        idxes = set()
        idxes.add(new_idx)
        for i in self.x_pos:
            bitmask = 1 << i
            new_idxes = set()
            for idx in idxes:
                new_idxes.add(idx | bitmask)
                new_idxes.add(idx & ~bitmask)
            idxes = new_idxes

        return idxes
