import copy
import random

class Hat:
    def __init__(self, **kwargs):
        if not kwargs:
            raise ValueError("Hat needs at least one ball")
        self.contents = [key for key, val in kwargs.items() for ball in range(val)]

    
    def draw(self, x):
        draw_list = []
        if x >= len(self.contents):
            draw_list = copy.copy(self.contents)
            self.contents = []
        else:
            for _ in range(x):
                random_number = random.randint(0, len(self.contents)-1)
                draw_list.append(self.contents[random_number])
                self.contents.pop(random_number)
        return draw_list
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hits = 0
    experiment_failed = False
    copy_hat = copy.deepcopy(hat)
    for _ in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        draw_list = copy_hat.draw(num_balls_drawn)
        for key in expected_balls:
            if draw_list.count(f"{key}") < expected_balls[f"{key}"]:
                experiment_failed = True
        if not experiment_failed:
            hits += 1
        experiment_failed = False
    probability = hits / num_experiments
    return probability
