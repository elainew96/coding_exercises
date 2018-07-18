'''
This solution is for finding a subset of areas that adds up to a total of where
100,000,000 people live. This solution uses dynamic programming by breaking the
problem down into smaller components, until it reaches the point where the total
population is the same as the population in one area and returns it, or 'None'
is returned. If 'None' is returned, that means that the first population area
that was subtracted from the total cannot be added to the areas that add up to
the total of where the 100,000,000 people live, so the function tries to find
a solution without that element.

Ex:
populations[3,5,1,6]
total = 4

Since total>1 and len(populations)>0, the function enters the first else
statement, and because populations[0] is 3 and total is 4, these are not equal
and the function goes to the second else statement. The variable current is
initialized by shortening the array and decreasing the total, so (4-3) = 1 and
the function is called again with new parameters: areas([5,1,6],1). Since both
len(populations) and total are greater than 0, we check the first element of
populations to see if it is the same as total, which is not true (5!=1). Then,
the function tries to find if we can have the current population[0] in our
solution, so areas([1,6],(1-5)) is called, but now total is -4, which is
negative, so None is returned and we do not include 5 in our solution. Instead,
we return areas([1,6],1) to remove the 5 from our solution and call the function
again with the previous total, and now, we get that populations[0]==total, and
it returns [1]. The variable current will then be [1], and the function will add
this element to the previous element that called it, which was seeing if [3]
was part of the solution, which is true, and the solution [3,1] is returned.
'''

def areas(populations,total):
    if (total<1 or len(populations)==0): #population must be at least 1
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


population = [18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170,
5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833,
3095313, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508,
2134411]
total = 100000000

a = areas(population,total)
print a
print sum(a)
