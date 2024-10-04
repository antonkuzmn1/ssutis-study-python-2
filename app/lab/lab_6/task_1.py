import pickle
import random


# noinspection PyTypeChecker
def main():
    dictionary = {}

    for i in range(20):
        departure_time = f"{random.randint(0, 23):02}:{random.randint(0, 59):02}"
        travel_time = f"{random.randint(0, 5)}ч {random.randint(0, 59)}мин"
        dictionary[departure_time] = travel_time

    with open("dictionary.dat", "wb") as file:
        pickle.dump(dictionary, file)
