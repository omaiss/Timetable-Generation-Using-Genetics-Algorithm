import random

# The chromosomes should be binary encoded with the following information:
# Course, Theory/Lab, Section, Section-Strength, Professor, First-lecture-day,
# First- lecture-timeslot, First-lecture-room, First-lecture-room-size, Second lecture-day,
# Second-lecture-timeslot, Second-lecture-room, Second-lecture room-size
university_dict = {
    "Course": 3,
    "Theory": 3,
    "Lab": 3,
    "Section": 3,
    "Strength": 3,
    "FL_Day": 3,
    "FLT_Slot": 3,
    "FL_Room": 3,
    "FLR_Size": 3,
    "SL_Day": 3,
    "SLT_Slot": 3,
    "SL_Room": 3,
    "SLR_Size": 3
}


def populate_chromosome():
    pop = []
    for index, each in enumerate(university_dict):
        pop.append([random.randint(0, 1) for _ in range(university_dict[each])])
    return pop


if __name__ == "__main__":
    print(populate_chromosome())
    pass
