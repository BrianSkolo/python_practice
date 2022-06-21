class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # create an empty map called edgeMap
        edgeMap = {}
        # access indices [0] and [1] from the list called edges (first and second values and assign them to variable to use below).
        for item in edges:
            firstVal = item[0]
            secondVal = item[1]
        # first we have to check and see if the values for the variable we just created are in edgeMap.  If a value is in edgeMap we return that value.
            if firstVal in edgeMap:
                return firstVal
            if secondVal in edgeMap:
                return secondVal
        # if a value is not in edgeMap then we add it with the syntax below and assigning it to True (boolean)
            edgeMap[firstVal] = True
            edgeMap[secondVal] = True