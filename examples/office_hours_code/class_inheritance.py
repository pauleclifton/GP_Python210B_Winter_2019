class rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def area(self):
        return self.width * self.length

    def present_figure(self):
        return f'This figure has a width of {self.width}, a length of {self.length} and an area of {self.area()}'

class square(rectangle):
    #pass
    def __init__(self, side):
        super().__init__(side, side)

    #def present_square(self):
    #    return self.present_figure()

    def present_figure(self):
        return f'{super().present_figure()}. The figure is a square.'

def main():
    #first_rectangle = rectangle(10, 5)
    #print(first_rectangle.area())
    #print(first_rectangle.present_figure())


    #first_square = square(10, 10)
    first_square = square(10)
    print(first_square.area())
    print(first_square.present_figure())
    #print(first_square.present_square())


if __name__ == '__main__':
    main()