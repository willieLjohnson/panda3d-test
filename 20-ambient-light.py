from panda3d.core import loadPrcFile

loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase
from panda3d.core import PointLight, AmbientLight
from math import sin, cos


class SimplePointLight(ShowBase):
    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0, 1)
        self.jack = self.loader.loadModel("models/jack")
        self.jack.setHpr(0, 180, 180)
        self.jack.setPos(0, 0, 0)
        self.jack.reparentTo(self.render)

        self.light_model = self.loader.loadModel('models/misc/sphere')
        self.light_model.setScale(0.2, 0.2, 0.2)
        self.light_model.setPos(4, 0, 0)
        self.light_model.reparentTo(self.render)

        self.cam.setPos(0, -12, 0)

        plight = PointLight("plight")
        plight.setColor((1, 1, 1, 1))
        self.plnp = self.light_model.attachNewNode(plight)
        # self.plnp.setPos(2, 0, 0)
        plight.setAttenuation((1, 0, 0))
        self.jack.setLight(self.plnp)

        alight = AmbientLight("aLight")
        alight.setColor((0.04, 0.04, 0.04, 1))
        alnp = self.render.attachNewNode(alight)
        self.jack.setLight(alnp)

        self.taskMgr.add(self.move_light, "move-light")

    def move_light(self, task):
        ft = globalClock.getFrameTime()

        self.light_model.setPos(cos(ft) * 4, sin(ft) * 4, 0)

        return task.cont


game = SimplePointLight()
game.run()
