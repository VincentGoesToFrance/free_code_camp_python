class Rectangle:
    def __init__(self, *args):
        
        if len(args) == 1:
            self.width = args[0]
            self.height = args[0]
        if len(args) == 2:
            self.width = args[0]
            self.height = args[1]
        self.area = self.width * self.height
        self.perimeter = 2 * self.width + 2 * self.height
        self.diagonal = (self.width ** 2 + self.height ** 2) ** .5

    def __str__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return self.area
    
    def get_perimeter(self):
        self.perimeter = 2 * self.width + 2 * self.height
        return self.perimeter
    
    def get_diagonal(self):
        self.diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return self.diagonal
    
    def get_picture(self):
        pic_string = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for _ in range(self.height):
            pic_string += self.width * "*" + "\n"
        return pic_string
    
    def get_amount_inside(self, Rectangle):
        Rectangle.get_area()
        self.get_area()
        return int(self.area / Rectangle.area)

class Square(Rectangle):
    
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return f"{self.__class__.__name__}(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_height(self, height):
        self.width = height
        self.height = height
    
    def set_width(self, width):
        self.width = width
        self.height = width

