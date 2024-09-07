import pgzrun
WIDTH=500
HEIGHT=500
red=255,0,0
rect=Rect((20,20),(100,100))

def draw():
    screen.clear()
    screen.fill('white')
    screen.draw.filled_circle((200,200),30,(0,0,255))
    screen.draw.filled_(rect,red)
    screen.draw.filled_square((rect),30,(255,10,100))
    screen.draw.filled_triangle(250,250),20,(red)


pgzrun.go()