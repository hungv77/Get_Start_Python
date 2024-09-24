import turtle
import random

# Hàm tạo rùa
def create_turtle(color, y_position):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(color)
    t.penup()
    t.goto(-200, y_position)  # vị trí bắt đầu
    t.pendown()
    return t

# Thiết lập màn hình
screen = turtle.Screen()
screen.setup(width=800, height=600)

# Nhập số lượng rùa
num_turtles = int(input("Nhập số lượng rùa: "))

# Danh sách màu sắc cho rùa
colors = ["red", "blue", "green", "orange", "purple", "pink", "yellow", "brown"]

# Tạo các con rùa
turtles = []
for i in range(num_turtles):
    turtle_color = colors[i % len(colors)]
    turtle_position = -200 + i * 50  # đặt vị trí từng con rùa
    t = create_turtle(turtle_color, turtle_position)
    turtles.append(t)

# Random tốc độ cho từng con rùa và bắt đầu đua
race_on = True
while race_on:
    for t in turtles:
        distance = random.randint(1, 10)  # random tốc độ từ 1 đến 10
        t.forward(distance)
        
        # Kiểm tra xem rùa có về đích chưa
        if t.xcor() > 200:  # vị trí đích là x = 200
            race_on = False
            print(f"{t.pencolor()} turtle wins!")
            break

turtle.done()
