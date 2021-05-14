import turtle
def tree(forward_len=200, minim_len=5):
    turtle.forward(forward_len)
    if forward_len > minim_len:
        turtle.left(45)
        tree(0.6*forward_len, minim_len)
        turtle.right(90)
        tree(0.6*forward_len, minim_len)
        turtle.left(45)
    turtle.back(forward_len)