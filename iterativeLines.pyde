

class CustomLine():
    def __init__(self, current, iterations):
        self.current = current
        self.iterations = iterations
        
    def pattern(self):
        for i in range(self.iterations):
            x, y = self.current
            self.current[0] += sin(i)*16
            self.current[1] += cos(i)*16
            line(x,y, self.current[0], self.current[1])
            if (round(x) > width) | (round(y) > height):
                self.current[0] = width/2
                self.current[1] = height/2
                self.iterations += 1
                self.pattern()
            
    def mirror(self):
        x = self.current[0]
        y = self.current[1]
        self.current[1] = x
        self.current[0] = y

def setup():
    size(1280, 720)
    background(240)
    global CENTER, linelist, baking, myline
    baking = 0
    CENTER = [width/2, height/2]
    # make a list of my line objects
    # linelist = [CustomLine(CENTER, i) for i in range(20)]
    # print(linelist)
    myline = CustomLine(CENTER, 1)
    


def draw():
    strokeWeight(2)
    color(20, 20, 100)
    global baking, myline
    # if baking < 19:
    #     baking += 1
    # else:
    #     baking = 0
    # if baking == 10:
    #     linelist[baking].mirror()
    myline.pattern()
    
