#Jonathan Kelly, Jonathan.kelly2@marist.edu
# draws a target and gives points based on rings clicked

from graphics import *
import math

def inCircle(pt1, circle):

    x = pt1.getX() - circle.getCenter().getX()
    y = pt1.getY() - circle.getCenter().getY()
    dist = math.sqrt(x*x + y*y)
    
    #uses distance formula to get distance between the point clicked and the center of the circle
    #If that distance is less than the radius than you clicked inside the circle and proper points are awarded
    
    return dist <= circle.getRadius()


def main():
    
    score = 0
    
    win = GraphWin()
    circle1 = Circle(Point(100,100), 10)
    circle1.setFill("yellow")
    circle1.setOutline("yellow")
    
    circle2 = Circle(Point(100,100), 20)
    circle2.setFill("red")
    circle2.setOutline("red")
    
    circle3 = Circle(Point(100,100), 30)
    circle3.setFill("blue")
    circle3.setOutline("blue")
    
    circle4 = Circle(Point(100,100), 40)
    circle4.setFill("black")
    circle4.setOutline("black")
    
    circle5 = Circle(Point(100,100), 50)
    circle5.setFill("white")
    circle5.setOutline("black")
    
    circle5.draw(win)
    circle4.draw(win)
    circle3.draw(win)
    circle2.draw(win)
    circle1.draw(win)
 
    for x in range(5):
        click = win.getMouse()
        
        if(inCircle(click, circle1)):
            score += 9
            print("+9")
        elif(inCircle(click, circle2)):
            score += 7
            print("+7")
        elif(inCircle(click, circle3)):
            score += 5
            print("+5")
        elif(inCircle(click, circle4)):
            score += 3
            print("+3")
        elif(inCircle(click, circle5)):
            score += 1
            print("+1")
            
    print(score)
    
    win.getMouse()
    
        
main()