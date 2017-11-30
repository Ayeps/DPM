import numpy as np
from random import randrange
import matplotlib.pyplot as plt

class Service_Requester:
  
    def __init__(self, size):

        self.inter_arrival = np.zeros(size)
        request_size = randrange(size)
        
        internal_clk  = 0
        while(internal_clk < request_size):
            self.inter_arrival[internal_clk] = internal_clk + randrange(1000)
            internal_clk += 1
        self.inter_arrival = list(set(self.inter_arrival))
        #print "self.inter_arrival \n", self.inter_arrival


    def inter_arrivals(self):
        return self.inter_arrival

    def time(self, value):
        return value in self.inter_arrival

    def request_count(self):
        return randrange(1, 50)

    def view(self):
        plt.plot(self.inter_arrival)
        plt.ylabel('Inter Arrival Time')
        plt.xlabel('global clock')
        plt.show()
