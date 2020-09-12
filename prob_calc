import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.balls = kwargs
    self.contents = [k for k, v in kwargs.items() for v in range(0, v)]   

  def draw(self, number_to_draw):
    if number_to_draw > len(self.contents):
      return self.contents
    else:
      draw_list = []
      length = len(self.contents)-1
      for x in range(0, number_to_draw):
        p = self.contents.pop(random.randint(0, length))
        draw_list.append(p)
        length -= 1
      
      return draw_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  denominator = num_experiments
  numerator = 0
  expected_ball_list = [k for k, v in expected_balls.items() for v in range(0, v)]

  for x in range(0, num_experiments):
    hat0 = copy.deepcopy(hat)
    expected_ball_list0 = copy.deepcopy(expected_ball_list)
    drawn = hat0.draw(num_balls_drawn)
    success = 0
    for expected_ball in expected_ball_list0:
      try:
        drawn.remove(expected_ball)
        success += 1
      except:
        break;
    if success == len(expected_ball_list0):
      numerator += 1  

  return round(numerator/denominator, 3)

