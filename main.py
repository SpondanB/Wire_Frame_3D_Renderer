import pygame as pg
from camera import *
from projection import *
from object_3d import *



class Renderer:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 800, 450
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 30
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_objects()
        
    def create_objects(self):
        self.camera = Camera(self, [-5, 5, -50])
        self.projection = Projection(self)
        self.object = self.get_obj_file_object("objects/Sting-Sword-lowpoly.obj") 
        
    def get_obj_file_object(self, path):
        vertices, faces = [], []
        with open(path) as f:
            for line in f:
                if line.startswith('v '):
                    vertices.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f '):
                    face = line.split()[1:]
                    faces.append([int(inface.split("/")[0]) - 1 for inface in face])
        return Object3D(self, vertices, faces)
    
    def draw(self):
        self.screen.fill("darkslategray")
        self.object.draw()
        
    def run(self):
        while True:
            self.draw()
            self.camera.controls()
            [pg.quit() for event in pg.event.get() if event.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)
            
            
            
if __name__ == "__main__":
    app = Renderer()
    app.run()