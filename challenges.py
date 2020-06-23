from collections import deque

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
    # Returning 0
    # Make sure there's a grid
    if not grid:
        print("No grid")
        return 0
    
    # Establish axes for the grid
    x, y = len(grid), len(grid[0])
    
    # Counter for the number of islands
    num_islands = 0
    
    # Helper Function
    def check_spaces(grid, pointX, pointY, x, y):
        # If the point coordinates are out of bounds, return
        if pointX not in range(0, x):
            print('X out of range')
            return
        if pointY not in range(0, y):
            print('Y out of range')
            return
        
        # Check for an island:
        if grid[pointX][pointY] == 1:
            # Set it to 0 so we don't check it again later
            grid[pointX][pointY] = 0
            
            # Check each space around the point, also turning them into 0s as to not check the same island
            check_spaces(grid, pointX+1, pointY, x, y)
            check_spaces(grid, pointX-1, pointY,x, y)
            check_spaces(grid, pointX, pointY+1, x, y)
            check_spaces(grid, pointX, pointY-1, x, y)
    
    # Run the check on every node
    for pointX in range(0, x):
        # print("works x")
        for pointY in range(0, y):
            # print("works y")
            if grid[pointX][pointY] == 1:
                num_islands += 1
                check_spaces(grid, pointX, pointY, x, y)
            
    # print(num_islands)
    return num_islands



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
    # use queue and 
    # Make sure there's a grid
    if not grid:
        print('No Grid')
        return 0
    
    # Axes for the graph
    x, y = len(grid), len(grid[0])
    
    # A queue to perform BFS on
    q = deque()
    
    # Number of normal oranges still left
    oranges = 0
    
    for row in range(x):
        for col in range(y):
            # Get the number of normal oranges
            if grid[row][col] == 1:
                oranges += 1
            # Find rotten oranges and add their coordinates to the queue
            elif grid[row][col] == 2:
                q.append((row, col))
    
    # If there's no normal oranges to infect, return 0
    if oranges == 0: return 0
    
    # BFS
    time = -1
    while q:
        time += 1
        
        for _ in range(len(q)):
            curr = q.popleft()

            # Get the sides and infect them
            # Side coordinate differences
            sides = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            # Add the differences to the current row and column
            for side in sides:
                curr_row = curr[0] + side[0]
                curr_col = curr[1] + side[1]
                
                # Check if the current coordinates are in bound. If they are, infect the orange and update the orange count
                if curr_row >= 0 and curr_col >= 0 and curr_row < x and curr_col < y and grid[curr_row][curr_col] == 1:
                    grid[curr_row][curr_col] = 2
                    q.append((curr_row, curr_col))
                    oranges -= 1
                    
    return time if oranges == 0 else -1
                    
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

if __name__ == "__main__":
    # Test numIslands
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

