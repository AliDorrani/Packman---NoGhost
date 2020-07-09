from collections import deque
import collections
import time



def locator(board):
    ppos = []
    qpos = []
    fpos = []

    for i in range( 0, len(board)):
        for j in range (0, len(board[i])):
            if board[i][j] == 'P':
                ppos.append(i)
                ppos.append(j)
                #print(position_P)
            if board[i][j] == 'Q':
                qpos.append(i)
                qpos.append(j)
                #print(position_Q)
            if board[i][j] == '1'or board[i][j] == '2' or board[i][j] == '3' :
                fpos.append([i,j])
            
    return ppos,qpos,fpos


##### __.main.__
filestream = open('test5', 'r')
board = filestream.read().split("\n")
filestream.close()
foods = []
position_Q = []
position_P = []
position_P, position_Q,foods = locator(board)
##### __.main.__


  
def AreEqual(list1 ,list2):
    list1.sort()
    list2.sort()
    if list2 == list1:
        return True


def proccess(node,board,foods,explored,mainNode,P_x,P_y,Q_x,Q_y, condition, poison):

    if(board[P_x][P_y] != "%"):
        if (P_x != Q_x or P_y != Q_y):
            if(board[P_x][P_y] != poison or [P_x,P_y] in node[2]):
                newFood = node[2].copy()
                if(board[P_x][P_y] == condition or board[P_x][P_y] == "3") :
                    if ([P_x,P_y] not in newFood):
                        newFood.append([P_x,P_y])
                        if( AreEqual(newFood, foods)):
                            return True
                newNode = [[P_x,P_y],[Q_x,Q_y],newFood]
                if(newNode not in explored and newNode not in mainNode):
                    mainNode.append(newNode)
    return False



def mainNodesExpand(node,board,foods,explored,mainNode):
    P_x = node[0][0]
    P_y = node[0][1]
    Q_x = node[1][0]
    Q_y = node[1][1]
    result = []
    
    condition = "1"
    poison = "2"
    

    result.append(proccess(node,board,foods,explored,mainNode,P_x+1,P_y,Q_x,Q_y, condition, poison))
    result.append(proccess(node,board,foods,explored,mainNode,P_x,P_y+1,Q_x,Q_y, condition, poison))
    result.append(proccess(node,board,foods,explored,mainNode,P_x-1,P_y,Q_x,Q_y, condition, poison))
    result.append(proccess(node,board,foods,explored,mainNode,P_x,P_y-1,Q_x,Q_y, condition, poison))


    result.append(proccess(node,board,foods,explored,mainNode,Q_x-1,Q_y,P_x,P_y, poison, condition))
    result.append(proccess(node,board,foods,explored,mainNode,Q_x,Q_y-1,P_x,P_y, poison, condition))
    result.append(proccess(node,board,foods,explored,mainNode,Q_x,Q_y+1,P_x,P_y, poison, condition))
    result.append(proccess(node,board,foods,explored,mainNode,Q_x+1,Q_y,P_x,P_y, poison, condition))




    
    
    

    for elem in result:
        if(elem):
            return elem  

    return False

##### __.main.__
mainNodes = deque()
newFoods = []
explored = []
mainNodes.append([position_P,position_Q,newFoods])
finish = False
starttime = time.time()
while(not finish):
    
    nodes = mainNodes.popleft()
    explored.append(nodes)
    finish = mainNodesExpand(nodes,board,foods,explored, mainNodes)
    print(nodes)
endtime  = time.time()

heheheheh = endtime - starttime

print(heheheheh)
print(len(explored))

##### __.main.__
























# if(board[P_x][P_y+1] != "%" and (P_x != Q_x or P_y+1 != Q_y) and (board[P_x][P_y+1] != "2" or [P_x][P_y+1] in node[2])):
#         newFood = node[2]
#         if(board[P_x][P_y+1] == "1" or board[P_x][P_y+1] == "3" and ([P_x][P_y+1] not in newFood)):
#             newFood.append([P_x][P_y+1])
#             if( AreEqual(newFood, foods)):
#                 return True
#         newNode = [[P_x,P_y+1],[Q_x,Q_y],newFood]
#         if(newNode not in explored):
#             mainNode.append(newNode)


    # if(board[P_x][P_y+1] != "%"):
    #     if (P_x != Q_x or P_y+1 != Q_y):
    #         if(board[P_x][P_y+1] != "2" or [P_x][P_y+1] in node[2])):
    #             newFood = node[2]
    #             if(board[P_x][P_y+1] == "1" or board[P_x][P_y+1] == "3":
    #                 if ([P_x][P_y+1] not in newFood)):
    #                     newFood.append([P_x][P_y+1])
    #                     if( AreEqual(newFood, foods)):
    #                         return True
    #                 newNode = [[P_x,P_y+1],[Q_x,Q_y],newFood]
    #                 if(newNode not in explored):
    #                     mainNode.append(newNode)

