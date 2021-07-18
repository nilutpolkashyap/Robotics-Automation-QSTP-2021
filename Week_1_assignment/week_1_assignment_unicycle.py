import numpy as np
import matplotlib.pyplot as plt

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n: int):
        
        x = self.x
        y= self.y
        theta = self.theta
        dt = self.dt
        
        for _ in range(n):
            x += v * np.cos(theta)
            y += v * np.sin(theta)
            theta += w * (dt)

            self.x_points.append(x)
            self.y_points.append(y)

        return x, y, theta

    def plot(self, v: float, w: float): 
        """Function that plots the intermeditate trajectory of the Robot"""
        plt.title(f"Unicycle Model: v = {v}, w = {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()
        plt.show() 
        #plt.savefig(f"Unicycle_v_{v}_w_{w}.png")
        print("Plot Created")

if __name__ == "__main__":
    print("Unicycle Model Assignment")
    
    
    #Start=(0, 0, 0); dt=0.1; vel=(1, 0.5); timesteps: 25
    uni1=Unicycle(0,0,0,0.1)
    uni1.step(1.0,0.5,25)
    uni1.plot(1.0,0.5)


    """
    #Start=(0, 0, 1.57); dt=0.2; vel=(0.5, 1); timesteps: 10
    uni2=Unicycle(0,0,1.57,0.2)
    uni2.step(0.5,1.0,10)
    uni2.plot(0.5,1.0) 
    """

    """    
    #Start(0, 0, 0.77); dt=0.05; vel=(5, 4); timestep: 50
    uni3=Unicycle(0,0,0.77,0.05)
    uni3.step(5,4,50)
    uni3.plot(5,4) 
    """
