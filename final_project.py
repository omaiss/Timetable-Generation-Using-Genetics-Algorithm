import random

# The chromosomes should be binary encoded with the following information:
# Course, Theory/Lab, Section, Section-Strength, Professor, First-lecture-day,
# First-lecture-timeslot, First-lecture-room, First-lecture-room-size, Second-lecture-day,
# Second-lecture-timeslot, Second-lecture-room, Second-lecture-room-size


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
courses_ll = []
sections_ll = []
sections_strengths_ll = []
professors_ll = []
lecture_days_ll = ['000', '001', '010', '011', '100']
lecture_timeslots_ll = []
lecture_rooms_ll = []

university_dict = {
    "Course": 5,
    "Theory/Lab": 1,
    "Section": 3,
    "Strength": 5,
    "FL_Day": 3,
    "FLT_Slot": 5,
    "FL_Room": 3,
    "FLR_Size": 1,
    "SL_Day": 3,
    "SLT_Slot": 5,
    "SL_Room": 3,
    "SLR_Size": 1,
    "Professor": 5
}


def populate_chromosome(n_pop):
    pop = []
    global courses_ll, lecture_timeslots_ll, sections_ll, professors_ll, sections_strengths_ll
    global lecture_rooms_ll
    flag = True
    j = 0
    for i in range(n_pop):
        pop.append([])
        for course in courses:
            for index, each in enumerate(university_dict):
                if each == 'FL_Day' or each == 'SL_Day':
                    pop[i].append(random.choice(lecture_days_ll))
                else:
                    pop[i].append(''.join(str(random.randint(0, 1)) for _ in range(university_dict[each])))
                if flag:
                    if each == 'Course':
                        courses_ll.append((course, pop[i][0]))
                    elif each == 'Section':
                        f = True
                        for section in sections:
                            if len(sections_ll) > 0:
                                for x in range(len(sections_ll)):
                                    if section not in sections_ll[x]:
                                        sections_ll.append((section, pop[i][2]))
                                        f = False
                                        break
                            else:
                                sections_ll.append((section, pop[i][2]))
                                break
                            if not f:
                                break
                    elif each == 'Strength':
                        f = True
                        for sec_str in section_strength:
                            if len(sections_strengths_ll) > 0:
                                for x in range(len(sections_strengths_ll)):
                                    if sec_str not in sections_strengths_ll[x]:
                                        sections_strengths_ll.append((sec_str, pop[i][3]))
                                        f = False
                                        break
                            else:
                                sections_strengths_ll.append((sec_str, pop[i][3]))
                                break
                            if not f:
                                break
                    elif each == 'FLT_Time':
                        f = True
                        for times in lecture_timeslots:
                            if len(lecture_rooms_ll) > 0:
                                for x in range(len(lecture_timeslots_ll)):
                                    if times not in lecture_timeslots_ll[x]:
                                        lecture_timeslots_ll.append((times, pop[i][5]))
                                        f = False
                                        break
                            else:
                                lecture_timeslots_ll.append((times, pop[i][5]))
                                break
                            if not f:
                                break
                    elif each == 'SLT_Time':
                        f = True
                        for times in lecture_timeslots:
                            if len(lecture_rooms_ll) > 0:
                                for x in range(len(lecture_timeslots_ll)):
                                    if times not in lecture_timeslots_ll:
                                        lecture_timeslots_ll.append((times, pop[i][9]))
                                        f = False
                                        break
                            else:
                                lecture_timeslots_ll.append((times, pop[i][5]))
                                break
                            if not f:
                                break
                    elif each == 'FL_Room':
                        f = True
                        for rooms in lecture_rooms:
                            if len(lecture_rooms_ll) > 0:
                                for x in range(len(lecture_rooms_ll)):
                                    if rooms not in lecture_rooms_ll[x]:
                                        lecture_rooms_ll.append((rooms, pop[i][6]))
                                        f = False
                                        break
                            else:
                                lecture_rooms_ll.append((rooms, pop[i][6]))
                                break
                            if not f:
                                break
                    elif each == 'SL_Room':
                        f = True
                        for rooms in lecture_rooms:
                            if len(lecture_rooms_ll) > 0:
                                for x in range(len(lecture_rooms_ll)):
                                    if rooms not in lecture_rooms_ll[x]:
                                        lecture_rooms_ll.append((rooms, pop[i][10]))
                                        f = True
                                        break
                            else:
                                lecture_rooms_ll.append((rooms, pop[i][6]))
                                break
                            if not f:
                                break
                    elif each == 'Professor':
                        f = True
                        for professor in professors:
                            if len(professors_ll) > 0:
                                for x in range(len(professors_ll)):
                                    if professor not in professors_ll[x]:
                                        professors_ll.append((professor, pop[i][12]))
                                        f = True
                                        break
                            else:
                                professors_ll.append((professor, pop[i][12]))
                                break
                            if not f:
                                break
        flag = False
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
                        if chromosome[i][12] == chromosome[j][12]:
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
    for i in range(len(courses)):
        for j in range(len(university_dict)):
            continue


def twoD_chromosome(chromosome):
    two_d_chromosome = []
    j = -1
    i = 0
    udc_len = len(university_dict)
    chr_len = len(chromosome)
    while 1:
        if i == chr_len:
            break
        if i % udc_len == 0:
            two_d_chromosome.append([])
            j += 1
        two_d_chromosome[j].append(chromosome[i])
        i += 1
    return two_d_chromosome


# tournament selection
def selection(pop, n_pop, scores):
    # Select two random individuals
    idx1 = random.randint(0, n_pop - 1)
    idx2 = random.randint(0, n_pop - 1)
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
        pt = random.randint(0, len(courses) - 1)
        # perform crossover
        temp = c1[pt]
        c1[pt] = c2[pt]
        c2[pt] = temp
    return [c1, c2]


def mutation(bitstring, r_mut):
    bitstring = twoD_chromosome(bitstring)
    if random.random() < r_mut:
        dc0 = random.randint(0, len(university_dict) - 1)
        cc0 = random.randint(0, len(courses) - 1)
        dc1 = random.randint(0, len(university_dict) - 1)
        cc1 = random.randint(0, len(courses) - 1)
        bitstring[cc0][dc0] = bitstring[cc1][dc1]


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
            if -scores[i] < best_eval:
                best, best_eval = pop[i], scores[i]
            print(">%d, new best f(%s) = %d" % (gen + 1, pop[i], scores[i]))
        # select parents
        selected = [selection(pop, n_pop, scores) for _ in range(n_pop)]
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
    # pop = populate_chromosome(2)
    # t = twoD_chromosome(pop[0])
    # print_chromosomes(t)
    best_timetable = None
    best_fitness = -float('inf')

    [current_best, current_fitness] = genetic_algorithm(calculate_fitness, n_iter=100, n_pop=2, r_cross=0.9,
                                                        r_mut=0.01)
    current_best = twoD_chromosome(current_best)
    print_chromosomes(current_best)
    print_chromosome_details(current_best)
    print(f'Fitness for the best time table: {current_fitness}')
    # print(courses_ll, sections_ll, sections_strengths_ll, lecture_timeslots_ll, lecture_rooms_ll, lecture_days_ll,
    #       professors_ll)
