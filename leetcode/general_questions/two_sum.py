# TwoSum (Easy)

def twoNumberSum(array, targetSum):
    # Write your code here.
    hash_comp = {}
    for val in array:
        comp = targetSum - val
        if comp != val and hash_comp.get(comp):
            return [val, comp]
        hash_comp[val] = 1
        print(hash_comp)
    return []


test_array = [-7, -5, -3, -1, 0, 1, 3, 5, 7]
test_targetSum = -5

assert -5 in twoNumberSum(test_array, test_targetSum)
assert 0 in twoNumberSum(test_array, test_targetSum)