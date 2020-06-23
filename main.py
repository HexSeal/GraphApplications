from challenges import *

if __name__ == "__main__":
    # Test NumIslands
    # map1 = [
    #     [1, 1, 1, 1, 0],
    #     [1, 1, 0, 1, 0],
    #     [1, 1, 0, 0, 0],
    #     [0, 0, 0, 0, 0]
    # ]
    # print('Your answer: {}\n'.format(numIslands(map1)))
    # assert numIslands(map1) == 1

    # map2 = [
    #     [1, 1, 0, 0, 0],
    #     [1, 1, 0, 0, 0],
    #     [0, 0, 1, 0, 0],
    #     [0, 0, 0, 1, 1]
    # ]
    # print('Your answer: {}\n'.format(numIslands(map2)))
    # assert numIslands(map2) == 3



    # Test Rotten Oranges
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

