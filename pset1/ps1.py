###########################
# 6.00.2x Problem Set 1: Space Cows

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    import operator
    scopy = sorted(cows.items(), key = operator.itemgetter(1), reverse = True)
    alltrips = []

    while len(scopy) != 0:
        l=limit
        trip = []
        ind = []
        for cow in scopy:
            if cow[1] <= l:
                trip.append(cow[0])
                l-=cow[1]
                ind.append(scopy.index(cow))
        for i in range(len(ind)):
            if i == 0:
                scopy.pop(ind[i])
            else:
                scopy.pop(ind[i]-i)
        alltrips.append(trip)
    return alltrips

def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    possibilities = []
    for possibility in get_partitions(cows):
        i = len(possibility)
        possibilities.append([possibility,i])

    possibilities.sort(key = lambda x:x[-1])

    obeys = False

    for item in possibilities:
        for i in range(item[1]):
            v=0
            for j in range(len(item[0][i])):
                v+=cows[item[0][i][j-1]]
            if v <= limit:
                obeys = True
            else:
                obeys = False
                break
        if obeys == True:
            return item[0]

# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    st1 = time.time()
    a = greedy_cow_transport(cows, 10)
    end1 = time.time()
    t1 = end1-st1

    st2 = time.time()
    b = brute_force_cow_transport(cows, 10)
    end2 = time.time()
    t2 = end2-st2

    print('Greedy:', len(a), t1)
    print('Brute Force:', len(b), t2)
"""
Here is some test data for you to see the results of your algorithms with.
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")

compare_cow_transport_algorithms()

print(greedy_cow_transport(cows, 10))
print(brute_force_cow_transport(cows, 10))
