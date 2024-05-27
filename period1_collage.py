from cmu_graphics import *
from cmu_graphics import cmu_graphics 
import random

def drawCollage():
        
    distance=200
    count=1 #used to display numbers on grid
    checksum=0 #used to count total drawings added


    for i in range(1, 7):
        for j in range (1, 8):
            cnt = random.randint(1, 5)
            if cnt == 1:
                Rect((i-1) * 200, (j-1) * 200, 200, 200, fill=rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),borderWidth=2,border="black")
            else:
                
                dirList = ["top", "bottom", "left", "right", "left-bottom", "right-bottom", "left-top", "right-top"]
                dir = random.choice(dirList)
                if cnt == 2:
                    Rect((i-1) * 200, (j-1) * 200, 200, 200, fill=gradient(rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), start = dir), borderWidth=2, border="black")
                elif cnt == 3:
                    Rect((i-1) * 200, (j-1) * 200, 200, 200, fill=gradient(rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), start = dir),borderWidth=2, border="black")
                elif cnt == 4:
                    Rect((i-1) * 200, (j-1) * 200, 200, 200, fill=gradient(rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), start = dir),borderWidth=2, border="black")
                else:
                    Rect((i-1) * 200, (j-1) * 200, 200, 200, fill=gradient(rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), start = dir),borderWidth=2, border="black")
            # Label(count, 200 * (j - 1) + 190, 200 * (i - 1) + 190, fill = "black")
            count += 1
        distance += 200


    #draws grid lines and counts squares
    for i in range(5):
        for j in range (6):
            Line(distance, 0, distance, 800)
            Line(0, distance, 1200, distance)
            Label(count,200*j+190,distance-10,fill="white", size=30)
            count+=1
        
        distance+=200


#period 1
distance = 80    
def ian_pau(x, y):
    # a little chicanery
    app.stepsPerSecond = 1e9223372036854775807
    # colour list
    cyka = ['red', 'green', 'blue', 'brown', 'purple']
    for i in range(5):
        # draw buddy
        Circle(x + 40 * i + 20, y + 100, 20, fill = cyka[i])
        if i == 0:
            # head
            Rect(x + 40 * i + 10, y + 95, 5, 10)
            Rect(x + 40 * i + 25, y + 95, 5, 10)
            Rect(x + 40 * i + 10, y + 75, 5, 10, rotateAngle = 330)
            Rect(x + 40 * i + 25, y + 75, 5, 10, rotateAngle = 30)
        else:
            # body
            Rect(x + 40 * i + 10, y + 120, 5, 10)
            Rect(x + 40 * i + 25, y + 120, 5, 10)
    # his name
    Label("Buddy, the mischievous caterpillar", x+100, y+60, size = 12)
def zoe_yu(x,y):
    Polygon(x,y+100,x+150,y+200,x+150,y, fill='aliceBlue')
    Polygon(x+150,y+100,x+200,y+130,x+200,y+70,fill='lavenderBlush')
    Polygon(x,y+100,x+60,y+140,x+60,y+60,fill='beige')
    Circle(x+30,y+100,7,fill='darkGray')
def alyssa_Jessa(x,y):
    Rect(x,y,200,200,border="powderBlue",fill='aliceBlue')
    #body
    Oval(x+100,y+100,60,80,fill=gradient('darkKhaki','burlyWood','saddleBrown', start='right-top'))
     #legs 
    Oval(x+80,y+60,10,30,fill=gradient('oliveDrab', 'darkOliveGreen', 'darkGreen',
     start='right-bottom'))
    Oval(x+120,y+60,10,30,fill=gradient('oliveDrab', 'darkOliveGreen', 'darkGreen',
     start='right-bottom'))
    #head
    Oval(x+100,y+146,26,30,fill=gradient('oliveDrab', 'darkOliveGreen', 'darkGreen',
     start='right-bottom'))
    Oval(x+95,y+143,6,10,fill='black')
    Oval(x+106,y+143,6,10,fill='black')
    #lips 
    
    #arms 
    Oval(x+125,y+130,10,30,fill=gradient('oliveDrab', 'darkOliveGreen', 'darkGreen',
     start='center'),rotateAngle=145)
    Oval(x+70,y+130,10,30,fill=gradient('oliveDrab', 'darkOliveGreen', 'darkGreen',
     start='center'), rotateAngle=35)
def ms_Ramirez(x,y):
    Rect(x,y,200,200,border="red",fill=None)
    
    #top right arm
    Polygon(x+100,y+100,x+140,y+50,x+180,y+80,x+140,y+65)
    Polygon(x+100,y+100,x+60,y+50,x+20,y+80,x+60,y+65)
    #top 2 left arms
    Polygon(x+100,y+130,x+140,y+70,x+180,y+100,x+140,y+85)
    Polygon(x+100,y+130,x+60,y+70,x+20,y+100,x+60,y+85)
    
    #bottom right leg 1
    Polygon(x+100,y+130,x+145,y+100,x+170,y+160,x+145,y+110)
    
    #bottom left leg 1
    Polygon(x+100,y+130,x+55,y+100,x+25,y+160,x+55,y+110)
    
    #TO:DO :finish last 2 legs
    #second bottom 
    Polygon(x+100,y+130,x+145,y+120,x+170,y+180,x+145,y+130)
    
    #bottom final leg
    Polygon(x+100,y+130,x+55,y+120,x+25,y+180,x+55,y+130)
    
    Oval(x+100,y+100,60,80,border="pink")
    Circle(x+100,y+50,20)
    Circle(x+90,y+50,10,fill="white")
    Circle(x+110,y+50,10, fill="white")
    Circle(x+113,y+50,6)
    Circle(x+93,y+50,6)
def AndrewGraham_FrancisFinney(x,y):
    for i in range(5):
    
        Rect(x,y,200,200,border='red',fill='blue')
        Label('1988 Toyota Camry',x+94,y+25)
        Rect(x+66,y+73,57,51) 
        Rect(x+32,y+97,129,38)
        Circle(x+56,y+135,20,fill='grey')
        Circle(x+129,y+135,20,fill='grey')
def aumritasDrawing(x,y):
    RegularPolygon(x+10,y+20,15,4, fill='red')
    RegularPolygon(x+110,y+20,15,4, fill='red')
    RegularPolygon(x+10,y+130,15,4, fill='red')
    RegularPolygon(x+110,y+130,15,4, fill='red')
    RegularPolygon(x+60,y+80,15,4,fill='red')
    Label('5', x-20, y, size=40, font='arial',bold=True, fill='red')
    RegularPolygon(x-20, y+30, 10, 4, fill='red')
    RegularPolygon(x+140, y+130, 10, 4, fill='red')
    Label('5', x+140, y+160, size=40, font='arial',bold=True, rotateAngle=180, fill='red')
def Chloette_Hobbs(x,y):
    Rect (x-100, y, x+300, y+300, fill= 'darkCyan')
    Circle (x+100, y+100, 100, fill='burlyWood')
    Circle (x+100, y+100, 90, fill='lightPink')
    Circle (x+100, y+100, 35, fill='darkCyan')
    Circle (x+65, y+30, 5, fill='yellow')
    Circle (x+105, y+40, 5, fill='red')
    Circle (x+45, y+45, 5, fill='blue')
    Circle (x+30, y+80, 5, fill='limeGreen')
    Circle (x+30, y+125, 5, fill='blueViolet')
    Circle (x+50, y+150, 5, fill='darkOrange')
    Circle (x+90,y+170, 5, fill='blue')
    Circle (x+150, y+160, 5, fill='red')
    Circle (x+160, y+130, 5, fill='limeGreen')
    Circle (x+180, y+100, 5, fill='yellow')
    Circle (x+160, y+75, 5, fill='blueViolet')
    Circle (x+140, y+45, 5, fill='darkOrange')
def cealan_holt(x,y):
    
    Circle(x,y, 90,fill='pink')
    Oval(x+30,y-40,20,60,fill=gradient('black','black','cyan',start='top'))
    Oval(x+30,y-50,10,30,fill='white')
    Oval(x-30,y-40,20,60,fill=gradient('black','black','cyan',start='top'))
    Oval(x-30,y-50,10,30,fill='white')
    Circle(x,y-10, 20,fill='darkRed')
    Circle(x,y-15, 20,fill='pink')
    Oval(x-90,y,30,60,rotateAngle=170,fill='pink')
    Oval(x+90,y,30,60,rotateAngle=210,fill='pink')
    Oval(x+30,y+80,30,35,fill=(gradient('pink','red',start='bottom')),rotateAngle = 170)
    Oval(x-30,y+80,30,35,fill=(gradient('pink','red',start='bottom')),rotateAngle = 190)
    Oval(x-40,y,15,13,fill=rgb(255,153,237))
    Oval(x+40,y,15,13,fill=rgb(255,153,237))  
def Dylan_Jia(x,y):
    Rect(x-135,y,200,70,fill='blue')
    Rect(x-120,y-60,20,60,fill="black")
    Rect(x+0,y-80,70,80,fill="green")
    Rect(x+20,y-60,30,50,fill="lightblue")
    for i in range(2):
        Circle(x-70*i,y+70,25,fill="gray", border="black")
def Lucy_Lyu(x,y):
    #Rect(x-125,y-125,200,200,fill='lightCyan',border='lightBlue')
    Circle(x,y,100,fill='lightSalmon')
    Oval(x-40,y-50,20,40,fill='white',border='black')
    Oval(x+40,y-50,20,40,fill='white',border='black')
    Circle(x-40,y-45,10,fill='black')
    Circle(x+40,y-45,10,fill='black')
    Circle(x,y,15,fill='crimson')
    Arc(x-32,y+50,120,10,30,120,fill='crimson')
def Tegh_Sidhu(x,y):
    Rect(x,y,200,200,border="blue",fill=None)
    Rect(x,y,40,40,border="red",fill=None)
    Rect(x,y,50,50,border="green",fill=None)
    Rect(x,y,60,60,border="yellow",fill=None)
    Rect(x,y,70,70,border="orange",fill=None)
    Rect(x,y,80,80,border="black",fill=None)
    Rect(x,y,90,90,border="red",fill=None)
    Rect(x,y,100,100,border="pink",fill=None)
    Rect(x,y,110,110,border="gold",fill=None)
    Rect(x,y,120,120,border="silver",fill=None)
    Rect(x,y,130,130,border="crimson",fill=None)
    Rect(x,y,140,140,border="violet",fill=None)
    Rect(x,y,150,150,border="purple",fill=None)
    Rect(x,y,160,160,border="teal",fill=None)
    Rect(x,y,170,170,border="black",fill=None)
    Rect(x,y,180,180,border="pink",fill=None)
    Rect(x,y,190,190,border="red",fill=None)
def Christopher_Hong (x, y):
    Rect(x, y, 50, 50, fill="lightblue")
    Rect(x+20, y+30, 10, 20, fill="brown")
    Polygon(x-5, y, x+25, y-30, x+55, y, fill="darkred")
    Rect(x+5, y+10, 15, 15, fill="lightyellow")
    Rect(x+30, y+10, 15, 15, fill="lightyellow")
def Ethan_Pessino(x, y, bongo):

    Rect(x+75, y+100-100, 25, 25, fill="black")
    Rect(x+75-25, y+100-75, 25, 25, fill="black")
    Rect(x+75-50, y+100-50, 25, 25, fill="black")
    Rect(x+75-50, y+100-25, 25, 25, fill="black")
    Rect(x+75-50, y+100, 25, 25, fill="black")
    Rect(x+75-25, y+100+25, 25, 25, fill="black")
    Rect(x+75, y+100+50, 25, 25, fill="black" )
    Rect(x+75+25, y+100+25, 25, 25, fill="black")
    Rect(x+75+50, y+100, 25, 25, fill="black")
    Rect(x+75+50, y+100-25, 25, 25, fill="black")
    Rect(x+75+50, y+100-50, 25, 25, fill="black")
    Rect(x+75+25, y+100-75, 25, 25, fill="black")
    
    Rect(x+75, y+100-50, 25, 25, fill="red")
    Rect(x+75, y+100-25, 25, 25, fill="red")
    Rect(x+75, y+100, 25, 25, fill="red")
    
    Rect(x+75, y+100+25, 25, 25, fill="gold")
    Rect(x+75+25, y+100, 25, 25, fill="gold")
    Rect(x+75+25, y+100-25, 25, 25, fill="gold")
    Rect(x+75+25, y+100-50, 25, 25, fill="gold")
    Rect(x+75, y+100-75, 25, 25, fill="gold")
    Rect(x+75-25, y+100-50, 25, 25, fill="gold")
    Rect(x+75-25, y+100-25, 25, 25, fill="gold")
    Rect(x+75-25, y+100, 25, 25, fill="gold")
    
    Rect(x+75, y+100+75, 25, 25, fill="purple")
    # Rect(100, 200, fill="purple")
    Rect(x+75-25, y+100+75, 25, 25, fill="purple")
    Rect(x+75+25, y+100+75, 25, 25, fill="purple")
    Rect(x+75-25, y+100+50, 25, 25, fill="purple")
    Rect(x+75+25, y+100+50, 25, 25, fill="purple")
    Rect(x+75-50, y+100+50, 25, 25, fill="purple")
    Rect(x+75+50, y+100+50, 25, 25, fill="purple")
    Rect(x+75+50, y+100+25, 25, 25, fill="purple")
    Rect(x+75-50, y+100+25, 25, 25, fill="purple")
    Rect(x+75-75, y+100+25, 25, 25, fill="purple")
    Rect(x+75-75, y+100, 25, 25, fill="purple")
    Rect(x+75-75, y+100-25, 25, 25, fill="purple")
    Rect(x+75-75, y+100-50, 25, 25, fill="purple")
    Rect(x+75-75, y+100-75, 25, 25, fill="purple")
    Rect(x+75-50, y+100-75, 25, 25, fill="purple")
    Rect(x+75-50, y+100-100, 25, 25, fill="purple")
    Rect(x+75+50, y+100-100, 25, 25, fill="purple")
    Rect(x+75-25, y+100-100, 25, 25, fill="purple")
    Rect(x+75+25, y+100-100, 25, 25, fill="purple")
    Rect(x+75+50, y+100-75, 25, 25, fill="purple")
    Rect(x+75+75, y+100-75, 25, 25, fill="purple")
    Rect(x+75+75, y+100-50, 25, 25, fill="purple")
    Rect(x+75+75, y+100-25, 25, 25, fill="purple")
    Rect(x+75+75, y+100, 25, 25, fill="purple")
    Rect(x+75+75, y+100+25, 25, 25, fill="purple")

def drawFirstPeriod():
#first row
    drawCollage()

    aumritasDrawing(40,20)
    ms_Ramirez(400,0)
    Dylan_Jia(740,100)  

    #second row
    alyssa_Jessa(0,200)
    zoe_yu(200,200)
    Lucy_Lyu(1100,100)

    #third row
    cealan_holt(500,300) 
    ian_pau(600,200)

    #fourth row
    AndrewGraham_FrancisFinney(0,400)
    Tegh_Sidhu(400,400)
    Christopher_Hong(300, 500)

    Chloette_Hobbs(0,600)
    Ethan_Pessino(800, 400, "yellow")
    



drawFirstPeriod()


cmu_graphics.run()
