from graphix import Window, Point, Circle, Line, Rectangle, Polygon, Text, Entry


# Function to draw a rectangle with specified parameters
def draw_rectangle(win, point1, point2, colour):
    rect = Rectangle(point1, point2)
    rect.fill_colour = colour
    rect.outline_colour = colour
    rect.draw(win)

# Function to draw a circle with specified parameters
def draw_circle(win, center, radius, colour):
    circle = Circle(center, radius)
    circle.fill_colour = colour
    circle.outline_colour = colour
    circle.draw(win)  

def triangle(win,points,tl,colour):
    triangle = Polygon(points)
    triangle.fill_colour = "white"
    triangle.outline_colour = "white"
    triangle.draw(win)
  



def plain_patch(win,tl,colour):
    point1 = tl
    point2 = Point(tl.x + 100,tl.y + 100)
    draw_rectangle(win, point1, point2,colour)

def pen_patch(win, tl, colour):
    point1 = tl
    point2 = Point(tl.x + 100, tl.y + 100) 

    draw_rectangle(win, point1, point2, "white")
    flag = True
    for Y in range(0, 100, 20): # starts at 0, stops at 100, counts at 20
        for X in range(0, 100, 20):
            if (flag == True): # if true, draws rectangles
                # Draw rectangle
                point1 = Point(X + tl.x, Y + tl.y) # top left
                point2 = Point(X + tl.x + 20, Y + tl.y + 20)  # 20 tile size
                draw_rectangle(win, point1, point2, colour)
            else:
                # Draw circle
                center = Point(X  + tl.x + 10, Y + tl.y + 10) # 10 radius
                draw_circle(win, center, 10, colour)
                
                if Y in [0, 40, 80]: # listing the rows
                    points = [
                    Point(X  + tl.x,Y + tl.y), # top
                    Point(X  + tl.x,Y + tl.y + 20),            
                    Point(X  + tl.x + 10, Y + tl.y + 10)  
                    ]
                    triangle(win,points,tl,colour)
                  
                else:
                    points = [
                    Point(X  + tl.x+ 20, Y + tl.y),
                    Point(X  + tl.x + 20, Y  + tl.y + 20),
                    Point(X  + tl.x + 10, Y + tl.y + 10)
                    ]
                    triangle(win,points,tl,colour)
                    
            flag = not flag
            
    border = Rectangle(tl, Point(100 + tl.x, 100 + tl.y))
    border.draw(win)
    



    
def final_patch(win,tl,colour):
    point1 = tl
    point2 = Point(tl.x + 100,tl.y + 100) 
   
    draw_rectangle(win, point1, point2, "white")
   
    for i in range(0,101,10): # 0 to 101 but counts in 10s
        line = Line(Point(point1.x + i, point1.y),Point(point2.x, point2.y + i - 100) ) # left edge to right edge. point.1 + i, adds up in 10s.
        line.outline_colour = colour
        line.draw(win)
        
        line2 = Line(Point(point1.x, point1.y - i + 100),Point(point2.x - i, point2.y) )
        line2.outline_colour = colour
        line2.draw(win)
        
  
def draw_patchwork(win, size, colours):
    flag = True
    for Y in range(0, 100 * size, 100):
        for X in range(0, 100 * size, 100):
            tl = Point(X, Y)

            # Diagonal patches
            if X == Y:
                if X == 0 or X == size * 100 - 100:  # Top-left or bottom-right corners
                    colour = colours[0]  # Top-left uses first colour
                else:
                    colour = colours[2]  # Bottom-right uses third colour
                final_patch(win, tl, colour)

            # Top and bottom rows
            elif Y == 0 or Y == size * 100 - 100:
                if flag: # alternate colours
                    colour = colours[0]  
                else:
                    colour = colours[1]
                pen_patch(win, tl, colour)

            # Left and right columns
            elif X == 0 or X == size * 100 - 100:
                if flag: 
                    colour = colours[0]  
                    pen_patch(win, tl, colour)
                else:
                    colour = colours[1]
                    plain_patch(win, tl, colour)

           
            elif Y in [200, 400, 600]: #specific rows
                if flag:
                    colour = colours[2]
                    pen_patch(win, tl, colour)
                else:
                    colour = colours[2]
                    pen_patch(win, tl, colour)

            # The rest of the tiles is plain
            else:
                plain_patch(win, tl, colours[2])  # Use plain patches for inner tiles

            # Toggle flag for alternating colours
            flag = not flag

    # Wait for a click before closing
    win.get_mouse()
    win.close()
 
def main():
    only_colours = ["red", "green", "blue", "magenta", "orange", "purple"]
    colours = []
    while len(colours) < 3: # Length of colours less than 3
        colour = input(f"Enter listed colours {only_colours}: ") 
        if colour not in colours:
            colours.append(colour)# adds only colours to the array that can be recovered by input
        else:
             print(f"You entered an duplicated colour, please enter another colour.")
    
      
    numbers = [5,7,9]
    while True: # condition loop
        size = int(input(f"Enter a size {numbers}: "))
        if size in numbers: 
            break 
        else:
            print("Invalid number, please enter again")
           
    win = Window("Patchwork Coursework", 100 * size, 100 * size)
    

    draw_patchwork(win,size,colours)
     



main()

# def challenge(win,colour, size):
#     point1 = tl
#     point2 = Point(tl.x + 100,tl.y + 100) 
#    
#     
#     tl = Point (x * size, y * size) 
#     point2 = Point((tl.x + 1) * size, (tl.y + 1) * size)
#     while True:
#         key = win.get_key()
#         
#         click = win.get_mouse()
#         if key == 1 and 2 and 3:
#              colour = ["red", "green", "blue"]
#              pen_patch(win, tl, colour)
#         elif key == 4 and 5 and 6:
#             colour = ["red", "green", "blue"]
#             final_patch(win, tl, colour)
#         elif key == 7 and 8 and 9:
#             colour = ["red", "green", "blue"]
#             plain_patch(win,tl,colour)
#             else :
#                 x
                
                
                
            
            
             
            
     

    
    
        
    
    
    
    
