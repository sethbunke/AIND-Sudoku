import solution
import collections

#c = solution.cross(solution.rows, solution.cols)
"""
print('peers')
print(solution.peers)
"""

a = [1,2,3,2,1,5,6,5,5,5]

result = [item for item, count in collections.Counter(a).items() if count > 1]

print(result)
