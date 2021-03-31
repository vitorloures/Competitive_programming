import math
import os
import random
import re
import sys
from collections import OrderedDict


class Schedule:
    def __init__(self):
        self.free_time = OrderedDict([(0, 24)])

    def add_meeting(self, start_time, stop_time):
        free_time = self.free_time.copy()
        for free_start, free_stop in free_time.items():

            if free_start <= start_time < free_stop:
                del self.free_time[free_start]
                self.free_time[free_start] = start_time
                self.free_time[stop_time] = free_stop

            if free_start <= stop_time < stop_time:
                self.free_time[free_start] = start_time
                self.free_time[stop_time] = free_stop

    def delete_wrong_time(self):
        free_time = self.free_time.copy()
        for free_start, free_stop in free_time.items():
            if free_start >= free_stop:
                del self.free_time[free_start]
        self.free_time = OrderedDict(sorted(self.free_time.items()))
        # self.free_time = sorted(self.free_time)


if __name__ == '__main__':
    n = int(input().split()[0])
    T = int(input().split()[0])
    people_start = []
    people_end = []
    schedule = Schedule()

    # start_time = 0
    # stop_time = 0
    busy_time = {}

    possible_time = {0: 24}

    for i in range(n):
        person_schedule = list(map(str, input().rstrip().split(' ')))
        person_start = sorted([int(time.split(',')[0]) for time in person_schedule])
        person_stop = sorted([int(time.split(',')[1]) for time in person_schedule])
        people_start.append(person_start)
        people_end.append(person_stop)

    # print('people start:', people_start)
    # print('people end', people_end)

    for i, person_start_list in enumerate(people_start):
        for j in range(len(person_start_list)):
            start = people_start[i][j]
            stop = people_end[i][j]
            # print(f'start {start}, stop {stop}')
            schedule.add_meeting(start, stop)

    print(schedule.free_time)
    schedule.delete_wrong_time()
    print('Schedule free time')
    print(schedule.free_time)
    printed = False
    for start, stop in schedule.free_time.items():
        diff = stop - start
        if diff >= T:
            print(f"O primeiro horario possivel para a reuniao eh das {start}h00 as {start+T}h00")
            printed = True
            break

    if not printed:
        print("Nao existe horario no dia para marcar a reuniao")