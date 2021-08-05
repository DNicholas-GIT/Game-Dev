import turtle

wn = turtle.Screen()
wn.title("Pong by Red")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

player_a_score = 0
player_b_score = 0

# wn.write(f"Player A score {player_a_score} Player B score {player_b_score}", font=("Arial", 10), align="center")




# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = .2
ball.dy = .2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
# Bindings

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    wn.update()

    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 400:
        player_a_score += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A score: {} Player B score: {}".format(player_a_score, player_b_score), align="center",
                  font=("Courier", 24, "normal"))

        # ball.dy *= -1

    if ball.xcor() < -400:
        player_b_score += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A score: {} Player B score: {}".format(player_a_score, player_b_score), align="center",
                  font=("Courier", 24, "normal"))
        # ball.dy *= -1

    # Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

    # if ball.xcor() > 390:
    #     ball.setx(390)
    #     ball.dx *= -1
    #
    # if ball.xcor() < -390:
    #     ball.setx(-390)
    #     ball.dx *= -1