import maya.cmds as mc

class ObjectDupli:

    def mainmenu(self,*args):
        if mc.window('objectdupli', ex=True):
            mc.deleteUI('objectdupli')
        mc.window('objectdupli', t='ObjectDupli')
        mc.columnLayout(adj=True)
        mc.checkBoxGrp('axis', l='Axis', ncb=3, la3=['X','Y','Z'])
        mc.intSliderGrp('repeat', l='Repeat', min=1, max=20, f=True)
        mc.button(l='EXPRESSION', c=self.expression)
        mc.showWindow('objectdupli')

    def expression(self,*args):
        xche = mc.checkBoxGrp('axis', q=True, v1=True)
        yche = mc.checkBoxGrp('axis', q=True, v2=True)
        zche = mc.checkBoxGrp('axis', q=True, v3=True)
        sel = mc.ls(sl=True)
        rep = mc.intSliderGrp('repeat', q=True, v=True)
        move = 1

        for i in range(rep):
            if xche == 0 and yche == 0 and zche == 0:
                print '-----ERROR!!-----'
                return
            if xche == 1:
                mc.duplicate()
                mc.move(move,0,0)
            if yche == 1:
                mc.duplicate()
                mc.move(0,move,0)
            if zche == 1:
                mc.duplicate()
                mc.move(0,0,move)
            move = move + 1
       


a = ObjectDupli()
a.mainmenu()