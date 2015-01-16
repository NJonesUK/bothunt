from math import sqrt

if __name__ == "__main__":
    threshold = 9
    time_delta_list = [0, 3603, 3603, 3603, 3604, 3604, 3604, 3610, 3610, 7206, 38790, 43718]
    sorted_deltas = sorted(time_delta_list)
    list_size = len(sorted_deltas)
    difference = list_size - threshold
    list_of_stdevs = []
    print "Difference:", difference
    for i in xrange(difference + 1):
        print "I:", i, "threshold+i:", (threshold + i)
        print str(sorted_deltas[(threshold + i - 1)]) + " : " + str(sorted_deltas[i])
        list_of_stdevs.append(round((sorted_deltas[(threshold + i - 1)] - sorted_deltas[i])/sqrt(2*list_size), 3))
    print list_of_stdevs