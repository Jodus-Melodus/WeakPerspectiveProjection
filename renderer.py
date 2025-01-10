import turtle

class Camera:
    def __init__(self, x:float, y:float, z:float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

class Vertex:
    def __init__(self, x:float, y:float, z:float, camera:Camera) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.camera = camera
        self.calculate_projection_coords()

    def calculate_projection_coords(self) -> None:

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

    def draw_vertex(self, vertex) -> None:
        self.turtle.goto(vertex.x, vertex.y)
        self.turtle.pendown()
        self.turtle.penup()

    def draw_edge(self, edge:Edge) -> None:
        self.turtle.pencolor(edge.color)
        self.turtle.goto(edge.x1, edge.y1)
        self.draw_vertex(edge.vertex1)
        self.turtle.pendown()
        self.turtle.goto(edge.x2, edge.y2)
        self.draw_vertex(edge.vertex2)
        self.turtle.penup()

    def render(self, edgeTable:list) -> None:
        self.turtle.clear()
        for edge in edgeTable:
            self.draw_edge(edge)

if __name__ == '__main__':

    edgeTable = []

    render = Renderer()
    camera = Camera(0, -150, 550)

    def initialize_renderer():
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

    def inc_x():
        camera.x += 50
        print(camera)
        initialize_renderer()
    
    def dec_x():
        camera.x -= 50
        print(camera)
        initialize_renderer()
    
    def inc_y():
        camera.y += 50
        print(camera)
        initialize_renderer()

    def dec_y():
        camera.y -= 50
        print(camera)
        initialize_renderer()

    def inc_z():
        camera.z += 50
        print(camera)
        initialize_renderer()

    def dec_z():
        camera.z -= 50
        print(camera)
        initialize_renderer()

    turtle.onkey(inc_x, 'a')
    turtle.onkey(dec_x, 'd')
    turtle.onkey(inc_z, 's')
    turtle.onkey(dec_z, 'w')
    turtle.onkey(dec_y, 'space')
    turtle.listen()
    initialize_renderer()
    turtle.mainloop()