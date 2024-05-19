input.onButtonPressed(Button.A, function () {
    Player1.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function () {
    Player1.change(LedSpriteProperty.X, 1)
})
let Player1: game.LedSprite = null
Player1 = game.createSprite(2, 4)
let ball = game.createSprite(2, 2)
ball.set(LedSpriteProperty.Brightness, 100)
game.setLife(5)
basic.forever(function () {
    basic.pause(800)
    ball.move(1)
    if (ball.isTouchingEdge()) {
        ball.change(LedSpriteProperty.Direction, randint(-180, 180))
        ball.ifOnEdgeBounce()
    }
    if (ball.get(LedSpriteProperty.Y) == 4) {
        if (ball.isTouching(Player1)) {
            game.addScore(1)
        } else {
            game.removeLife(1)
        }
    }
})
