# Problem 1: Number of islands
"""Write a function, numIslands, which takes in a 2D grid map
of 1s (land) and 0s (water). Your function should 
return the number of distinct islands in the grid. 
An island is surrounded by water and is formed by 
connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded 
by water."""

# Utilize BFS or DFS

def numIslands(grid):
    """Take in a grid of 1s (land) and 0s (water) and return the number of islands."""
    pass

    # Test Cases
    map1 = [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert numIslands(map1) == 1

    map2 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]
    assert numIslands(map2) == 3



# Problem 2: Rotting Oranges
"""Write a function, timeToRot, which takes in a grid of numbers, each of which is one of the following three values:

A 0 represents an empty spot;
A 1 represents a fresh orange;
A 2 represents a rotten orange.
Every minute, any fresh orange that is adjacent (up, down, left, right) to a rotten orange becomes rotten.

Your function should return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead."""
def timeToRot(grid):
    """
    Take in a grid of numbers, where 0 is an empty space, 1 is a fresh orange, and 2 is a rotten
    orange. Each minute, a rotten orange contaminates its 4-directional neighbors. Return the number
    of minutes until all oranges rot.
    """
    pass

    # Test Cases
    oranges1 = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    assert timeToRot(oranges1) == 4

    oranges2 = [
        [2,1,1],
        [0,1,1],
        [1,0,1]
    ]
    assert timeToRot(oranges2) == -1

    oranges3 = [
        [0,2]
    ]
    assert timeToRot(oranges3) == 0



# Problem 3: Class Scheduling
"""There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array."""
def courseOrder(numCourses, prerequisites):
    """Return a course schedule according to the prerequisites provided."""
    pass

    # Test Cases
    courses1 = [ [1,0] ]
    assert courseOrder(2, courses1) == [0, 1]

courses2 = [ [1,0], [2,0], [3,1], [3,2] ]
possibleSchedules = [ [0, 1, 2, 3], [0, 2, 1, 3] ]
assert courseOrder(4, courses2) in possibleSchedules



# Problem 4: Word Ladder
"""Write a function that takes in two words (beginWord and endWord), and a dictionary’s word list. A word can be transformed into another word if 1), they differ by only one letter, and 2) the new word exists in the dictionary.

Return the length of shortest transformation sequence from beginWord to endWord."""

def wordLadderLength(beginWord, endWord, wordList):
    """Return the length of the shortest word chain from beginWord to endWord, using words from wordList."""
    pass

# Test Cases
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

assert wordLadderLength(beginWord, endWord, wordList) == 5
