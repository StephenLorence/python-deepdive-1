import math

class Polygon:
    
    def __init__(self, edges, circumradius):
        self.edges = edges
        n = self.edges
        self.circumradius = circumradius
        r = self.circumradius
        self.vertices = self.edges
        self.edge_length = 2*r*math.sin(math.pi/n)
        s = self.edge_length
        self.apothem = r*math.cos(math.pi/n)
        a = self.apothem
        self.area = 0.5*n*s*a
        self.perimeter = n*s
        self.interior_angle = (n-2) * (180/n)
        
    def __repr__(self):
        return f'Polygon(edges(n) = {self.edges}, circumradius(R) = {self.circumradius})'
    
    def __eq__(self, other):
        if isinstance(other, Polygon):
            return self.edges == other.edges and self.circumradius == other.circumradius
        else:
            raise TypeError('Polygon equality not supported with non-Polygons.')
            
    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self.edges > other.edges
        else:
            raise TypeError('Polygon comparison not supported with non-Polygons.')   