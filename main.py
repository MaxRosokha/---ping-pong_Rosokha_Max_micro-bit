def on_button_pressed_a():
    Player1.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    Player1.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

Player1: game.LedSprite = None
Player1 = game.create_sprite(2, 4)
ball = game.create_sprite(2, 2)
ball.set(LedSpriteProperty.BRIGHTNESS, 100)
game.set_life(5)

def on_forever():
    basic.pause(800)
    ball.move(1)
    if ball.is_touching_edge():
        ball.change(LedSpriteProperty.DIRECTION, randint(-180, 180))
        ball.if_on_edge_bounce()
    if ball.get(LedSpriteProperty.Y) == 4:
        if ball.is_touching(Player1):
            game.add_score(1)
        else:
            game.remove_life(1)
basic.forever(on_forever)
