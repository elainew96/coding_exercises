def areas(populations,total):
    if (total<1 or len(populations)==0): #for general cases
        return None
    else:
        if populations[0]==total:        #this is the base case
            return [populations[0]]
        else:
            # see if the first element can be included in the solution using
            # recursion, or else None will be returned
            current = areas(populations[1:],total-populations[0])
            if current:
                return [populations[0]] + current
            # cannot include the first element in the total
            else:
                return areas(populations[1:],total)


pop = [2,4,2,6,1]
print areas(pop,10)


population = [18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170,
5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833,
3095313, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508,
2134411]
total = 100000000

a = areas(population,total)
print a
print sum(a)
