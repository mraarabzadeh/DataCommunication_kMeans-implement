import math
import numpy.random as rd

SIZE_OF_SAMPLE = 5000


def find_index(number,previos_index):
    # if previos_index != 0:
    #     previos_index -= 1
    for x in range(previos_index, SIZE_OF_SAMPLE):
        if sample[x] > number:
            return x
    print('not found {} {}'.format(number, previos_index))

bits, var = [int(x) for x in(input().split())] 
bits = 2**bits - 1
sample = rd.normal(0,var,SIZE_OF_SAMPLE)
sample.sort()
sample = sample.tolist()
range_of_sample = sample[-1] - sample[0]
range_of_sample /= bits + 1
# burders = [find_index(range_of_sample * x + sample[0], 0) for x in range(1,bits+1)]
burders = rd.normal(0,var,bits)
burders.sort()
burders = burders.tolist()
burders = [find_index(burders[x], 0) for x in range(bits)]
# burders.append(SIZE_OF_SAMPLE - 2)
# centers = [int((burders[x] + burders[x+1])/2) for x in range(bits)]
centers = [0 for x in range(bits + 1)]

def find_center_in_a_single_cluster(ith_cluster):
    mini = 9999999999
    selected = 0
    # print(ith_cluster)
    st = burders[ith_cluster] if ith_cluster != -1 else 0
    end = burders[ith_cluster+1] if ith_cluster != bits-1 else SIZE_OF_SAMPLE
    for x in range(st, end):
        sums = 0
        for y in range(st, end):
            sums += (sample[y] - sample[x])**2
        if sums < mini:
            mini = sums
            selected = x
    return sample[selected]

def find_centers():
    for x in range(-1,bits):
        centers[x+1] = find_center_in_a_single_cluster(x)
    for x in range(bits):
        burders[x] = find_index((centers[x] + centers[x+1]) / 2, burders[x-1] if x != 0 else 0)
        # print(x)

if __name__ == "__main__":
    for x in range(200):
        print(burders)
        find_centers()
        # print(x)
    for x in range(bits):
        print(sample[burders[x]])