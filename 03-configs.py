# from panda3d.core import loadPrcFile
# loadPrcFile("config/conf.prc")

from panda3d.core import loadPrcFileData

confVars = """
win-size 1280 720
window-title My Panda3D Game with ConfVars
show-frame-rate-meter True
"""

loadPrcFileData("", confVars)

from panda3d.core import ConfigVariableManager

ConfigVariableManager.getGlobalPtr().listVariables()

from direct.showbase.ShowBase import ShowBase


class MyGame(ShowBase):
    def __init__(self):
        super().__init__()


game = MyGame()
game.run()
