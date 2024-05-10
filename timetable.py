import random


# The chromosomes should be binary encoded with the following information:
# Course, Theory/Lab, Section, Section-Strength, Professor, First-lecture-day,
# First-lecture-timeslot, First-lecture-room, First-lecture-room-size, Second-lecture-day,
# Second-lecture-timeslot, Second-lecture-room, Second-lecture-room-size

class Node:
    def __init__(self, data, represents):
        self.data = ''
        self.represents = ''
        self.next = None


courses = ['Database', 'Programming Fundamentals', 'Data Structures', 'Algorithms', 'Computer Networks',
           'Artificial Intelligence', 'Object Oriented Programming', 'Calculus', 'Data Structures', 'Linear Algebra',
           'Applied Pyhsics', 'Operating Systems', 'Web Programming']
theory_lab = ['Theory', 'Lab']
sections = ['A', 'B', 'C']
section_strength = [random.randint(30, 120) for _ in range(len(sections))]
professors = ['Prof. Ahmed Khan', 'Prof. Fatima Ali', 'Prof. Mohammad Khan']
lecture_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
lecture_timeslots = ['8:30 - 9:50', '10:00 - 11:20', '11:30 - 11:50', '1:00 - 2:20', '2:30 - 3:50']
lecture_rooms = ['101', '102', '103']
room_sizes = [60, 120]

# linked lists for mapping strings to binaries
courses_ll = None
sections_ll = None
sections_strengths_ll = None
professors_ll = None
lecture_days_ll = None
lecture_timeslots_ll = None
lecture_rooms_ll = None

university_dict = {
    "Course": 5,
    "Theory/Lab": 1,
    "Section": 3,
    "Strength": 5,
    "FL_Day": 3,
    "FLT_Slot": 5,
    "FL_Room": 5,
    "FLR_Size": 1,
    "SL_Day": 3,
    "SLT_Slot": 5,
    "SL_Room": 5,
    "SLR_Size": 1,
    "Professor": 5
}


def populate_chromosome():
    pop = []
    for _ in courses:
        for index, each in enumerate(university_dict):
            pop.append(''.join(str(random.randint(0, 1)) for _ in range(university_dict[each])))
    return pop


def print_chromosomes(chromosome):
    for i in range(len(courses)):  # rows
        print(chromosome[i])


def calculate_fitness(chromosome):
    clash_counts = 0
    for i in range(len(courses)):
        for j in range(len(courses)):
            # check if the course's First Lectures are on the same day
            if i != j:
                if chromosome[i][0] == chromosome[j][0]:
                    if chromosome[i][2] == chromosome[i][2]:
                        if chromosome[i][11] == chromosome[j][11]:
                            clash_counts -= 1
                            continue
                        if (chromosome[i][4] == chromosome[i][4] or chromosome[i][8] == chromosome[j][8]
                                or chromosome[i][8] == chromosome[j][4] or chromosome[i][4] == chromosome[j][8]):
                            if (chromosome[i][5] == chromosome[j][5] or chromosome[i][9] == chromosome[j][9]
                                    or chromosome[i][5] == chromosome[i][9] or chromosome[i][9] == chromosome[i][
                                        5]):
                                if (chromosome[i][6] == chromosome[j][6] or chromosome[i][10] == chromosome[j][
                                    10] or
                                        chromosome[i][6] == chromosome[j][10] or chromosome[i][10] == chromosome[j][
                                            6]):
                                    clash_counts -= 1
    return int(clash_counts / 2)


def print_chromosome_details(chromosome):
    pass


def twoD_chromosome(chromosome):
    two_d_chromosome = []
    j = 0
    i = 0
    for _ in range(len(chromosome)):
        two_d_chromosome.append([])
        while (i + 1) % len(university_dict) != 0 or i == 0:
            if i < len(chromosome):
                two_d_chromosome[j].append(chromosome[i])
            else:
                break
            i += 1
        if i == len(chromosome):
            break
        j += 1
        i += 1
    return two_d_chromosome


# tournament selection
def selection(pop, scores, k=3):
    # first random selection
    selection_ix = random.randint(0, len(pop))
    for ix in [random.randint(0, len(pop), k - 1)]:
        # check if better (e.g. perform a tournament)
        if scores[ix] < scores[selection_ix]:
            selection_ix = ix
    return pop[selection_ix]


def genetic_algorithm(_population_):
    fitness_score = calculate_fitness(_population_)
    print(f'Fitness for current generation: {fitness_score}')


if __name__ == "__main__":
    population = populate_chromosome()
    two_d_population = twoD_chromosome(chromosome=population)
    print_chromosomes(two_d_population)
    # print_chromosome_details(population)
