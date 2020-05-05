from panda3d.core import loadPrcFile

loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor


class MyGame(ShowBase):
    def __init__(self):
        super().__init__()

        self.anim = Actor("my-models/anim", {"attack": "my-models/anim-attack"})
        self.anim.reparentTo(self.render)
        self.anim.setPos(0, 40, 0)
        self.anim.loop("attack")

        self.x = 0
        self.z = 0

        self.taskMgr.add(self.update, "update")

    def update(self, task):
        self.anim.setPos(self.x, 40, self.z)

        self.x -= 0.02
        self.z += 0.05

        return task.cont


game = MyGame()
game.run()
