import pygame as pg
from matrix_function import *

class Object3D():
    def __init__(self, render, vertices, faces):
        self.render = render
        self.vertices = np.array(vertices)
        self.faces = faces #np.array([np.array(face) for face in faces])
        '''
        # The vertices for cube
        self.vertices = np.array([
            (0, 0, 0, 1),
            (0, 1, 0, 1),
            (1, 1, 0, 1),
            (1, 0, 0, 1),
            (0, 0, 1, 1),
            (0, 1, 1, 1),
            (1, 1, 1, 1),
            (1, 0, 1, 1)
        ]) # the vertices are in a homogeneous coordinate system (x, y, z, w) ; where w = scale = 1
        # note: the vertices index is important as that will be used to identify the face of the surfaces
        # for eg: if face one can be represented by vertices 0, 1, 2 and 3 then
        # face 1 = (0, 1, 2, 3) and similarly for other faces.
        self.faces = np.array([
            (0, 1, 2, 3),
            (4, 5, 6, 7),
            (0, 4, 5, 1),
            (2, 3, 7, 6),
            (1, 2, 6, 5),
            (0, 3, 7, 4)
        ])
        '''
        
    def draw(self):
        self.screen_projection()
        #self.movement()
    
    def movement(self):
        self.rotate_y(pg.time.get_ticks() % 0.05)
    
    def screen_projection(self):
        vertices = self.vertices @ self.render.camera.camera_matrix() # transfer the vertices to camera matrix
        vertices = vertices @ self.render.projection.projection_matrix # transfer the vertices to clip space
        vertices /= vertices[:,-1].reshape(-1, 1) # [x/w, y/w, z/w, w/w]
        vertices[(vertices > 2) | (vertices < -2)] = 0 # removing values >1 or <-1 and equating them to 0
        vertices = vertices @ self.render.projection.to_screen_matrix
        vertices = vertices[:, :2] # converting [x, y, z] -> [x, y]
        
        for face in self.faces:
            polygon = vertices[face]
            if not np.any((polygon == self.render.H_WIDTH) | (polygon == self.render.H_HEIGHT)):
                pg.draw.polygon(self.render.screen, pg.Color("orange"), polygon, 1)
        '''
        for vertex in vertices:
            if not np.any((vertex == self.render.H_WIDTH) | (vertex == self.render.H_HEIGHT)):
                pg.draw.circle(self.render.screen, pg.Color("white"), vertex, 1)
        '''
                
        
    def translate(self, pos):
        self.vertices = self.vertices @ translate(pos)
    
    def scale(self, scale_to):
        self.vertices = self.vertices @ scale(scale_to)
    
    def rotate_x(self, angle):
        self.vertices = self.vertices @ rotate_x(angle)
    
    def rotate_y(self, angle):
        self.vertices = self.vertices @ rotate_y(angle)
        
    def rotate_z(self, angle):
        self.vertices = self.vertices @ rotate_z(angle)
    
    def print_op(self):
        vertices = self.vertices @ self.render.camera.camera_matrix() # transfer the vertices to camera matrix
        vertices = vertices @ self.render.projection.projection_matrix # transfer the vertices to clip space
        print(vertices)
        
    
    