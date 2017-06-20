'''
simulating the situation of choosing the most hygenic toilet
in a music festivel.
link: https://www.youtube.com/watch?v=ZWib5olGbQ0
'''

import itertools

def nextBetter(option, n=1):
    '''
    Take in one possible permutation,
    reject the first n element,
    Return the next better one (than the best among first n).
    If no one is better, return the last one.
    '''
    ref = min(option[0:n])
    for ele in option[n:]:
        if ele < ref:
            return ele
    return option[len(option) - 1]


def getOptimals(options, n=1):
    '''
    Take in a nested list of all possible permutations,
    Return a sorted list of the final choice of each permutation.
    '''
    optimals = []
    for option in options:
        optimals.append(nextBetter(option, n))
    return sorted(optimals)

def mostSaniRate(optList):
    '''
    Take in a list,
    of which each element is the final choice of one permutation,
    Return the rate of choosing the most sanitary toilet.
    (represented in '1')
    '''
    return optList.count(1) / len(optList)



def test():
    opt1 = [1,2,3]
    opt2 = [1,3,2]
    opt3 = [2,1,3]
    opt4 = [2,3,1]
    opt5 = [3,1,2]
    opt6 = [3,2,1]
    opts = list(itertools.permutations([1,2,3], 3))
    assert nextBetter(opt1) == 3
    assert nextBetter(opt2) == 2
    assert nextBetter(opt3) == 1
    assert nextBetter(opt4) == 1
    assert nextBetter(opt5) == 1
    assert nextBetter(opt6) == 2
    assert getOptimals(opts) == [1,1,1,2,2,3]
    assert mostSaniRate(getOptimals(opts)) == 0.5
    assert allPoss_rates(3) == [0.5, 2/6]
    print('test pass\n')



'''
For a given toilet number N, the result of each option of n(number of initial rejection)
will be aggregated into one single number --- the rate of choosing the
most sanitary toilet.

So, in order to test all possible value of n for a given N,
we need a loop and an empty list to store the many mostSaniRates.
'''
def allPoss_rates(N):
    opts = list(itertools.permutations(list(range(1, N+1)), N) )
    allRates = []
    for n in range(1, N):
        allRates.append(mostSaniRate(getOptimals(opts, n)))
    return allRates

# test()


'''
Now let's test the case when number of toilets N=10,
find out what's the highest possible rate of getting the most sanitary one,
and the corresponding n first toilets to reject.
'''

print(allPoss_rates(10))
print('Work is done!')

# This approach of find the best first-n-to-reject might be very limited,
# When N=20, my mac is frozen!
