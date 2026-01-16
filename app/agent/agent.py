from app.agent.planner import Planner
from app.agent.executor import Executor
from app.agent.evaluator import Evaluator
from app.agent.memory import Memory

class AutonomousAgent:
    def __init__(self):
        self.planner = Planner()
        self.executor = Executor()
        self.evaluator = Evaluator()
        self.memory = Memory()

    def run(self, goal):
        steps = self.planner.plan(goal)
        for step in steps:
            result = self.executor.execute(step)
            success = self.evaluator.evaluate(step, result)
            self.memory.store(step, result, success)
