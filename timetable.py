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


def populate_chromosome(n_pop):
    pop = []
    for i in range(n_pop):
        pop.append([])
        for _ in courses:
            for index, each in enumerate(university_dict):
                pop[i].append(''.join(str(random.randint(0, 1)) for _ in range(university_dict[each])))
    return pop


def print_chromosomes(chromosome):
    for i in range(len(courses)):  # rows
        print(chromosome[i])


def calculate_fitness(chromosome):
    clash_counts = 0
    chromosome = twoD_chromosome(chromosome)
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
def selection(pop, scores):
    # Select two random individuals
    idx1 = random.randint(0, len(pop) - 1)
    idx2 = random.randint(0, len(pop) - 1)

    # Return the individual with the lower fitness score
    if scores[idx1] < scores[idx2]:
        return pop[idx1]
    else:
        return pop[idx2]


def crossover(p1, p2, r_cross):
    # children are copies of parents by default
    c1, c2 = p1.copy(), p2.copy()
    # check for recombination
    if random.random() < r_cross:
        # select crossover point that is not on the end of the string
        pt = random.randint(1, len(p1) - 2)
        # perform crossover
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
    return [c1, c2]


def mutation(bitstring, r_mut):
    for i in range(len(bitstring)):
        # check for a mutation
        if random.random() < r_mut:
            # flip the bit
            bitstring[i] = 1 - bitstring[i]


# genetic algorithm
def genetic_algorithm(objective, n_iter, n_pop, r_cross, r_mut):
    # initial population of random bitstring
    pop = populate_chromosome(n_pop)
    # keep track of best solution
    best, best_eval = None, float('inf')
    # enumerate generations
    for gen in range(n_iter):
        # evaluate all candidates in the population
        scores = [objective(c) for c in pop]
        # check for new best solution
        for i in range(n_pop):
            if scores[i] < best_eval:
                best, best_eval = pop[i], scores[i]
                print(">%d, new best f(%s) = %.3f" % (gen, pop[i], scores[i]))
        # select parents
        selected = [selection(pop, scores) for _ in range(n_pop)]
        # create the next generation
        children = list()
        for i in range(0, n_pop, 2):
            # get selected parents in pairs
            p1, p2 = selected[i], selected[i + 1]
            # crossover and mutation
            for c in crossover(p1, p2, r_cross):
                # mutation
                mutation(c, r_mut)
                # store for next generation
                children.append(c)
        # replace population
        pop = children
    return [best, best_eval]


if __name__ == "__main__":
    pop = populate_chromosome(2)
    t = twoD_chromosome(pop[0])
    print_chromosomes(t)
    # best_timetable = None
    # best_fitness = float('inf')
    #
    # while True:
    #     [current_best, current_fitness] = genetic_algorithm(calculate_fitness, n_iter=100, n_pop=2, r_cross=0.9,
    #                                                         r_mut=0.01)
    #
    #     if current_fitness < best_fitness:
    #         best_timetable = current_best
    #         best_fitness = current_fitness
    #         print("New best timetable found with fitness:", best_fitness)
    #     else:
    #         print("No improvement in fitness. Continuing...")
