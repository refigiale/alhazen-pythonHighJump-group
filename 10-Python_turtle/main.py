#import semuanya dari package turtle (visual python)
from turtle import *

getscreen() #return screenTurtle
bgcolor("pink") #background color pink
speed("slowest") #kecepatan garis lambat
forward(150) #garis ke depan
backward(300) #garis ke belakang

#turn
showturtle() #menampilkan pergerakan tanda panah
left(90) #mengatur arah tanda panah ke kiri 90derajat
forward(150)
right(90) #mengatur arah tanda panah ke kanan 90derajat
forward(300)
pensize(10) #mengatur ketebalan pen
right(90) #mengatur arah tanda panah ke kanan 90derajat
forward(150)

penup() #tidak menampilkan garis
forward(50)

hideturtle() #tidak menampilkan pergerakan tanda panah, langsung menampilkan garis
pencolor("blue")#warna garis
pendown() #tampilkan garis
forward(50)

fillcolor("red")#warna tanda panah
left(90)
backward(100)
done() #looping (jadinya dia bisa menampilkan screen turtle secara terus menerus)