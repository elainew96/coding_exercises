def areas(populations,total):
    result_pop = []
    result_pop.append(populations[0])
    total -= populations[0]
    count = 1
    while (total!=0):
        min_pop = min(populations)
        if (total<min_pop or total<0 or count>=len(populations)):
            bad = result_pop.pop()
            total += bad
        total -= populations[count]
        result_pop.append(populations[count])
    return result_pop





population = [18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170,
5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833,
3095313, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508,
2134411]

pop = [2,4,2,1]
places = areas(pop,5)
print places
