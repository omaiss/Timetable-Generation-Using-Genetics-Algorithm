import random

# The chromosomes should be binary encoded with the following information:
# Course, Theory/Lab, Section, Section-Strength, Professor, First-lecture-day,
# First- lecture-timeslot, First-lecture-room, First-lecture-room-size, Second lecture-day,
# Second-lecture-timeslot, Second-lecture-room, Second-lecture room-size

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
            a = [random.randint(0, 1) for _ in range(university_dict[each])]
            while a in pop:
                a = [random.randint(0, 1) for _ in range(university_dict[each])]
            pop.append(a)
    return pop


if __name__ == "__main__":
    pop = populate_chromosome()
    j = 0
    for i in range(len(courses)):
        print('[', end="")
        for _ in range(len(university_dict)):
            print(pop[j], end="")
            j += 1
        print(']')
