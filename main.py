from challenges import *

if __name__ == "__main__":
    # # Test NumIslands
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



    # Test timeToRot
    # oranges1 = [
    #     [2,1,1],
    #     [1,1,0],
    #     [0,1,1]
    # ]
    # print(timeToRot(oranges1))
    # assert timeToRot(oranges1) == 4

    # oranges2 = [
    #     [2,1,1],
    #     [0,1,1],
    #     [1,0,1]
    # ]
    # print(timeToRot(oranges2))
    # assert timeToRot(oranges2) == -1

    # oranges3 = [
    #     [0,2]
    # ]
    # print(timeToRot(oranges3))
    # assert timeToRot(oranges3) == 0



    # Test courseOrder
    # courses1 = [ [1,0] ]
    # assert courseOrder(2, courses1) == [0, 1]

    # courses2 = [ [1,0], [2,0], [3,1], [3,2] ]
    # possibleSchedules = [ [0, 1, 2, 3], [0, 2, 1, 3] ]
    # assert courseOrder(4, courses2) in possibleSchedules
    
    
    
    # Test Tribonacci
    # print("Testing fib(): {}".format(trib(100)))
    # print("Testing make_trib_table(): {}".format(make_trib_table(100)))
    
    # pass
    items = [ ('boots', 10, 60), ('tent', 20, 100), ('water', 30, 120), ('first aid', 15, 70) ]
    capacity = 50
    print("Highest value: {}".format(knapsack(items, capacity)))