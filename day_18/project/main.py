import turtle as t
import colorgram

brush = t.Turtle()
screen = t.Screen()



# Extract colors from image.jpg
colors = colorgram.extract('image.jpg', 6)
print(colors)


brush.circle(10)










screen.exitonclick()