import turtle

class Camera:
    def __init__(self, x:float, y:float, z:float) -> None:
        self.x = x
        self.y = y
        self.z = z

class Vertex:
    def __init__(self, x:float, y:float, z:float, camera:Camera) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.camera = camera
        self.calculateProjectionCoords()

    def calculateProjectionCoords(self) -> None:

        self.x = (self.camera.z * (self.camera.x + self.x)) / (camera.z + self.z)
        self.y = (self.camera.z * (self.camera.y + self.y)) / (camera.z + self.z)

        # self.x = (focalLength * self.x) / (focalLength + self.z)
        # self.y = (focalLength * self.y) / (focalLength + self.z)

class Edge:
    def __init__(self, vertex1:Vertex, vertex2:Vertex, color:str='red') -> None:
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.color = color
        self.x1 = vertex1.x
        self.y1 = vertex1.y
        self.x2 = vertex2.x
        self.y2 = vertex2.y    

class Renderer:
    def __init__(self) -> None:
        turtle.bgcolor('black')
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.goto(0, 0)
        self.turtle.hideturtle()
        self.defaultColor = 'blue'

    def drawVertex(self, vertex) -> None:
        self.turtle.goto(vertex.x, vertex.y)
        self.turtle.pendown()
        self.turtle.penup()

    def drawEdge(self, edge:Edge) -> None:
        self.turtle.pencolor(edge.color)
        self.turtle.goto(edge.x1, edge.y1)
        self.drawVertex(edge.vertex1)
        self.turtle.pendown()
        self.turtle.goto(edge.x2, edge.y2)
        self.drawVertex(edge.vertex2)
        self.turtle.penup()

    def render(self, edgeTable:list) -> None:
        self.turtle.clear()
        for edge in edgeTable:
            self.drawEdge(edge)

if __name__ == '__main__':

    edgeTable = []

    render = Renderer()
    camera = Camera(-50, -50, 250)

    def update():
        # cube
        # A = Vertex(0, 0, 50, camera)
        # B = Vertex(100, 0, 50, camera)
        # C = Vertex(100, 100, 50, camera)
        # D = Vertex(0, 100, 50, camera)
        # E = Vertex(0, 0, -150, camera)
        # F = Vertex(100, 0, -150, camera)
        # G = Vertex(100, 100, -150, camera)
        # H = Vertex(0, 100, -150, camera)
        # cube = [
        #     Edge(A, B),
        #     Edge(B, C),
        #     Edge(C, D),
        #     Edge(D, A),
        #     Edge(E, F),
        #     Edge(F, G),
        #     Edge(G, H),
        #     Edge(H, E),
        #     Edge(A, E),
        #     Edge(B, F),
        #     Edge(C, G),
        #     Edge(D, H)
        # ]
        # render.render(cube)

        # pyramid
        A = Vertex(0, 400, -200, camera)
        B = Vertex(150 , 0, -350, camera)
        C = Vertex(-150, 0, -50, camera)
        D = Vertex(150, 0, -50, camera)
        E = Vertex(-150, 0, -350, camera)
        pyramid =[
            Edge(A,B),
            Edge(A,C),
            Edge(A,D),
            Edge(A,E),
            Edge(B,E),
            Edge(E,C),
            Edge(B,D),
            Edge(D,C)
        ]
        render.render(pyramid)

    def incX():
        camera.x += 50
        print('incx')
        update()
    
    def decX():
        camera.x -= 50
        print('decx')
        update()
    
    def incY():
        camera.y += 50
        print('incy')
        update()

    def decY():
        camera.y -= 50
        print('decy')
        update()

    def incZ():
        camera.z += 50
        print('incz')
        update()

    def decZ():
        camera.z -= 50
        print('decz')
        update()

    turtle.onkey(incX, 'a')
    turtle.onkey(decX, 'd')
    turtle.onkey(incZ, 's')
    turtle.onkey(decZ, 'w')

    turtle.listen()

    update()

    
    turtle.mainloop()