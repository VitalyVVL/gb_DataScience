import time
from itertools import  cycle


class TrafficLight:
    __color ='red'


    def running(self, sleep_time):
       for light in cycle(self.__color):

                print(f'\r \033[{self.__color[light]}m {light} ',end='')
                time.sleep(sleep_time)


    def __init__(self, color_list):
        self.__color = color_list
        self.running(3)



TL =TrafficLight({'red':'31', 'yellow':'33', 'green':'32'})
