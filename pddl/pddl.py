from .parser import PDDL_Parser
from .planner import Planner

class PDDL:
    def __init__(self, domain_path, problem_path):
        self.parser = PDDL_Parser()
        self.planner = Planner()
        self.parser.parse_domain(domain_path)
        self.parser.parse_problem(problem_path)

    def plan(self):
        return self.planner.solve(self.parser)

    # example for new_state: frozenset({('on', 'light1'), ('at', 'room1')})
    def set_state(self, new_state):
        self.parser.state = new_state

if __name__ == '__main__':
    pddl = PDDL("../AIPlanning/Domain.pddl", "../AIPlanning/Problem.pddl")
    plan = pddl.plan()
    print(plan)
    if plan != None:
        for action in plan:
            print(action)