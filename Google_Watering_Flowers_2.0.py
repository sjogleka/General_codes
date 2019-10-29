# Link Ref - https://leetcode.com/discuss/interview-question/394347/


class Worker:
    def __init__(self, capacity, ptr=0, water=0):
        self.capacity = capacity
        self.ptr = ptr
        self.water = water
        self.n_refill = 0

    def refill(self):
        self.water = self.capacity
        self.n_refill += 1

    def water_plant(self, plant):
        if plant > self.water:
            self.refill()
            self.water_plant(plant)
        else:
            self.water -= plant


def solution(plants, capacity1, capacity2):
    result = 0
    n_plants = len(plants)
    # current tank state of each worker
    worker_left, worker_right = Worker(capacity1, 0), Worker(capacity2, n_plants - 1)
    # watering process
    while worker_left.ptr <= worker_right.ptr:
        # concurrent watering
        if worker_left.ptr < worker_right.ptr:
            # logic for worker_left
            plant_left = plants[worker_left.ptr]
            worker_left.water_plant(plant_left)
            # logic for worker_right
            plant_right = plants[worker_right.ptr]
            worker_right.water_plant(plant_right)
            # move together
            worker_left.ptr += 1
            worker_right.ptr -= 1
        # joint watering
        else:
            plant = plants[worker_left.ptr]
            # not enough water
            if worker_left.water + worker_right.water < plant:
                result += 1
            break
    return worker_left.n_refill + worker_right.n_refill + result


if __name__ == '__main__':
    plants = [2, 4, 5, 1, 2]
    print(solution(plants, 5, 7))  # should return 3

