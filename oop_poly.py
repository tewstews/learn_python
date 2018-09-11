class Rectangle:
    def __init__(self, width, height, sign):
        self.w = int(width)
        self.h = int(height)
        self.s = str(sign)
    def __str__(self):
        rect = []
        for i in range(self.h): # количество строк
            rect.append(self.s * self.w) # знак повторяется w раз
        rect = '\n'.join(rect) # превращаем список в строку
        return rect
 
b = Rectangle(10, 10, 'o')
print(b)