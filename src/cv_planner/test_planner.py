from ai_interpreter.parser import parse_instruction
from cv_planner.planner import plan_jobs

instr = "Ensure the O-ring is present and seated correctly."
contract = parse_instruction(instr)
print("hey this is the contract made from parsing instructios:")
print(contract)
jobs = plan_jobs(contract)
print("hey this is the jobs")
print(jobs)
for job in jobs:
    print(job)
