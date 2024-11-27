from env import draw_wall

class Tile:
    def __init__(self,n,e,s,w,is_dirty=True,home=0):
        self.is_dirty = is_dirty
        self.n = n
        self.e = e
        self.s = s
        self.w = w
        self.home=home

    def __str__(self):
        return f"{'D' if self.is_dirty else 'C'} {self.n}{self.e}{self.s}{self.w}"

class Room:
    def __init__(self):
        self.tiles = [[Tile(0,0,0,0) for _ in range(10)] for _ in range(10)]
        self.tiles[9][0].home=1
        for i in range(10):
            self.set_wall(0,i,1)  #Upper Wall
            self.set_wall(i,0,4)  #left wall
            self.set_wall(9,i,3)  #Lower Wall
            self.set_wall(i,9,2)  #right Wall
        
    def set_tile_clean(self, x, y):
        self.tiles[x][y].is_dirty = False

    def set_wall(self, x, y, direction):
        if direction==1:
            if x!=0 :
                self.tiles[x-1][y].s=1
            self.tiles[x][y].n=1
        elif direction==2:
            if y!=9 :
                self.tiles[x][y+1].w=1
            self.tiles[x][y].e=1
        elif direction==3:
            if x!=9 :
                self.tiles[x+1][y].n=1
            self.tiles[x][y].s=1
        elif direction==4:
            if y!=0 :
                self.tiles[x][y-1].e=1
            self.tiles[x][y].w=1

    def print_room(self):
        for i in range(10):
            for j in range(10):
                print(self.tiles[i][j], end=' ')
            print()
