import random

# The chromosomes should be binary encoded with the following information:
# Course, Theory/Lab, Section, Section-Strength, Professor, First-lecture-day,
# First-lecture-timeslot, First-lecture-room, First-lecture-room-size, Second-lecture-day,
# Second-lecture-timeslot, Second-lecture-room, Second-lecture-room-size

courses = ['Database', 'Programming Fundamentals', 'Data Structures', 'Algorithms', 'Computer Networks']
theory_lab = ['Theory', 'Lab']
sections = ['A', 'B', 'C']
section_strength = [random.randint(30, 120) for _ in range(len(sections))]
professors = ['Prof. Ahmed Khan', 'Prof. Fatima Ali', 'Prof. Mohammad Khan']
lecture_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
lecture_timeslots = ['8:30 - 9:50', '10:00 - 11:20', '11:30 - 12:50', '1:00 - 2:20', '2:30 - 3:50']
lecture_rooms = ['101', '102', '103']
room_sizes = [60, 120]

university_dict = {
    "Course": 5,
    "Theory/Lab": 1,
    "Section": 5,
    "Strength": 5,
    "FL_Day": 3,
    "FLT_Slot": 5,
    "FL_Room": 5,
    "FLR_Size": 1,
    "SL_Day": 3,
    "SLT_Slot": 5,
    "SL_Room": 5,
    "SLR_Size": 1
}


def populate_chromosome():
    pop = []
    for _ in courses:
        for index, each in enumerate(university_dict):
            pop.append(''.join(str(random.randint(0, 1)) for _ in range(university_dict[each])))
    return pop


def print_chromosomes(chromosome):
    print(chromosome)
    print('[', end="")
    for i in range(len(chromosome)):
        if i % 12 == 0 and i != 0:
            print(']')
            print('[', end="")
        if i != 0 and i % 12 != 0:
            print(', ', end="")
        print(str(chromosome[i]), end="")
    print(']')


def print_chromosome_details(chromosome):
    pass


if __name__ == "__main__":
    population = populate_chromosome()
    # print_chromosome_details(population)
    print_chromosomes(population)
