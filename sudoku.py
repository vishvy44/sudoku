# sudoku
import random
list = [[0 for i in range(4)] for j in range(4)]
#print(list)
ls=list
r=0
co=0
ne=0
lnew=[]
count=0
count2=0
emptylist = []
column_list=[]
Y = random.randint(0, 3)
#print(Y)
list[0][Y] = 2
list[1][Y - 1] = 1
list[2][Y - 3] = 2
list[3][Y] = 3
# ------------------------------------------------------------------------------
def sud(str):
    print("\n")
    print(list[0][0], end=' ')
    print(list[0][1], '|', end=' ')
    print(list[0][2], end=' ')
    print(list[0][3])
    print(list[1][0], end=' ')
    print(list[1][1], '|', end=' ')
    print(list[1][2], end=' ')
    print(list[1][3])
    print('----------')
    print(list[2][0], end=' ')
    print(list[2][1], '|', end=' ')
    print(list[2][2], end=' ')
    print(list[2][3])
    print(list[3][0], end=' ')
    print(list[3][1], '|', end=' ')
    print(list[3][2], end=' ')
    print(list[3][3])
    return str
# ------------------------------------------------------------------------------
print('WELCOME to SUDOKU')
print('Rules-')
print('Fill the grid so every horizontal row,every vertical coloum and........... ', end=' ')
print('every 2*2 box contaions digits(1-4),without repeating the numbers.........')
print('in the same row,coloumn or box.you can not change the digits already givin', end=' ')
print('in the puzzle....................................................')
sud('a')
# ------------------------------------------------------------------------------
def num(str):
    x = int(input("Enter the row at which you want to enter number--"))
    y = int(input("Enter the couloum at which you want to enter number--"))
    z = int(input("Enter a number between 1-4--"))
    if z < 1 or z > 4:
        print('Wrong input pls enter a valid number--')
        z=0
        num('a')
    elif x < 1 or x > 4:
        print('Wrong input pls enter a valid row--')
        x=0
        num('a')
    elif y < 1 or y > 4:
        print('Wrong input pls enter a valid coloum--')
        y=0
        num('a')
    print('row', x)
    print('coloum', y)
    print('number', z)
    list[x - 1][y - 1] = z
    sud('a')
    

num('a')
#--------------------------------------------------------------------------------
def ex():
    print("click ok to quit the game")
    exit()
#---------------------------------------------------------------------------------
def sud_checK(str):
    r=0
    co=0
    count2=0
    for r in range (0,4):
        for i in list[r]:
            if (list[r].count(i)==1):
                if(emptylist[r].count(i)==1):
                    if(column_list[r].count(i)==1):
                        if 0 not in column_list[r]:
                            count=count+1
                            continue
                        else:
                            count2=count2+1
                    else:
                        print("column number - {} have duplicate value".format(r))
                        inp=input("you want to correct it or quit   Y/N  ")
                        if(inp=='y'):
                            num('a')
                            break
                        else:   
                            ex()
                else:
                    print("box number - {} have duplicate value".format(r))
                    inp=input("you want to correct it or quit   Y/N  ")
                    if(inp=='y'):
                        num('a')
                        break
                    else:   
                        ex()
            else:
                print("row number - {} have duplicate value".format(r))
                inp=input("you want to correct it or quit   Y/N  ")
                if(inp=='y'):
                    num('a')
                    break
                else:   
                    ex()
    if(count==3):
        print("sudoku completed congratulations")
    elif(count2>0):
        print("your sudoku is correct you were going well :)")
#--------------------------------------------------------------------------
for r in range(0,4):
    if(r==2):
        ne=1
        
    for co in range(0,2):
        me = ls[r][co]
        lnew.append(me)
        if(ne==0 and co==1 and r==1):
            emptylist.append(lnew[0:4])
        if(ne==1 and co==1 and r==3):
            emptylist.append(lnew[4:8])
            
ne=2
lneww=[]
for r in range(0,4):
    if(r==2):
        ne=3
    for co in range(2,4):
        me = ls[r][co]
        lnew.append(me)
        if(ne==2 and co==3 and r==1):
            emptylist.append(lnew[8:12])
        if(ne==3 and co==3 and r==3):
            emptylist.append(lnew[12:16])
#print(emptylist)
#-------------------------------------------------------------
r=0
co=0
for r in range(0,4):
    
    for co in range(0,4):
        me = ls[co][r]
        lneww.append(me)
        if(r==0 and co==3):
            column_list.append(lneww[0:4])
        if(r==1 and co==3):
            column_list.append(lneww[4:8])
        if(r==2 and co==3):
            column_list.append(lneww[8:12])
        if(r==3 and co==3):
            column_list.append(lneww[12:16])
#print(column_list)
# ----------------------------------------------------------------------------
m = 1
for i in range(50):
    n = input("Are you ready to paly or you want to exit ----Y/N---")
    if n == 'y' or n == 'Y':
        num('a')
        if(i==0):
            print("\n")
            sud('a')
    else:
        sud_checK('a')
        print('Thanks for playing')
        break
    m = m + 1
# ------------------------------------------------------------------------------
print('bye')






