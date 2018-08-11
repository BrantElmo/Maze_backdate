"""
    Class : Maze -->to find a path to arrive the ending from starting

    the information of this maze:
    0 wall or way can't through again
    1 way
    2 way through (footprint tag)

"""


class Maze:

    """
        __start : a tuple save 'start'
        __end : a tuple save 'end'
        __maze : a list save 'maze'
        __path : a list ave 'path'
    """

    __start = ()
    __end = ()
    __maze = []
    __path = []

    '''
        initialization of variables
        default : None
        @:param maze: Given a maze created by Two-dimensional array
        @:param start: Given a start of the maze
        @:param end: Given a end of the maze
    '''

    def __init__(self, maze=None, start=None, end=None):
        self.__start = start
        self.__end = end
        self.__maze = maze
        self.__path.append(self.__start)

    '''
        To get a path not shortest
        method:
            1. save 'start' to stack
            2. find the position which can arrive and never arrived.
               (if did,go 3;else,go 5.Clockwise to find) 
            3. if it is a new position, save it
            4. loop 2->3 ,until the top of stack equal 'end'
            5. if there are no way to got it,then go back to last position
            6. loop 2->5
        exm:
        start : (1,1)
        end : (2,1)
        a).                             b).
        0 0 0 0 0   ↑north              0 0 0 0 0   ↑north
        0 1 1 1 0                       0 2 1 1 0
        0 1 1 0 0                       0 1 1 0 0
        0 0 0 0 0                       0 0 0 0 0
        
        c).                             d)
        0 0 0 0 0   ↑north              0 0 0 0 0   ↑north
        0 2 2 1 0                       0 2 2 2 0
        0 1 1 0 0                       0 1 1 0 0
        0 0 0 0 0                       0 0 0 0 0
        
        e).                             f)
        0 0  0  0 0   ↑north             0 0 0 0 0   ↑north
        0 2 (2) 2 0   back               0 2 2 2 0
        0 1  1  0 0                      0 1 2 0 0
        0 0  0  0 0                      0 0 0 0 0
        
        g).                             
        0 0 0 0 0   ↑north             
        0 2 2 2 0   find!              
        0 2 2 0 0                     
        0 0 0 0 0                  
        
        stack:
                                                                    (2,1)
                                (1,3)                   (2,2)       (2,2)
                    (1,2)       (1,2)       (1,2)       (1,2)       (1,2)
        (1,1)       (1,1)       (1,1)       (1,1)       (1,1)       (1,1)
                    
    '''
    def maze_path(self):
        i, j = self.__start[0], self.__start[1]
        path_count = 0
        while True:
            # tag this place arrived
            self.__maze[i][j] = 2
            # judge aside way
            wall = self.__can_through(i, j)
            # not way to arrive
            if wall == -1:
                # go back to last place
                self.__path.pop()

                path_count -= 1
                if path_count == -1:
                    return -1
                i = self.__path[path_count][0]
                j = self.__path[path_count][1]
            # find way
            else:
                path_count += 1
                # north way can arrive
                if wall == 0:
                    i -= 1
                # no north way but east way can arrive
                elif wall == 1:
                    j += 1
                # no north and east way but south way can arrive
                elif wall == 2:
                    i += 1
                # no north, east and south but west way can arrive
                elif wall == 3:
                    j -= 1
                # save the new way at top
                self.__path.append((i, j))
            # judge the top,if equal 'end'.return the path
            if self.__path[path_count][0] == self.__end[0] and self.__path[path_count][1] == self.__end[1]:
                return self.__path

    '''
        __private_method
        @:param m: The current x-axis coordinate in this maze 
        @:param n: The current y-axis coordinate in this maze 
        @:return : If there is a way aside that never go,given a position which can go through.
                   Else,given a information that can tell to go back to last coordinate
    '''

    def __can_through(self, x, y):
        # north
        if self.__maze[x-1][y] == 1:
            return 0
        # no north but east
        elif self.__maze[x][y+1] == 1:
            return 1
        # no north, east but south
        elif self.__maze[x+1][y] == 1:
            return 2
        # no north, east and south but west
        elif self.__maze[x][y-1] == 1:
            return 3
        # no way not arrived
        else:
            return -1


# create a maze
maze_test = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
    ]
# create a class
maze1 = Maze(maze_test, (1, 1), (2, 1))
# print path,if no,print -1
print('The maze path:', maze1.maze_path())
