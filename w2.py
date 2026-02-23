
import random 


class Action:
    def __init__(self, name, utility, isDirty, location):
        self.name = name
        self.utility = utility
        self.isDirty = False
        self.location = ""

class Agent:
    def __init__(self):
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    def choose_action(self):
        best_action = None
        max_utility = float('-inf')

        for action in self.actions:
            if action.utility > max_utility:
                max_utility = action.utility
                best_action = action

        return best_action

# Example usage:
if __name__ == "__main__":
    agent = Agent()
    
    def weighted_bool(prob_true):
        return random.choices([True, False], weights=[prob_true, 1-prob_true], k=1)[0]

    isDirtyA = weighted_bool(0.4)
    isDirtyB = weighted_bool(0.2)
    print(isDirtyA)
    print(isDirtyB)
    

    # Define actions with their utilities
    action1 = Action("Go left", 1)
    action1.isDirty = isDirtyA
    action2 = Action("Go right", 1)
    action2.isDirty = isDirtyB
    action3 = Action("Clean", 1)
    action3.isDirty = isDirtyA

    # Add actions to the agent
    agent.add_action(action1)
    agent.add_action(action2)
    agent.add_action(action3)

    # Choose the best action based on utility
    best_action = agent.choose_action()
    print("Best action:", best_action.name)