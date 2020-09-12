class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    picture = ''
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
    else:
      for y in range(0, self.height):
        picture += ''.rjust(self.width, '*')+'\n'
      return picture

  def get_amount_inside(self, shape):
    amount = 0
    y0 = self.height
    y1 = shape.height
    x0 = self.width
    x1 = shape.width

    num_h = y0 // y1
    num_w = x0 // x1

    return num_h * num_w

  def __repr__(self):
    return 'Rectangle(width='+str(self.width)+', height='+str(self.height)+')'

     

class Square(Rectangle):

  def __init__(self, side_length):
    self.set_width(side_length)
    self.set_height(side_length)

  def set_side(self, side):
    self.set_width(side)
    self.set_height(side)

  def __repr__(self):
    return 'Square(side='+str(self.width)+')'

