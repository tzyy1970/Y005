from Components.VariableText import VariableText
from Renderer import Renderer
from Screens.InfoBar import InfoBar
from Tools.Directories import resolveFilename, SCOPE_SYSETC
from enigma import eLabel

class speedyEmuInfo(VariableText, Renderer):

    def __init__(self):
        Renderer.__init__(self)
        VariableText.__init__(self)

    GUI_WIDGET = eLabel

    def connect(self, source):
        Renderer.connect(self, source)
        self.changed((self.CHANGED_DEFAULT,))

    def changed(self, what):
        if what[0] == self.CHANGED_CLEAR:
            self.text = 'not detected Softcam'
        else:
            self.text = self.getVtiEmuInfo()

    def getVtiEmuInfo(self):
        try:
            file = open(resolveFilename(SCOPE_SYSETC, '/media/usb/tmp/oscam.info'), 'r')
            emuversion = file.readline()
            file.close()
            return emuversion
        except IOError:
            return 'not detected Softcam'
