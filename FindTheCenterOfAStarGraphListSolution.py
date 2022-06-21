class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # create an empty list called edgeList
        edgeList = []
        # access indices [0] and [1] from the list called edges (first and second values and assign them to variable to use below).
        for item in edges:
            firstVal = item[0]
            secondVal = item[1]
        # first we have to check and see if the values for the variable we just created are in edgeList.  If a value is in edgeList we return that value.
            if firstVal in edgeList:
                return firstVal
            if secondVal in edgeList:
                return secondVal
        # if a value is not in edgeList then we add it using the append() function, passing the variable for the value through it, and appending that value to edgeList.
            edgeList.append(firstVal)
            edgeList.append(secondVal)