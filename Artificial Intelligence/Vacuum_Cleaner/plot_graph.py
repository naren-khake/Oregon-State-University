import matplotlib.pyplot as plot
class Plot_graph:
    def _init_(self):
            self.gp = {'x': [0], 'y': [0]}

    def generate_graph(self,gp):
        plot.plot(gp['x'], gp['y'], linestyle='-',marker='.', color='b')
        plot.xlabel('Actions Taken')
        plot.ylabel('Tiles Cleaned')
        plot.grid(True)
        plot.show()