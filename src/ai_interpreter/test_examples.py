from src.ai_interpreter.parser import parse_instruction

TEST_INSTRUCTIONS = [
    "Ensure the O-ring is present and seated correctly.",
    "Verify that four screws secure the motor housing.",
    "Visually inspect PCB for missing components."
]

for instr in TEST_INSTRUCTIONS:
    print("\nInstruction:", instr)
    print(parse_instruction(instr))
