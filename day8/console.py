from abc import ABC, abstractmethod
from enum import Enum

class Console:
    class Status(Enum):
        OK = 0
        LOOP = 1

    def __init__(self):
        self.instructions = []

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def run(self):
        end = len(self.instructions)
        executed = [False] * end
        acc = 0
        idx = 0
        while idx < end:
            # Detect loop
            if executed[idx]:
                return acc, Console.Status.LOOP
            executed[idx] = True
            instruction = self.instructions[idx]
            acc, idx = instruction.execute(acc, idx)
        return acc, Console.Status.OK

    def repair(self):
        for i, instruction in enumerate(self.instructions):
            # Swap the current instruction if it is a jump or nop
            if isinstance(instruction, JumpInstruction):
                self.instructions[i] = NopInstruction(instruction.arg)
            elif isinstance(instruction, NopInstruction):
                self.instructions[i] = JumpInstruction(instruction.arg)
            else:
                continue

            acc, status = self.run()
            if status == Console.Status.OK:
                return acc
            # Restore the original instruction
            self.instructions[i] = instruction

class Instruction(ABC):
    @abstractmethod
    def __init__(self, arg):
        self.arg = arg

    @abstractmethod
    def execute(self, acc, idx):
        pass

class JumpInstruction(Instruction):
    def __init__(self, arg):
        super().__init__(arg)

    def execute(self, acc, idx):
        return acc, idx + self.arg

class AccInstruction(Instruction):
    def __init__(self, arg):
        super().__init__(arg)

    def execute(self, acc, idx):
        return acc + self.arg, idx + 1

class NopInstruction(Instruction):
    def __init__(self, arg):
        super().__init__(arg)

    def execute(self, acc, idx):
        return acc, idx + 1

class InstructionFactory():
    instructions = {
        'jmp': JumpInstruction,
        'acc': AccInstruction,
        'nop': NopInstruction
    }

    def create_instruction(self, op, arg):
        return self.instructions[op](arg)
