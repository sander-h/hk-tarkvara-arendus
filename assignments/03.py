'''
laud,
tool,
kapp,
voodi,
diivan,
taburett,
tumba,
baaritool,
välivoodi

https://en.wikipedia.org/wiki/List_of_furniture_types
- furniture types
    - seating
    - sleeping
    - entertainment
    - tables
    - storage
    
- sets
    - bedroom
    - dining
    - vanity
    - patio

- materials
    - wooden
    - bamboo
    - wicker
    - metal
    - plastic
    - glass
    - concrete
    - bombay
'''


# materialid
from abc import ABCMeta, abstractmethod
class IMat (metaclass = ABCMeta):
    type = 'undefined'

class MatWooden(IMat):
    type = 'wooden'

class MatMetal(IMat):
    type = 'metallic'

class MatPlastic(IMat):
    type = 'plastic'

class MatLeather(IMat):
    type = 'leather'

class MatCloth(IMat):
    type = 'cloth'

# m66bel
class IFur (metaclass = ABCMeta):
    material : IMat
    def __init__(self,pos = (0,0,0),rot = (0,0,0), size = (0,0,0)):
        self.material = IMat
        self.name = 'undefined'
        self.pos = pos
        self.rot = rot
        self.size = size
    def draw(self):
        print ('Drawing a ' + self.material.type + ' ' + self.name)

class FurChair(IFur):
    material : IMat
    def __init__(self, material : IMat,pos = (0,0,0),rot = (0,0,0),size=(1,1,1)):
        super().__init__(pos,rot,size)
        self.material = material
        self.name = 'chair'

class FurTable(IFur):
    material : IMat
    def __init__(self, material : IMat,pos = (0,0,0),rot = (0,0,0),size=(2,2,1)):
        super().__init__(pos,rot,size)
        self.material = material
        self.name = 'table'

class FurCloset(IFur):
    material : IMat
    def __init__(self, material : IMat,pos = (0,0,0),rot = (0,0,0),size=(2,1,2)):
        super().__init__(pos,rot,size)
        self.material = material
        self.name = 'closet'

class FurBed(IFur):
    def __init__(self, material : IMat,pos = (0,0,0),rot = (0,0,0),size=(3,2,1)):
        super().__init__(pos,rot,size)
        self.material = material
        self.name = 'bed'

class FurSofa(IFur):
    def __init__(self, material : IMat,pos = (0,0,0),rot = (0,0,0),size=(1,3,1.5)):
        super().__init__(pos,rot,size)
        self.material = material
        self.name = 'sofa'

class FurStool(IFur):
    material : IMat
    def __init__(self, material : IMat,pos = (0,0,0),rot = (0,0,0),size=(0.5,0.5,1)):
        super().__init__(pos,rot,size)
        self.material = material
        self.name = 'stool'

class FurPuffe(IFur):
    material : IMat
    def __init__(self, material : IMat,pos = (0,0,0),rot = (0,0,0),size=(0.5,0.5,0.5)):
        super().__init__(pos,rot,size)
        self.material = material
        self.name = 'puffe'

class FurBarStool(IFur):
    material : IMat
    def __init__(self, material : IMat,pos = (0,0,0),rot = (0,0,0),size=(0.5,0.5,0.75)):
        super().__init__(pos,rot,size)
        self.material = material
        self.name = 'bar stool'

class FurCot(IFur):
    material : IMat
    def __init__(self, material : IMat,pos = (0,0,0),rot = (0,0,0),size=(3,1.5,1)):
        super().__init__(pos,rot,size)
        self.material = material
        self.name = 'cot'


list = (
    FurChair(MatPlastic),
    FurTable(MatPlastic),
    FurCloset(MatWooden),
    FurBed(MatCloth),
    FurSofa(MatLeather),
    FurStool(MatWooden),
    FurPuffe(MatCloth),
    FurBarStool(MatMetal),
    FurCot(MatCloth)
)
for item in list:
    item.draw()


