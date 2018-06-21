class FloorPlan:
    lastId = 0
    def __init__(
        self,
        color = 'white',
        name = 'nil',
        text = 'nil',
        picture = 'missing.jpg',
        symbol = '+',
        x = 0,
        y = 0,
        w = 0,
        h = 0,
        r = 0
    ):
        self.id = FloorPlan.lastId + 1
        FloorPlan.lastId = self.id
        self.color = color
        self.name = name
        self.text = text
        self.picture = picture
        self.symbol = symbol
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    # kontrollib kas xy on sellel p6randal
    def isInArea(self, x, y):
        return (
            x >= self.x and x < (self.x + self.w) and
            y >= self.y and y < (self.y + self.h)
        )

    # joonistab selle elemendi
    def draw(self):
        print('joonistame seda elementi')

    # export??? tagastab elemendi andmed s6nastikkuna
    def export(self):
        return {
            'id': self.id,
            'color': self.color,
            'name': self.name,
            'text': self.text,
            'picture': self.picture,
            'symbol': self.symbol,
            'x': self.x,
            'y': self.y,
            'w': self.w,
            'h': self.h
        }




# test
floors = [
    FloorPlan(x = 0, y = 0, w = 30, h = 30, symbol = '.'),
    FloorPlan(x = 4, y = 7, w = 10, h = 10, symbol = 's'),
    FloorPlan(x = 2, y = 2, w = 8, h = 4, symbol = 'x'),
    FloorPlan(x = 1, y = 1, w = 4, h = 2, symbol = 'p')
]

o = FloorPlan(x = 5,y = 5,w = 5,h = 5)
for y in range (19, -1, -1):
    s = ''
    for x in range (0, 20):
        text = '   '
        for f in floors:
            if (f.isInArea(x,y)):
                text = f.symbol + '  '
       

        s = s + text
    
    print(s)

# 2 on alas
#floor1 = floors[2]
floor1 = floors[3]
if (floor1.isInArea(5,5)):
    print ('5,5 on alas')
else :
    print ('5,5 ei ole alas')

exportedData = floor1.export()
print(str(exportedData))
