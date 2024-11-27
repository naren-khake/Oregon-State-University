import matplotlib.pyplot as plot
class Agent:
    def __init__(self, room):
        self.room = room
        self.x = 9 
        self.y = 0
        self.direction = 'North'
        self.is_running = True
        self.clean_tile=0
        self.action_count=0
        self.graph = {'x': [0], 'y': [0]}
        for i in range(10):
            for j in range(10):
                self.room.tiles[i][j].is_dirty=True

    def sense_wall(self):
        if self.direction == 'North':
            return  self.room.tiles[self.x][self.y].n == 1
        elif self.direction == 'South':
            return self.room.tiles[self.x][self.y].s == 1
        elif self.direction == 'West':
            return self.room.tiles[self.x][self.y].w == 1
        elif self.direction == 'East':
            return  self.room.tiles[self.x][self.y].e == 1

    def sense_dirt(self):
        return self.room.tiles[self.x][self.y].is_dirty

    def sense_home(self):
        return self.room.tiles[self.x][self.y].home == 1

    def clean(self):
        self.action_count+=1
        if self.sense_dirt():
            self.clean_tile+=1
            self.graph['y'].append(self.clean_tile)
            self.graph['x'].append(self.action_count)
        self.room.set_tile_clean(self.x, self.y)
        print(f"Cleaning tile [{self.x}, {self.y}]")
        

    def turn_right(self):
        directions = ['North', 'East', 'South', 'West']
        self.direction = directions[(directions.index(self.direction) + 1) % 4]
        print("Turning right")
        self.action_count+=1

    def turn_left(self):
        directions = ['North', 'East', 'South', 'West']
        self.direction = directions[(directions.index(self.direction) - 1) % 4]
        print("Turning left")
        self.action_count+=1

    def move_forward(self):
        if self.direction == 'North':
            self.x -= 1
        elif self.direction == 'South':
            self.x += 1
        elif self.direction == 'West':
            self.y -= 1
        elif self.direction == 'East':
            self.y += 1
        print(f"Moving forward to [{self.x}, {self.y}]")
        self.action_count+=1

    def turn_off(self):
        self.is_running = False
        print("Turning off")
        self.action_count+=1