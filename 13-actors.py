from panda3d.core import loadPrcFile

loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor


class MyGame(ShowBase):
    def __init__(self):
        super().__init__()

        self.anim = Actor("my-models/anim", {"attack": "my-models/anim-attack"})
        self.anim.reparentTo(self.render)
        self.anim.setPos(0, 20, 0)

        self.anim.loop("attack")

game = MyGame()
game.run()
