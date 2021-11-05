# importing python turtle library
import turtle


class Rangoli:
    # constructor to initise the number of iteration and the backgeound color
    def __init__(self, num_iters, bgcolor="black"):
        s.bgcolor(bgcolor)
        # running the pen at the fastest speed
        t.speed(0)
        # initialised number of iterationa
        self.num_iters = num_iters
        # started with a primary color
        r, g, b = 255, 0, 0
        self.color = [r, g, b]

    # a function to generate chnaged rgb color codes bases on the index given
    # max allowed pixel value is 255
    def get_color(self, i):
        # more blue shade is added for index values less than (1/3)*max_pixel
        if(i < 255//3):
            self.color[1] += 3
        # red shade is decreased for index values less than (2/3)*max_pixel and greater than (1/3)*max_pixel
        elif(i < 2*255//3):
            self.color[0] -= 3
        # green shade is increased for index values greater than (2/3)*max_index
        elif(i < 255):
            self.color[2] += 3
        # tuple containg the modified color returned
        return (self.color[0], self.color[1], self.color[2])

    def draw_design(self):
        for i in range(self.num_iters):
            # color mode set to rgb max_pixel 255
            s.colormode(255)
            # move the pen forwars 100+i units
            t.fd(100+i)
            # move pen right 100 units
            t.rt(100)
            # set the modified color to the pen
            t.pencolor(self.get_color(i))
        # triggers the exit from programme on click
        s.exitonclick()


if __name__ == "__main__":
    # created a global instance of turtle
    t = turtle.Turtle()
    # ceated a global instance of screen
    s = turtle.Screen()
    t.hideturtle()
    # created an instance of rangoli
    R = Rangoli(num_iters=300)
    R.draw_design()
