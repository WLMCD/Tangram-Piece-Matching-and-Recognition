
import numpy as np
from tkinter import *
from tkinter import ttk

'''
		quu..__
         $$$b  `---.__
          "$$b        `--.                          ___.---uuudP
           `$$b           `.__.------.__     __.---'      $$$$"              .
             "$b          -'            `-.-'            $$$"              .'|
               ".                                       d$"             _.'  |
                 `.   /                              ..."             .'     |
                   `./                           ..::-'            _.'       |
                    /                         .:::-'            .-'         .'
                   :                          ::''\          _.'            |
                  .' .-.             .-.           `.      .'               |
                  : /'$$|           .@"$\           `.   .'              _.-'
                 .'|$u$$|          |$$,$$|           |  <            _.-'
                 | `:$$:'          :$$$$$:           `.  `.       .-'
                 :                  `"--'             |    `-.     \
                :##.       ==             .###.       `.      `.    `\
                |##:                      :###:        |        >     >
                |#'     `..'`..'          `###'        x:      /     /
                 \                                   xXX|     /    ./
                  \                                xXXX'|    /   ./
                  /`-.                                  `.  /   /
                 :    `-  ...........,                   | /  .'
                 |         ``:::::::'       .            |<    `.
                 |             ```          |           x| \ `.:``.
                 |                         .'    /'   xXX|  `:`M`M':.
                 |    |                    ;    /:' xXXX'|  -'MMMMM:'
                 `.  .'                   :    /:'       |-'MMMM.-'
                  |  |                   .'   /'        .'MMM.-'
                  `'`'                   :  ,'          |MMM<
                    |                     `'            |tbap\
                     \                                  :MM.-'
                      \                 |              .''
                       \.               `.            /
                        /     .:::::::.. :           /
                       |     .:::::::::::`.         /
                       |   .:::------------\       /
                      /   .''               >::'  /
                      `',:                 :    .'
                                           `:.:'
                                皮卡大人在上
                                  佑本项目
                            代码无bug ，运行不卡死
                            试验走预判，一轮就稳定
'''
Model1 = np.zeros([10,10,4],dtype=np.int32)
Model2 = np.zeros([10,10,4],dtype=np.int32)
Model3 = np.zeros([10,10,4],dtype=np.int32)
Model4 = np.zeros([10,10,4],dtype=np.int32)
Model5 = np.zeros([10,10,4],dtype=np.int32)
Model6 = np.zeros([10,10,4],dtype=np.int32)
Model7 = np.zeros([10,10,4],dtype=np.int32)
Model8 = np.zeros([10,10,4],dtype=np.int32)
Model9 = np.zeros([10,10,4],dtype=np.int32)
Model10 = np.zeros([10,10,4],dtype=np.int32)
Model11 = np.zeros([10,10,4],dtype=np.int32)
Model12 = np.zeros([10,10,4],dtype=np.int32)
Model13 = np.zeros([10,10,4],dtype=np.int32)

Model1[2,2:6,0:2] = 1
Model1[2,2:5,2:4] = 1
Model1[3,2:5,0:2] = 1
Model1[3,2:4,2:4] = 1
Model1[4,2:4,0:2] = 1
Model1[4,2:3,2:4] = 1
Model1[5,2:3,0:2] = 1
#print (Model1)

Model2[1,4,0] = 1
Model2[1,3,2] = 1
Model2[1,3:5,3] = 1
Model2[2,3:6,0] = 1
Model2[2,3:5,1] = 1
Model2[2,2:5,2] = 1
Model2[2,2:6,3] = 1
Model2[3,3:6,0] = 1
Model2[3,2:6,1] = 1
Model2[3,2:5,2] = 1
Model2[3,3:5,3] = 1
Model2[4,4,0] = 1
Model2[4,3:5,1] = 1
Model2[4,3,2] = 1
#print (Model2)

Model3[2,2:6,0:4] = 1
Model3[3,2:6,0:4] = 1
#print (Model3[2,2:6,0:4])

Model4[2,1:5,1:3] = 1
Model4[2,2:6,0] = 1
Model4[2,2:6,3] = 1
Model4[3,2:6,1:3] = 1
Model4[3,3:7,0] = 1
Model4[3,3:7,3] = 1
#print (Model4)

Model5[2,2,0] = 1
Model5[2,2,3] = 1
Model5[3,2:4,0] = 1
Model5[3,2,1] = 1
Model5[3,2,2] = 1
Model5[3,2:4,3] = 1
Model5[4:6,2:4,0:4] = 1
Model5[6,2:4,0] = 1
Model5[6,2:4,1] = 1
Model5[6,2,2] = 1
Model5[6,2,3] = 1
Model5[7,2,0:2] = 1
#print (Model5)

Model6[2, 2:7, 0:2]=1
Model6[2, 2:6, 2:4]=1
Model6[3, 2:6, 0:2]=1
Model6[3, 2:5, 2:4]=1


Model7[2, 2:3, 0:1]=1
Model7[2, 2:3, 3:4]=1
Model7[3, 2:3, 0:2]=1
Model7[3, 2:3, 2:4]=1
Model7[3, 3:4, 0:1]=1
Model7[3, 3:4, 3:4]=1
Model7[4, 2:4, 0:2]=1
Model7[4, 2:4, 2:4]=1
Model7[4, 4:5, 0:1]=1
Model7[4, 4:5, 3:4]=1
Model7[5, 2:5, 0:2]=1
Model7[5, 2:4, 2:4]=1
Model7[6, 2:3, 1:2]=1
Model7[6, 2:3, 2:3]=1
Model7[6, 3:4, 0:2]=1

Model8[2, 2:4, 2:4]=1
Model8[2, 3:4, 0:2]=1
Model8[2, 4:5, 0:1]=1
Model8[2, 4:5, 3:4]=1
Model8[3, 2:3, 1:2]=1
Model8[3, 2:3, 2:3]=1
Model8[3, 3:5, 0:2]=1
Model8[3, 3:5, 2:4]=1
Model8[3, 5:6, 0:1]=1
Model8[3, 5:6, 3:4]=1
Model8[4, 3:6, 1:3]=1
Model8[4, 4:7, 3:4]=1
Model8[4, 4:7, 0:1]=1

Model9[2, 2:3, 0:2]=1
Model9[2, 2:3, 2:4]=1
Model9[2, 3:4, 0:1]=1
Model9[2, 3:4, 3:4]=1
Model9[3, 2:4, 0:2]=1
Model9[3, 2:4, 2:4]=1
Model9[3, 4:5, 0:1]=1
Model9[3, 4:5, 3:4]=1
Model9[4, 2:5, 0:2]=1
Model9[4, 2:4, 2:4]=1
Model9[5, 2:4, 0:2]=1
Model9[5, 2:3, 2:4]=1

Model10[2, 2:5, 0] = 1
Model10[2, 2:5, 3] = 1
Model10[2, 2:4, 1:3] = 1
Model10[3, 2:5, 0:4] = 1
Model10[4, 3:5, 0] = 1
Model10[4, 2:5, 1:3] = 1
Model10[4, 3:5, 2:4] = 1

Model11[2, 2:4, 1:3] = 1
Model11[2, 2:5, 0] = 1
Model11[2, 2:5, 3] = 1
Model11[3, 2:5, 1:3] = 1
Model11[3, 3:6, 0] = 1
Model11[3, 3:6, 3] = 1
Model11[4, 3:6, 1:3] = 1
Model11[4, 4:6, 0] = 1
Model11[4, 4:6, 3] = 1

Model12[2, 2:5, 0] = 1
Model12[2, 2:5, 3] = 1
Model12[2, 2:4, 1:3] = 1
Model12[3, 2:5, 0:4] = 1
Model12[4, 2:5, 0] = 1
Model12[4, 2:5, 1] = 1
Model12[4, 2:4, 2:4] = 1
Model12[2, 2:4, 1:3] = 1

Model13[2, 2:6, 2:4] = 1
Model13[2, 3:6, 0:2] = 1
Model13[2, 6:7, 0:1] = 1
Model13[2, 6:7, 3:4] = 1
Model13[3, 2:6, 1:3] = 1
Model13[3, 3:7, 0:1] = 1
Model13[3, 3:6, 3:4] = 1
Model13[3, 6:7, 1:2] = 1

########################################################################################3
#大三角左下垂直
def B_T_LD_LD(Model,x,y):
    M = np.zeros([6, 2], dtype=np.int32)
    if  Model[x, y, 0]==1 and Model[x, y, 1]==1 and Model[x, y, 2]==1 and Model[x, y, 3]==1 and Model[x, y+1, 0]==1 and Model[x, y+1, 1]==1 and Model[x+1, y, 0]==1 and Model[x+1, y, 1]==1 :
       Model[x, y, 0:4] = -1
       Model[x, y+1, 0:2] = -1
       Model[x+1, y, 0:2] = -1
       if Model[x - 1, y, 3] == 1:
           M[0, 0] = x - 1
           M[0, 1] = y
       if Model[x - 1, y + 1, 3] == 1:
           M[1, 0] = x - 1
           M[1, 1] = y + 1
       if Model[x, y + 1, 3] == 1:
           M[2, 0] = x
           M[2, 1] = y + 1
       if Model[x + 1, y, 3] == 1:
           M[3, 0] = x + 1
           M[3, 1] = y
       if Model[x, y - 1, 2] == 1:
           M[4, 0] = x
           M[4, 1] = y - 1
       if Model[x + 1, y - 1, 2] == 1:
           M[5, 0] = x + 1
           M[5, 1] = y - 1
    else:
       M[0, 0] = -1
       return M
    return M
def B_T_LD_RD(Model,x,y):
    M = np.zeros([6, 2], dtype=np.int32)
    if Model[x-1, y, 0]==1 and Model[x-1, y, 1]==1 and Model[x-1, y, 2]==1 and Model[x-1, y, 3]==1 and Model[x-1, y+1, 0]==1 and Model[x-1, y+1, 1]==1 and Model[x, y, 0]==1 and Model[x, y, 1]==1 :
        Model[x-1, y, 0:4] = -1
        Model[x-1, y + 1, 0:2] = -1
        Model[x , y, 0:2] = -1
        #print(1231231231)
        if Model[x - 2, y, 3] == 1:
            M[0, 0] = x - 2
            M[0, 1] = y
        if Model[x - 2, y + 1, 3] == 1:
            M[1, 0] = x - 2
            M[1, 1] = y + 1
        if Model[x-1, y + 1, 3] == 1:
            M[2, 0] = x-1
            M[2, 1] = y + 1
        if Model[x, y, 3] == 1:
            M[3, 0] = x
            M[3, 1] = y
        if Model[x, y - 1, 2] == 1:
            M[4, 0] = x
            M[4, 1] = y - 1
        if Model[x - 1, y - 1, 2] == 1:
            M[5, 0] = x -1
            M[5, 1] = y - 1
    else:
       M[0, 0] = -1
       return M
    return M
def B_T_LD_LU(Model,x,y):
    M = np.zeros([6, 2], dtype=np.int32)
    if Model[x, y-1, 0]==1 and Model[x, y-1, 1]==1 and Model[x, y-1, 2]==1 and Model[x, y-1, 3]==1 and Model[x, y, 0]==1 and Model[x, y, 1]==1 and Model[x+1, y-1, 0]==1 and Model[x+1, y-1, 1]==1 :
        Model[x, y-1, 0:4] = -1
        Model[x, y, 0:2] = -1
        Model[x+1 , y-1, 0:2] = -1
        #print(555555555555555)
        if Model[x - 1, y-1, 3] == 1:
            M[0, 0] = x - 1
            M[0, 1] = y-1
        if Model[x - 1, y , 3] == 1:
            M[1, 0] = x - 1
            M[1, 1] = y
        if Model[x, y , 3] == 1:
            M[2, 0] = x
            M[2, 1] = y
        if Model[x+1, y-1, 3] == 1:
            M[3, 0] = x + 1
            M[3, 1] = y-1
        if Model[x, y - 2, 2] == 1:
            M[4, 0] = x
            M[4, 1] = y - 2
        if Model[x +1, y - 2, 2] == 1:
            M[5, 0] = x + 1
            M[5, 1] = y - 2
    else:
       M[0, 0] = -1
       return M
    return M

#大三角右下垂直
def B_T_RD_LD(Model,x,y):
    M = np.zeros([6, 2], dtype=np.int32)
    if  Model[x+1, y, 0]==1 and Model[x+1, y, 1]==1 and Model[x+1, y, 2]==1 and Model[x+1, y, 3]==1 and Model[x, y, 0]==1 and Model[x, y, 3]==1 and Model[x+1, y+1, 0]==1 and Model[x+1, y+1, 3]==1 :
       Model[x+1, y, 0:4] = -1
       Model[x, y, 0] = -1
       Model[x, y, 3] = -1
       Model[x+1, y+1, 0] = -1
       Model[x+1, y+1, 3] = -1
       if Model[x, y, 2] == 1:
           M[0, 0] = x
           M[0, 1] = y
       if Model[x +1, y + 1, 2] == 1:
           M[1, 0] = x + 1
           M[1, 1] = y + 1
       if Model[x+2, y + 1, 1] == 1:
           M[2, 0] = x+2
           M[2, 1] = y + 1
       if Model[x + 2, y, 1] == 1:
           M[3, 0] = x + 2
           M[3, 1] = y
       if Model[x, y -1 , 2] == 1:
           M[4, 0] = x
           M[4, 1] = y - 1
       if Model[x + 1, y - 1, 2] == 1:
           M[5, 0] = x + 1
           M[5, 1] = y - 1
    else:
       M[0, 0] = -1
       return M
    return M
def B_T_RD_RD(Model,x,y):
    M = np.zeros([6, 2], dtype=np.int32)
    if  Model[x, y, 0]==1 and Model[x, y, 1]==1 and Model[x, y, 2]==1 and Model[x, y, 3]==1 and Model[x-1, y, 0]==1 and Model[x-1, y, 3]==1 and Model[x, y+1, 0]==1 and Model[x, y+1, 3]==1 :
       Model[x, y, 0:4] = -1
       Model[x-1, y, 0] = -1
       Model[x-1, y, 3] = -1
       Model[x, y+1, 0] = -1
       Model[x, y+1, 3] = -1
       if Model[x-1, y, 2] == 1:
           M[0, 0] = x-1
           M[0, 1] = y
       if Model[x , y + 1, 2] == 1:
           M[1, 0] = x
           M[1, 1] = y + 1
       if Model[x+1, y + 1, 1] == 1:
           M[2, 0] = x+1
           M[2, 1] = y + 1
       if Model[x + 1, y, 1] == 1:
           M[3, 0] = x + 1
           M[3, 1] = y
       if Model[x-1, y -1 , 2] == 1:
           M[4, 0] = x-1
           M[4, 1] = y - 1
       if Model[x , y - 1, 2] == 1:
           M[5, 0] = x
           M[5, 1] = y - 1
    else:
       M[0, 0] = -1
       return M
    return M
def B_T_RD_RU(Model,x,y):
    M = np.zeros([6, 2], dtype=np.int32)
    if  Model[x, y-1, 0]==1 and Model[x, y-1, 1]==1 and Model[x, y-1, 2]==1 and Model[x, y-1, 3]==1 and Model[x-1, y-1, 0]==1 and Model[x-1, y-1, 3]==1 and Model[x, y, 0]==1 and Model[x, y, 3]==1 :
       Model[x, y-1, 0:4] = -1
       Model[x-1, y-1, 0] = -1
       Model[x-1, y-1, 3] = -1
       Model[x, y, 0] = -1
       Model[x, y, 3] = -1
       if Model[x-1, y-1, 2] == 1:
           M[0, 0] = x-1
           M[0, 1] = y-1
       if Model[x , y , 2] == 1:
           M[1, 0] = x
           M[1, 1] = y
       if Model[x+1, y, 1] == 1:
           M[2, 0] = x+1
           M[2, 1] = y
       if Model[x + 1, y-1, 1] == 1:
           M[3, 0] = x + 1
           M[3, 1] = y-1
       if Model[x-1, y -2 , 2] == 1:
           M[4, 0] = x-1
           M[4, 1] = y - 2
       if Model[x , y - 2, 2] == 1:
           M[5, 0] = x
           M[5, 1] = y - 2
    else:
       M[0, 0] = -1
       return M
    return M

#大三角右上垂直
def B_T_RU_LU(Model,x,y):
    M = np.zeros([6, 2], dtype=np.int32)
    if  Model[x+1, y, 0]==1 and Model[x+1, y, 1]==1 and Model[x+1, y, 2]==1 and Model[x+1, y, 3]==1 and Model[x, y,2]==1 and Model[x, y, 3]==1 and Model[x+1, y-1, 2]==1 and Model[x+1, y-1, 3]==1 :
       Model[x+1, y, 0:4] = -1
       Model[x, y, 2] = -1
       Model[x, y, 3] = -1
       Model[x+1, y-1, 2] = -1
       Model[x+1, y-1, 3] = -1
       if Model[x, y, 1] == 1:
           M[0, 0] = x
           M[0, 1] = y
       if Model[x , y +1 , 0] == 1:
           M[1, 0] = x
           M[1, 1] = y + 1
       if Model[x+1, y + 1, 0] == 1:
           M[2, 0] = x+1
           M[2, 1] = y + 1
       if Model[x + 2, y, 1] == 1:
           M[3, 0] = x + 2
           M[3, 1] = y
       if Model[x, y -1 , 1] == 1:
           M[4, 0] = x
           M[4, 1] = y - 1
       if Model[x + 1, y - 1, 1] == 1:
           M[5, 0] = x + 1
           M[5, 1] = y - 1
    else:
       M[0, 0] = -1
       return M
    return M
def B_T_RU_RU(Model,x,y):
    M = np.zeros([6, 2], dtype=np.int32)
    if  Model[x, y, 0]==1 and Model[x, y, 1]==1 and Model[x, y, 2]==1 and Model[x, y, 3]==1 and Model[x-1, y,2]==1 and Model[x-1, y, 3]==1 and Model[x, y-1, 2]==1 and Model[x, y-1, 3]==1 :
       Model[x, y, 0:4] = -1
       Model[x-1, y, 2] = -1
       Model[x-1, y, 3] = -1
       Model[x, y-1, 2] = -1
       Model[x, y-1, 3] = -1
       if Model[x-1, y, 1] == 1:
           M[0, 0] = x-1
           M[0, 1] = y
       if Model[x-1 , y +1 , 0] == 1:
           M[1, 0] = x-1
           M[1, 1] = y + 1
       if Model[x, y + 1, 0] == 1:
           M[2, 0] = x
           M[2, 1] = y + 1
       if Model[x + 1, y, 1] == 1:
           M[3, 0] = x + 1
           M[3, 1] = y
       if Model[x-1, y -1 , 1] == 1:
           M[4, 0] = x-1
           M[4, 1] = y - 1
       if Model[x , y - 1, 1] == 1:
           M[5, 0] = x
           M[5, 1] = y - 1
    else:
       M[0, 0] = -1
       return M
    return M
def B_T_RU_RD(Model,x,y):
    M = np.zeros([6, 2], dtype=np.int32)
    if  Model[x, y+1, 0]==1 and Model[x, y+1, 1]==1 and Model[x, y+1, 2]==1 and Model[x, y+1, 3]==1 and Model[x-1, y+1,2]==1 and Model[x-1, y+1, 3]==1 and Model[x, y, 2]==1 and Model[x, y, 3]==1 :
       Model[x, y+1, 0:4] = -1
       Model[x-1, y+1, 2] = -1
       Model[x-1, y+1, 3] = -1
       Model[x, y, 2] = -1
       Model[x, y, 3] = -1
       if Model[x-1, y+1, 1] == 1:
           M[0, 0] = x-1
           M[0, 1] = y+1
       if Model[x-1 , y +2 , 0] == 1:
           M[1, 0] = x-1
           M[1, 1] = y + 2
       if Model[x, y + 2, 0] == 1:
           M[2, 0] = x
           M[2, 1] = y + 2
       if Model[x + 1, y+1, 1] == 1:
           M[3, 0] = x + 1
           M[3, 1] = y+1
       if Model[x-1, y  , 1] == 1:
           M[4, 0] = x-1
           M[4, 1] = y
       if Model[x , y , 1] == 1:
           M[5, 0] = x
           M[5, 1] = y
    else:
       M[0, 0] = -1
       return M
    return M

#大三角左上垂直
def B_T_LU_LU(Model,x,y):
    M = np.zeros([6, 2], dtype=np.int32)
    if  Model[x, y, 0]==1 and Model[x, y, 1]==1 and Model[x, y, 2]==1 and Model[x, y, 3]==1 and Model[x+1, y,1]==1 and Model[x+1, y, 2]==1 and Model[x, y-1, 1]==1 and Model[x, y-1, 2]==1 :
       Model[x, y, 0:4] = -1
       Model[x+1, y, 1] = -1
       Model[x+1, y, 2] = -1
       Model[x, y-1, 1] = -1
       Model[x, y-1, 2] = -1
       if Model[x, y+1, 0] == 1:
           M[0, 0] = x
           M[0, 1] = y+1
       if Model[x+1 , y +1 , 0] == 1:
           M[1, 0] = x+1
           M[1, 1] = y + 1
       if Model[x+1, y , 3] == 1:
           M[2, 0] = x+1
           M[2, 1] = y
       if Model[x, y-1, 3] == 1:
           M[3, 0] = x
           M[3, 1] = y-1
       if Model[x-1, y -1 , 3] == 1:
           M[4, 0] = x-1
           M[4, 1] = y - 1
       if Model[x -1, y, 3] == 1:
           M[5, 0] = x - 1
           M[5, 1] = y
    else:
       M[0, 0] = -1
       return M
    return M
def B_T_LU_RU(Model,x,y):
    M = np.zeros([6, 2], dtype=np.int32)
    if  Model[x-1, y, 0]==1 and Model[x-1, y, 1]==1 and Model[x-1, y, 2]==1 and Model[x-1, y, 3]==1 and Model[x, y,1]==1 and Model[x, y, 2]==1 and Model[x-1, y-1, 1]==1 and Model[x-1, y-1, 2]==1 :
       Model[x-1, y, 0:4] = -1
       Model[x, y, 1] = -1
       Model[x, y, 2] = -1
       Model[x-1, y-1, 1] = -1
       Model[x-1, y-1, 2] = -1
       if Model[x-1, y+1, 0] == 1:
           M[0, 0] = x-1
           M[0, 1] = y+1
       if Model[x , y +1 , 0] == 1:
           M[1, 0] = x
           M[1, 1] = y + 1
       if Model[x, y , 3] == 1:
           M[2, 0] = x
           M[2, 1] = y
       if Model[x-1, y-1, 3] == 1:
           M[3, 0] = x-1
           M[3, 1] = y-1
       if Model[x-2, y -1 , 3] == 1:
           M[4, 0] = x-2
           M[4, 1] = y - 1
       if Model[x -2, y, 3] == 1:
           M[5, 0] = x - 2
           M[5, 1] = y
    else:
       M[0, 0] = -1
       return M
    return M
def B_T_LU_LD(Model,x,y):
    M = np.zeros([6, 2], dtype=np.int32)
    if  Model[x, y+1, 0]==1 and Model[x, y+1, 1]==1 and Model[x, y+1, 2]==1 and Model[x, y+1, 3]==1 and Model[x+1, y+1,1]==1 and Model[x+1, y+1, 2]==1 and Model[x, y, 1]==1 and Model[x, y, 2]==1 :
       Model[x, y+1, 0:4] = -1
       Model[x+1, y+1, 1] = -1
       Model[x+1, y+1, 2] = -1
       Model[x, y, 1] = -1
       Model[x, y, 2] = -1
       if Model[x, y+2, 0] == 1:
           M[0, 0] = x
           M[0, 1] = y+2
       if Model[x+1 , y +2 , 0] == 1:
           M[1, 0] = x+1
           M[1, 1] = y + 2
       if Model[x+1, y +1, 3] == 1:
           M[2, 0] = x+1
           M[2, 1] = y+1
       if Model[x, y, 3] == 1:
           M[3, 0] = x
           M[3, 1] = y
       if Model[x-1, y  , 3] == 1:
           M[4, 0] = x-1
           M[4, 1] = y
       if Model[x -1, y+1, 3] == 1:
           M[5, 0] = x - 1
           M[5, 1] = y+1
    else:
       M[0, 0] = -1
       return M
    return M

#中三角形下
def M_T_D_L(Model,x,y):
    M = np.zeros([4, 2], dtype=np.int32)
    if  Model[x+1, y, 0]==1 and Model[x+1, y, 1]==1 and Model[x, y, 0]==1 and Model[x, y, 3]==1:
       Model[x+1, y, 1] = -2
       Model[x+1, y, 0] = -2
       Model[x, y, 0] = -2
       Model[x, y,3] = -2
       if Model[x, y , 1] == 1:
           M[0, 0] = x
           M[0, 1] = y
       if Model[x +1, y, 3] == 1:
           M[1, 0] = x + 1
           M[1, 1] = y
       if Model[x + 1, y - 1, 2] == 1:
           M[2, 0] = x + 1
           M[2, 1] = y - 1
       if Model[x, y-1, 2] == 1:
           M[3, 0] = x
           M[3, 1] = y-1
    else:
        M[0, 0] = -1
        return M
    return M
def M_T_D_R(Model,x,y):
    M = np.zeros([4, 2], dtype=np.int32)
    if  Model[x, y, 0]==1 and Model[x, y, 1]==1 and Model[x-1, y, 0]==1 and Model[x-1, y, 3]==1:
       Model[x, y, 1] = -2
       Model[x, y, 0] = -2
       Model[x-1, y, 0] = -2
       Model[x-1, y,3] = -2
       if Model[x-1, y , 1] == 1:
           M[0, 0] = x-1
           M[0, 1] = y
       if Model[x , y, 3] == 1:
           M[1, 0] = x
           M[1, 1] = y
       if Model[x , y - 1, 2] == 1:
           M[2, 0] = x
           M[2, 1] = y - 1
       if Model[x-1, y-1, 2] == 1:
           M[3, 0] = x-1
           M[3, 1] = y-1
    else:
        M[0, 0] = -1
        return M
    return M

#中三角形长边右
def M_T_R_D(Model,x,y):
    M = np.zeros([4, 2], dtype=np.int32)
    if  Model[x, y+1, 0]==1 and Model[x, y+1, 3]==1 and Model[x, y, 2]==1 and Model[x, y, 3]==1:
       Model[x, y+1, 0] = -2
       Model[x, y+1, 3] = -2
       Model[x, y, 2] = -2
       Model[x, y,3] = -2
       if Model[x, y , 1] == 1:
           M[0, 0] = x
           M[0, 1] = y
       if Model[x , y+1, 1] == 1:
           M[1, 0] = x
           M[1, 1] = y+1
       if Model[x + 1, y , 1] == 1:
           M[2, 0] = x + 1
           M[2, 1] = y
       if Model[x+1, y+1, 1] == 1:
           M[3, 0] = x+1
           M[3, 1] = y+1
    else:
        M[0, 0] = -1
        return M
    return M
def M_T_R_U(Model,x,y):
    M = np.zeros([4, 2], dtype=np.int32)
    if  Model[x, y, 0]==1 and Model[x, y, 3]==1 and Model[x, y-1, 2]==1 and Model[x, y-1, 3]==1:
       Model[x, y, 0] = -2
       Model[x, y, 3] = -2
       Model[x, y-1, 2] = -2
       Model[x, y-1,3] = -2
       if Model[x, y-1 , 1] == 1:
           M[0, 0] = x
           M[0, 1] = y-1
       if Model[x , y, 1] == 1:
           M[1, 0] = x
           M[1, 1] = y
       if Model[x + 1, y-1 , 1] == 1:
           M[2, 0] = x + 1
           M[2, 1] = y-1
       if Model[x+1, y, 1] == 1:
           M[3, 0] = x+1
           M[3, 1] = y
    else:
        M[0, 0] = -1
        return M
    return M

#中三角形上
def M_T_U_L(Model,x,y):
    M = np.zeros([4, 2], dtype=np.int32)
    if  Model[x+1, y, 1]==1 and Model[x+1, y, 2]==1 and Model[x, y, 2]==1 and Model[x, y, 3]==1:
       Model[x+1, y, 1] = -2
       Model[x+1, y, 2] = -2
       Model[x, y, 2] = -2
       Model[x, y,3] = -2
       if Model[x, y , 1] == 1:
           M[0, 0] = x
           M[0, 1] = y
       if Model[x +1, y, 3] == 1:
           M[1, 0] = x + 1
           M[1, 1] = y
       if Model[x + 1, y + 1, 0] == 1:
           M[2, 0] = x + 1
           M[2, 1] = y + 1
       if Model[x, y+1, 0] == 1:
           M[3, 0] = x
           M[3, 1] = y+1
    else:

        M[0, 0] = -1
        return M
    return M
def M_T_U_R(Model,x,y):
    M = np.zeros([4, 2], dtype=np.int32)
    if  Model[x, y, 1]==1 and Model[x, y, 2]==1 and Model[x-1, y, 2]==1 and Model[x-1, y, 3]==1:
       Model[x, y, 1] = -2
       Model[x, y, 2] = -2
       Model[x-1, y, 2] = -2
       Model[x-1, y,3] = -2
       if Model[x-1, y , 1] == 1:
           M[0, 0] = x-1
           M[0, 1] = y
       if Model[x , y, 3] == 1:
           M[1, 0] = x
           M[1, 1] = y
       if Model[x , y + 1, 0] == 1:
           M[2, 0] = x
           M[2, 1] = y + 1
       if Model[x-1, y+1, 0] == 1:
           M[3, 0] = x-1
           M[3, 1] = y+1
    else:
        M[0, 0] = -1
        return M
    return M

#中三角形长边左
def M_T_L_D(Model,x,y):

    M = np.zeros([4, 2], dtype=np.int32)
    if  Model[x, y+1, 0]==1 and Model[x, y+1, 1]==1 and Model[x, y, 2]==1 and Model[x, y, 1]==1:
       Model[x, y+1, 0] = -2
       Model[x, y+1, 1] = -2
       Model[x, y, 2] = -2
       Model[x, y,1] = -2
       if Model[x, y , 3] == 1:
           M[0, 0] = x
           M[0, 1] = y
       if Model[x , y+1, 3] == 1:
           M[1, 0] = x
           M[1, 1] = y+1
       if Model[x - 1, y , 3] == 1:
           M[2, 0] = x - 1
           M[2, 1] = y
       if Model[x-1, y+1, 3] == 1:
           M[3, 0] = x-1
           M[3, 1] = y+1
    else:

        M[0, 0] = -1
        return M
    return M
def M_T_L_U(Model,x,y):

    M = np.zeros([4, 2], dtype=np.int32)
    if  Model[x, y, 0]==1 and Model[x, y, 1]==1 and Model[x, y-1, 2]==1 and Model[x, y-1, 1]==1:
       Model[x, y, 0] = -2
       Model[x, y, 1] = -2
       Model[x, y-1, 2] = -2
       Model[x, y-1,1] = -2
       if Model[x, y-1 , 3] == 1:
           M[0, 0] = x
           M[0, 1] = y-1
       if Model[x , y, 3] == 1:
           M[1, 0] = x
           M[1, 1] = y
       if Model[x - 1, y-1 , 3] == 1:
           M[2, 0] = x - 1
           M[2, 1] = y-1
       if Model[x-1, y, 3] == 1:
           M[3, 0] = x-1
           M[3, 1] = y
    else:

        M[0, 0] = -1
        return M
    return M

#小三角直角左下
def S_T_LD(Model,x,y):

    M = np.zeros([3, 2], dtype=np.int32)
    if  Model[x, y, 0]==1 and Model[x, y, 1]==1 :
       Model[x, y, 0] = -3
       Model[x, y, 1] = -3
       if Model[x, y, 3] == 1:
           M[0, 0] = x
           M[0, 1] = y
       if Model[x , y-1, 2] == 1:
           M[1, 0] = x
           M[1, 1] = y-1
       if Model[x -1, y , 3] == 1:
           M[2, 0] = x - 1
           M[2, 1] = y
    else:
        M[0, 0] = -1
        return M
    return M

#小三角直角右下
def S_T_RD(Model,x,y):

    M = np.zeros([3, 2], dtype=np.int32)
    if  Model[x, y, 0]==1 and Model[x, y, 3]==1 :
       Model[x, y, 0] = -3
       Model[x, y, 3] = -3
       if Model[x, y, 1] == 1:
           M[0, 0] = x
           M[0, 1] = y
       if Model[x , y-1, 2] == 1:
           M[1, 0] = x
           M[1, 1] = y-1
       if Model[x +1, y , 1] == 1:
           M[2, 0] = x + 1
           M[2, 1] = y
    else:

        M[0, 0] = -1
        return M
    return M
def S_T_RU(Model,x,y):

    M = np.zeros([3, 2], dtype=np.int32)
    if  Model[x, y, 2]==1 and Model[x, y, 3]==1 :
       Model[x, y, 2] = -3
       Model[x, y, 3] = -3
       if Model[x, y, 0] == 1:
           M[0, 0] = x
           M[0, 1] = y
       if Model[x , y+1, 0] == 1:
           M[1, 0] = x
           M[1, 1] = y+1
       if Model[x +1, y , 1] == 1:
           M[2, 0] = x + 1
           M[2, 1] = y
    else:

        M[0, 0] = -1
        return M
    return M
def S_T_LU(Model,x,y):

    M = np.zeros([3, 2], dtype=np.int32)
    if  Model[x, y, 1]==1 and Model[x, y, 2]==1 :
       Model[x, y, 2] = -3
       Model[x, y, 1] = -3
       if Model[x, y, 3] == 1:
           M[0, 0] = x
           M[0, 1] = y
       if Model[x , y+1, 0] == 1:
           M[1, 0] = x
           M[1, 1] = y+1
       if Model[x -1, y , 3] == 1:
           M[2, 0] = x - 1
           M[2, 1] = y
    else:

        M[0, 0] = -1
        return M
    return M

#正方形
def Square(Model,x,y):
    M = np.zeros([4, 2], dtype=np.int32)
    if Model[x, y, 0] == 1 and Model[x, y, 1] == 1 and Model[x, y, 2] == 1 and Model[x, y, 3] == 1 :
        Model[x, y, 0:4] = -4
        if Model[x, y+1, 0] == 1:
            M[0, 0] = x
            M[0, 1] = y+1
        if Model[x, y - 1, 2] == 1:
            M[1, 0] = x
            M[1, 1] = y - 1
        if Model[x + 1, y, 1] == 1:
            M[2, 0] = x + 1
            M[2, 1] = y
        if Model[x - 1, y, 3] == 1:
            M[3, 0] = x - 1
            M[3, 1] = y
    else:
        M[0, 0] = -1
        return M
    return M

#平行四边形左上到右下左右斜边
def  Para_LU_Hor_L(Model,x,y):

    M = np.zeros([4, 2], dtype=np.int32)
    if  Model[x, y, 2]==1 and Model[x, y, 3]==1 and Model[x+1, y, 0]==1 and Model[x+1, y, 1]==1:
       Model[x, y, 2] = -5
       Model[x, y, 3] = -5
       Model[x+1, y, 0] = -5
       Model[x+1, y,1] = -5
       if Model[x, y , 1] == 1:
           M[0, 0] = x
           M[0, 1] = y
       if Model[x , y+1, 0] == 1:
           M[1, 0] = x
           M[1, 1] = y+1
       if Model[x + 1, y , 3] == 1:
           M[2, 0] = x + 1
           M[2, 1] = y
       if Model[x+1, y-1, 2] == 1:
           M[3, 0] = x+1
           M[3, 1] = y-1
    else:

        M[0, 0] = -1
        return M
    return M
def  Para_LU_Hor_R(Model,x,y):

    M = np.zeros([4, 2], dtype=np.int32)
    if  Model[x-1, y, 2]==1 and Model[x-1, y, 3]==1 and Model[x, y, 0]==1 and Model[x, y, 1]==1:
       Model[x-1, y, 2] = -5
       Model[x-1, y, 3] = -5
       Model[x, y, 0] = -5
       Model[x, y,1] = -5
       if Model[x-1, y , 1] == 1:
           M[0, 0] = x-1
           M[0, 1] = y
       if Model[x-1 , y+1, 0] == 1:
           M[1, 0] = x-1
           M[1, 1] = y+1
       if Model[x , y , 3] == 1:
           M[2, 0] = x
           M[2, 1] = y
       if Model[x, y-1, 2] == 1:
           M[3, 0] = x
           M[3, 1] = y-1
    else:

        M[0, 0] = -1
        return M
    return M

#平行四边形左下到右上左右斜边
def  Para_LD_Hor_L(Model,x,y):

    M = np.zeros([4, 2], dtype=np.int32)
    if  Model[x, y, 0]==1 and Model[x, y, 3]==1 and Model[x+1, y, 2]==1 and Model[x+1, y, 1]==1:
       Model[x, y, 0] = -5
       Model[x, y, 3] = -5
       Model[x+1, y, 1] = -5
       Model[x+1, y,2] = -5
       if Model[x, y , 1] == 1:
           M[0, 0] = x
           M[0, 1] = y
       if Model[x , y-1, 2] == 1:
           M[1, 0] = x
           M[1, 1] = y-1
       if Model[x + 1, y , 3] == 1:
           M[2, 0] = x + 1
           M[2, 1] = y
       if Model[x+1, y+1, 0] == 1:
           M[3, 0] = x+1
           M[3, 1] = y+1
    else:

        M[0, 0] = -1
        return M
    return M
def  Para_LD_Hor_R(Model,x,y):

    M = np.zeros([4, 2], dtype=np.int32)
    if  Model[x-1, y, 0]==1 and Model[x-1, y, 3]==1 and Model[x, y, 2]==1 and Model[x, y, 1]==1:
       Model[x-1, y, 0] = -5
       Model[x-1, y, 3] = -5
       Model[x, y, 1] = -5
       Model[x, y,2] = -5
       if Model[x-1, y , 1] == 1:
           M[0, 0] = x-1
           M[0, 1] = y
       if Model[x-1 , y-1, 2] == 1:
           M[1, 0] = x-1
           M[1, 1] = y-1
       if Model[x , y , 3] == 1:
           M[2, 0] = x
           M[2, 1] = y
       if Model[x, y+1, 0] == 1:
           M[3, 0] = x
           M[3, 1] = y+1
    else:

        M[0, 0] = -1
        return M
    return M

#平行四边形左下到右上上下斜边
def  Para_LD_Ver_D(Model,x,y):
    M = np.zeros([4, 2], dtype=np.int32)
    if  Model[x, y+1, 0]==1 and Model[x, y+1, 3]==1 and Model[x, y, 2]==1 and Model[x, y, 1]==1:
       Model[x, y+1, 0] = -5
       Model[x, y+1, 3] = -5
       Model[x, y, 1] = -5
       Model[x, y,2] = -5
       if Model[x, y , 3] == 1:
           M[0, 0] = x
           M[0, 1] = y
       if Model[x , y+1, 1] == 1:
           M[1, 0] = x
           M[1, 1] = y+1
       if Model[x - 1, y , 3] == 1:
           M[2, 0] = x - 1
           M[2, 1] = y
       if Model[x+1, y+1, 1] == 1:
           M[3, 0] = x+1
           M[3, 1] = y+1
    else:
        M[0, 0] = -1
        return M
    return M
def  Para_LD_Ver_U(Model,x,y):

    M = np.zeros([4, 2], dtype=np.int32)
    if  Model[x, y, 0]==1 and Model[x, y, 3]==1 and Model[x, y-1, 2]==1 and Model[x, y-1, 1]==1:
       Model[x, y, 0] = -5
       Model[x, y, 3] = -5
       Model[x, y-1, 1] = -5
       Model[x, y-1,2] = -5
       if Model[x, y -1, 3] == 1:
           M[0, 0] = x
           M[0, 1] = y-1
       if Model[x , y, 1] == 1:
           M[1, 0] = x
           M[1, 1] = y
       if Model[x - 1, y-1 , 3] == 1:
           M[2, 0] = x - 1
           M[2, 1] = y-1
       if Model[x+1, y, 1] == 1:
           M[3, 0] = x+1
           M[3, 1] = y
    else:

        M[0, 0] = -1
        return M
    return M

#平行四边形左上到右下上下斜边
def  Para_LU_Ver_D(Model,x,y):

    M = np.zeros([4, 2], dtype=np.int32)
    if  Model[x, y+1, 0]==1 and Model[x, y+1, 1]==1 and Model[x, y, 2]==1 and Model[x, y, 3]==1:
       Model[x, y+1, 0] = -5
       Model[x, y+1, 1] = -5
       Model[x, y, 3] = -5
       Model[x, y,2] = -5
       if Model[x, y , 1] == 1:
           M[0, 0] = x
           M[0, 1] = y
       if Model[x , y+1, 3] == 1:
           M[1, 0] = x
           M[1, 1] = y+1
       if Model[x + 1, y , 1] == 1:
           M[2, 0] = x + 1
           M[2, 1] = y
       if Model[x-1, y+1, 3] == 1:
           M[3, 0] = x-1
           M[3, 1] = y+1
    else:
        M[0, 0] = -1
        return M
    return M
def  Para_LU_Ver_U(Model,x,y):
    M = np.zeros([4, 2], dtype=np.int32)
    if  Model[x, y, 0]==1 and Model[x, y, 1]==1 and Model[x, y-1, 2]==1 and Model[x, y-1, 3]==1:
       Model[x, y, 0] = -5
       Model[x, y, 1] = -5
       Model[x, y-1, 3] = -5
       Model[x, y-1,2] = -5
       if Model[x, y-1 , 1] == 1:
           M[0, 0] = x
           M[0, 1] = y-1
       if Model[x , y, 3] == 1:
           M[1, 0] = x
           M[1, 1] = y
       if Model[x + 1, y-1 , 1] == 1:
           M[2, 0] = x + 1
           M[2, 1] = y-1
       if Model[x-1, y, 3] == 1:
           M[3, 0] = x-1
           M[3, 1] = y
    else:
        M[0, 0] = -1
        return M
    return M

def draw(Model,root,w):

    for x in range(10):
        for y in range(10):
            if Model[x, y, 0] == -1:
                points = [
                    x*20, y*20,
                    x*20+20, y*20,
                    x*20+10, y*20+10,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='red' # 填充色
                )
            elif Model[x, y, 0] == -2:
                points = [
                    x*20, y*20,
                    x*20+20, y*20,
                    x*20+10, y*20+10,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='gray' # 填充色
                )
            elif Model[x, y, 0] == -3:
                points = [
                    x*20, y*20,
                    x*20+20, y*20,
                    x*20+10, y*20+10,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='green' # 填充色
                )
            elif Model[x, y, 0] == -4:
                points = [
                    x*20, y*20,
                    x*20+20, y*20,
                    x*20+10, y*20+10,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='orange' # 填充色
                )
            elif Model[x, y, 0] == -5:
                points = [
                    x * 20, y * 20,
                    x * 20 + 20, y * 20,
                    x * 20 + 10, y * 20 + 10,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='blue'  # 填充色
                )
            elif Model[x, y, 0] == 1:
                points = [
                    x * 20, y * 20,
                    x * 20 + 20, y * 20,
                    x * 20+10, y * 20 + 10,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='yellow'  # 填充色
                )
            elif Model[x, y, 0] == 0:
                points = [
                    x * 20, y * 20,
                    x * 20 + 20, y * 20,
                    x * 20+10, y * 20 + 10,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='white'  # 填充色
                )
#################################################################
            if Model[x, y, 2] == -1:
                points = [
                    x*20+20, y*20+20,
                    x*20, y*20+20,
                    x*20+10, y*20+10,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='red'  # 填充色
                )
            elif Model[x, y, 2] == -2:
                points = [
                    x*20+20, y*20+20,
                    x*20, y*20+20,
                    x*20+10, y*20+10,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='gray'  # 填充色
                )
            elif Model[x, y, 2] == -3:
                points = [
                    x * 20 + 20, y * 20 + 20,
                    x * 20, y * 20 + 20,
                    x * 20 + 10, y * 20 + 10,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='green'  # 填充色
                )
            elif Model[x, y, 2] == -4:
                points = [
                    x * 20 + 20, y * 20 + 20,
                    x * 20, y * 20 + 20,
                    x * 20 + 10, y * 20 + 10,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='orange'  # 填充色
                )
            elif Model[x, y, 2] == -5:
                points = [
                    x * 20 + 20, y * 20 + 20,
                    x * 20, y * 20 + 20,
                    x * 20 + 10, y * 20 + 10,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='blue'  # 填充色
                )
            elif Model[x, y, 2] == 1:
                points = [
                    x * 20 + 20, y * 20 + 20,
                    x * 20, y * 20 + 20,
                    x * 20 + 10, y * 20 + 10,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='yellow'  # 填充色
                )
            elif Model[x, y, 2] == 0:
                points = [
                    x * 20 + 20, y * 20 + 20,
                    x * 20, y * 20 + 20,
                    x * 20 + 10, y * 20 + 10,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='white'  # 填充色
                )
#############################################
            if Model[x, y, 1] == -1:
                points = [
                    x*20, y*20,
                    x*20+10, y*20+10,
                    x*20, y*20+20,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='red'  # 填充色
                )
            elif Model[x, y, 1] == -2:
                points = [
                    x * 20, y * 20,
                    x * 20 + 10, y * 20 + 10,
                    x * 20, y * 20 + 20,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='gray'  # 填充色
                )
            elif Model[x, y, 1] == -3:
                points = [
                    x * 20, y * 20,
                    x * 20 + 10, y * 20 + 10,
                    x * 20, y * 20 + 20,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='green'  # 填充色
                )
            elif Model[x, y, 1] == -4:
                points = [
                    x * 20, y * 20,
                    x * 20 + 10, y * 20 + 10,
                    x * 20, y * 20 + 20,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='orange'  # 填充色
                )
            elif Model[x, y, 1] == -5:
                points = [
                    x * 20, y * 20,
                    x * 20 + 10, y * 20 + 10,
                    x * 20, y * 20 + 20,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='blue'  # 填充色
                )
            elif Model[x, y, 1] == 1:
                points = [
                    x * 20, y * 20,
                    x * 20 + 10, y * 20 + 10,
                    x * 20, y * 20 + 20,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='yellow'  # 填充色
                )
            elif Model[x, y, 1] == 0:
                points = [
                    x * 20, y * 20,
                    x * 20 + 10, y * 20 + 10,
                    x * 20, y * 20 + 20,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='white'  # 填充色
                )
                #################################
            if Model[x, y, 3] == -1:
                points = [
                    x*20+20, y*20,
                    x*20+10, y*20+10,
                    x*20+20, y*20+20,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='red'  # 填充色
                )
            elif Model[x, y, 3] == -2:
                points = [
                    x * 20 + 20, y * 20,
                    x * 20 + 10, y * 20 + 10,
                    x * 20 + 20, y * 20 + 20,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='gray'  # 填充色
                )
            elif Model[x, y, 3] == -3:
                points = [
                    x * 20 + 20, y * 20,
                    x * 20 + 10, y * 20 + 10,
                    x * 20 + 20, y * 20 + 20,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='green'  # 填充色
                )
            elif Model[x, y, 3] == -4:
                points = [
                    x * 20 + 20, y * 20,
                    x * 20 + 10, y * 20 + 10,
                    x * 20 + 20, y * 20 + 20,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='orange'  # 填充色
                )
            elif Model[x, y, 3] == -5:
                points = [
                    x * 20 + 20, y * 20,
                    x * 20 + 10, y * 20 + 10,
                    x * 20 + 20, y * 20 + 20,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='blue'  # 填充色
                )
            elif Model[x, y, 3] == 1:
                points = [
                    x * 20+20, y * 20,
                    x * 20 + 10, y * 20 + 10,
                    x * 20+20, y * 20 + 20,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='yellow'  # 填充色
                )
            elif Model[x, y, 3] == 0:
                points = [
                    x * 20+20, y * 20,
                    x * 20 + 10, y * 20 + 10,
                    x * 20+20, y * 20 + 20,
                ]
                w.create_polygon(
                    points,
                    outline="blue",  # 线的颜色
                    fill='white'  # 填充色
                )

def run_model(Model,use,x,y):
    if(use==1):
        Z=B_T_LD_LD(Model,x,y)
    elif(use==2):
        Z = B_T_LD_RD(Model, x, y)
    elif (use == 3):
        Z = B_T_LD_LU(Model, x, y)
    elif (use == 4):
        Z = B_T_RD_LD(Model, x, y)
    elif (use == 5):
        Z = B_T_RD_RD(Model, x, y)
    elif (use == 6):
        Z = B_T_RD_RU(Model, x, y)
    elif (use == 7):
        Z = B_T_RU_LU(Model, x, y)
    elif (use == 8):
        Z = B_T_RU_RU(Model, x, y)
    elif (use == 9):
        Z = B_T_RU_RD(Model, x, y)
    elif (use == 10):
        Z = B_T_LU_LU(Model, x, y)
    elif (use == 11):
        Z = B_T_LU_RU(Model, x, y)
    elif (use == 12):
        Z = B_T_LU_LD(Model, x, y)
    elif (use == 21):
        Z = M_T_D_L(Model, x, y)
    elif (use == 22):
        Z = M_T_D_R(Model, x, y)
    elif (use == 23):
        Z = M_T_R_D(Model, x, y)
    elif (use == 24):
        Z = M_T_R_U(Model, x, y)
    elif (use == 25):
        Z = M_T_U_L(Model, x, y)
    elif (use == 26):
        Z = M_T_U_R(Model, x, y)
    elif (use == 27):
        Z = M_T_L_D(Model, x, y)
    elif (use == 28):
        Z = M_T_L_U(Model, x, y)
    elif (use == 31):
        Z = S_T_LD(Model, x, y)
    elif (use == 32):
        Z = S_T_LU(Model, x, y)
    elif (use == 33):
        Z = S_T_RD(Model, x, y)
    elif (use == 34):
        Z = S_T_RU(Model, x, y)
    elif (use == 41):
        Z = Square(Model, x, y)
    elif (use == 51):
        Z = Para_LU_Hor_L(Model, x, y)
    elif (use == 52):
        Z = Para_LU_Hor_R(Model, x, y)
    elif (use == 53):
        Z = Para_LD_Hor_L(Model, x, y)
    elif (use == 54):
        Z = Para_LD_Hor_R(Model, x, y)
    elif (use == 55):
        Z = Para_LD_Ver_D(Model, x, y)
    elif (use == 56):
        Z = Para_LD_Ver_U(Model, x, y)
    elif (use == 57):
        Z = Para_LU_Ver_D(Model, x, y)
    elif (use == 58):
        Z = Para_LU_Ver_U(Model, x, y)
    else :print("No model number")
    return Model,Z

def Upgrade():
    f1.pack()
    f2.pack()
    f3.pack()
    f4.pack()
    f5.pack()
    f6.pack()
    f7.pack()
    S = [1,2,3,4,5,6,7,8,9,10,11,12,21,22,23,24,25,26,27,28,31,32,33,34,41,51,52,53,54,55,56,57,58]
    if (numberChosen.get() == '1'):
        Model = Model1.copy()
    elif (numberChosen.get() == '2'):
        Model = Model2.copy()
    elif (numberChosen.get() == '3'):
        Model = Model3.copy()
    elif (numberChosen.get() == '4'):
        Model = Model4.copy()
    elif (numberChosen.get() == '5'):
        Model = Model5.copy()
    elif (numberChosen.get() == '6'):
        Model = Model6.copy()
    elif (numberChosen.get() == '7'):
        Model = Model7.copy()
    elif (numberChosen.get() == '8'):
        Model = Model8.copy()
    elif (numberChosen.get() == '9'):
        Model = Model9.copy()
    elif (numberChosen.get() == '10'):
        Model = Model10.copy()
    elif (numberChosen.get() == '11'):
        Model = Model11.copy()
    elif (numberChosen.get() == '12'):
        Model = Model12.copy()
    elif (numberChosen.get() == '13'):
        Model = Model13.copy()
    for j in range(1):
        panduan = 0
        List = []
        if (aChosen.get() == "DFS"):
            S1 = S.copy()
            w = Canvas(
                f1,
                width=200,
                height=200,
                background="white"
            )
            w.pack(side=LEFT, expand=YES)
            for search in S1:
                BT=2
                MT=1
                ST=2
                SQ=1
                PA=1
                ####################第一层
                Model_1, Z1 = run_model(Model.copy(), search, 2, 2)
                node1 = []
                #删除相关S1对应数据生成S2
                if(Z1[0][0]!=-1) :
                    dell = (search - search % 10)
                    if(dell == 0 or dell ==10) :
                        BT1 = BT-1
                        MT1 = MT
                        ST1 = ST
                        SQ1 = SQ
                        PA1 = PA
                        S2 = S1.copy()
                        if(BT1==0):
                            S2.remove(1)
                            S2.remove(2)
                            S2.remove(3)
                            S2.remove(4)
                            S2.remove(5)
                            S2.remove(6)
                            S2.remove(7)
                            S2.remove(8)
                            S2.remove(9)
                            S2.remove(10)
                            S2.remove(11)
                            S2.remove(12)
                    elif(dell == 20):
                        BT1 = BT
                        MT1 = MT - 1
                        ST1 = ST
                        SQ1 = SQ
                        PA1 = PA
                        S2 = S1.copy()
                        S2.remove(21)
                        S2.remove(22)
                        S2.remove(23)
                        S2.remove(24)
                        S2.remove(25)
                        S2.remove(26)
                        S2.remove(27)
                        S2.remove(28)
                    elif(dell == 30) :
                        BT1 = BT
                        MT1 = MT
                        ST1 = ST -1
                        SQ1 = SQ
                        PA1 = PA
                        S2 = S1.copy()
                        if(ST1==0):
                            S2.remove(31)
                            S2.remove(32)
                            S2.remove(33)
                            S2.remove(34)
                    elif (dell == 40):
                        BT1 = BT
                        MT1 = MT
                        ST1 = ST
                        SQ1 = SQ-1
                        PA1 = PA
                        S2 = S1.copy()
                        S2.remove(41)
                    elif (dell == 50):
                        BT1 = BT
                        MT1 = MT
                        ST1 = ST
                        SQ1 = SQ
                        PA1 = PA-1
                        S2 = S1.copy()
                        S2.remove(51)
                        S2.remove(52)
                        S2.remove(53)
                        S2.remove(54)
                        S2.remove(55)
                        S2.remove(56)
                        S2.remove(57)
                        S2.remove(58)
                    List.append([search,0,0,0,0,0,0,2,2,0])#存储节点信息
                    # 判断是否使用过该节点
                    for ss1 in range(len(Z1)):
                        if (Z1[ss1][0] != 0):
                            node1.append([Z1[ss1][0],Z1[ss1][1],0])
                    #按照节点遍历
                    for sn1 in range(len(node1)):
                        if(node1[sn1][2] == 0):
                            x1 = node1[sn1][0]
                            y1 = node1[sn1][1]
                            node1[sn1][2] = 1
                        for search1 in S2:
                            ####################第二层
                            Model_2, Z2 = run_model(Model_1.copy(), search1, x1, y1)
                            node2 = []
                            if (Z2[0][0] != -1):
                                dell = (search1 - search1 % 10)
                                if (dell == 0 or dell == 10):
                                    BT2 = BT1 - 1
                                    MT2 = MT1
                                    ST2 = ST1
                                    SQ2 = SQ1
                                    PA2 = PA1
                                    S3 = S2.copy()
                                    if (BT2 == 0):
                                        S3.remove(1)
                                        S3.remove(2)
                                        S3.remove(3)
                                        S3.remove(4)
                                        S3.remove(5)
                                        S3.remove(6)
                                        S3.remove(7)
                                        S3.remove(8)
                                        S3.remove(9)
                                        S3.remove(10)
                                        S3.remove(11)
                                        S3.remove(12)
                                elif (dell == 20):
                                    BT2 = BT1
                                    MT2 = MT1-1
                                    ST2 = ST1
                                    SQ2 = SQ1
                                    PA2 = PA1
                                    S3 = S2.copy()
                                    S3.remove(21)
                                    S3.remove(22)
                                    S3.remove(23)
                                    S3.remove(24)
                                    S3.remove(25)
                                    S3.remove(26)
                                    S3.remove(27)
                                    S3.remove(28)
                                elif (dell == 30):
                                    BT2 = BT1
                                    MT2 = MT1
                                    ST2 = ST1-1
                                    SQ2 = SQ1
                                    PA2 = PA1
                                    S3 = S2.copy()
                                    if (ST2 == 0):
                                        S3.remove(31)
                                        S3.remove(32)
                                        S3.remove(33)
                                        S3.remove(34)
                                elif (dell == 40):
                                    BT2 = BT1
                                    MT2 = MT1
                                    ST2 = ST1
                                    SQ2 = SQ1-1
                                    PA2 = PA1
                                    S3 = S2.copy()
                                    S3.remove(41)
                                elif (dell == 50):
                                    BT2 = BT1
                                    MT2 = MT1
                                    ST2 = ST1
                                    SQ2 = SQ1
                                    PA2 = PA1-1
                                    S3 = S2.copy()
                                    S3.remove(51)
                                    S3.remove(52)
                                    S3.remove(53)
                                    S3.remove(54)
                                    S3.remove(55)
                                    S3.remove(56)
                                    S3.remove(57)
                                    S3.remove(58)
                                List.append([search, search1, 0, 0, 0, 0, 0, x1, y1, 0])
                                for ss2 in range(len(Z2)):
                                    if (Z2[ss2][0] != 0):
                                        node2.append([Z2[ss2][0], Z2[ss2][1], 0])
                                for sn2 in range(len(node2)):
                                    if (node2[sn2][2] == 0):
                                        x2 = node2[sn2][0]
                                        y2 = node2[sn2][1]
                                        node2[sn2][2] = 1
                                    for search2 in S3:
                                        ####################第三层
                                        Model_3, Z3 = run_model(Model_2.copy(), search2, x2, y2)
                                        node3 = []
                                        if (Z3[0][0] != -1):
                                            dell = (search2 - search2 % 10)
                                            if (dell == 0 or dell == 10):
                                                BT3 = BT2 - 1
                                                MT3 = MT2
                                                ST3 = ST2
                                                SQ3 = SQ2
                                                PA3 = PA2
                                                S4 = S3.copy()
                                                if (BT3 == 0):
                                                    S4.remove(1)
                                                    S4.remove(2)
                                                    S4.remove(3)
                                                    S4.remove(4)
                                                    S4.remove(5)
                                                    S4.remove(6)
                                                    S4.remove(7)
                                                    S4.remove(8)
                                                    S4.remove(9)
                                                    S4.remove(10)
                                                    S4.remove(11)
                                                    S4.remove(12)
                                            elif (dell == 20):
                                                BT3 = BT2
                                                MT3 = MT2-1
                                                ST3 = ST2
                                                SQ3 = SQ2
                                                PA3 = PA2
                                                S4 = S3.copy()
                                                S4.remove(21)
                                                S4.remove(22)
                                                S4.remove(23)
                                                S4.remove(24)
                                                S4.remove(25)
                                                S4.remove(26)
                                                S4.remove(27)
                                                S4.remove(28)
                                            elif (dell == 30):
                                                BT3 = BT2
                                                MT3 = MT2
                                                ST3 = ST2-1
                                                SQ3 = SQ2
                                                PA3 = PA2
                                                S4 = S3.copy()
                                                if (ST3 == 0):
                                                    S4.remove(31)
                                                    S4.remove(32)
                                                    S4.remove(33)
                                                    S4.remove(34)
                                            elif (dell == 40):
                                                BT3 = BT2
                                                MT3 = MT2
                                                ST3 = ST2
                                                SQ3 = SQ2-1
                                                PA3 = PA2
                                                S4 = S3.copy()
                                                S4.remove(41)
                                            elif (dell == 50):
                                                BT3 = BT2
                                                MT3 = MT2
                                                ST3 = ST2
                                                SQ3 = SQ2
                                                PA3 = PA2-1
                                                S4 = S3.copy()
                                                S4.remove(51)
                                                S4.remove(52)
                                                S4.remove(53)
                                                S4.remove(54)
                                                S4.remove(55)
                                                S4.remove(56)
                                                S4.remove(57)
                                                S4.remove(58)
                                            List.append([search, search1, search2, 0, 0, 0, 0, x2, y2, 0])
                                            for ss3 in range(len(Z3)):
                                                if (Z3[ss3][0] != 0):
                                                    node3.append([Z3[ss3][0], Z3[ss3][1], 0])
                                            for sn3 in range(len(node3)):
                                                if (node3[sn3][2] == 0):
                                                    x3 = node3[sn3][0]
                                                    y3 = node3[sn3][1]
                                                    node3[sn3][2] = 1
                                                for search3 in S4:
                                                    ####################第四层
                                                    Model_4, Z4 = run_model(Model_3.copy(), search3, x3, y3)
                                                    node4 = []
                                                    if (Z4[0][0] != -1):
                                                        dell = (search3 - search3 % 10)
                                                        if (dell == 0 or dell == 10):
                                                            BT4 = BT3 - 1
                                                            MT4 = MT3
                                                            ST4 = ST3
                                                            SQ4 = SQ3
                                                            PA4 = PA3
                                                            S5 = S4.copy()
                                                            if (BT4 == 0):
                                                                S5.remove(1)
                                                                S5.remove(2)
                                                                S5.remove(3)
                                                                S5.remove(4)
                                                                S5.remove(5)
                                                                S5.remove(6)
                                                                S5.remove(7)
                                                                S5.remove(8)
                                                                S5.remove(9)
                                                                S5.remove(10)
                                                                S5.remove(11)
                                                                S5.remove(12)
                                                        elif (dell == 20):
                                                            BT4 = BT3
                                                            MT4 = MT3-1
                                                            ST4 = ST3
                                                            SQ4 = SQ3
                                                            PA4 = PA3
                                                            S5 = S4.copy()
                                                            S5.remove(21)
                                                            S5.remove(22)
                                                            S5.remove(23)
                                                            S5.remove(24)
                                                            S5.remove(25)
                                                            S5.remove(26)
                                                            S5.remove(27)
                                                            S5.remove(28)
                                                        elif (dell == 30):
                                                            BT4 = BT3
                                                            MT4 = MT3
                                                            ST4 = ST3-1
                                                            SQ4 = SQ3
                                                            PA4 = PA3
                                                            S5 = S4.copy()
                                                            if (ST4 == 0):
                                                                S5.remove(31)
                                                                S5.remove(32)
                                                                S5.remove(33)
                                                                S5.remove(34)
                                                        elif (dell == 40):
                                                            BT4 = BT3
                                                            MT4 = MT3
                                                            ST4 = ST3
                                                            SQ4 = SQ3-1
                                                            PA4 = PA3
                                                            S5 = S4.copy()
                                                            S5.remove(41)
                                                        elif (dell == 50):
                                                            BT4 = BT3
                                                            MT4 = MT3
                                                            ST4 = ST3
                                                            SQ4 = SQ3
                                                            PA4 = PA3-1
                                                            S5 = S4.copy()
                                                            S5.remove(51)
                                                            S5.remove(52)
                                                            S5.remove(53)
                                                            S5.remove(54)
                                                            S5.remove(55)
                                                            S5.remove(56)
                                                            S5.remove(57)
                                                            S5.remove(58)
                                                        List.append([search, search1,search2, search3, 0, 0, 0, x3, y3, 0])
                                                        for ss4 in range(len(Z4)):
                                                            if (Z4[ss4][0] != 0):
                                                                node4.append([Z4[ss4][0], Z4[ss4][1], 0])
                                                        for sn4 in range(len(node4)):
                                                            if (node4[sn4][2] == 0):
                                                                x4 = node4[sn4][0]
                                                                y4 = node4[sn4][1]
                                                                node4[sn4][2] = 1
                                                            for search4 in S5:
                                                                ####################第五层
                                                                Model_5, Z5 = run_model(Model_4.copy(), search4, x4, y4)
                                                                node5 = []
                                                                if (Z5[0][0] != -1):
                                                                    dell = (search4 - search4 % 10)
                                                                    if (dell == 0 or dell == 10):
                                                                        BT5 = BT4 - 1
                                                                        MT5 = MT4
                                                                        ST5 = ST4
                                                                        SQ5 = SQ4
                                                                        PA5 = PA4
                                                                        S6 = S5.copy()
                                                                        if (BT5 == 0):
                                                                            S6.remove(1)
                                                                            S6.remove(2)
                                                                            S6.remove(3)
                                                                            S6.remove(4)
                                                                            S6.remove(5)
                                                                            S6.remove(6)
                                                                            S6.remove(7)
                                                                            S6.remove(8)
                                                                            S6.remove(9)
                                                                            S6.remove(10)
                                                                            S6.remove(11)
                                                                            S6.remove(12)
                                                                    elif (dell == 20):
                                                                        BT5 = BT4
                                                                        MT5 = MT4-1
                                                                        ST5 = ST4
                                                                        SQ5 = SQ4
                                                                        PA5 = PA4
                                                                        S6 = S5.copy()
                                                                        S6.remove(21)
                                                                        S6.remove(22)
                                                                        S6.remove(23)
                                                                        S6.remove(24)
                                                                        S6.remove(25)
                                                                        S6.remove(26)
                                                                        S6.remove(27)
                                                                        S6.remove(28)
                                                                    elif (dell == 30):
                                                                        BT5 = BT4
                                                                        MT5 = MT4
                                                                        ST5 = ST4-1
                                                                        SQ5 = SQ4
                                                                        PA5 = PA4
                                                                        S6 = S5.copy()
                                                                        if (ST5 == 0):
                                                                            S6.remove(31)
                                                                            S6.remove(32)
                                                                            S6.remove(33)
                                                                            S6.remove(34)
                                                                    elif (dell == 40):
                                                                        BT5 = BT4
                                                                        MT5 = MT4
                                                                        ST5 = ST4
                                                                        SQ5 = SQ4-1
                                                                        PA5 = PA4
                                                                        S6 = S5.copy()
                                                                        S6.remove(41)
                                                                    elif (dell == 50):
                                                                        BT5 = BT4
                                                                        MT5 = MT4
                                                                        ST5 = ST4
                                                                        SQ5 = SQ4
                                                                        PA5 = PA4-1
                                                                        S6 = S5.copy()
                                                                        S6.remove(51)
                                                                        S6.remove(52)
                                                                        S6.remove(53)
                                                                        S6.remove(54)
                                                                        S6.remove(55)
                                                                        S6.remove(56)
                                                                        S6.remove(57)
                                                                        S6.remove(58)
                                                                    List.append(
                                                                        [search, search1, search2, search3,search4, 0, 0, x4,y4, 0])
                                                                    for ss5 in range(len(Z5)):
                                                                        if (Z5[ss5][0] != 0):
                                                                            node5.append([Z5[ss5][0], Z5[ss5][1], 0])
                                                                    for sn5 in range(len(node5)):
                                                                        if (node5[sn5][2] == 0):
                                                                            x5 = node5[sn5][0]
                                                                            y5 = node5[sn5][1]
                                                                            node5[sn5][2] = 1
                                                                        for search5 in S6:
                                                                            #print(S6, x5, y5)
                                                                            ####################第六层
                                                                            Model_6, Z6 = run_model(Model_5.copy(), search5, x5,
                                                                                                  y5)
                                                                            node6 = []
                                                                            if (Z6[0][0] != -1):
                                                                                dell = (search5 - search5 % 10)
                                                                                if (dell == 0 or dell == 10):
                                                                                    BT6 = BT5 - 1
                                                                                    MT6 = MT5
                                                                                    ST6 = ST5
                                                                                    SQ6 = SQ5
                                                                                    PA6 = PA5
                                                                                    S7 = S6.copy()
                                                                                    if (BT6 == 0):
                                                                                        S7.remove(1)
                                                                                        S7.remove(2)
                                                                                        S7.remove(3)
                                                                                        S7.remove(4)
                                                                                        S7.remove(5)
                                                                                        S7.remove(6)
                                                                                        S7.remove(7)
                                                                                        S7.remove(8)
                                                                                        S7.remove(9)
                                                                                        S7.remove(10)
                                                                                        S7.remove(11)
                                                                                        S7.remove(12)
                                                                                elif (dell == 20):
                                                                                    BT6 = BT5
                                                                                    MT6 = MT5 - 1
                                                                                    ST6 = ST5
                                                                                    SQ6 = SQ5
                                                                                    PA6 = PA5
                                                                                    S7 = S6.copy()
                                                                                    S7.remove(21)
                                                                                    S7.remove(22)
                                                                                    S7.remove(23)
                                                                                    S7.remove(24)
                                                                                    S7.remove(25)
                                                                                    S7.remove(26)
                                                                                    S7.remove(27)
                                                                                    S7.remove(28)
                                                                                elif (dell == 30):
                                                                                    BT6 = BT5
                                                                                    MT6 = MT5
                                                                                    ST6 = ST5 - 1
                                                                                    SQ6 = SQ5
                                                                                    PA6 = PA5
                                                                                    S7 = S6.copy()
                                                                                    if (ST6== 0):
                                                                                        S7.remove(31)
                                                                                        S7.remove(32)
                                                                                        S7.remove(33)
                                                                                        S7.remove(34)
                                                                                elif (dell == 40):
                                                                                    BT6 = BT5
                                                                                    MT6 = MT5
                                                                                    ST6 = ST5
                                                                                    SQ6 = SQ5 - 1
                                                                                    PA6 = PA5
                                                                                    S7 = S6.copy()
                                                                                    S7.remove(41)
                                                                                elif (dell == 50):
                                                                                    BT6 = BT5
                                                                                    MT6 = MT5
                                                                                    ST6 = ST5
                                                                                    SQ6 = SQ5
                                                                                    PA6 = PA5 - 1
                                                                                    S7 = S6.copy()
                                                                                    S7.remove(51)
                                                                                    S7.remove(52)
                                                                                    S7.remove(53)
                                                                                    S7.remove(54)
                                                                                    S7.remove(55)
                                                                                    S7.remove(56)
                                                                                    S7.remove(57)
                                                                                    S7.remove(58)
                                                                                List.append(
                                                                                    [search, search1, search2, search3,
                                                                                     search4, search5, 0, x5, y5, 0])
                                                                                for ss6 in range(len(Z6)):
                                                                                    if (Z6[ss6][0] != 0):
                                                                                        node6.append(
                                                                                            [Z6[ss6][0], Z6[ss6][1], 0])
                                                                                for sn6 in range(len(node6)):
                                                                                    if (node6[sn6][2] == 0):
                                                                                        x6 = node6[sn6][0]
                                                                                        y6 = node6[sn6][1]
                                                                                        node6[sn6][2] = 1
                                                                                    for search6 in S7:
                                                                                        ####################第七层
                                                                                        Model_7, Z7 = run_model(
                                                                                            Model_6.copy(), search6, x6,
                                                                                            y6)
                                                                                        if (Z7[0][0] != -1):
                                                                                            List.append(
                                                                                                [search, search1,
                                                                                                 search2, search3,
                                                                                                 search4, search5, search6,
                                                                                                 x6, y6, 0])
                                                                                            panduan = -1
                                                                                            break
                                                                                    if (panduan == -1): break
                                                                                if (panduan == -1): break
                                                                        if (panduan == -1): break
                                                                    if (panduan == -1): break
                                                                if (panduan == -1): break
                                                            if (panduan == -1): break
                                                        if (panduan == -1): break
                                                    if (panduan == -1): break
                                                if (panduan == -1): break
                                            if (panduan == -1): break
                                        if (panduan == -1): break
                                    if (panduan == -1): break
                                if (panduan == -1): break
                            if (panduan == -1): break
                        if (panduan == -1): break
                    if (panduan == -1): break
                if (panduan == -1):break

            print("List",List)
            draw(Model_7, root, w)
        if (aChosen.get() == "BFS"):
            numNode_1 = 0
            numNode_2 = 0
            numNode_3 = 0
            numNode_4 = 0
            numNode_5 = 0
            numNode_6 = 0
            numNode_7 = 0
            S1 = S.copy()
            Node_1 = []
            Node_2 = []
            Node_3 = []
            Node_4 = []
            Node_5 = []
            Node_6 = []
            Node_7 = []
            #第一层
            fnode = []
            for a in range(10):
                for b in range(10):
                    if (Model[a][b][0] == 1 or Model[a][b][1] == 1 or Model[a][b][2] == 1 or Model[a][b][3] == 1):
                        fnode.append([a, b])
            kInt = 0
            for k in fnode:
                kInt+=1
                if(kInt>5): break
                for search in S1:
                    BT=2
                    MT=1
                    ST=2
                    SQ=1
                    PA=1
                    ####################第一层运行
                    Model_1, Z1 = run_model(Model.copy(), search, k[0],k[1] )
                    if (Z1[0][0] != -1):
                        dell = (search - search % 10)
                        if (dell == 0 or dell == 10):
                            BT1 = BT - 1
                            MT1 = MT
                            ST1 = ST
                            SQ1 = SQ
                            PA1 = PA
                            S2 = S1.copy()
                            if (BT1 == 0):
                                S2.remove(1)
                                S2.remove(2)
                                S2.remove(3)
                                S2.remove(4)
                                S2.remove(5)
                                S2.remove(6)
                                S2.remove(7)
                                S2.remove(8)
                                S2.remove(9)
                                S2.remove(10)
                                S2.remove(11)
                                S2.remove(12)
                        elif (dell == 20):
                            BT1 = BT
                            MT1 = MT - 1
                            ST1 = ST
                            SQ1 = SQ
                            PA1 = PA
                            S2 = S1.copy()
                            S2.remove(21)
                            S2.remove(22)
                            S2.remove(23)
                            S2.remove(24)
                            S2.remove(25)
                            S2.remove(26)
                            S2.remove(27)
                            S2.remove(28)
                        elif (dell == 30):
                            BT1 = BT
                            MT1 = MT
                            ST1 = ST - 1
                            SQ1 = SQ
                            PA1 = PA
                            S2 = S1.copy()
                            if (ST1 == 0):
                                S2.remove(31)
                                S2.remove(32)
                                S2.remove(33)
                                S2.remove(34)
                        elif (dell == 40):
                            BT1 = BT
                            MT1 = MT
                            ST1 = ST
                            SQ1 = SQ - 1
                            PA1 = PA
                            S2 = S1.copy()
                            S2.remove(41)
                        elif (dell == 50):
                            BT1 = BT
                            MT1 = MT
                            ST1 = ST
                            SQ1 = SQ
                            PA1 = PA - 1
                            S2 = S1.copy()
                            S2.remove(51)
                            S2.remove(52)
                            S2.remove(53)
                            S2.remove(54)
                            S2.remove(55)
                            S2.remove(56)
                            S2.remove(57)
                            S2.remove(58)
                        node1 = []
                        for ss1 in range(len(Z1)):
                            if (Z1[ss1][0] != 0):
                                node1.append([Z1[ss1][0],Z1[ss1][1],0])
                        Node_1.append([Model_1.copy(),node1.copy(),S2.copy(),BT1,MT1,ST1,SQ1,PA1,numNode_1,-1,-1,-1,-1,-1,-1,search, k[0], k[1]])
                        numNode_1+=1
            ###第二层
            for node in Node_1:
                Model_1 = node[0]
                node1 = node[1]
                S2 = node[2]
                BT1 = node[3]
                MT1 = node[4]
                ST1 = node[5]
                SQ1 = node[6]
                PA1 = node[7]
                numNode_1 = node[8]
                for sn1 in range(len(node1)):
                    if (node1[sn1][2] == 0):
                        x1 = node1[sn1][0]
                        y1 = node1[sn1][1]
                        node1[sn1][2] = 1
                    for search1 in S2:
                        Model_2, Z2 = run_model(Model_1.copy(), search1, x1, y1)
                        node2 = []
                        if (Z2[0][0] != -1):
                            dell = (search1 - search1 % 10)
                            if (dell == 0 or dell == 10):
                                BT2 = BT1 - 1
                                MT2 = MT1
                                ST2 = ST1
                                SQ2 = SQ1
                                PA2 = PA1
                                S3 = S2.copy()
                                if (BT2 == 0):
                                    S3.remove(1)
                                    S3.remove(2)
                                    S3.remove(3)
                                    S3.remove(4)
                                    S3.remove(5)
                                    S3.remove(6)
                                    S3.remove(7)
                                    S3.remove(8)
                                    S3.remove(9)
                                    S3.remove(10)
                                    S3.remove(11)
                                    S3.remove(12)
                            elif (dell == 20):
                                BT2 = BT1
                                MT2 = MT1 - 1
                                ST2 = ST1
                                SQ2 = SQ1
                                PA2 = PA1
                                S3 = S2.copy()
                                S3.remove(21)
                                S3.remove(22)
                                S3.remove(23)
                                S3.remove(24)
                                S3.remove(25)
                                S3.remove(26)
                                S3.remove(27)
                                S3.remove(28)
                            elif (dell == 30):
                                BT2 = BT1
                                MT2 = MT1
                                ST2 = ST1 - 1
                                SQ2 = SQ1
                                PA2 = PA1
                                S3 = S2.copy()
                                if (ST2 == 0):
                                    S3.remove(31)
                                    S3.remove(32)
                                    S3.remove(33)
                                    S3.remove(34)
                            elif (dell == 40):
                                BT2 = BT1
                                MT2 = MT1
                                ST2 = ST1
                                SQ2 = SQ1 - 1
                                PA2 = PA1
                                S3 = S2.copy()
                                S3.remove(41)
                            elif (dell == 50):
                                BT2 = BT1
                                MT2 = MT1
                                ST2 = ST1
                                SQ2 = SQ1
                                PA2 = PA1 - 1
                                S3 = S2.copy()
                                S3.remove(51)
                                S3.remove(52)
                                S3.remove(53)
                                S3.remove(54)
                                S3.remove(55)
                                S3.remove(56)
                                S3.remove(57)
                                S3.remove(58)
                            for ss2 in range(len(Z2)):
                                if (Z2[ss2][0] != 0):
                                    node2.append([Z2[ss2][0], Z2[ss2][1], 0])
                            Node_2.append(
                                [Model_2.copy(), node2.copy(), S3.copy(), BT2, MT2, ST2, SQ2, PA2, numNode_1, numNode_2, -1,
                                 -1, -1, -1, -1, search1, x1, y1])
                            numNode_2 +=1
            ###第三层
            for node in Node_2:
                Model_2 = node[0]
                node2 = node[1]
                S3 = node[2]
                BT2 = node[3]
                MT2 = node[4]
                ST2 = node[5]
                SQ2 = node[6]
                PA2 = node[7]
                numNode_1 = node[8]
                numNode_2 = node[9]
                for sn2 in range(len(node2)):
                    if (node2[sn2][2] == 0):
                        x2 = node2[sn2][0]
                        y2 = node2[sn2][1]
                        node2[sn2][2] = 1
                    for search2 in S3:
                            Model_3, Z3 = run_model(Model_2.copy(), search2, x2, y2)
                            node3 = []
                            if (Z3[0][0] != -1):
                                dell = (search2 - search2 % 10)
                                if (dell == 0 or dell == 10):
                                    BT3 = BT2 - 1
                                    MT3 = MT2
                                    ST3 = ST2
                                    SQ3 = SQ2
                                    PA3 = PA2
                                    S4 = S3.copy()
                                    if (BT3 == 0):
                                        S4.remove(1)
                                        S4.remove(2)
                                        S4.remove(3)
                                        S4.remove(4)
                                        S4.remove(5)
                                        S4.remove(6)
                                        S4.remove(7)
                                        S4.remove(8)
                                        S4.remove(9)
                                        S4.remove(10)
                                        S4.remove(11)
                                        S4.remove(12)
                                elif (dell == 20):
                                    BT3 = BT2
                                    MT3 = MT2 - 1
                                    ST3 = ST2
                                    SQ3 = SQ2
                                    PA3 = PA2
                                    S4 = S3.copy()
                                    S4.remove(21)
                                    S4.remove(22)
                                    S4.remove(23)
                                    S4.remove(24)
                                    S4.remove(25)
                                    S4.remove(26)
                                    S4.remove(27)
                                    S4.remove(28)
                                elif (dell == 30):
                                    BT3 = BT2
                                    MT3 = MT2
                                    ST3 = ST2 - 1
                                    SQ3 = SQ2
                                    PA3 = PA2
                                    S4 = S3.copy()
                                    if (ST3 == 0):
                                        S4.remove(31)
                                        S4.remove(32)
                                        S4.remove(33)
                                        S4.remove(34)
                                elif (dell == 40):
                                    BT3 = BT2
                                    MT3 = MT2
                                    ST3 = ST2
                                    SQ3 = SQ2 - 1
                                    PA3 = PA2
                                    S4 = S3.copy()
                                    S4.remove(41)
                                elif (dell == 50):
                                    BT3 = BT2
                                    MT3 = MT2
                                    ST3 = ST2
                                    SQ3 = SQ2
                                    PA3 = PA2 - 1
                                    S4 = S3.copy()
                                    S4.remove(51)
                                    S4.remove(52)
                                    S4.remove(53)
                                    S4.remove(54)
                                    S4.remove(55)
                                    S4.remove(56)
                                    S4.remove(57)
                                    S4.remove(58)
                                for ss3 in range(len(Z3)):
                                    if (Z3[ss3][0] != 0):
                                        node3.append([Z3[ss3][0], Z3[ss3][1], 0])
                                Node_3.append(
                                    [Model_3.copy(), node3.copy(), S4.copy(), BT3, MT3, ST3, SQ3, PA3, numNode_1, numNode_2,
                                     numNode_3,
                                     -1, -1, -1, -1,search2, x2, y2])
                                numNode_3 += 1
            ##第四层
            for node in Node_3:
                Model_3 = node[0]
                node3 = node[1]
                S4 = node[2]
                BT3 = node[3]
                MT3 = node[4]
                ST3 = node[5]
                SQ3 = node[6]
                PA3 = node[7]
                numNode_1 = node[8]
                numNode_2 = node[9]
                numNode_3 = node[10]
                for sn3 in range(len(node3)):
                    if (node3[sn3][2] == 0):
                        x3 = node3[sn3][0]
                        y3 = node3[sn3][1]
                        node3[sn3][2] = 1
                    for search3 in S4:
                        Model_4, Z4 = run_model(Model_3.copy(), search3, x3, y3)
                        node4 = []
                        if (Z4[0][0] != -1):
                            dell = (search3 - search3 % 10)
                            if (dell == 0 or dell == 10):
                                BT4 = BT3 - 1
                                MT4 = MT3
                                ST4 = ST3
                                SQ4 = SQ3
                                PA4 = PA3
                                S5 = S4.copy()
                                if (BT4 == 0):
                                    S5.remove(1)
                                    S5.remove(2)
                                    S5.remove(3)
                                    S5.remove(4)
                                    S5.remove(5)
                                    S5.remove(6)
                                    S5.remove(7)
                                    S5.remove(8)
                                    S5.remove(9)
                                    S5.remove(10)
                                    S5.remove(11)
                                    S5.remove(12)
                            elif (dell == 20):
                                BT4 = BT3
                                MT4 = MT3 - 1
                                ST4 = ST3
                                SQ4 = SQ3
                                PA4 = PA3
                                S5 = S4.copy()
                                S5.remove(21)
                                S5.remove(22)
                                S5.remove(23)
                                S5.remove(24)
                                S5.remove(25)
                                S5.remove(26)
                                S5.remove(27)
                                S5.remove(28)
                            elif (dell == 30):
                                BT4 = BT3
                                MT4 = MT3
                                ST4 = ST3 - 1
                                SQ4 = SQ3
                                PA4 = PA3
                                S5 = S4.copy()
                                if (ST4 == 0):
                                    S5.remove(31)
                                    S5.remove(32)
                                    S5.remove(33)
                                    S5.remove(34)
                            elif (dell == 40):
                                BT4 = BT3
                                MT4 = MT3
                                ST4 = ST3
                                SQ4 = SQ3 - 1
                                PA4 = PA3
                                S5 = S4.copy()
                                S5.remove(41)
                            elif (dell == 50):
                                BT4 = BT3
                                MT4 = MT3
                                ST4 = ST3
                                SQ4 = SQ3
                                PA4 = PA3 - 1
                                S5 = S4.copy()
                                S5.remove(51)
                                S5.remove(52)
                                S5.remove(53)
                                S5.remove(54)
                                S5.remove(55)
                                S5.remove(56)
                                S5.remove(57)
                                S5.remove(58)

                            for ss4 in range(len(Z4)):
                                if (Z4[ss4][0] != 0):
                                    node4.append([Z4[ss4][0], Z4[ss4][1], 0])
                            Node_4.append(
                                [Model_4.copy(), node4.copy(), S5.copy(), BT4, MT4, ST4, SQ4, PA4, numNode_1, numNode_2,
                                 numNode_3,
                                 numNode_4 , -1, -1, -1, search3, x3, y3])
                            numNode_4 += 1
            ##第五层
            for node in Node_4:
                Model_4 = node[0]
                node4 = node[1]
                S5 = node[2]
                BT4 = node[3]
                MT4 = node[4]
                ST4 = node[5]
                SQ4 = node[6]
                PA4 = node[7]
                numNode_1 = node[8]
                numNode_2 = node[9]
                numNode_3 = node[10]
                numNode_4 = node[11]
                for sn4 in range(len(node4)):
                    if (node4[sn4][2] == 0):
                        x4 = node4[sn4][0]
                        y4 = node4[sn4][1]
                        node4[sn4][2] = 1
                    for search4 in S5:
                        Model_5, Z5 = run_model(Model_4.copy(), search4, x4, y4)
                        node5 = []
                        if (Z5[0][0] != -1):
                            dell = (search4 - search4 % 10)
                            if (dell == 0 or dell == 10):
                                BT5 = BT4 - 1
                                MT5 = MT4
                                ST5 = ST4
                                SQ5 = SQ4
                                PA5 = PA4
                                S6 = S5.copy()
                                if (BT5 == 0):
                                    S6.remove(1)
                                    S6.remove(2)
                                    S6.remove(3)
                                    S6.remove(4)
                                    S6.remove(5)
                                    S6.remove(6)
                                    S6.remove(7)
                                    S6.remove(8)
                                    S6.remove(9)
                                    S6.remove(10)
                                    S6.remove(11)
                                    S6.remove(12)
                            elif (dell == 20):
                                BT5 = BT4
                                MT5 = MT4 - 1
                                ST5 = ST4
                                SQ5 = SQ4
                                PA5 = PA4
                                S6 = S5.copy()
                                S6.remove(21)
                                S6.remove(22)
                                S6.remove(23)
                                S6.remove(24)
                                S6.remove(25)
                                S6.remove(26)
                                S6.remove(27)
                                S6.remove(28)
                            elif (dell == 30):
                                BT5 = BT4
                                MT5 = MT4
                                ST5 = ST4 - 1
                                SQ5 = SQ4
                                PA5 = PA4
                                S6 = S5.copy()
                                if (ST5 == 0):
                                    S6.remove(31)
                                    S6.remove(32)
                                    S6.remove(33)
                                    S6.remove(34)
                            elif (dell == 40):
                                BT5 = BT4
                                MT5 = MT4
                                ST5 = ST4
                                SQ5 = SQ4 - 1
                                PA5 = PA4
                                S6 = S5.copy()
                                S6.remove(41)
                            elif (dell == 50):
                                BT5 = BT4
                                MT5 = MT4
                                ST5 = ST4
                                SQ5 = SQ4
                                PA5 = PA4 - 1
                                S6 = S5.copy()
                                S6.remove(51)
                                S6.remove(52)
                                S6.remove(53)
                                S6.remove(54)
                                S6.remove(55)
                                S6.remove(56)
                                S6.remove(57)
                                S6.remove(58)

                            for ss5 in range(len(Z5)):
                                if (Z5[ss5][0] != 0):
                                    node5.append([Z5[ss5][0], Z5[ss5][1], 0])
                            Node_5.append(
                                [Model_5.copy(), node5.copy(), S6.copy(), BT5, MT5, ST5, SQ5, PA5, numNode_1, numNode_2,
                                 numNode_3,
                                 numNode_4, numNode_5 , -1, -1, search4, x4, y4])
                            numNode_5 += 1
            ###第六层
            for node in Node_5:
                Model_5 = node[0]
                node5 = node[1]
                S6 = node[2]
                BT5 = node[3]
                MT5 = node[4]
                ST5 = node[5]
                SQ5 = node[6]
                PA5 = node[7]
                numNode_1 = node[8]
                numNode_2 = node[9]
                numNode_3 = node[10]
                numNode_4 = node[11]
                numNode_5 = node[12]
                for sn5 in range(len(node5)):
                    if (node5[sn5][2] == 0):
                        x5 = node5[sn5][0]
                        y5 = node5[sn5][1]
                        node5[sn5][2] = 1
                    for search5 in S6:
                        # print(S6, x5, y5)
                        ####################第六层
                        Model_6, Z6 = run_model(Model_5.copy(), search5, x5,
                                                y5)
                        node6 = []
                        if (Z6[0][0] != -1):
                            dell = (search5 - search5 % 10)
                            if (dell == 0 or dell == 10):
                                BT6 = BT5 - 1
                                MT6 = MT5
                                ST6 = ST5
                                SQ6 = SQ5
                                PA6 = PA5
                                S7 = S6.copy()
                                if (BT6 == 0):
                                    S7.remove(1)
                                    S7.remove(2)
                                    S7.remove(3)
                                    S7.remove(4)
                                    S7.remove(5)
                                    S7.remove(6)
                                    S7.remove(7)
                                    S7.remove(8)
                                    S7.remove(9)
                                    S7.remove(10)
                                    S7.remove(11)
                                    S7.remove(12)
                            elif (dell == 20):
                                BT6 = BT5
                                MT6 = MT5 - 1
                                ST6 = ST5
                                SQ6 = SQ5
                                PA6 = PA5
                                S7 = S6.copy()
                                S7.remove(21)
                                S7.remove(22)
                                S7.remove(23)
                                S7.remove(24)
                                S7.remove(25)
                                S7.remove(26)
                                S7.remove(27)
                                S7.remove(28)
                            elif (dell == 30):
                                BT6 = BT5
                                MT6 = MT5
                                ST6 = ST5 - 1
                                SQ6 = SQ5
                                PA6 = PA5
                                S7 = S6.copy()
                                if (ST6 == 0):
                                    S7.remove(31)
                                    S7.remove(32)
                                    S7.remove(33)
                                    S7.remove(34)
                            elif (dell == 40):
                                BT6 = BT5
                                MT6 = MT5
                                ST6 = ST5
                                SQ6 = SQ5 - 1
                                PA6 = PA5
                                S7 = S6.copy()
                                S7.remove(41)
                            elif (dell == 50):
                                BT6 = BT5
                                MT6 = MT5
                                ST6 = ST5
                                SQ6 = SQ5
                                PA6 = PA5 - 1
                                S7 = S6.copy()
                                S7.remove(51)
                                S7.remove(52)
                                S7.remove(53)
                                S7.remove(54)
                                S7.remove(55)
                                S7.remove(56)
                                S7.remove(57)
                                S7.remove(58)
                            List.append(
                                [search, search1, search2, search3,
                                 search4, search5, 0, x5, y5, 0])
                            for ss6 in range(len(Z6)):
                                if (Z6[ss6][0] != 0):
                                    node6.append(
                                        [Z6[ss6][0], Z6[ss6][1], 0])
                            Node_6.append(
                                [Model_6.copy(), node6.copy(), S7.copy(), BT6, MT6, ST6, SQ6, PA6,numNode_1, numNode_2,
                                 numNode_3,numNode_4, numNode_5 , numNode_6 , -1, search5, x5,y5])
                            numNode_6 += 1
            ###第七层
            for node in Node_6:
                Model_6 = node[0]
                node6 = node[1]
                S7 = node[2]
                BT6 = node[3]
                MT6 = node[4]
                ST6 = node[5]
                SQ6 = node[6]
                PA6 = node[7]
                numNode_1 = node[8]
                numNode_2 = node[9]
                numNode_3 = node[10]
                numNode_4 = node[11]
                numNode_5 = node[12]
                numNode_6 = node[13]
                for sn6 in range(len(node6)):
                    if (node6[sn6][2] == 0):
                        x6 = node6[sn6][0]
                        y6 = node6[sn6][1]
                        node6[sn6][2] = 1
                    for search6 in S7:
                        ####################第七层
                        Model_7, Z7 = run_model(
                            Model_6.copy(), search6, x6,
                            y6)
                        if (Z7[0][0] != -1):
                            if(numNode_7 == 0):
                                print("1:", Node_1[numNode_1][15:18], "2:", Node_2[numNode_2][15:18], "3:",
                                      Node_3[numNode_3][15:18], "4:", Node_4[numNode_4][15:18], "5:",
                                      Node_5[numNode_5][15:18], "6:", Node_6[numNode_6][15:18], "7:", search6, x6, y6)
                                Node_7.append(
                                    [Model_7.copy(), numNode_1, numNode_2,
                                     numNode_3,
                                     numNode_4, numNode_5 , numNode_6 , numNode_7,search6, x6,y6])
                                numNode_7 += 1
                                if (numNode_7 < 10):
                                    w = Canvas(
                                        f1,
                                        width=160,
                                        height=160,
                                        background="white"
                                    )
                                elif (numNode_7 < 19):
                                    w = Canvas(
                                        f2,
                                        width=160,
                                        height=160,
                                        background="white"
                                    )
                                elif (numNode_7 < 28):
                                    w = Canvas(
                                        f3,
                                        width=160,
                                        height=160,
                                        background="white"
                                    )
                                elif (numNode_7 < 37):
                                    w = Canvas(
                                        f4,
                                        width=160,
                                        height=160,
                                        background="white"
                                    )
                                else:
                                    w = Canvas(
                                        f5,
                                        width=160,
                                        height=160,
                                        background="white"
                                    )
                                w.pack(side=LEFT, expand=YES)
                                draw(Model_7, root, w)
                            else:
                                pnodeInt =0
                                for pnode in Node_7:
                                    if ((search6 == pnode[8] and x6 == pnode[9] and y6 == pnode[10]) or (
                                            search6 == Node_1[pnode[1]][15] and x6 == Node_1[pnode[1]][16] and y6 ==
                                            Node_1[pnode[1]][17]) or (
                                            search6 == Node_2[pnode[2]][15] and x6 == Node_2[pnode[2]][16] and y6 ==
                                            Node_2[pnode[2]][17]) or (
                                            search6 == Node_3[pnode[3]][15] and x6 == Node_3[pnode[3]][16] and y6 ==
                                            Node_3[pnode[3]][17]) or (
                                            search6 == Node_4[pnode[4]][15] and x6 == Node_4[pnode[4]][16] and y6 ==
                                            Node_4[pnode[4]][17]) or (
                                            search6 == Node_5[pnode[5]][15] and x6 == Node_5[pnode[5]][16] and y6 ==
                                            Node_5[pnode[5]][17]) or (
                                            search6 == Node_6[pnode[6]][15] and x6 == Node_6[pnode[6]][16] and y6 ==
                                            Node_6[pnode[6]][17])or (
                                            search6 == 1 and pnode[8] == 2 and x6 == pnode[9]-1 and y6 ==
                                            pnode[10])or (
                                            search6 == 1 and pnode[8] == 3 and x6 == pnode[9] and y6 ==
                                            pnode[10]-1)or (
                                            search6 == 2 and pnode[8] == 1 and x6 == pnode[9]+1 and y6 ==
                                            pnode[10])or (
                                            search6 == 2 and pnode[8] == 3 and x6 == pnode[9]+1 and y6 ==
                                            pnode[10]-1)or (
                                            search6 == 3 and pnode[8] == 2 and x6 == pnode[9]-1 and y6 ==
                                            pnode[10]+1)or (
                                            search6 == 3 and pnode[8] == 1 and x6 == pnode[9] and y6 ==
                                            pnode[10]+1)or (
                                            search6 == 4 and pnode[8] == 6 and x6 == pnode[9]-1 and y6 ==
                                            pnode[10]-1)or (
                                            search6 == 4 and pnode[8] == 5 and x6 == pnode[9]-1 and y6 ==
                                            pnode[10])or (
                                            search6 == 5 and pnode[8] == 4 and x6 == pnode[9]+1 and y6 ==
                                            pnode[10])or (
                                            search6 == 5 and pnode[8] == 6 and x6 == pnode[9] and y6 ==
                                            pnode[10]-1)or (
                                            search6 == 6 and pnode[8] == 4 and x6 == pnode[9]+1 and y6 ==
                                            pnode[10]+1) or (
                                            search6 == 6 and pnode[8] == 5 and x6 == pnode[9] and y6 ==
                                            pnode[10]+1)or (
                                            search6 == 7 and pnode[8] == 9 and x6 == pnode[9]-1 and y6 ==
                                            pnode[10]+1)or (
                                            search6 == 7 and pnode[8] == 8 and x6 == pnode[9]-1 and y6 ==
                                            pnode[10])or (
                                            search6 == 8 and pnode[8] == 7 and x6 == pnode[9]+1 and y6 ==
                                            pnode[10])or (
                                            search6 == 8 and pnode[8] == 9 and x6 == pnode[9] and y6 ==
                                            pnode[10]+1)or (
                                            search6 == 9 and pnode[8] == 8 and x6 == pnode[9] and y6 ==
                                            pnode[10]-1)or (
                                            search6 == 9 and pnode[8] == 7 and x6 == pnode[9]+1 and y6 ==
                                            pnode[10]-1)or (
                                            search6 == 10 and pnode[8] == 11 and x6 == pnode[9]-1 and y6 ==
                                            pnode[10])or (
                                            search6 == 10 and pnode[8] == 12 and x6 == pnode[9] and y6 ==
                                            pnode[10]+1)or (
                                            search6 == 11 and pnode[8] == 12 and x6 == pnode[9]+1 and y6 ==
                                            pnode[10]+1)or (
                                            search6 == 11 and pnode[8] == 10 and x6 == pnode[9]+1 and y6 ==
                                            pnode[10])or (
                                            search6 == 12 and pnode[8] == 11 and x6 == pnode[9]-1 and y6 ==
                                            pnode[10]+1)or (
                                            search6 == 21 and pnode[8] == 22 and x6 == pnode[9]-1 and y6 ==
                                            pnode[10])or (
                                            search6 == 12 and pnode[8] == 10 and x6 == pnode[9] and y6 ==
                                            pnode[10]-1)or (
                                            search6 == 22 and pnode[8] == 21 and x6 == pnode[9]+1 and y6 ==
                                            pnode[10])or (
                                            search6 == 23 and pnode[8] == 24 and x6 == pnode[9] and y6 ==
                                            pnode[10]-1)or (
                                            search6 == 24 and pnode[8] == 23 and x6 == pnode[9] and y6 ==
                                            pnode[10]+1)or (
                                            search6 == 25 and pnode[8] == 26 and x6 == pnode[9] - 1 and y6 ==
                                            pnode[10]) or (
                                            search6 == 26 and pnode[8] == 25 and x6 == pnode[9] + 1 and y6 ==
                                            pnode[10])or (
                                            search6 == 27 and pnode[8] == 28 and x6 == pnode[9] and y6 ==
                                            pnode[10]-1) or (
                                            search6 == 28 and pnode[8] == 27 and x6 == pnode[9] and y6 ==
                                            pnode[10]+1)or (
                                            search6 == 51 and pnode[8] == 52 and x6 == pnode[9]-1 and y6 ==
                                            pnode[10])or (
                                            search6 == 52 and pnode[8] == 51 and x6 == pnode[9]+1 and y6 ==
                                            pnode[10])or (
                                            search6 == 53 and pnode[8] == 54 and x6 == pnode[9] - 1 and y6 ==
                                            pnode[10]) or (
                                            search6 == 54 and pnode[8] == 53 and x6 == pnode[9] + 1 and y6 ==
                                            pnode[10])or (
                                            search6 == 55 and pnode[8] == 56 and x6 == pnode[9] and y6 ==
                                            pnode[10]-1)or (
                                            search6 == 56 and pnode[8] == 55 and x6 == pnode[9] and y6 ==
                                            pnode[10]+1)or (
                                            search6 == 57 and pnode[8] == 58 and x6 == pnode[9] and y6 ==
                                            pnode[10]-1) or (
                                            search6 == 58 and pnode[8] == 57 and x6 == pnode[9] and y6 ==
                                            pnode[10]+1)or (
                                            search6 == 1 and Node_1[pnode[1]][15] == 2 and x6 == Node_1[pnode[1]][16]-1 and y6 ==
                                            Node_1[pnode[1]][17])or (
                                            search6 == 1 and Node_1[pnode[1]][15] == 3 and x6 == Node_1[pnode[1]][16] and y6 ==
                                            Node_1[pnode[1]][17])or (
                                            search6 == 2 and Node_1[pnode[1]][15] == 1 and x6 == Node_1[pnode[1]][16]+1 and y6 ==
                                            Node_1[pnode[1]][17])or (
                                            search6 == 2 and Node_1[pnode[1]][15] == 3 and x6 == Node_1[pnode[1]][16]+1 and y6 ==
                                            Node_1[pnode[1]][17]-1)or (
                                            search6 == 3 and Node_1[pnode[1]][15] == 2 and x6 == Node_1[pnode[1]][16]-1 and y6 ==
                                            Node_1[pnode[1]][17]+1)or (
                                            search6 == 3 and Node_1[pnode[1]][15] == 1 and x6 == Node_1[pnode[1]][16] and y6 ==
                                            Node_1[pnode[1]][17]+1)or (
                                            search6 == 4 and Node_1[pnode[1]][15] == 6 and x6 == Node_1[pnode[1]][16]-1 and y6 ==
                                            Node_1[pnode[1]][17]-1)or (
                                            search6 == 4 and Node_1[pnode[1]][15] == 5 and x6 == Node_1[pnode[1]][16]-1 and y6 ==
                                            Node_1[pnode[1]][17])or (
                                            search6 == 5 and Node_1[pnode[1]][15] == 4 and x6 == Node_1[pnode[1]][16]+1 and y6 ==
                                            Node_1[pnode[1]][17])or (
                                            search6 == 5 and Node_1[pnode[1]][15] == 6 and x6 == Node_1[pnode[1]][16] and y6 ==
                                            Node_1[pnode[1]][17]-1)or (
                                            search6 == 6 and Node_1[pnode[1]][15] == 4 and x6 == Node_1[pnode[1]][16]+1 and y6 ==
                                            Node_1[pnode[1]][17]+1) or (
                                            search6 == 6 and Node_1[pnode[1]][15] == 5 and x6 == Node_1[pnode[1]][16] and y6 ==
                                            Node_1[pnode[1]][17]+1)or (
                                            search6 == 7 and Node_1[pnode[1]][15] == 9 and x6 == Node_1[pnode[1]][16]-1 and y6 ==
                                            Node_1[pnode[1]][17]+1)or (
                                            search6 == 7 and Node_1[pnode[1]][15] == 8 and x6 == Node_1[pnode[1]][16]-1 and y6 ==
                                            Node_1[pnode[1]][17])or (
                                            search6 == 8 and Node_1[pnode[1]][15] == 7 and x6 == Node_1[pnode[1]][16]+1 and y6 ==
                                            Node_1[pnode[1]][17])or (
                                            search6 == 8 and Node_1[pnode[1]][15] == 9 and x6 == Node_1[pnode[1]][16] and y6 ==
                                            Node_1[pnode[1]][17]+1)or (
                                            search6 == 9 and Node_1[pnode[1]][15] == 8 and x6 == Node_1[pnode[1]][16] and y6 ==
                                            Node_1[pnode[1]][17]-1)or (
                                            search6 == 9 and Node_1[pnode[1]][15] == 7 and x6 == Node_1[pnode[1]][16]+1 and y6 ==
                                            Node_1[pnode[1]][17]-1)or (
                                            search6 == 10 and Node_1[pnode[1]][15] == 11 and x6 == Node_1[pnode[1]][16]-1 and y6 ==
                                            Node_1[pnode[1]][17])or (
                                            search6 == 10 and Node_1[pnode[1]][15] == 12 and x6 == Node_1[pnode[1]][16] and y6 ==
                                            Node_1[pnode[1]][17]+1)or (
                                            search6 == 11 and Node_1[pnode[1]][15] == 12 and x6 == Node_1[pnode[1]][16]+1 and y6 ==
                                            Node_1[pnode[1]][17]+1)or (
                                            search6 == 11 and Node_1[pnode[1]][15] == 10 and x6 == Node_1[pnode[1]][16]+1 and y6 ==
                                            Node_1[pnode[1]][17])or (
                                            search6 == 12 and Node_1[pnode[1]][15] == 11 and x6 == Node_1[pnode[1]][16]-1 and y6 ==
                                            Node_1[pnode[1]][17]+1)or (
                                            search6 == 21 and Node_1[pnode[1]][15] == 22 and x6 == Node_1[pnode[1]][16]-1 and y6 ==
                                            Node_1[pnode[1]][17])or (
                                            search6 == 12 and Node_1[pnode[1]][15] == 10 and x6 == Node_1[pnode[1]][16] and y6 ==
                                            Node_1[pnode[1]][17]-1)or (
                                            search6 == 22 and Node_1[pnode[1]][15] == 21 and x6 == Node_1[pnode[1]][16]+1 and y6 ==
                                            Node_1[pnode[1]][17])or (
                                            search6 == 23 and Node_1[pnode[1]][15] == 24 and x6 == Node_1[pnode[1]][16] and y6 ==
                                            Node_1[pnode[1]][17]-1)or (
                                            search6 == 24 and Node_1[pnode[1]][15] == 23 and x6 == Node_1[pnode[1]][16] and y6 ==
                                            Node_1[pnode[1]][17]+1)or (
                                            search6 == 25 and Node_1[pnode[1]][15] == 26 and x6 == Node_1[pnode[1]][16] - 1 and y6 ==
                                            Node_1[pnode[1]][17]) or (
                                            search6 == 26 and Node_1[pnode[1]][15] == 25 and x6 == Node_1[pnode[1]][16] + 1 and y6 ==
                                            Node_1[pnode[1]][17])or (
                                            search6 == 27 and Node_1[pnode[1]][15] == 28 and x6 == Node_1[pnode[1]][16] and y6 ==
                                            Node_1[pnode[1]][17]-1) or (
                                            search6 == 28 and Node_1[pnode[1]][15] == 27 and x6 == Node_1[pnode[1]][16] and y6 ==
                                            Node_1[pnode[1]][17]+1)or (
                                            search6 == 51 and Node_1[pnode[1]][15] == 52 and x6 == Node_1[pnode[1]][16]-1 and y6 ==
                                            Node_1[pnode[1]][17])or (
                                            search6 == 52 and Node_1[pnode[1]][15] == 51 and x6 == Node_1[pnode[1]][16]+1 and y6 ==
                                            Node_1[pnode[1]][17])or (
                                            search6 == 53 and Node_1[pnode[1]][15] == 54 and x6 == Node_1[pnode[1]][16] - 1 and y6 ==
                                            Node_1[pnode[1]][17]) or (
                                            search6 == 54 and Node_1[pnode[1]][15] == 53 and x6 == Node_1[pnode[1]][16] + 1 and y6 ==
                                            Node_1[pnode[1]][17])or (
                                            search6 == 55 and Node_1[pnode[1]][15] == 56 and x6 == Node_1[pnode[1]][16] and y6 ==
                                            Node_1[pnode[1]][17]-1)or (
                                            search6 == 56 and Node_1[pnode[1]][15] == 55 and x6 == Node_1[pnode[1]][16] and y6 ==
                                            Node_1[pnode[1]][17]+1)or (
                                            search6 == 57 and Node_1[pnode[1]][15] == 58 and x6 == Node_1[pnode[1]][16] and y6 ==
                                            Node_1[pnode[1]][17]-1) or (
                                            search6 == 58 and Node_1[pnode[1]][15] == 57 and x6 == Node_1[pnode[1]][16] and y6 ==
                                            Node_1[pnode[1]][17]+1)or (
                                            search6 == 1 and Node_2[pnode[2]][15] == 2 and x6 == Node_2[pnode[2]][16]-1 and y6 ==
                                            Node_2[pnode[2]][17])or (
                                            search6 == 1 and Node_2[pnode[2]][15] == 3 and x6 == Node_2[pnode[2]][16] and y6 ==
                                            Node_2[pnode[2]][17])or (
                                            search6 == 2 and Node_2[pnode[2]][15] == 1 and x6 == Node_2[pnode[2]][16]+1 and y6 ==
                                            Node_2[pnode[2]][17])or (
                                            search6 == 2 and Node_2[pnode[2]][15] == 3 and x6 == Node_2[pnode[2]][16]+1 and y6 ==
                                            Node_2[pnode[2]][17]-1)or (
                                            search6 == 3 and Node_2[pnode[2]][15] == 2 and x6 == Node_2[pnode[2]][16]-1 and y6 ==
                                            Node_2[pnode[2]][17]+1)or (
                                            search6 == 3 and Node_2[pnode[2]][15] == 1 and x6 == Node_2[pnode[2]][16] and y6 ==
                                            Node_2[pnode[2]][17]+1)or (
                                            search6 == 4 and Node_2[pnode[2]][15] == 6 and x6 == Node_2[pnode[2]][16]-1 and y6 ==
                                            Node_2[pnode[2]][17]-1)or (
                                            search6 == 4 and Node_2[pnode[2]][15] == 5 and x6 == Node_2[pnode[2]][16]-1 and y6 ==
                                            Node_2[pnode[2]][17])or (
                                            search6 == 5 and Node_2[pnode[2]][15] == 4 and x6 == Node_2[pnode[2]][16]+1 and y6 ==
                                            Node_2[pnode[2]][17])or (
                                            search6 == 5 and Node_2[pnode[2]][15] == 6 and x6 == Node_2[pnode[2]][16] and y6 ==
                                            Node_2[pnode[2]][17]-1)or (
                                            search6 == 6 and Node_2[pnode[2]][15] == 4 and x6 == Node_2[pnode[2]][16]+1 and y6 ==
                                            Node_2[pnode[2]][17]+1) or (
                                            search6 == 6 and Node_2[pnode[2]][15] == 5 and x6 == Node_2[pnode[2]][16] and y6 ==
                                            Node_2[pnode[2]][17]+1)or (
                                            search6 == 7 and Node_2[pnode[2]][15] == 9 and x6 == Node_2[pnode[2]][16]-1 and y6 ==
                                            Node_2[pnode[2]][17]+1)or (
                                            search6 == 7 and Node_2[pnode[2]][15] == 8 and x6 == Node_2[pnode[2]][16]-1 and y6 ==
                                            Node_2[pnode[2]][17])or (
                                            search6 == 8 and Node_2[pnode[2]][15] == 7 and x6 == Node_2[pnode[2]][16]+1 and y6 ==
                                            Node_2[pnode[2]][17])or (
                                            search6 == 8 and Node_2[pnode[2]][15] == 9 and x6 == Node_2[pnode[2]][16] and y6 ==
                                            Node_2[pnode[2]][17]+1)or (
                                            search6 == 9 and Node_2[pnode[2]][15] == 8 and x6 == Node_2[pnode[2]][16] and y6 ==
                                            Node_2[pnode[2]][17]-1)or (
                                            search6 == 9 and Node_2[pnode[2]][15] == 7 and x6 == Node_2[pnode[2]][16]+1 and y6 ==
                                            Node_2[pnode[2]][17]-1)or (
                                            search6 == 10 and Node_2[pnode[2]][15] == 11 and x6 == Node_2[pnode[2]][16]-1 and y6 ==
                                            Node_2[pnode[2]][17])or (
                                            search6 == 10 and Node_2[pnode[2]][15] == 12 and x6 == Node_2[pnode[2]][16] and y6 ==
                                            Node_2[pnode[2]][17]+1)or (
                                            search6 == 11 and Node_2[pnode[2]][15] == 12 and x6 == Node_2[pnode[2]][16]+1 and y6 ==
                                            Node_2[pnode[2]][17]+1)or (
                                            search6 == 11 and Node_2[pnode[2]][15] == 10 and x6 == Node_2[pnode[2]][16]+1 and y6 ==
                                            Node_2[pnode[2]][17])or (
                                            search6 == 12 and Node_2[pnode[2]][15] == 11 and x6 == Node_2[pnode[2]][16]-1 and y6 ==
                                            Node_2[pnode[2]][17]+1)or (
                                            search6 == 21 and Node_2[pnode[2]][15] == 22 and x6 == Node_2[pnode[2]][16]-1 and y6 ==
                                            Node_2[pnode[2]][17])or (
                                            search6 == 12 and Node_2[pnode[2]][15] == 10 and x6 == Node_2[pnode[2]][16] and y6 ==
                                            Node_2[pnode[2]][17]-1)or (
                                            search6 == 22 and Node_2[pnode[2]][15] == 21 and x6 == Node_2[pnode[2]][16]+1 and y6 ==
                                            Node_2[pnode[2]][17])or (
                                            search6 == 23 and Node_2[pnode[2]][15] == 24 and x6 == Node_2[pnode[2]][16] and y6 ==
                                            Node_2[pnode[2]][17]-1)or (
                                            search6 == 24 and Node_2[pnode[2]][15] == 23 and x6 == Node_2[pnode[2]][16] and y6 ==
                                            Node_2[pnode[2]][17]+1)or (
                                            search6 == 25 and Node_2[pnode[2]][15] == 26 and x6 == Node_2[pnode[2]][16] - 1 and y6 ==
                                            Node_2[pnode[2]][17]) or (
                                            search6 == 26 and Node_2[pnode[2]][15] == 25 and x6 == Node_2[pnode[2]][16] + 1 and y6 ==
                                            Node_2[pnode[2]][17])or (
                                            search6 == 27 and Node_2[pnode[2]][15] == 28 and x6 == Node_2[pnode[2]][16] and y6 ==
                                            Node_2[pnode[2]][17]-1) or (
                                            search6 == 28 and Node_2[pnode[2]][15] == 27 and x6 == Node_2[pnode[2]][16] and y6 ==
                                            Node_2[pnode[2]][17]+1)or (
                                            search6 == 51 and Node_2[pnode[2]][15] == 52 and x6 == Node_2[pnode[2]][16]-1 and y6 ==
                                            Node_2[pnode[2]][17])or (
                                            search6 == 52 and Node_2[pnode[2]][15] == 51 and x6 == Node_2[pnode[2]][16]+1 and y6 ==
                                            Node_2[pnode[2]][17])or (
                                            search6 == 53 and Node_2[pnode[2]][15] == 54 and x6 == Node_2[pnode[2]][16] - 1 and y6 ==
                                            Node_2[pnode[2]][17]) or (
                                            search6 == 54 and Node_2[pnode[2]][15] == 53 and x6 == Node_2[pnode[2]][16] + 1 and y6 ==
                                            Node_2[pnode[2]][17])or (
                                            search6 == 55 and Node_2[pnode[2]][15] == 56 and x6 == Node_2[pnode[2]][16] and y6 ==
                                            Node_2[pnode[2]][17]-1)or (
                                            search6 == 56 and Node_2[pnode[2]][15] == 55 and x6 == Node_2[pnode[2]][16] and y6 ==
                                            Node_2[pnode[2]][17]+1)or (
                                            search6 == 57 and Node_2[pnode[2]][15] == 58 and x6 == Node_2[pnode[2]][16] and y6 ==
                                            Node_2[pnode[2]][17]-1) or (
                                            search6 == 58 and Node_2[pnode[2]][15] == 57 and x6 == Node_2[pnode[2]][16] and y6 ==
                                            Node_2[pnode[2]][17]+1)or (
                                            search6 == 1 and Node_3[pnode[3]][15] == 2 and x6 == Node_3[pnode[3]][16]-1 and y6 ==
                                            Node_3[pnode[3]][17])or (
                                            search6 == 1 and Node_3[pnode[3]][15] == 3 and x6 == Node_3[pnode[3]][16] and y6 ==
                                            Node_3[pnode[3]][17])or (
                                            search6 == 2 and Node_3[pnode[3]][15] == 1 and x6 == Node_3[pnode[3]][16]+1 and y6 ==
                                            Node_3[pnode[3]][17])or (
                                            search6 == 2 and Node_3[pnode[3]][15] == 3 and x6 == Node_3[pnode[3]][16]+1 and y6 ==
                                            Node_3[pnode[3]][17]-1)or (
                                            search6 == 3 and Node_3[pnode[3]][15] == 2 and x6 == Node_3[pnode[3]][16]-1 and y6 ==
                                            Node_3[pnode[3]][17]+1)or (
                                            search6 == 3 and Node_3[pnode[3]][15] == 1 and x6 == Node_3[pnode[3]][16] and y6 ==
                                            Node_3[pnode[3]][17]+1)or (
                                            search6 == 4 and Node_3[pnode[3]][15] == 6 and x6 == Node_3[pnode[3]][16]-1 and y6 ==
                                            Node_3[pnode[3]][17]-1)or (
                                            search6 == 4 and Node_3[pnode[3]][15] == 5 and x6 == Node_3[pnode[3]][16]-1 and y6 ==
                                            Node_3[pnode[3]][17])or (
                                            search6 == 5 and Node_3[pnode[3]][15] == 4 and x6 == Node_3[pnode[3]][16]+1 and y6 ==
                                            Node_3[pnode[3]][17])or (
                                            search6 == 5 and Node_3[pnode[3]][15] == 6 and x6 == Node_3[pnode[3]][16] and y6 ==
                                            Node_3[pnode[3]][17]-1)or (
                                            search6 == 6 and Node_3[pnode[3]][15] == 4 and x6 == Node_3[pnode[3]][16]+1 and y6 ==
                                            Node_3[pnode[3]][17]+1) or (
                                            search6 == 6 and Node_3[pnode[3]][15] == 5 and x6 == Node_3[pnode[3]][16] and y6 ==
                                            Node_3[pnode[3]][17]+1)or (
                                            search6 == 7 and Node_3[pnode[3]][15] == 9 and x6 == Node_3[pnode[3]][16]-1 and y6 ==
                                            Node_3[pnode[3]][17]+1)or (
                                            search6 == 7 and Node_3[pnode[3]][15] == 8 and x6 == Node_3[pnode[3]][16]-1 and y6 ==
                                            Node_3[pnode[3]][17])or (
                                            search6 == 8 and Node_3[pnode[3]][15] == 7 and x6 == Node_3[pnode[3]][16]+1 and y6 ==
                                            Node_3[pnode[3]][17])or (
                                            search6 == 8 and Node_3[pnode[3]][15] == 9 and x6 == Node_3[pnode[3]][16] and y6 ==
                                            Node_3[pnode[3]][17]+1)or (
                                            search6 == 9 and Node_3[pnode[3]][15] == 8 and x6 == Node_3[pnode[3]][16] and y6 ==
                                            Node_3[pnode[3]][17]-1)or (
                                            search6 == 9 and Node_3[pnode[3]][15] == 7 and x6 == Node_3[pnode[3]][16]+1 and y6 ==
                                            Node_3[pnode[3]][17]-1)or (
                                            search6 == 10 and Node_3[pnode[3]][15] == 11 and x6 == Node_3[pnode[3]][16]-1 and y6 ==
                                            Node_3[pnode[3]][17])or (
                                            search6 == 10 and Node_3[pnode[3]][15] == 12 and x6 == Node_3[pnode[3]][16] and y6 ==
                                            Node_3[pnode[3]][17]+1)or (
                                            search6 == 11 and Node_3[pnode[3]][15] == 12 and x6 == Node_3[pnode[3]][16]+1 and y6 ==
                                            Node_3[pnode[3]][17]+1)or (
                                            search6 == 11 and Node_3[pnode[3]][15] == 10 and x6 == Node_3[pnode[3]][16]+1 and y6 ==
                                            Node_3[pnode[3]][17])or (
                                            search6 == 12 and Node_3[pnode[3]][15] == 11 and x6 == Node_3[pnode[3]][16]-1 and y6 ==
                                            Node_3[pnode[3]][17]+1)or (
                                            search6 == 21 and Node_3[pnode[3]][15] == 22 and x6 == Node_3[pnode[3]][16]-1 and y6 ==
                                            Node_3[pnode[3]][17])or (
                                            search6 == 12 and Node_3[pnode[3]][15] == 10 and x6 == Node_3[pnode[3]][16] and y6 ==
                                            Node_3[pnode[3]][17]-1)or (
                                            search6 == 22 and Node_3[pnode[3]][15] == 21 and x6 == Node_3[pnode[3]][16]+1 and y6 ==
                                            Node_3[pnode[3]][17])or (
                                            search6 == 23 and Node_3[pnode[3]][15] == 24 and x6 == Node_3[pnode[3]][16] and y6 ==
                                            Node_3[pnode[3]][17]-1)or (
                                            search6 == 24 and Node_3[pnode[3]][15] == 23 and x6 == Node_3[pnode[3]][16] and y6 ==
                                            Node_3[pnode[3]][17]+1)or (
                                            search6 == 25 and Node_3[pnode[3]][15] == 26 and x6 == Node_3[pnode[3]][16] - 1 and y6 ==
                                            Node_3[pnode[3]][17]) or (
                                            search6 == 26 and Node_3[pnode[3]][15] == 25 and x6 == Node_3[pnode[3]][16] + 1 and y6 ==
                                            Node_3[pnode[3]][17])or (
                                            search6 == 27 and Node_3[pnode[3]][15] == 28 and x6 == Node_3[pnode[3]][16] and y6 ==
                                            Node_3[pnode[3]][17]-1) or (
                                            search6 == 28 and Node_3[pnode[3]][15] == 27 and x6 == Node_3[pnode[3]][16] and y6 ==
                                            Node_3[pnode[3]][17]+1)or (
                                            search6 == 51 and Node_3[pnode[3]][15] == 52 and x6 == Node_3[pnode[3]][16]-1 and y6 ==
                                            Node_3[pnode[3]][17])or (
                                            search6 == 52 and Node_3[pnode[3]][15] == 51 and x6 == Node_3[pnode[3]][16]+1 and y6 ==
                                            Node_3[pnode[3]][17])or (
                                            search6 == 53 and Node_3[pnode[3]][15] == 54 and x6 == Node_3[pnode[3]][16] - 1 and y6 ==
                                            Node_3[pnode[3]][17]) or (
                                            search6 == 54 and Node_3[pnode[3]][15] == 53 and x6 == Node_3[pnode[3]][16] + 1 and y6 ==
                                            Node_3[pnode[3]][17])or (
                                            search6 == 55 and Node_3[pnode[3]][15] == 56 and x6 == Node_3[pnode[3]][16] and y6 ==
                                            Node_3[pnode[3]][17]-1)or (
                                            search6 == 56 and Node_3[pnode[3]][15] == 55 and x6 == Node_3[pnode[3]][16] and y6 ==
                                            Node_3[pnode[3]][17]+1)or (
                                            search6 == 57 and Node_3[pnode[3]][15] == 58 and x6 == Node_3[pnode[3]][16] and y6 ==
                                            Node_3[pnode[3]][17]-1) or (
                                            search6 == 58 and Node_3[pnode[3]][15] == 57 and x6 == Node_3[pnode[3]][16] and y6 ==
                                            Node_3[pnode[3]][17]+1) or (
                                            search6 == 1 and Node_4[pnode[4]][15] == 2 and x6 == Node_4[pnode[4]][16]-1 and y6 ==
                                            Node_4[pnode[4]][17])or (
                                            search6 == 1 and Node_4[pnode[4]][15] == 3 and x6 == Node_4[pnode[4]][16] and y6 ==
                                            Node_4[pnode[4]][17])or (
                                            search6 == 2 and Node_4[pnode[4]][15] == 1 and x6 == Node_4[pnode[4]][16]+1 and y6 ==
                                            Node_4[pnode[4]][17])or (
                                            search6 == 2 and Node_4[pnode[4]][15] == 3 and x6 == Node_4[pnode[4]][16]+1 and y6 ==
                                            Node_4[pnode[4]][17]-1)or (
                                            search6 == 3 and Node_4[pnode[4]][15] == 2 and x6 == Node_4[pnode[4]][16]-1 and y6 ==
                                            Node_4[pnode[4]][17]+1)or (
                                            search6 == 3 and Node_4[pnode[4]][15] == 1 and x6 == Node_4[pnode[4]][16] and y6 ==
                                            Node_4[pnode[4]][17]+1)or (
                                            search6 == 4 and Node_4[pnode[4]][15] == 6 and x6 == Node_4[pnode[4]][16]-1 and y6 ==
                                            Node_4[pnode[4]][17]-1)or (
                                            search6 == 4 and Node_4[pnode[4]][15] == 5 and x6 == Node_4[pnode[4]][16]-1 and y6 ==
                                            Node_4[pnode[4]][17])or (
                                            search6 == 5 and Node_4[pnode[4]][15] == 4 and x6 == Node_4[pnode[4]][16]+1 and y6 ==
                                            Node_4[pnode[4]][17])or (
                                            search6 == 5 and Node_4[pnode[4]][15] == 6 and x6 == Node_4[pnode[4]][16] and y6 ==
                                            Node_4[pnode[4]][17]-1)or (
                                            search6 == 6 and Node_4[pnode[4]][15] == 4 and x6 == Node_4[pnode[4]][16]+1 and y6 ==
                                            Node_4[pnode[4]][17]+1) or (
                                            search6 == 6 and Node_4[pnode[4]][15] == 5 and x6 == Node_4[pnode[4]][16] and y6 ==
                                            Node_4[pnode[4]][17]+1)or (
                                            search6 == 7 and Node_4[pnode[4]][15] == 9 and x6 == Node_4[pnode[4]][16]-1 and y6 ==
                                            Node_4[pnode[4]][17]+1)or (
                                            search6 == 7 and Node_4[pnode[4]][15] == 8 and x6 == Node_4[pnode[4]][16]-1 and y6 ==
                                            Node_4[pnode[4]][17])or (
                                            search6 == 8 and Node_4[pnode[4]][15] == 7 and x6 == Node_4[pnode[4]][16]+1 and y6 ==
                                            Node_4[pnode[4]][17])or (
                                            search6 == 8 and Node_4[pnode[4]][15] == 9 and x6 == Node_4[pnode[4]][16] and y6 ==
                                            Node_4[pnode[4]][17]+1)or (
                                            search6 == 9 and Node_4[pnode[4]][15] == 8 and x6 == Node_4[pnode[4]][16] and y6 ==
                                            Node_4[pnode[4]][17]-1)or (
                                            search6 == 9 and Node_4[pnode[4]][15] == 7 and x6 == Node_4[pnode[4]][16]+1 and y6 ==
                                            Node_4[pnode[4]][17]-1)or (
                                            search6 == 10 and Node_4[pnode[4]][15] == 11 and x6 == Node_4[pnode[4]][16]-1 and y6 ==
                                            Node_4[pnode[4]][17])or (
                                            search6 == 10 and Node_4[pnode[4]][15] == 12 and x6 == Node_4[pnode[4]][16] and y6 ==
                                            Node_4[pnode[4]][17]+1)or (
                                            search6 == 11 and Node_4[pnode[4]][15] == 12 and x6 == Node_4[pnode[4]][16]+1 and y6 ==
                                            Node_4[pnode[4]][17]+1)or (
                                            search6 == 11 and Node_4[pnode[4]][15] == 10 and x6 == Node_4[pnode[4]][16]+1 and y6 ==
                                            Node_4[pnode[4]][17])or (
                                            search6 == 12 and Node_4[pnode[4]][15] == 11 and x6 == Node_4[pnode[4]][16]-1 and y6 ==
                                            Node_4[pnode[4]][17]+1)or (
                                            search6 == 21 and Node_4[pnode[4]][15] == 22 and x6 == Node_4[pnode[4]][16]-1 and y6 ==
                                            Node_4[pnode[4]][17])or (
                                            search6 == 12 and Node_4[pnode[4]][15] == 10 and x6 == Node_4[pnode[4]][16] and y6 ==
                                            Node_4[pnode[4]][17]-1)or (
                                            search6 == 22 and Node_4[pnode[4]][15] == 21 and x6 == Node_4[pnode[4]][16]+1 and y6 ==
                                            Node_4[pnode[4]][17])or (
                                            search6 == 23 and Node_4[pnode[4]][15] == 24 and x6 == Node_4[pnode[4]][16] and y6 ==
                                            Node_4[pnode[4]][17]-1)or (
                                            search6 == 24 and Node_4[pnode[4]][15] == 23 and x6 == Node_4[pnode[4]][16] and y6 ==
                                            Node_4[pnode[4]][17]+1)or (
                                            search6 == 25 and Node_4[pnode[4]][15] == 26 and x6 == Node_4[pnode[4]][16] - 1 and y6 ==
                                            Node_4[pnode[4]][17]) or (
                                            search6 == 26 and Node_4[pnode[4]][15] == 25 and x6 == Node_4[pnode[4]][16] + 1 and y6 ==
                                            Node_4[pnode[4]][17])or (
                                            search6 == 27 and Node_4[pnode[4]][15] == 28 and x6 == Node_4[pnode[4]][16] and y6 ==
                                            Node_4[pnode[4]][17]-1) or (
                                            search6 == 28 and Node_4[pnode[4]][15] == 27 and x6 == Node_4[pnode[4]][16] and y6 ==
                                            Node_4[pnode[4]][17]+1)or (
                                            search6 == 51 and Node_4[pnode[4]][15] == 52 and x6 == Node_4[pnode[4]][16]-1 and y6 ==
                                            Node_4[pnode[4]][17])or (
                                            search6 == 52 and Node_4[pnode[4]][15] == 51 and x6 == Node_4[pnode[4]][16]+1 and y6 ==
                                            Node_4[pnode[4]][17])or (
                                            search6 == 53 and Node_4[pnode[4]][15] == 54 and x6 == Node_4[pnode[4]][16] - 1 and y6 ==
                                            Node_4[pnode[4]][17]) or (
                                            search6 == 54 and Node_4[pnode[4]][15] == 53 and x6 == Node_4[pnode[4]][16] + 1 and y6 ==
                                            Node_4[pnode[4]][17])or (
                                            search6 == 55 and Node_4[pnode[4]][15] == 56 and x6 == Node_4[pnode[4]][16] and y6 ==
                                            Node_4[pnode[4]][17]-1)or (
                                            search6 == 56 and Node_4[pnode[4]][15] == 55 and x6 == Node_4[pnode[4]][16] and y6 ==
                                            Node_4[pnode[4]][17]+1)or (
                                            search6 == 57 and Node_4[pnode[4]][15] == 58 and x6 == Node_4[pnode[4]][16] and y6 ==
                                            Node_4[pnode[4]][17]-1) or (
                                            search6 == 58 and Node_4[pnode[4]][15] == 57 and x6 == Node_4[pnode[4]][16] and y6 ==
                                            Node_4[pnode[4]][17]+1)or (
                                            search6 == 1 and Node_5[pnode[5]][15] == 2 and x6 == Node_5[pnode[5]][16]-1 and y6 ==
                                            Node_5[pnode[5]][17])or (
                                            search6 == 1 and Node_5[pnode[5]][15] == 3 and x6 == Node_5[pnode[5]][16] and y6 ==
                                            Node_5[pnode[5]][17])or (
                                            search6 == 2 and Node_5[pnode[5]][15] == 1 and x6 == Node_5[pnode[5]][16]+1 and y6 ==
                                            Node_5[pnode[5]][17])or (
                                            search6 == 2 and Node_5[pnode[5]][15] == 3 and x6 == Node_5[pnode[5]][16]+1 and y6 ==
                                            Node_5[pnode[5]][17]-1)or (
                                            search6 == 3 and Node_5[pnode[5]][15] == 2 and x6 == Node_5[pnode[5]][16]-1 and y6 ==
                                            Node_5[pnode[5]][17]+1)or (
                                            search6 == 3 and Node_5[pnode[5]][15] == 1 and x6 == Node_5[pnode[5]][16] and y6 ==
                                            Node_5[pnode[5]][17]+1)or (
                                            search6 == 4 and Node_5[pnode[5]][15] == 6 and x6 == Node_5[pnode[5]][16]-1 and y6 ==
                                            Node_5[pnode[5]][17]-1)or (
                                            search6 == 4 and Node_5[pnode[5]][15] == 5 and x6 == Node_5[pnode[5]][16]-1 and y6 ==
                                            Node_5[pnode[5]][17])or (
                                            search6 == 5 and Node_5[pnode[5]][15] == 4 and x6 == Node_5[pnode[5]][16]+1 and y6 ==
                                            Node_5[pnode[5]][17])or (
                                            search6 == 5 and Node_5[pnode[5]][15] == 6 and x6 == Node_5[pnode[5]][16] and y6 ==
                                            Node_5[pnode[5]][17]-1)or (
                                            search6 == 6 and Node_5[pnode[5]][15] == 4 and x6 == Node_5[pnode[5]][16]+1 and y6 ==
                                            Node_5[pnode[5]][17]+1) or (
                                            search6 == 6 and Node_5[pnode[5]][15] == 5 and x6 == Node_5[pnode[5]][16] and y6 ==
                                            Node_5[pnode[5]][17]+1)or (
                                            search6 == 7 and Node_5[pnode[5]][15] == 9 and x6 == Node_5[pnode[5]][16]-1 and y6 ==
                                            Node_5[pnode[5]][17]+1)or (
                                            search6 == 7 and Node_5[pnode[5]][15] == 8 and x6 == Node_5[pnode[5]][16]-1 and y6 ==
                                            Node_5[pnode[5]][17])or (
                                            search6 == 8 and Node_5[pnode[5]][15] == 7 and x6 == Node_5[pnode[5]][16]+1 and y6 ==
                                            Node_5[pnode[5]][17])or (
                                            search6 == 8 and Node_5[pnode[5]][15] == 9 and x6 == Node_5[pnode[5]][16] and y6 ==
                                            Node_5[pnode[5]][17]+1)or (
                                            search6 == 9 and Node_5[pnode[5]][15] == 8 and x6 == Node_5[pnode[5]][16] and y6 ==
                                            Node_5[pnode[5]][17]-1)or (
                                            search6 == 9 and Node_5[pnode[5]][15] == 7 and x6 == Node_5[pnode[5]][16]+1 and y6 ==
                                            Node_5[pnode[5]][17]-1)or (
                                            search6 == 10 and Node_5[pnode[5]][15] == 11 and x6 == Node_5[pnode[5]][16]-1 and y6 ==
                                            Node_5[pnode[5]][17])or (
                                            search6 == 10 and Node_5[pnode[5]][15] == 12 and x6 == Node_5[pnode[5]][16] and y6 ==
                                            Node_5[pnode[5]][17]+1)or (
                                            search6 == 11 and Node_5[pnode[5]][15] == 12 and x6 == Node_5[pnode[5]][16]+1 and y6 ==
                                            Node_5[pnode[5]][17]+1)or (
                                            search6 == 11 and Node_5[pnode[5]][15] == 10 and x6 == Node_5[pnode[5]][16]+1 and y6 ==
                                            Node_5[pnode[5]][17])or (
                                            search6 == 12 and Node_5[pnode[5]][15] == 11 and x6 == Node_5[pnode[5]][16]-1 and y6 ==
                                            Node_5[pnode[5]][17]+1)or (
                                            search6 == 21 and Node_5[pnode[5]][15] == 22 and x6 == Node_5[pnode[5]][16]-1 and y6 ==
                                            Node_5[pnode[5]][17])or (
                                            search6 == 12 and Node_5[pnode[5]][15] == 10 and x6 == Node_5[pnode[5]][16] and y6 ==
                                            Node_5[pnode[5]][17]-1)or (
                                            search6 == 22 and Node_5[pnode[5]][15] == 21 and x6 == Node_5[pnode[5]][16]+1 and y6 ==
                                            Node_5[pnode[5]][17])or (
                                            search6 == 23 and Node_5[pnode[5]][15] == 24 and x6 == Node_5[pnode[5]][16] and y6 ==
                                            Node_5[pnode[5]][17]-1)or (
                                            search6 == 24 and Node_5[pnode[5]][15] == 23 and x6 == Node_5[pnode[5]][16] and y6 ==
                                            Node_5[pnode[5]][17]+1)or (
                                            search6 == 25 and Node_5[pnode[5]][15] == 26 and x6 == Node_5[pnode[5]][16] - 1 and y6 ==
                                            Node_5[pnode[5]][17]) or (
                                            search6 == 26 and Node_5[pnode[5]][15] == 25 and x6 == Node_5[pnode[5]][16] + 1 and y6 ==
                                            Node_5[pnode[5]][17])or (
                                            search6 == 27 and Node_5[pnode[5]][15] == 28 and x6 == Node_5[pnode[5]][16] and y6 ==
                                            Node_5[pnode[5]][17]-1) or (
                                            search6 == 28 and Node_5[pnode[5]][15] == 27 and x6 == Node_5[pnode[5]][16] and y6 ==
                                            Node_5[pnode[5]][17]+1)or (
                                            search6 == 51 and Node_5[pnode[5]][15] == 52 and x6 == Node_5[pnode[5]][16]-1 and y6 ==
                                            Node_5[pnode[5]][17])or (
                                            search6 == 52 and Node_5[pnode[5]][15] == 51 and x6 == Node_5[pnode[5]][16]+1 and y6 ==
                                            Node_5[pnode[5]][17])or (
                                            search6 == 53 and Node_5[pnode[5]][15] == 54 and x6 == Node_5[pnode[5]][16] - 1 and y6 ==
                                            Node_5[pnode[5]][17]) or (
                                            search6 == 54 and Node_5[pnode[5]][15] == 53 and x6 == Node_5[pnode[5]][16] + 1 and y6 ==
                                            Node_5[pnode[5]][17])or (
                                            search6 == 55 and Node_5[pnode[5]][15] == 56 and x6 == Node_5[pnode[5]][16] and y6 ==
                                            Node_5[pnode[5]][17]-1)or (
                                            search6 == 56 and Node_5[pnode[5]][15] == 55 and x6 == Node_5[pnode[5]][16] and y6 ==
                                            Node_5[pnode[5]][17]+1)or (
                                            search6 == 57 and Node_5[pnode[5]][15] == 58 and x6 == Node_5[pnode[5]][16] and y6 ==
                                            Node_5[pnode[5]][17]-1) or (
                                            search6 == 58 and Node_5[pnode[5]][15] == 57 and x6 == Node_5[pnode[5]][16] and y6 ==
                                            Node_5[pnode[5]][17]+1)or (
                                            search6 == 1 and Node_6[pnode[6]][15] == 2 and x6 == Node_6[pnode[6]][16]-1 and y6 ==
                                            Node_6[pnode[6]][17])or (
                                            search6 == 1 and Node_6[pnode[6]][15] == 3 and x6 == Node_6[pnode[6]][16] and y6 ==
                                            Node_6[pnode[6]][17])or (
                                            search6 == 2 and Node_6[pnode[6]][15] == 1 and x6 == Node_6[pnode[6]][16]+1 and y6 ==
                                            Node_6[pnode[6]][17])or (
                                            search6 == 2 and Node_6[pnode[6]][15] == 3 and x6 == Node_6[pnode[6]][16]+1 and y6 ==
                                            Node_6[pnode[6]][17]-1)or (
                                            search6 == 3 and Node_6[pnode[6]][15] == 2 and x6 == Node_6[pnode[6]][16]-1 and y6 ==
                                            Node_6[pnode[6]][17]+1)or (
                                            search6 == 3 and Node_6[pnode[6]][15] == 1 and x6 == Node_6[pnode[6]][16] and y6 ==
                                            Node_6[pnode[6]][17]+1)or (
                                            search6 == 4 and Node_6[pnode[6]][15] == 6 and x6 == Node_6[pnode[6]][16]-1 and y6 ==
                                            Node_6[pnode[6]][17]-1)or (
                                            search6 == 4 and Node_6[pnode[6]][15] == 5 and x6 == Node_6[pnode[6]][16]-1 and y6 ==
                                            Node_6[pnode[6]][17])or (
                                            search6 == 5 and Node_6[pnode[6]][15] == 4 and x6 == Node_6[pnode[6]][16]+1 and y6 ==
                                            Node_6[pnode[6]][17])or (
                                            search6 == 5 and Node_6[pnode[6]][15] == 6 and x6 == Node_6[pnode[6]][16] and y6 ==
                                            Node_6[pnode[6]][17]-1)or (
                                            search6 == 6 and Node_6[pnode[6]][15] == 4 and x6 == Node_6[pnode[6]][16]+1 and y6 ==
                                            Node_6[pnode[6]][17]+1) or (
                                            search6 == 6 and Node_6[pnode[6]][15] == 5 and x6 == Node_6[pnode[6]][16] and y6 ==
                                            Node_6[pnode[6]][17]+1)or (
                                            search6 == 7 and Node_6[pnode[6]][15] == 9 and x6 == Node_6[pnode[6]][16]-1 and y6 ==
                                            Node_6[pnode[6]][17]+1)or (
                                            search6 == 7 and Node_6[pnode[6]][15] == 8 and x6 == Node_6[pnode[6]][16]-1 and y6 ==
                                            Node_6[pnode[6]][17])or (
                                            search6 == 8 and Node_6[pnode[6]][15] == 7 and x6 == Node_6[pnode[6]][16]+1 and y6 ==
                                            Node_6[pnode[6]][17])or (
                                            search6 == 8 and Node_6[pnode[6]][15] == 9 and x6 == Node_6[pnode[6]][16] and y6 ==
                                            Node_6[pnode[6]][17]+1)or (
                                            search6 == 9 and Node_6[pnode[6]][15] == 8 and x6 == Node_6[pnode[6]][16] and y6 ==
                                            Node_6[pnode[6]][17]-1)or (
                                            search6 == 9 and Node_6[pnode[6]][15] == 7 and x6 == Node_6[pnode[6]][16]+1 and y6 ==
                                            Node_6[pnode[6]][17]-1)or (
                                            search6 == 10 and Node_6[pnode[6]][15] == 11 and x6 == Node_6[pnode[6]][16]-1 and y6 ==
                                            Node_6[pnode[6]][17])or (
                                            search6 == 10 and Node_6[pnode[6]][15] == 12 and x6 == Node_6[pnode[6]][16] and y6 ==
                                            Node_6[pnode[6]][17]+1)or (
                                            search6 == 11 and Node_6[pnode[6]][15] == 12 and x6 == Node_6[pnode[6]][16]+1 and y6 ==
                                            Node_6[pnode[6]][17]+1)or (
                                            search6 == 11 and Node_6[pnode[6]][15] == 10 and x6 == Node_6[pnode[6]][16]+1 and y6 ==
                                            Node_6[pnode[6]][17])or (
                                            search6 == 12 and Node_6[pnode[6]][15] == 11 and x6 == Node_6[pnode[6]][16]-1 and y6 ==
                                            Node_6[pnode[6]][17]+1)or (
                                            search6 == 21 and Node_6[pnode[6]][15] == 22 and x6 == Node_6[pnode[6]][16]-1 and y6 ==
                                            Node_6[pnode[6]][17])or (
                                            search6 == 12 and Node_6[pnode[6]][15] == 10 and x6 == Node_6[pnode[6]][16] and y6 ==
                                            Node_6[pnode[6]][17]-1)or (
                                            search6 == 22 and Node_6[pnode[6]][15] == 21 and x6 == Node_6[pnode[6]][16]+1 and y6 ==
                                            Node_6[pnode[6]][17])or (
                                            search6 == 23 and Node_6[pnode[6]][15] == 24 and x6 == Node_6[pnode[6]][16] and y6 ==
                                            Node_6[pnode[6]][17]-1)or (
                                            search6 == 24 and Node_6[pnode[6]][15] == 23 and x6 == Node_6[pnode[6]][16] and y6 ==
                                            Node_6[pnode[6]][17]+1)or (
                                            search6 == 25 and Node_6[pnode[6]][15] == 26 and x6 == Node_6[pnode[6]][16] - 1 and y6 ==
                                            Node_6[pnode[6]][17]) or (
                                            search6 == 26 and Node_6[pnode[6]][15] == 25 and x6 == Node_6[pnode[6]][16] + 1 and y6 ==
                                            Node_6[pnode[6]][17])or (
                                            search6 == 27 and Node_6[pnode[6]][15] == 28 and x6 == Node_6[pnode[6]][16] and y6 ==
                                            Node_6[pnode[6]][17]-1) or (
                                            search6 == 28 and Node_6[pnode[6]][15] == 27 and x6 == Node_6[pnode[6]][16] and y6 ==
                                            Node_6[pnode[6]][17]+1)or (
                                            search6 == 51 and Node_6[pnode[6]][15] == 52 and x6 == Node_6[pnode[6]][16]-1 and y6 ==
                                            Node_6[pnode[6]][17])or (
                                            search6 == 52 and Node_6[pnode[6]][15] == 51 and x6 == Node_6[pnode[6]][16]+1 and y6 ==
                                            Node_6[pnode[6]][17])or (
                                            search6 == 53 and Node_6[pnode[6]][15] == 54 and x6 == Node_6[pnode[6]][16] - 1 and y6 ==
                                            Node_6[pnode[6]][17]) or (
                                            search6 == 54 and Node_6[pnode[6]][15] == 53 and x6 == Node_6[pnode[6]][16] + 1 and y6 ==
                                            Node_6[pnode[6]][17])or (
                                            search6 == 55 and Node_6[pnode[6]][15] == 56 and x6 == Node_6[pnode[6]][16] and y6 ==
                                            Node_6[pnode[6]][17]-1)or (
                                            search6 == 56 and Node_6[pnode[6]][15] == 55 and x6 == Node_6[pnode[6]][16] and y6 ==
                                            Node_6[pnode[6]][17]+1)or (
                                            search6 == 57 and Node_6[pnode[6]][15] == 58 and x6 == Node_6[pnode[6]][16] and y6 ==
                                            Node_6[pnode[6]][17]-1) or (
                                            search6 == 58 and Node_6[pnode[6]][15] == 57 and x6 == Node_6[pnode[6]][16] and y6 ==
                                            Node_6[pnode[6]][17]+1)):
                                        if ((Node_4[numNode_4][15] == pnode[8] and Node_4[numNode_4][16] == pnode[9] and
                                             Node_4[numNode_4][17] == pnode[10]) or (
                                                Node_4[numNode_4][15] == Node_1[pnode[1]][15] and Node_4[numNode_4][
                                            16] == Node_1[pnode[1]][16] and Node_4[numNode_4][17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == Node_2[pnode[2]][15] and Node_4[numNode_4][
                                            16] == Node_2[pnode[2]][16] and Node_4[numNode_4][17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == Node_3[pnode[3]][15] and Node_4[numNode_4][
                                            16] == Node_3[pnode[3]][16] and Node_4[numNode_4][17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == Node_4[pnode[4]][15] and Node_4[numNode_4][
                                            16] == Node_4[pnode[4]][16] and Node_4[numNode_4][17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == Node_5[pnode[5]][15] and Node_4[numNode_4][
                                            16] == Node_5[pnode[5]][16] and Node_4[numNode_4][17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == Node_6[pnode[6]][15] and Node_4[numNode_4][
                                            16] == Node_6[pnode[6]][16] and Node_4[numNode_4][17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 1 and pnode[8] == 2 and Node_4[numNode_4][
                                            16] == pnode[9] - 1 and Node_4[numNode_4][17] ==
                                                pnode[10]) or (
                                                Node_4[numNode_4][15] == 1 and pnode[8] == 3 and Node_4[numNode_4][
                                            16] == pnode[9] and Node_4[numNode_4][17] ==
                                                pnode[10] - 1) or (
                                                Node_4[numNode_4][15] == 2 and pnode[8] == 1 and Node_4[numNode_4][
                                            16] == pnode[9] + 1 and Node_4[numNode_4][17] ==
                                                pnode[10]) or (
                                                Node_4[numNode_4][15] == 2 and pnode[8] == 3 and Node_4[numNode_4][
                                            16] == pnode[9] + 1 and Node_4[numNode_4][17] ==
                                                pnode[10] - 1) or (
                                                Node_4[numNode_4][15] == 3 and pnode[8] == 2 and Node_4[numNode_4][
                                            16] == pnode[9] - 1 and Node_4[numNode_4][17] ==
                                                pnode[10] + 1) or (
                                                Node_4[numNode_4][15] == 3 and pnode[8] == 1 and Node_4[numNode_4][
                                            16] == pnode[9] and Node_4[numNode_4][17] ==
                                                pnode[10] + 1) or (
                                                Node_4[numNode_4][15] == 4 and pnode[8] == 6 and Node_4[numNode_4][
                                            16] == pnode[9] - 1 and Node_4[numNode_4][17] ==
                                                pnode[10] - 1) or (
                                                Node_4[numNode_4][15] == 4 and pnode[8] == 5 and Node_4[numNode_4][
                                            16] == pnode[9] - 1 and Node_4[numNode_4][17] ==
                                                pnode[10]) or (
                                                Node_4[numNode_4][15] == 5 and pnode[8] == 4 and Node_4[numNode_4][
                                            16] == pnode[9] + 1 and Node_4[numNode_4][17] ==
                                                pnode[10]) or (
                                                Node_4[numNode_4][15] == 5 and pnode[8] == 6 and Node_4[numNode_4][
                                            16] == pnode[9] and Node_4[numNode_4][17] ==
                                                pnode[10] - 1) or (
                                                Node_4[numNode_4][15] == 6 and pnode[8] == 4 and Node_4[numNode_4][
                                            16] == pnode[9] + 1 and Node_4[numNode_4][17] ==
                                                pnode[10] + 1) or (
                                                Node_4[numNode_4][15] == 6 and pnode[8] == 5 and Node_4[numNode_4][
                                            16] == pnode[9] and Node_4[numNode_4][17] ==
                                                pnode[10] + 1) or (
                                                Node_4[numNode_4][15] == 7 and pnode[8] == 9 and Node_4[numNode_4][
                                            16] == pnode[9] - 1 and Node_4[numNode_4][17] ==
                                                pnode[10] + 1) or (
                                                Node_4[numNode_4][15] == 7 and pnode[8] == 8 and Node_4[numNode_4][
                                            16] == pnode[9] - 1 and Node_4[numNode_4][17] ==
                                                pnode[10]) or (
                                                Node_4[numNode_4][15] == 8 and pnode[8] == 7 and Node_4[numNode_4][
                                            16] == pnode[9] + 1 and Node_4[numNode_4][17] ==
                                                pnode[10]) or (
                                                Node_4[numNode_4][15] == 8 and pnode[8] == 9 and Node_4[numNode_4][
                                            16] == pnode[9] and Node_4[numNode_4][17] ==
                                                pnode[10] + 1) or (
                                                Node_4[numNode_4][15] == 9 and pnode[8] == 8 and Node_4[numNode_4][
                                            16] == pnode[9] and Node_4[numNode_4][17] ==
                                                pnode[10] - 1) or (
                                                Node_4[numNode_4][15] == 9 and pnode[8] == 7 and Node_4[numNode_4][
                                            16] == pnode[9] + 1 and Node_4[numNode_4][17] ==
                                                pnode[10] - 1) or (
                                                Node_4[numNode_4][15] == 10 and pnode[8] == 11 and Node_4[numNode_4][
                                            16] == pnode[9] - 1 and Node_4[numNode_4][17] ==
                                                pnode[10]) or (
                                                Node_4[numNode_4][15] == 10 and pnode[8] == 12 and Node_4[numNode_4][
                                            16] == pnode[9] and Node_4[numNode_4][17] ==
                                                pnode[10] + 1) or (
                                                Node_4[numNode_4][15] == 11 and pnode[8] == 12 and Node_4[numNode_4][
                                            16] == pnode[9] + 1 and Node_4[numNode_4][17] ==
                                                pnode[10] + 1) or (
                                                Node_4[numNode_4][15] == 11 and pnode[8] == 10 and Node_4[numNode_4][
                                            16] == pnode[9] + 1 and Node_4[numNode_4][17] ==
                                                pnode[10]) or (
                                                Node_4[numNode_4][15] == 12 and pnode[8] == 11 and Node_4[numNode_4][
                                            16] == pnode[9] - 1 and Node_4[numNode_4][17] ==
                                                pnode[10] + 1) or (
                                                Node_4[numNode_4][15] == 21 and pnode[8] == 22 and Node_4[numNode_4][
                                            16] == pnode[9] - 1 and Node_4[numNode_4][17] ==
                                                pnode[10]) or (
                                                Node_4[numNode_4][15] == 12 and pnode[8] == 10 and Node_4[numNode_4][
                                            16] == pnode[9] and Node_4[numNode_4][17] ==
                                                pnode[10] - 1) or (
                                                Node_4[numNode_4][15] == 22 and pnode[8] == 21 and Node_4[numNode_4][
                                            16] == pnode[9] + 1 and Node_4[numNode_4][17] ==
                                                pnode[10]) or (
                                                Node_4[numNode_4][15] == 23 and pnode[8] == 24 and Node_4[numNode_4][
                                            16] == pnode[9] and Node_4[numNode_4][17] ==
                                                pnode[10] - 1) or (
                                                Node_4[numNode_4][15] == 24 and pnode[8] == 23 and Node_4[numNode_4][
                                            16] == pnode[9] and Node_4[numNode_4][17] ==
                                                pnode[10] + 1) or (
                                                Node_4[numNode_4][15] == 25 and pnode[8] == 26 and Node_4[numNode_4][
                                            16] == pnode[9] - 1 and Node_4[numNode_4][17] ==
                                                pnode[10]) or (
                                                Node_4[numNode_4][15] == 26 and pnode[8] == 25 and Node_4[numNode_4][
                                            16] == pnode[9] + 1 and Node_4[numNode_4][17] ==
                                                pnode[10]) or (
                                                Node_4[numNode_4][15] == 27 and pnode[8] == 28 and Node_4[numNode_4][
                                            16] == pnode[9] and Node_4[numNode_4][17] ==
                                                pnode[10] - 1) or (
                                                Node_4[numNode_4][15] == 28 and pnode[8] == 27 and Node_4[numNode_4][
                                            16] == pnode[9] and Node_4[numNode_4][17] ==
                                                pnode[10] + 1) or (
                                                Node_4[numNode_4][15] == 51 and pnode[8] == 52 and Node_4[numNode_4][
                                            16] == pnode[9] - 1 and Node_4[numNode_4][17] ==
                                                pnode[10]) or (
                                                Node_4[numNode_4][15] == 52 and pnode[8] == 51 and Node_4[numNode_4][
                                            16] == pnode[9] + 1 and Node_4[numNode_4][17] ==
                                                pnode[10]) or (
                                                Node_4[numNode_4][15] == 53 and pnode[8] == 54 and Node_4[numNode_4][
                                            16] == pnode[9] - 1 and Node_4[numNode_4][17] ==
                                                pnode[10]) or (
                                                Node_4[numNode_4][15] == 54 and pnode[8] == 53 and Node_4[numNode_4][
                                            16] == pnode[9] + 1 and Node_4[numNode_4][17] ==
                                                pnode[10]) or (
                                                Node_4[numNode_4][15] == 55 and pnode[8] == 56 and Node_4[numNode_4][
                                            16] == pnode[9] and Node_4[numNode_4][17] ==
                                                pnode[10] - 1) or (
                                                Node_4[numNode_4][15] == 56 and pnode[8] == 55 and Node_4[numNode_4][
                                            16] == pnode[9] and Node_4[numNode_4][17] ==
                                                pnode[10] + 1) or (
                                                Node_4[numNode_4][15] == 57 and pnode[8] == 58 and Node_4[numNode_4][
                                            16] == pnode[9] and Node_4[numNode_4][17] ==
                                                pnode[10] - 1) or (
                                                Node_4[numNode_4][15] == 58 and pnode[8] == 57 and Node_4[numNode_4][
                                            16] == pnode[9] and Node_4[numNode_4][17] ==
                                                pnode[10] + 1) or (
                                                Node_4[numNode_4][15] == 1 and Node_1[pnode[1]][15] == 2 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == 1 and Node_1[pnode[1]][15] == 3 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == 2 and Node_1[pnode[1]][15] == 1 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == 2 and Node_1[pnode[1]][15] == 3 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] - 1) or (
                                                Node_4[numNode_4][15] == 3 and Node_1[pnode[1]][15] == 2 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] + 1) or (
                                                Node_4[numNode_4][15] == 3 and Node_1[pnode[1]][15] == 1 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] + 1) or (
                                                Node_4[numNode_4][15] == 4 and Node_1[pnode[1]][15] == 6 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] - 1) or (
                                                Node_4[numNode_4][15] == 4 and Node_1[pnode[1]][15] == 5 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == 5 and Node_1[pnode[1]][15] == 4 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == 5 and Node_1[pnode[1]][15] == 6 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] - 1) or (
                                                Node_4[numNode_4][15] == 6 and Node_1[pnode[1]][15] == 4 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] + 1) or (
                                                Node_4[numNode_4][15] == 6 and Node_1[pnode[1]][15] == 5 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] + 1) or (
                                                Node_4[numNode_4][15] == 7 and Node_1[pnode[1]][15] == 9 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] + 1) or (
                                                Node_4[numNode_4][15] == 7 and Node_1[pnode[1]][15] == 8 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == 8 and Node_1[pnode[1]][15] == 7 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == 8 and Node_1[pnode[1]][15] == 9 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] + 1) or (
                                                Node_4[numNode_4][15] == 9 and Node_1[pnode[1]][15] == 8 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] - 1) or (
                                                Node_4[numNode_4][15] == 9 and Node_1[pnode[1]][15] == 7 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] - 1) or (
                                                Node_4[numNode_4][15] == 10 and Node_1[pnode[1]][15] == 11 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == 10 and Node_1[pnode[1]][15] == 12 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] + 1) or (
                                                Node_4[numNode_4][15] == 11 and Node_1[pnode[1]][15] == 12 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] + 1) or (
                                                Node_4[numNode_4][15] == 11 and Node_1[pnode[1]][15] == 10 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == 12 and Node_1[pnode[1]][15] == 11 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] + 1) or (
                                                Node_4[numNode_4][15] == 21 and Node_1[pnode[1]][15] == 22 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == 12 and Node_1[pnode[1]][15] == 10 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] - 1) or (
                                                Node_4[numNode_4][15] == 22 and Node_1[pnode[1]][15] == 21 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == 23 and Node_1[pnode[1]][15] == 24 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] - 1) or (
                                                Node_4[numNode_4][15] == 24 and Node_1[pnode[1]][15] == 23 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] + 1) or (
                                                Node_4[numNode_4][15] == 25 and Node_1[pnode[1]][15] == 26 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == 26 and Node_1[pnode[1]][15] == 25 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == 27 and Node_1[pnode[1]][15] == 28 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] - 1) or (
                                                Node_4[numNode_4][15] == 28 and Node_1[pnode[1]][15] == 27 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] + 1) or (
                                                Node_4[numNode_4][15] == 51 and Node_1[pnode[1]][15] == 52 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == 52 and Node_1[pnode[1]][15] == 51 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == 53 and Node_1[pnode[1]][15] == 54 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == 54 and Node_1[pnode[1]][15] == 53 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17]) or (
                                                Node_4[numNode_4][15] == 55 and Node_1[pnode[1]][15] == 56 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] - 1) or (
                                                Node_4[numNode_4][15] == 56 and Node_1[pnode[1]][15] == 55 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] + 1) or (
                                                Node_4[numNode_4][15] == 57 and Node_1[pnode[1]][15] == 58 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] - 1) or (
                                                Node_4[numNode_4][15] == 58 and Node_1[pnode[1]][15] == 57 and
                                                Node_4[numNode_4][16] == Node_1[pnode[1]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_1[pnode[1]][17] + 1) or (
                                                Node_4[numNode_4][15] == 1 and Node_2[pnode[2]][15] == 2 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == 1 and Node_2[pnode[2]][15] == 3 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == 2 and Node_2[pnode[2]][15] == 1 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == 2 and Node_2[pnode[2]][15] == 3 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] - 1) or (
                                                Node_4[numNode_4][15] == 3 and Node_2[pnode[2]][15] == 2 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] + 1) or (
                                                Node_4[numNode_4][15] == 3 and Node_2[pnode[2]][15] == 1 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] + 1) or (
                                                Node_4[numNode_4][15] == 4 and Node_2[pnode[2]][15] == 6 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] - 1) or (
                                                Node_4[numNode_4][15] == 4 and Node_2[pnode[2]][15] == 5 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == 5 and Node_2[pnode[2]][15] == 4 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == 5 and Node_2[pnode[2]][15] == 6 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] - 1) or (
                                                Node_4[numNode_4][15] == 6 and Node_2[pnode[2]][15] == 4 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] + 1) or (
                                                Node_4[numNode_4][15] == 6 and Node_2[pnode[2]][15] == 5 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] + 1) or (
                                                Node_4[numNode_4][15] == 7 and Node_2[pnode[2]][15] == 9 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] + 1) or (
                                                Node_4[numNode_4][15] == 7 and Node_2[pnode[2]][15] == 8 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == 8 and Node_2[pnode[2]][15] == 7 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == 8 and Node_2[pnode[2]][15] == 9 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] + 1) or (
                                                Node_4[numNode_4][15] == 9 and Node_2[pnode[2]][15] == 8 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] - 1) or (
                                                Node_4[numNode_4][15] == 9 and Node_2[pnode[2]][15] == 7 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] - 1) or (
                                                Node_4[numNode_4][15] == 10 and Node_2[pnode[2]][15] == 11 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == 10 and Node_2[pnode[2]][15] == 12 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] + 1) or (
                                                Node_4[numNode_4][15] == 11 and Node_2[pnode[2]][15] == 12 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] + 1) or (
                                                Node_4[numNode_4][15] == 11 and Node_2[pnode[2]][15] == 10 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == 12 and Node_2[pnode[2]][15] == 11 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] + 1) or (
                                                Node_4[numNode_4][15] == 21 and Node_2[pnode[2]][15] == 22 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == 12 and Node_2[pnode[2]][15] == 10 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] - 1) or (
                                                Node_4[numNode_4][15] == 22 and Node_2[pnode[2]][15] == 21 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == 23 and Node_2[pnode[2]][15] == 24 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] - 1) or (
                                                Node_4[numNode_4][15] == 24 and Node_2[pnode[2]][15] == 23 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] + 1) or (
                                                Node_4[numNode_4][15] == 25 and Node_2[pnode[2]][15] == 26 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == 26 and Node_2[pnode[2]][15] == 25 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == 27 and Node_2[pnode[2]][15] == 28 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] - 1) or (
                                                Node_4[numNode_4][15] == 28 and Node_2[pnode[2]][15] == 27 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] + 1) or (
                                                Node_4[numNode_4][15] == 51 and Node_2[pnode[2]][15] == 52 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == 52 and Node_2[pnode[2]][15] == 51 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == 53 and Node_2[pnode[2]][15] == 54 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == 54 and Node_2[pnode[2]][15] == 53 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17]) or (
                                                Node_4[numNode_4][15] == 55 and Node_2[pnode[2]][15] == 56 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] - 1) or (
                                                Node_4[numNode_4][15] == 56 and Node_2[pnode[2]][15] == 55 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] + 1) or (
                                                Node_4[numNode_4][15] == 57 and Node_2[pnode[2]][15] == 58 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] - 1) or (
                                                Node_4[numNode_4][15] == 58 and Node_2[pnode[2]][15] == 57 and
                                                Node_4[numNode_4][16] == Node_2[pnode[2]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_2[pnode[2]][17] + 1) or (
                                                Node_4[numNode_4][15] == 1 and Node_3[pnode[3]][15] == 2 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == 1 and Node_3[pnode[3]][15] == 3 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == 2 and Node_3[pnode[3]][15] == 1 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == 2 and Node_3[pnode[3]][15] == 3 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] - 1) or (
                                                Node_4[numNode_4][15] == 3 and Node_3[pnode[3]][15] == 2 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] + 1) or (
                                                Node_4[numNode_4][15] == 3 and Node_3[pnode[3]][15] == 1 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] + 1) or (
                                                Node_4[numNode_4][15] == 4 and Node_3[pnode[3]][15] == 6 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] - 1) or (
                                                Node_4[numNode_4][15] == 4 and Node_3[pnode[3]][15] == 5 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == 5 and Node_3[pnode[3]][15] == 4 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == 5 and Node_3[pnode[3]][15] == 6 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] - 1) or (
                                                Node_4[numNode_4][15] == 6 and Node_3[pnode[3]][15] == 4 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] + 1) or (
                                                Node_4[numNode_4][15] == 6 and Node_3[pnode[3]][15] == 5 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] + 1) or (
                                                Node_4[numNode_4][15] == 7 and Node_3[pnode[3]][15] == 9 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] + 1) or (
                                                Node_4[numNode_4][15] == 7 and Node_3[pnode[3]][15] == 8 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == 8 and Node_3[pnode[3]][15] == 7 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == 8 and Node_3[pnode[3]][15] == 9 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] + 1) or (
                                                Node_4[numNode_4][15] == 9 and Node_3[pnode[3]][15] == 8 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] - 1) or (
                                                Node_4[numNode_4][15] == 9 and Node_3[pnode[3]][15] == 7 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] - 1) or (
                                                Node_4[numNode_4][15] == 10 and Node_3[pnode[3]][15] == 11 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == 10 and Node_3[pnode[3]][15] == 12 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] + 1) or (
                                                Node_4[numNode_4][15] == 11 and Node_3[pnode[3]][15] == 12 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] + 1) or (
                                                Node_4[numNode_4][15] == 11 and Node_3[pnode[3]][15] == 10 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == 12 and Node_3[pnode[3]][15] == 11 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] + 1) or (
                                                Node_4[numNode_4][15] == 21 and Node_3[pnode[3]][15] == 22 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == 12 and Node_3[pnode[3]][15] == 10 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] - 1) or (
                                                Node_4[numNode_4][15] == 22 and Node_3[pnode[3]][15] == 21 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == 23 and Node_3[pnode[3]][15] == 24 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] - 1) or (
                                                Node_4[numNode_4][15] == 24 and Node_3[pnode[3]][15] == 23 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] + 1) or (
                                                Node_4[numNode_4][15] == 25 and Node_3[pnode[3]][15] == 26 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == 26 and Node_3[pnode[3]][15] == 25 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == 27 and Node_3[pnode[3]][15] == 28 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] - 1) or (
                                                Node_4[numNode_4][15] == 28 and Node_3[pnode[3]][15] == 27 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] + 1) or (
                                                Node_4[numNode_4][15] == 51 and Node_3[pnode[3]][15] == 52 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == 52 and Node_3[pnode[3]][15] == 51 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == 53 and Node_3[pnode[3]][15] == 54 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == 54 and Node_3[pnode[3]][15] == 53 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17]) or (
                                                Node_4[numNode_4][15] == 55 and Node_3[pnode[3]][15] == 56 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] - 1) or (
                                                Node_4[numNode_4][15] == 56 and Node_3[pnode[3]][15] == 55 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] + 1) or (
                                                Node_4[numNode_4][15] == 57 and Node_3[pnode[3]][15] == 58 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] - 1) or (
                                                Node_4[numNode_4][15] == 58 and Node_3[pnode[3]][15] == 57 and
                                                Node_4[numNode_4][16] == Node_3[pnode[3]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_3[pnode[3]][17] + 1) or (
                                                Node_4[numNode_4][15] == 1 and Node_4[pnode[4]][15] == 2 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == 1 and Node_4[pnode[4]][15] == 3 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == 2 and Node_4[pnode[4]][15] == 1 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == 2 and Node_4[pnode[4]][15] == 3 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] - 1) or (
                                                Node_4[numNode_4][15] == 3 and Node_4[pnode[4]][15] == 2 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] + 1) or (
                                                Node_4[numNode_4][15] == 3 and Node_4[pnode[4]][15] == 1 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] + 1) or (
                                                Node_4[numNode_4][15] == 4 and Node_4[pnode[4]][15] == 6 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] - 1) or (
                                                Node_4[numNode_4][15] == 4 and Node_4[pnode[4]][15] == 5 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == 5 and Node_4[pnode[4]][15] == 4 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == 5 and Node_4[pnode[4]][15] == 6 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] - 1) or (
                                                Node_4[numNode_4][15] == 6 and Node_4[pnode[4]][15] == 4 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] + 1) or (
                                                Node_4[numNode_4][15] == 6 and Node_4[pnode[4]][15] == 5 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] + 1) or (
                                                Node_4[numNode_4][15] == 7 and Node_4[pnode[4]][15] == 9 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] + 1) or (
                                                Node_4[numNode_4][15] == 7 and Node_4[pnode[4]][15] == 8 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == 8 and Node_4[pnode[4]][15] == 7 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == 8 and Node_4[pnode[4]][15] == 9 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] + 1) or (
                                                Node_4[numNode_4][15] == 9 and Node_4[pnode[4]][15] == 8 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] - 1) or (
                                                Node_4[numNode_4][15] == 9 and Node_4[pnode[4]][15] == 7 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] - 1) or (
                                                Node_4[numNode_4][15] == 10 and Node_4[pnode[4]][15] == 11 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == 10 and Node_4[pnode[4]][15] == 12 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] + 1) or (
                                                Node_4[numNode_4][15] == 11 and Node_4[pnode[4]][15] == 12 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] + 1) or (
                                                Node_4[numNode_4][15] == 11 and Node_4[pnode[4]][15] == 10 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == 12 and Node_4[pnode[4]][15] == 11 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] + 1) or (
                                                Node_4[numNode_4][15] == 21 and Node_4[pnode[4]][15] == 22 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == 12 and Node_4[pnode[4]][15] == 10 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] - 1) or (
                                                Node_4[numNode_4][15] == 22 and Node_4[pnode[4]][15] == 21 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == 23 and Node_4[pnode[4]][15] == 24 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] - 1) or (
                                                Node_4[numNode_4][15] == 24 and Node_4[pnode[4]][15] == 23 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] + 1) or (
                                                Node_4[numNode_4][15] == 25 and Node_4[pnode[4]][15] == 26 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == 26 and Node_4[pnode[4]][15] == 25 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == 27 and Node_4[pnode[4]][15] == 28 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] - 1) or (
                                                Node_4[numNode_4][15] == 28 and Node_4[pnode[4]][15] == 27 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] + 1) or (
                                                Node_4[numNode_4][15] == 51 and Node_4[pnode[4]][15] == 52 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == 52 and Node_4[pnode[4]][15] == 51 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == 53 and Node_4[pnode[4]][15] == 54 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == 54 and Node_4[pnode[4]][15] == 53 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17]) or (
                                                Node_4[numNode_4][15] == 55 and Node_4[pnode[4]][15] == 56 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] - 1) or (
                                                Node_4[numNode_4][15] == 56 and Node_4[pnode[4]][15] == 55 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] + 1) or (
                                                Node_4[numNode_4][15] == 57 and Node_4[pnode[4]][15] == 58 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] - 1) or (
                                                Node_4[numNode_4][15] == 58 and Node_4[pnode[4]][15] == 57 and
                                                Node_4[numNode_4][16] == Node_4[pnode[4]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_4[pnode[4]][17] + 1) or (
                                                Node_4[numNode_4][15] == 1 and Node_5[pnode[5]][15] == 2 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == 1 and Node_5[pnode[5]][15] == 3 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == 2 and Node_5[pnode[5]][15] == 1 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == 2 and Node_5[pnode[5]][15] == 3 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] - 1) or (
                                                Node_4[numNode_4][15] == 3 and Node_5[pnode[5]][15] == 2 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] + 1) or (
                                                Node_4[numNode_4][15] == 3 and Node_5[pnode[5]][15] == 1 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] + 1) or (
                                                Node_4[numNode_4][15] == 4 and Node_5[pnode[5]][15] == 6 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] - 1) or (
                                                Node_4[numNode_4][15] == 4 and Node_5[pnode[5]][15] == 5 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == 5 and Node_5[pnode[5]][15] == 4 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == 5 and Node_5[pnode[5]][15] == 6 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] - 1) or (
                                                Node_4[numNode_4][15] == 6 and Node_5[pnode[5]][15] == 4 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] + 1) or (
                                                Node_4[numNode_4][15] == 6 and Node_5[pnode[5]][15] == 5 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] + 1) or (
                                                Node_4[numNode_4][15] == 7 and Node_5[pnode[5]][15] == 9 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] + 1) or (
                                                Node_4[numNode_4][15] == 7 and Node_5[pnode[5]][15] == 8 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == 8 and Node_5[pnode[5]][15] == 7 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == 8 and Node_5[pnode[5]][15] == 9 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] + 1) or (
                                                Node_4[numNode_4][15] == 9 and Node_5[pnode[5]][15] == 8 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] - 1) or (
                                                Node_4[numNode_4][15] == 9 and Node_5[pnode[5]][15] == 7 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] - 1) or (
                                                Node_4[numNode_4][15] == 10 and Node_5[pnode[5]][15] == 11 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == 10 and Node_5[pnode[5]][15] == 12 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] + 1) or (
                                                Node_4[numNode_4][15] == 11 and Node_5[pnode[5]][15] == 12 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] + 1) or (
                                                Node_4[numNode_4][15] == 11 and Node_5[pnode[5]][15] == 10 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == 12 and Node_5[pnode[5]][15] == 11 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] + 1) or (
                                                Node_4[numNode_4][15] == 21 and Node_5[pnode[5]][15] == 22 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == 12 and Node_5[pnode[5]][15] == 10 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] - 1) or (
                                                Node_4[numNode_4][15] == 22 and Node_5[pnode[5]][15] == 21 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == 23 and Node_5[pnode[5]][15] == 24 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] - 1) or (
                                                Node_4[numNode_4][15] == 24 and Node_5[pnode[5]][15] == 23 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] + 1) or (
                                                Node_4[numNode_4][15] == 25 and Node_5[pnode[5]][15] == 26 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == 26 and Node_5[pnode[5]][15] == 25 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == 27 and Node_5[pnode[5]][15] == 28 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] - 1) or (
                                                Node_4[numNode_4][15] == 28 and Node_5[pnode[5]][15] == 27 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] + 1) or (
                                                Node_4[numNode_4][15] == 51 and Node_5[pnode[5]][15] == 52 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == 52 and Node_5[pnode[5]][15] == 51 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == 53 and Node_5[pnode[5]][15] == 54 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == 54 and Node_5[pnode[5]][15] == 53 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17]) or (
                                                Node_4[numNode_4][15] == 55 and Node_5[pnode[5]][15] == 56 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] - 1) or (
                                                Node_4[numNode_4][15] == 56 and Node_5[pnode[5]][15] == 55 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] + 1) or (
                                                Node_4[numNode_4][15] == 57 and Node_5[pnode[5]][15] == 58 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] - 1) or (
                                                Node_4[numNode_4][15] == 58 and Node_5[pnode[5]][15] == 57 and
                                                Node_4[numNode_4][16] == Node_5[pnode[5]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_5[pnode[5]][17] + 1) or (
                                                Node_4[numNode_4][15] == 1 and Node_6[pnode[6]][15] == 2 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 1 and Node_6[pnode[6]][15] == 3 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 2 and Node_6[pnode[6]][15] == 1 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 2 and Node_6[pnode[6]][15] == 3 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] - 1) or (
                                                Node_4[numNode_4][15] == 3 and Node_6[pnode[6]][15] == 2 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] + 1) or (
                                                Node_4[numNode_4][15] == 3 and Node_6[pnode[6]][15] == 1 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] + 1) or (
                                                Node_4[numNode_4][15] == 4 and Node_6[pnode[6]][15] == 6 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] - 1) or (
                                                Node_4[numNode_4][15] == 4 and Node_6[pnode[6]][15] == 5 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 5 and Node_6[pnode[6]][15] == 4 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 5 and Node_6[pnode[6]][15] == 6 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] - 1) or (
                                                Node_4[numNode_4][15] == 6 and Node_6[pnode[6]][15] == 4 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] + 1) or (
                                                Node_4[numNode_4][15] == 6 and Node_6[pnode[6]][15] == 5 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] + 1) or (
                                                Node_4[numNode_4][15] == 7 and Node_6[pnode[6]][15] == 9 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] + 1) or (
                                                Node_4[numNode_4][15] == 7 and Node_6[pnode[6]][15] == 8 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 8 and Node_6[pnode[6]][15] == 7 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 8 and Node_6[pnode[6]][15] == 9 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] + 1) or (
                                                Node_4[numNode_4][15] == 9 and Node_6[pnode[6]][15] == 8 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] - 1) or (
                                                Node_4[numNode_4][15] == 9 and Node_6[pnode[6]][15] == 7 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] - 1) or (
                                                Node_4[numNode_4][15] == 10 and Node_6[pnode[6]][15] == 11 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 10 and Node_6[pnode[6]][15] == 12 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] + 1) or (
                                                Node_4[numNode_4][15] == 11 and Node_6[pnode[6]][15] == 12 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] + 1) or (
                                                Node_4[numNode_4][15] == 11 and Node_6[pnode[6]][15] == 10 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 12 and Node_6[pnode[6]][15] == 11 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] + 1) or (
                                                Node_4[numNode_4][15] == 21 and Node_6[pnode[6]][15] == 22 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 12 and Node_6[pnode[6]][15] == 10 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] - 1) or (
                                                Node_4[numNode_4][15] == 22 and Node_6[pnode[6]][15] == 21 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 23 and Node_6[pnode[6]][15] == 24 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] - 1) or (
                                                Node_4[numNode_4][15] == 24 and Node_6[pnode[6]][15] == 23 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] + 1) or (
                                                Node_4[numNode_4][15] == 25 and Node_6[pnode[6]][15] == 26 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 26 and Node_6[pnode[6]][15] == 25 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 27 and Node_6[pnode[6]][15] == 28 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] - 1) or (
                                                Node_4[numNode_4][15] == 28 and Node_6[pnode[6]][15] == 27 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] + 1) or (
                                                Node_4[numNode_4][15] == 51 and Node_6[pnode[6]][15] == 52 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 52 and Node_6[pnode[6]][15] == 51 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 53 and Node_6[pnode[6]][15] == 54 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] - 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 54 and Node_6[pnode[6]][15] == 53 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] + 1 and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17]) or (
                                                Node_4[numNode_4][15] == 55 and Node_6[pnode[6]][15] == 56 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] - 1) or (
                                                Node_4[numNode_4][15] == 56 and Node_6[pnode[6]][15] == 55 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] + 1) or (
                                                Node_4[numNode_4][15] == 57 and Node_6[pnode[6]][15] == 58 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] - 1) or (
                                                Node_4[numNode_4][15] == 58 and Node_6[pnode[6]][15] == 57 and
                                                Node_4[numNode_4][16] == Node_6[pnode[6]][16] and Node_4[numNode_4][
                                                    17] ==
                                                Node_6[pnode[6]][17] + 1)):
                                            if ((Node_5[numNode_5][15] == pnode[8] and Node_5[numNode_5][16] == pnode[
                                                9] and Node_5[numNode_5][17] == pnode[10]) or (
                                                    Node_5[numNode_5][15] == Node_1[pnode[1]][15] and Node_5[numNode_5][
                                                16] == Node_1[pnode[1]][16] and Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == Node_2[pnode[2]][15] and Node_5[numNode_5][
                                                16] == Node_2[pnode[2]][16] and Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == Node_3[pnode[3]][15] and Node_5[numNode_5][
                                                16] == Node_3[pnode[3]][16] and Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == Node_4[pnode[4]][15] and Node_5[numNode_5][
                                                16] == Node_4[pnode[4]][16] and Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == Node_5[pnode[5]][15] and Node_5[numNode_5][
                                                16] == Node_5[pnode[5]][16] and Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == Node_6[pnode[6]][15] and Node_5[numNode_5][
                                                16] == Node_6[pnode[6]][16] and Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 1 and pnode[8] == 2 and Node_5[numNode_5][
                                                16] == pnode[9] - 1 and Node_5[numNode_5][17] ==
                                                    pnode[10]) or (
                                                    Node_5[numNode_5][15] == 1 and pnode[8] == 3 and Node_5[numNode_5][
                                                16] == pnode[9] and Node_5[numNode_5][17] ==
                                                    pnode[10] - 1) or (
                                                    Node_5[numNode_5][15] == 2 and pnode[8] == 1 and Node_5[numNode_5][
                                                16] == pnode[9] + 1 and Node_5[numNode_5][17] ==
                                                    pnode[10]) or (
                                                    Node_5[numNode_5][15] == 2 and pnode[8] == 3 and Node_5[numNode_5][
                                                16] == pnode[9] + 1 and Node_5[numNode_5][17] ==
                                                    pnode[10] - 1) or (
                                                    Node_5[numNode_5][15] == 3 and pnode[8] == 2 and Node_5[numNode_5][
                                                16] == pnode[9] - 1 and Node_5[numNode_5][17] ==
                                                    pnode[10] + 1) or (
                                                    Node_5[numNode_5][15] == 3 and pnode[8] == 1 and Node_5[numNode_5][
                                                16] == pnode[9] and Node_5[numNode_5][17] ==
                                                    pnode[10] + 1) or (
                                                    Node_5[numNode_5][15] == 4 and pnode[8] == 6 and Node_5[numNode_5][
                                                16] == pnode[9] - 1 and Node_5[numNode_5][17] ==
                                                    pnode[10] - 1) or (
                                                    Node_5[numNode_5][15] == 4 and pnode[8] == 5 and Node_5[numNode_5][
                                                16] == pnode[9] - 1 and Node_5[numNode_5][17] ==
                                                    pnode[10]) or (
                                                    Node_5[numNode_5][15] == 5 and pnode[8] == 4 and Node_5[numNode_5][
                                                16] == pnode[9] + 1 and Node_5[numNode_5][17] ==
                                                    pnode[10]) or (
                                                    Node_5[numNode_5][15] == 5 and pnode[8] == 6 and Node_5[numNode_5][
                                                16] == pnode[9] and Node_5[numNode_5][17] ==
                                                    pnode[10] - 1) or (
                                                    Node_5[numNode_5][15] == 6 and pnode[8] == 4 and Node_5[numNode_5][
                                                16] == pnode[9] + 1 and Node_5[numNode_5][17] ==
                                                    pnode[10] + 1) or (
                                                    Node_5[numNode_5][15] == 6 and pnode[8] == 5 and Node_5[numNode_5][
                                                16] == pnode[9] and Node_5[numNode_5][17] ==
                                                    pnode[10] + 1) or (
                                                    Node_5[numNode_5][15] == 7 and pnode[8] == 9 and Node_5[numNode_5][
                                                16] == pnode[9] - 1 and Node_5[numNode_5][17] ==
                                                    pnode[10] + 1) or (
                                                    Node_5[numNode_5][15] == 7 and pnode[8] == 8 and Node_5[numNode_5][
                                                16] == pnode[9] - 1 and Node_5[numNode_5][17] ==
                                                    pnode[10]) or (
                                                    Node_5[numNode_5][15] == 8 and pnode[8] == 7 and Node_5[numNode_5][
                                                16] == pnode[9] + 1 and Node_5[numNode_5][17] ==
                                                    pnode[10]) or (
                                                    Node_5[numNode_5][15] == 8 and pnode[8] == 9 and Node_5[numNode_5][
                                                16] == pnode[9] and Node_5[numNode_5][17] ==
                                                    pnode[10] + 1) or (
                                                    Node_5[numNode_5][15] == 9 and pnode[8] == 8 and Node_5[numNode_5][
                                                16] == pnode[9] and Node_5[numNode_5][17] ==
                                                    pnode[10] - 1) or (
                                                    Node_5[numNode_5][15] == 9 and pnode[8] == 7 and Node_5[numNode_5][
                                                16] == pnode[9] + 1 and Node_5[numNode_5][17] ==
                                                    pnode[10] - 1) or (
                                                    Node_5[numNode_5][15] == 10 and pnode[8] == 11 and
                                                    Node_5[numNode_5][16] == pnode[9] - 1 and Node_5[numNode_5][17] ==
                                                    pnode[10]) or (
                                                    Node_5[numNode_5][15] == 10 and pnode[8] == 12 and
                                                    Node_5[numNode_5][16] == pnode[9] and Node_5[numNode_5][17] ==
                                                    pnode[10] + 1) or (
                                                    Node_5[numNode_5][15] == 11 and pnode[8] == 12 and
                                                    Node_5[numNode_5][16] == pnode[9] + 1 and Node_5[numNode_5][17] ==
                                                    pnode[10] + 1) or (
                                                    Node_5[numNode_5][15] == 11 and pnode[8] == 10 and
                                                    Node_5[numNode_5][16] == pnode[9] + 1 and Node_5[numNode_5][17] ==
                                                    pnode[10]) or (
                                                    Node_5[numNode_5][15] == 12 and pnode[8] == 11 and
                                                    Node_5[numNode_5][16] == pnode[9] - 1 and Node_5[numNode_5][17] ==
                                                    pnode[10] + 1) or (
                                                    Node_5[numNode_5][15] == 21 and pnode[8] == 22 and
                                                    Node_5[numNode_5][16] == pnode[9] - 1 and Node_5[numNode_5][17] ==
                                                    pnode[10]) or (
                                                    Node_5[numNode_5][15] == 12 and pnode[8] == 10 and
                                                    Node_5[numNode_5][16] == pnode[9] and Node_5[numNode_5][17] ==
                                                    pnode[10] - 1) or (
                                                    Node_5[numNode_5][15] == 22 and pnode[8] == 21 and
                                                    Node_5[numNode_5][16] == pnode[9] + 1 and Node_5[numNode_5][17] ==
                                                    pnode[10]) or (
                                                    Node_5[numNode_5][15] == 23 and pnode[8] == 24 and
                                                    Node_5[numNode_5][16] == pnode[9] and Node_5[numNode_5][17] ==
                                                    pnode[10] - 1) or (
                                                    Node_5[numNode_5][15] == 24 and pnode[8] == 23 and
                                                    Node_5[numNode_5][16] == pnode[9] and Node_5[numNode_5][17] ==
                                                    pnode[10] + 1) or (
                                                    Node_5[numNode_5][15] == 25 and pnode[8] == 26 and
                                                    Node_5[numNode_5][16] == pnode[9] - 1 and Node_5[numNode_5][17] ==
                                                    pnode[10]) or (
                                                    Node_5[numNode_5][15] == 26 and pnode[8] == 25 and
                                                    Node_5[numNode_5][16] == pnode[9] + 1 and Node_5[numNode_5][17] ==
                                                    pnode[10]) or (
                                                    Node_5[numNode_5][15] == 27 and pnode[8] == 28 and
                                                    Node_5[numNode_5][16] == pnode[9] and Node_5[numNode_5][17] ==
                                                    pnode[10] - 1) or (
                                                    Node_5[numNode_5][15] == 28 and pnode[8] == 27 and
                                                    Node_5[numNode_5][16] == pnode[9] and Node_5[numNode_5][17] ==
                                                    pnode[10] + 1) or (
                                                    Node_5[numNode_5][15] == 51 and pnode[8] == 52 and
                                                    Node_5[numNode_5][16] == pnode[9] - 1 and Node_5[numNode_5][17] ==
                                                    pnode[10]) or (
                                                    Node_5[numNode_5][15] == 52 and pnode[8] == 51 and
                                                    Node_5[numNode_5][16] == pnode[9] + 1 and Node_5[numNode_5][17] ==
                                                    pnode[10]) or (
                                                    Node_5[numNode_5][15] == 53 and pnode[8] == 54 and
                                                    Node_5[numNode_5][16] == pnode[9] - 1 and Node_5[numNode_5][17] ==
                                                    pnode[10]) or (
                                                    Node_5[numNode_5][15] == 54 and pnode[8] == 53 and
                                                    Node_5[numNode_5][16] == pnode[9] + 1 and Node_5[numNode_5][17] ==
                                                    pnode[10]) or (
                                                    Node_5[numNode_5][15] == 55 and pnode[8] == 56 and
                                                    Node_5[numNode_5][16] == pnode[9] and Node_5[numNode_5][17] ==
                                                    pnode[10] - 1) or (
                                                    Node_5[numNode_5][15] == 56 and pnode[8] == 55 and
                                                    Node_5[numNode_5][16] == pnode[9] and Node_5[numNode_5][17] ==
                                                    pnode[10] + 1) or (
                                                    Node_5[numNode_5][15] == 57 and pnode[8] == 58 and
                                                    Node_5[numNode_5][16] == pnode[9] and Node_5[numNode_5][17] ==
                                                    pnode[10] - 1) or (
                                                    Node_5[numNode_5][15] == 58 and pnode[8] == 57 and
                                                    Node_5[numNode_5][16] == pnode[9] and Node_5[numNode_5][17] ==
                                                    pnode[10] + 1) or (
                                                    Node_5[numNode_5][15] == 1 and Node_1[pnode[1]][15] == 2 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == 1 and Node_1[pnode[1]][15] == 3 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == 2 and Node_1[pnode[1]][15] == 1 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == 2 and Node_1[pnode[1]][15] == 3 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 3 and Node_1[pnode[1]][15] == 2 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 3 and Node_1[pnode[1]][15] == 1 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_1[pnode[1]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 4 and Node_1[pnode[1]][15] == 6 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 4 and Node_1[pnode[1]][15] == 5 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == 5 and Node_1[pnode[1]][15] == 4 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == 5 and Node_1[pnode[1]][15] == 6 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_1[pnode[1]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 6 and Node_1[pnode[1]][15] == 4 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 6 and Node_1[pnode[1]][15] == 5 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_1[pnode[1]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 7 and Node_1[pnode[1]][15] == 9 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 7 and Node_1[pnode[1]][15] == 8 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == 8 and Node_1[pnode[1]][15] == 7 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == 8 and Node_1[pnode[1]][15] == 9 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_1[pnode[1]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 9 and Node_1[pnode[1]][15] == 8 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_1[pnode[1]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 9 and Node_1[pnode[1]][15] == 7 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 10 and Node_1[pnode[1]][15] == 11 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == 10 and Node_1[pnode[1]][15] == 12 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_1[pnode[1]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 11 and Node_1[pnode[1]][15] == 12 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 11 and Node_1[pnode[1]][15] == 10 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == 12 and Node_1[pnode[1]][15] == 11 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 21 and Node_1[pnode[1]][15] == 22 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == 12 and Node_1[pnode[1]][15] == 10 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_1[pnode[1]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 22 and Node_1[pnode[1]][15] == 21 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == 23 and Node_1[pnode[1]][15] == 24 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_1[pnode[1]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 24 and Node_1[pnode[1]][15] == 23 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_1[pnode[1]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 25 and Node_1[pnode[1]][15] == 26 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == 26 and Node_1[pnode[1]][15] == 25 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == 27 and Node_1[pnode[1]][15] == 28 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_1[pnode[1]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 28 and Node_1[pnode[1]][15] == 27 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_1[pnode[1]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 51 and Node_1[pnode[1]][15] == 52 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == 52 and Node_1[pnode[1]][15] == 51 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == 53 and Node_1[pnode[1]][15] == 54 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == 54 and Node_1[pnode[1]][15] == 53 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_1[pnode[1]][17]) or (
                                                    Node_5[numNode_5][15] == 55 and Node_1[pnode[1]][15] == 56 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_1[pnode[1]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 56 and Node_1[pnode[1]][15] == 55 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_1[pnode[1]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 57 and Node_1[pnode[1]][15] == 58 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_1[pnode[1]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 58 and Node_1[pnode[1]][15] == 57 and
                                                    Node_5[numNode_5][16] == Node_1[pnode[1]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_1[pnode[1]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 1 and Node_2[pnode[2]][15] == 2 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == 1 and Node_2[pnode[2]][15] == 3 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == 2 and Node_2[pnode[2]][15] == 1 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == 2 and Node_2[pnode[2]][15] == 3 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 3 and Node_2[pnode[2]][15] == 2 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 3 and Node_2[pnode[2]][15] == 1 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_2[pnode[2]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 4 and Node_2[pnode[2]][15] == 6 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 4 and Node_2[pnode[2]][15] == 5 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == 5 and Node_2[pnode[2]][15] == 4 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == 5 and Node_2[pnode[2]][15] == 6 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_2[pnode[2]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 6 and Node_2[pnode[2]][15] == 4 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 6 and Node_2[pnode[2]][15] == 5 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_2[pnode[2]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 7 and Node_2[pnode[2]][15] == 9 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 7 and Node_2[pnode[2]][15] == 8 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == 8 and Node_2[pnode[2]][15] == 7 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == 8 and Node_2[pnode[2]][15] == 9 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_2[pnode[2]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 9 and Node_2[pnode[2]][15] == 8 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_2[pnode[2]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 9 and Node_2[pnode[2]][15] == 7 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 10 and Node_2[pnode[2]][15] == 11 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == 10 and Node_2[pnode[2]][15] == 12 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_2[pnode[2]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 11 and Node_2[pnode[2]][15] == 12 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 11 and Node_2[pnode[2]][15] == 10 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == 12 and Node_2[pnode[2]][15] == 11 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 21 and Node_2[pnode[2]][15] == 22 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == 12 and Node_2[pnode[2]][15] == 10 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_2[pnode[2]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 22 and Node_2[pnode[2]][15] == 21 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == 23 and Node_2[pnode[2]][15] == 24 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_2[pnode[2]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 24 and Node_2[pnode[2]][15] == 23 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_2[pnode[2]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 25 and Node_2[pnode[2]][15] == 26 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == 26 and Node_2[pnode[2]][15] == 25 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == 27 and Node_2[pnode[2]][15] == 28 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_2[pnode[2]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 28 and Node_2[pnode[2]][15] == 27 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_2[pnode[2]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 51 and Node_2[pnode[2]][15] == 52 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == 52 and Node_2[pnode[2]][15] == 51 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == 53 and Node_2[pnode[2]][15] == 54 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == 54 and Node_2[pnode[2]][15] == 53 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_2[pnode[2]][17]) or (
                                                    Node_5[numNode_5][15] == 55 and Node_2[pnode[2]][15] == 56 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_2[pnode[2]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 56 and Node_2[pnode[2]][15] == 55 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_2[pnode[2]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 57 and Node_2[pnode[2]][15] == 58 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_2[pnode[2]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 58 and Node_2[pnode[2]][15] == 57 and
                                                    Node_5[numNode_5][16] == Node_2[pnode[2]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_2[pnode[2]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 1 and Node_3[pnode[3]][15] == 2 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == 1 and Node_3[pnode[3]][15] == 3 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == 2 and Node_3[pnode[3]][15] == 1 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == 2 and Node_3[pnode[3]][15] == 3 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 3 and Node_3[pnode[3]][15] == 2 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 3 and Node_3[pnode[3]][15] == 1 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_3[pnode[3]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 4 and Node_3[pnode[3]][15] == 6 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 4 and Node_3[pnode[3]][15] == 5 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == 5 and Node_3[pnode[3]][15] == 4 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == 5 and Node_3[pnode[3]][15] == 6 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_3[pnode[3]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 6 and Node_3[pnode[3]][15] == 4 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 6 and Node_3[pnode[3]][15] == 5 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_3[pnode[3]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 7 and Node_3[pnode[3]][15] == 9 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 7 and Node_3[pnode[3]][15] == 8 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == 8 and Node_3[pnode[3]][15] == 7 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == 8 and Node_3[pnode[3]][15] == 9 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_3[pnode[3]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 9 and Node_3[pnode[3]][15] == 8 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_3[pnode[3]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 9 and Node_3[pnode[3]][15] == 7 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 10 and Node_3[pnode[3]][15] == 11 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == 10 and Node_3[pnode[3]][15] == 12 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_3[pnode[3]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 11 and Node_3[pnode[3]][15] == 12 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 11 and Node_3[pnode[3]][15] == 10 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == 12 and Node_3[pnode[3]][15] == 11 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 21 and Node_3[pnode[3]][15] == 22 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == 12 and Node_3[pnode[3]][15] == 10 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_3[pnode[3]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 22 and Node_3[pnode[3]][15] == 21 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == 23 and Node_3[pnode[3]][15] == 24 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_3[pnode[3]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 24 and Node_3[pnode[3]][15] == 23 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_3[pnode[3]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 25 and Node_3[pnode[3]][15] == 26 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == 26 and Node_3[pnode[3]][15] == 25 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == 27 and Node_3[pnode[3]][15] == 28 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_3[pnode[3]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 28 and Node_3[pnode[3]][15] == 27 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_3[pnode[3]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 51 and Node_3[pnode[3]][15] == 52 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == 52 and Node_3[pnode[3]][15] == 51 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == 53 and Node_3[pnode[3]][15] == 54 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == 54 and Node_3[pnode[3]][15] == 53 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_3[pnode[3]][17]) or (
                                                    Node_5[numNode_5][15] == 55 and Node_3[pnode[3]][15] == 56 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_3[pnode[3]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 56 and Node_3[pnode[3]][15] == 55 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_3[pnode[3]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 57 and Node_3[pnode[3]][15] == 58 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_3[pnode[3]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 58 and Node_3[pnode[3]][15] == 57 and
                                                    Node_5[numNode_5][16] == Node_3[pnode[3]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_3[pnode[3]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 1 and Node_4[pnode[4]][15] == 2 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == 1 and Node_4[pnode[4]][15] == 3 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == 2 and Node_4[pnode[4]][15] == 1 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == 2 and Node_4[pnode[4]][15] == 3 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 3 and Node_4[pnode[4]][15] == 2 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 3 and Node_4[pnode[4]][15] == 1 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_4[pnode[4]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 4 and Node_4[pnode[4]][15] == 6 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 4 and Node_4[pnode[4]][15] == 5 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == 5 and Node_4[pnode[4]][15] == 4 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == 5 and Node_4[pnode[4]][15] == 6 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_4[pnode[4]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 6 and Node_4[pnode[4]][15] == 4 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 6 and Node_4[pnode[4]][15] == 5 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_4[pnode[4]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 7 and Node_4[pnode[4]][15] == 9 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 7 and Node_4[pnode[4]][15] == 8 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == 8 and Node_4[pnode[4]][15] == 7 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == 8 and Node_4[pnode[4]][15] == 9 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_4[pnode[4]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 9 and Node_4[pnode[4]][15] == 8 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_4[pnode[4]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 9 and Node_4[pnode[4]][15] == 7 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 10 and Node_4[pnode[4]][15] == 11 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == 10 and Node_4[pnode[4]][15] == 12 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_4[pnode[4]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 11 and Node_4[pnode[4]][15] == 12 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 11 and Node_4[pnode[4]][15] == 10 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == 12 and Node_4[pnode[4]][15] == 11 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 21 and Node_4[pnode[4]][15] == 22 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == 12 and Node_4[pnode[4]][15] == 10 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_4[pnode[4]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 22 and Node_4[pnode[4]][15] == 21 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == 23 and Node_4[pnode[4]][15] == 24 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_4[pnode[4]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 24 and Node_4[pnode[4]][15] == 23 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_4[pnode[4]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 25 and Node_4[pnode[4]][15] == 26 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == 26 and Node_4[pnode[4]][15] == 25 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == 27 and Node_4[pnode[4]][15] == 28 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_4[pnode[4]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 28 and Node_4[pnode[4]][15] == 27 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_4[pnode[4]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 51 and Node_4[pnode[4]][15] == 52 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == 52 and Node_4[pnode[4]][15] == 51 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == 53 and Node_4[pnode[4]][15] == 54 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == 54 and Node_4[pnode[4]][15] == 53 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_4[pnode[4]][17]) or (
                                                    Node_5[numNode_5][15] == 55 and Node_4[pnode[4]][15] == 56 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_4[pnode[4]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 56 and Node_4[pnode[4]][15] == 55 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_4[pnode[4]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 57 and Node_4[pnode[4]][15] == 58 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_4[pnode[4]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 58 and Node_4[pnode[4]][15] == 57 and
                                                    Node_5[numNode_5][16] == Node_4[pnode[4]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_4[pnode[4]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 1 and Node_5[pnode[5]][15] == 2 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == 1 and Node_5[pnode[5]][15] == 3 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == 2 and Node_5[pnode[5]][15] == 1 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == 2 and Node_5[pnode[5]][15] == 3 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 3 and Node_5[pnode[5]][15] == 2 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 3 and Node_5[pnode[5]][15] == 1 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_5[pnode[5]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 4 and Node_5[pnode[5]][15] == 6 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 4 and Node_5[pnode[5]][15] == 5 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == 5 and Node_5[pnode[5]][15] == 4 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == 5 and Node_5[pnode[5]][15] == 6 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_5[pnode[5]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 6 and Node_5[pnode[5]][15] == 4 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 6 and Node_5[pnode[5]][15] == 5 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_5[pnode[5]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 7 and Node_5[pnode[5]][15] == 9 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 7 and Node_5[pnode[5]][15] == 8 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == 8 and Node_5[pnode[5]][15] == 7 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == 8 and Node_5[pnode[5]][15] == 9 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_5[pnode[5]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 9 and Node_5[pnode[5]][15] == 8 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_5[pnode[5]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 9 and Node_5[pnode[5]][15] == 7 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 10 and Node_5[pnode[5]][15] == 11 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == 10 and Node_5[pnode[5]][15] == 12 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_5[pnode[5]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 11 and Node_5[pnode[5]][15] == 12 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 11 and Node_5[pnode[5]][15] == 10 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == 12 and Node_5[pnode[5]][15] == 11 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 21 and Node_5[pnode[5]][15] == 22 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == 12 and Node_5[pnode[5]][15] == 10 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_5[pnode[5]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 22 and Node_5[pnode[5]][15] == 21 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == 23 and Node_5[pnode[5]][15] == 24 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_5[pnode[5]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 24 and Node_5[pnode[5]][15] == 23 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_5[pnode[5]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 25 and Node_5[pnode[5]][15] == 26 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == 26 and Node_5[pnode[5]][15] == 25 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == 27 and Node_5[pnode[5]][15] == 28 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_5[pnode[5]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 28 and Node_5[pnode[5]][15] == 27 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_5[pnode[5]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 51 and Node_5[pnode[5]][15] == 52 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == 52 and Node_5[pnode[5]][15] == 51 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == 53 and Node_5[pnode[5]][15] == 54 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == 54 and Node_5[pnode[5]][15] == 53 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_5[pnode[5]][17]) or (
                                                    Node_5[numNode_5][15] == 55 and Node_5[pnode[5]][15] == 56 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_5[pnode[5]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 56 and Node_5[pnode[5]][15] == 55 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_5[pnode[5]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 57 and Node_5[pnode[5]][15] == 58 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_5[pnode[5]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 58 and Node_5[pnode[5]][15] == 57 and
                                                    Node_5[numNode_5][16] == Node_5[pnode[5]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_5[pnode[5]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 1 and Node_6[pnode[6]][15] == 2 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 1 and Node_6[pnode[6]][15] == 3 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 2 and Node_6[pnode[6]][15] == 1 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 2 and Node_6[pnode[6]][15] == 3 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 3 and Node_6[pnode[6]][15] == 2 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 3 and Node_6[pnode[6]][15] == 1 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_6[pnode[6]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 4 and Node_6[pnode[6]][15] == 6 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 4 and Node_6[pnode[6]][15] == 5 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 5 and Node_6[pnode[6]][15] == 4 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 5 and Node_6[pnode[6]][15] == 6 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_6[pnode[6]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 6 and Node_6[pnode[6]][15] == 4 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 6 and Node_6[pnode[6]][15] == 5 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_6[pnode[6]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 7 and Node_6[pnode[6]][15] == 9 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 7 and Node_6[pnode[6]][15] == 8 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 8 and Node_6[pnode[6]][15] == 7 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 8 and Node_6[pnode[6]][15] == 9 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_6[pnode[6]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 9 and Node_6[pnode[6]][15] == 8 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_6[pnode[6]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 9 and Node_6[pnode[6]][15] == 7 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 10 and Node_6[pnode[6]][15] == 11 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 10 and Node_6[pnode[6]][15] == 12 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_6[pnode[6]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 11 and Node_6[pnode[6]][15] == 12 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 11 and Node_6[pnode[6]][15] == 10 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 12 and Node_6[pnode[6]][15] == 11 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 21 and Node_6[pnode[6]][15] == 22 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 12 and Node_6[pnode[6]][15] == 10 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_6[pnode[6]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 22 and Node_6[pnode[6]][15] == 21 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 23 and Node_6[pnode[6]][15] == 24 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_6[pnode[6]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 24 and Node_6[pnode[6]][15] == 23 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_6[pnode[6]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 25 and Node_6[pnode[6]][15] == 26 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 26 and Node_6[pnode[6]][15] == 25 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 27 and Node_6[pnode[6]][15] == 28 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_6[pnode[6]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 28 and Node_6[pnode[6]][15] == 27 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_6[pnode[6]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 51 and Node_6[pnode[6]][15] == 52 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 52 and Node_6[pnode[6]][15] == 51 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 53 and Node_6[pnode[6]][15] == 54 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] - 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 54 and Node_6[pnode[6]][15] == 53 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] + 1 and
                                                    Node_5[numNode_5][17] ==
                                                    Node_6[pnode[6]][17]) or (
                                                    Node_5[numNode_5][15] == 55 and Node_6[pnode[6]][15] == 56 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_6[pnode[6]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 56 and Node_6[pnode[6]][15] == 55 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_6[pnode[6]][17] + 1) or (
                                                    Node_5[numNode_5][15] == 57 and Node_6[pnode[6]][15] == 58 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_6[pnode[6]][17] - 1) or (
                                                    Node_5[numNode_5][15] == 58 and Node_6[pnode[6]][15] == 57 and
                                                    Node_5[numNode_5][16] == Node_6[pnode[6]][16] and Node_5[numNode_5][
                                                        17] ==
                                                    Node_6[pnode[6]][17] + 1)):
                                                if ((Node_3[numNode_3][15] == pnode[8] and Node_3[numNode_3][16] ==
                                                     pnode[9] and Node_3[numNode_3][17] == pnode[10]) or (
                                                        Node_3[numNode_3][15] == Node_1[pnode[1]][15] and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == Node_2[pnode[2]][15] and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == Node_3[pnode[3]][15] and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == Node_4[pnode[4]][15] and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == Node_5[pnode[5]][15] and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == Node_6[pnode[6]][15] and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 1 and pnode[8] == 2 and
                                                        Node_3[numNode_3][16] == pnode[9] - 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10]) or (
                                                        Node_3[numNode_3][15] == 1 and pnode[8] == 3 and
                                                        Node_3[numNode_3][16] == pnode[9] and Node_3[numNode_3][17] ==
                                                        pnode[10] - 1) or (
                                                        Node_3[numNode_3][15] == 2 and pnode[8] == 1 and
                                                        Node_3[numNode_3][16] == pnode[9] + 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10]) or (
                                                        Node_3[numNode_3][15] == 2 and pnode[8] == 3 and
                                                        Node_3[numNode_3][16] == pnode[9] + 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10] - 1) or (
                                                        Node_3[numNode_3][15] == 3 and pnode[8] == 2 and
                                                        Node_3[numNode_3][16] == pnode[9] - 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10] + 1) or (
                                                        Node_3[numNode_3][15] == 3 and pnode[8] == 1 and
                                                        Node_3[numNode_3][16] == pnode[9] and Node_3[numNode_3][17] ==
                                                        pnode[10] + 1) or (
                                                        Node_3[numNode_3][15] == 4 and pnode[8] == 6 and
                                                        Node_3[numNode_3][16] == pnode[9] - 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10] - 1) or (
                                                        Node_3[numNode_3][15] == 4 and pnode[8] == 5 and
                                                        Node_3[numNode_3][16] == pnode[9] - 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10]) or (
                                                        Node_3[numNode_3][15] == 5 and pnode[8] == 4 and
                                                        Node_3[numNode_3][16] == pnode[9] + 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10]) or (
                                                        Node_3[numNode_3][15] == 5 and pnode[8] == 6 and
                                                        Node_3[numNode_3][16] == pnode[9] and Node_3[numNode_3][17] ==
                                                        pnode[10] - 1) or (
                                                        Node_3[numNode_3][15] == 6 and pnode[8] == 4 and
                                                        Node_3[numNode_3][16] == pnode[9] + 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10] + 1) or (
                                                        Node_3[numNode_3][15] == 6 and pnode[8] == 5 and
                                                        Node_3[numNode_3][16] == pnode[9] and Node_3[numNode_3][17] ==
                                                        pnode[10] + 1) or (
                                                        Node_3[numNode_3][15] == 7 and pnode[8] == 9 and
                                                        Node_3[numNode_3][16] == pnode[9] - 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10] + 1) or (
                                                        Node_3[numNode_3][15] == 7 and pnode[8] == 8 and
                                                        Node_3[numNode_3][16] == pnode[9] - 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10]) or (
                                                        Node_3[numNode_3][15] == 8 and pnode[8] == 7 and
                                                        Node_3[numNode_3][16] == pnode[9] + 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10]) or (
                                                        Node_3[numNode_3][15] == 8 and pnode[8] == 9 and
                                                        Node_3[numNode_3][16] == pnode[9] and Node_3[numNode_3][17] ==
                                                        pnode[10] + 1) or (
                                                        Node_3[numNode_3][15] == 9 and pnode[8] == 8 and
                                                        Node_3[numNode_3][16] == pnode[9] and Node_3[numNode_3][17] ==
                                                        pnode[10] - 1) or (
                                                        Node_3[numNode_3][15] == 9 and pnode[8] == 7 and
                                                        Node_3[numNode_3][16] == pnode[9] + 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10] - 1) or (
                                                        Node_3[numNode_3][15] == 10 and pnode[8] == 11 and
                                                        Node_3[numNode_3][16] == pnode[9] - 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10]) or (
                                                        Node_3[numNode_3][15] == 10 and pnode[8] == 12 and
                                                        Node_3[numNode_3][16] == pnode[9] and Node_3[numNode_3][17] ==
                                                        pnode[10] + 1) or (
                                                        Node_3[numNode_3][15] == 11 and pnode[8] == 12 and
                                                        Node_3[numNode_3][16] == pnode[9] + 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10] + 1) or (
                                                        Node_3[numNode_3][15] == 11 and pnode[8] == 10 and
                                                        Node_3[numNode_3][16] == pnode[9] + 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10]) or (
                                                        Node_3[numNode_3][15] == 12 and pnode[8] == 11 and
                                                        Node_3[numNode_3][16] == pnode[9] - 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10] + 1) or (
                                                        Node_3[numNode_3][15] == 21 and pnode[8] == 22 and
                                                        Node_3[numNode_3][16] == pnode[9] - 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10]) or (
                                                        Node_3[numNode_3][15] == 12 and pnode[8] == 10 and
                                                        Node_3[numNode_3][16] == pnode[9] and Node_3[numNode_3][17] ==
                                                        pnode[10] - 1) or (
                                                        Node_3[numNode_3][15] == 22 and pnode[8] == 21 and
                                                        Node_3[numNode_3][16] == pnode[9] + 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10]) or (
                                                        Node_3[numNode_3][15] == 23 and pnode[8] == 24 and
                                                        Node_3[numNode_3][16] == pnode[9] and Node_3[numNode_3][17] ==
                                                        pnode[10] - 1) or (
                                                        Node_3[numNode_3][15] == 24 and pnode[8] == 23 and
                                                        Node_3[numNode_3][16] == pnode[9] and Node_3[numNode_3][17] ==
                                                        pnode[10] + 1) or (
                                                        Node_3[numNode_3][15] == 25 and pnode[8] == 26 and
                                                        Node_3[numNode_3][16] == pnode[9] - 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10]) or (
                                                        Node_3[numNode_3][15] == 26 and pnode[8] == 25 and
                                                        Node_3[numNode_3][16] == pnode[9] + 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10]) or (
                                                        Node_3[numNode_3][15] == 27 and pnode[8] == 28 and
                                                        Node_3[numNode_3][16] == pnode[9] and Node_3[numNode_3][17] ==
                                                        pnode[10] - 1) or (
                                                        Node_3[numNode_3][15] == 28 and pnode[8] == 27 and
                                                        Node_3[numNode_3][16] == pnode[9] and Node_3[numNode_3][17] ==
                                                        pnode[10] + 1) or (
                                                        Node_3[numNode_3][15] == 51 and pnode[8] == 52 and
                                                        Node_3[numNode_3][16] == pnode[9] - 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10]) or (
                                                        Node_3[numNode_3][15] == 52 and pnode[8] == 51 and
                                                        Node_3[numNode_3][16] == pnode[9] + 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10]) or (
                                                        Node_3[numNode_3][15] == 53 and pnode[8] == 54 and
                                                        Node_3[numNode_3][16] == pnode[9] - 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10]) or (
                                                        Node_3[numNode_3][15] == 54 and pnode[8] == 53 and
                                                        Node_3[numNode_3][16] == pnode[9] + 1 and Node_3[numNode_3][
                                                            17] ==
                                                        pnode[10]) or (
                                                        Node_3[numNode_3][15] == 55 and pnode[8] == 56 and
                                                        Node_3[numNode_3][16] == pnode[9] and Node_3[numNode_3][17] ==
                                                        pnode[10] - 1) or (
                                                        Node_3[numNode_3][15] == 56 and pnode[8] == 55 and
                                                        Node_3[numNode_3][16] == pnode[9] and Node_3[numNode_3][17] ==
                                                        pnode[10] + 1) or (
                                                        Node_3[numNode_3][15] == 57 and pnode[8] == 58 and
                                                        Node_3[numNode_3][16] == pnode[9] and Node_3[numNode_3][17] ==
                                                        pnode[10] - 1) or (
                                                        Node_3[numNode_3][15] == 58 and pnode[8] == 57 and
                                                        Node_3[numNode_3][16] == pnode[9] and Node_3[numNode_3][17] ==
                                                        pnode[10] + 1) or (
                                                        Node_3[numNode_3][15] == 1 and Node_1[pnode[1]][15] == 2 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == 1 and Node_1[pnode[1]][15] == 3 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == 2 and Node_1[pnode[1]][15] == 1 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == 2 and Node_1[pnode[1]][15] == 3 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 3 and Node_1[pnode[1]][15] == 2 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 3 and Node_1[pnode[1]][15] == 1 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 4 and Node_1[pnode[1]][15] == 6 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 4 and Node_1[pnode[1]][15] == 5 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == 5 and Node_1[pnode[1]][15] == 4 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == 5 and Node_1[pnode[1]][15] == 6 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 6 and Node_1[pnode[1]][15] == 4 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 6 and Node_1[pnode[1]][15] == 5 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 7 and Node_1[pnode[1]][15] == 9 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 7 and Node_1[pnode[1]][15] == 8 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == 8 and Node_1[pnode[1]][15] == 7 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == 8 and Node_1[pnode[1]][15] == 9 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 9 and Node_1[pnode[1]][15] == 8 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 9 and Node_1[pnode[1]][15] == 7 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 10 and Node_1[pnode[1]][15] == 11 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == 10 and Node_1[pnode[1]][15] == 12 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 11 and Node_1[pnode[1]][15] == 12 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 11 and Node_1[pnode[1]][15] == 10 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == 12 and Node_1[pnode[1]][15] == 11 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 21 and Node_1[pnode[1]][15] == 22 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == 12 and Node_1[pnode[1]][15] == 10 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 22 and Node_1[pnode[1]][15] == 21 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == 23 and Node_1[pnode[1]][15] == 24 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 24 and Node_1[pnode[1]][15] == 23 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 25 and Node_1[pnode[1]][15] == 26 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == 26 and Node_1[pnode[1]][15] == 25 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == 27 and Node_1[pnode[1]][15] == 28 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 28 and Node_1[pnode[1]][15] == 27 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 51 and Node_1[pnode[1]][15] == 52 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == 52 and Node_1[pnode[1]][15] == 51 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == 53 and Node_1[pnode[1]][15] == 54 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == 54 and Node_1[pnode[1]][15] == 53 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17]) or (
                                                        Node_3[numNode_3][15] == 55 and Node_1[pnode[1]][15] == 56 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 56 and Node_1[pnode[1]][15] == 55 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 57 and Node_1[pnode[1]][15] == 58 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 58 and Node_1[pnode[1]][15] == 57 and
                                                        Node_3[numNode_3][16] == Node_1[pnode[1]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_1[pnode[1]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 1 and Node_2[pnode[2]][15] == 2 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == 1 and Node_2[pnode[2]][15] == 3 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == 2 and Node_2[pnode[2]][15] == 1 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == 2 and Node_2[pnode[2]][15] == 3 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 3 and Node_2[pnode[2]][15] == 2 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 3 and Node_2[pnode[2]][15] == 1 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 4 and Node_2[pnode[2]][15] == 6 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 4 and Node_2[pnode[2]][15] == 5 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == 5 and Node_2[pnode[2]][15] == 4 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == 5 and Node_2[pnode[2]][15] == 6 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 6 and Node_2[pnode[2]][15] == 4 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 6 and Node_2[pnode[2]][15] == 5 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 7 and Node_2[pnode[2]][15] == 9 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 7 and Node_2[pnode[2]][15] == 8 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == 8 and Node_2[pnode[2]][15] == 7 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == 8 and Node_2[pnode[2]][15] == 9 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 9 and Node_2[pnode[2]][15] == 8 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 9 and Node_2[pnode[2]][15] == 7 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 10 and Node_2[pnode[2]][15] == 11 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == 10 and Node_2[pnode[2]][15] == 12 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 11 and Node_2[pnode[2]][15] == 12 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 11 and Node_2[pnode[2]][15] == 10 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == 12 and Node_2[pnode[2]][15] == 11 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 21 and Node_2[pnode[2]][15] == 22 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == 12 and Node_2[pnode[2]][15] == 10 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 22 and Node_2[pnode[2]][15] == 21 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == 23 and Node_2[pnode[2]][15] == 24 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 24 and Node_2[pnode[2]][15] == 23 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 25 and Node_2[pnode[2]][15] == 26 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == 26 and Node_2[pnode[2]][15] == 25 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == 27 and Node_2[pnode[2]][15] == 28 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 28 and Node_2[pnode[2]][15] == 27 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 51 and Node_2[pnode[2]][15] == 52 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == 52 and Node_2[pnode[2]][15] == 51 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == 53 and Node_2[pnode[2]][15] == 54 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == 54 and Node_2[pnode[2]][15] == 53 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17]) or (
                                                        Node_3[numNode_3][15] == 55 and Node_2[pnode[2]][15] == 56 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 56 and Node_2[pnode[2]][15] == 55 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 57 and Node_2[pnode[2]][15] == 58 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 58 and Node_2[pnode[2]][15] == 57 and
                                                        Node_3[numNode_3][16] == Node_2[pnode[2]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_2[pnode[2]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 1 and Node_3[pnode[3]][15] == 2 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == 1 and Node_3[pnode[3]][15] == 3 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == 2 and Node_3[pnode[3]][15] == 1 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == 2 and Node_3[pnode[3]][15] == 3 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 3 and Node_3[pnode[3]][15] == 2 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 3 and Node_3[pnode[3]][15] == 1 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 4 and Node_3[pnode[3]][15] == 6 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 4 and Node_3[pnode[3]][15] == 5 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == 5 and Node_3[pnode[3]][15] == 4 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == 5 and Node_3[pnode[3]][15] == 6 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 6 and Node_3[pnode[3]][15] == 4 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 6 and Node_3[pnode[3]][15] == 5 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 7 and Node_3[pnode[3]][15] == 9 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 7 and Node_3[pnode[3]][15] == 8 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == 8 and Node_3[pnode[3]][15] == 7 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == 8 and Node_3[pnode[3]][15] == 9 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 9 and Node_3[pnode[3]][15] == 8 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 9 and Node_3[pnode[3]][15] == 7 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 10 and Node_3[pnode[3]][15] == 11 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == 10 and Node_3[pnode[3]][15] == 12 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 11 and Node_3[pnode[3]][15] == 12 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 11 and Node_3[pnode[3]][15] == 10 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == 12 and Node_3[pnode[3]][15] == 11 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 21 and Node_3[pnode[3]][15] == 22 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == 12 and Node_3[pnode[3]][15] == 10 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 22 and Node_3[pnode[3]][15] == 21 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == 23 and Node_3[pnode[3]][15] == 24 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 24 and Node_3[pnode[3]][15] == 23 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 25 and Node_3[pnode[3]][15] == 26 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == 26 and Node_3[pnode[3]][15] == 25 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == 27 and Node_3[pnode[3]][15] == 28 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 28 and Node_3[pnode[3]][15] == 27 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 51 and Node_3[pnode[3]][15] == 52 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == 52 and Node_3[pnode[3]][15] == 51 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == 53 and Node_3[pnode[3]][15] == 54 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == 54 and Node_3[pnode[3]][15] == 53 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17]) or (
                                                        Node_3[numNode_3][15] == 55 and Node_3[pnode[3]][15] == 56 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 56 and Node_3[pnode[3]][15] == 55 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 57 and Node_3[pnode[3]][15] == 58 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 58 and Node_3[pnode[3]][15] == 57 and
                                                        Node_3[numNode_3][16] == Node_3[pnode[3]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_3[pnode[3]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 1 and Node_4[pnode[4]][15] == 2 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == 1 and Node_4[pnode[4]][15] == 3 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == 2 and Node_4[pnode[4]][15] == 1 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == 2 and Node_4[pnode[4]][15] == 3 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 3 and Node_4[pnode[4]][15] == 2 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 3 and Node_4[pnode[4]][15] == 1 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 4 and Node_4[pnode[4]][15] == 6 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 4 and Node_4[pnode[4]][15] == 5 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == 5 and Node_4[pnode[4]][15] == 4 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == 5 and Node_4[pnode[4]][15] == 6 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 6 and Node_4[pnode[4]][15] == 4 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 6 and Node_4[pnode[4]][15] == 5 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 7 and Node_4[pnode[4]][15] == 9 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 7 and Node_4[pnode[4]][15] == 8 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == 8 and Node_4[pnode[4]][15] == 7 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == 8 and Node_4[pnode[4]][15] == 9 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 9 and Node_4[pnode[4]][15] == 8 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 9 and Node_4[pnode[4]][15] == 7 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 10 and Node_4[pnode[4]][15] == 11 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == 10 and Node_4[pnode[4]][15] == 12 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 11 and Node_4[pnode[4]][15] == 12 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 11 and Node_4[pnode[4]][15] == 10 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == 12 and Node_4[pnode[4]][15] == 11 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 21 and Node_4[pnode[4]][15] == 22 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == 12 and Node_4[pnode[4]][15] == 10 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 22 and Node_4[pnode[4]][15] == 21 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == 23 and Node_4[pnode[4]][15] == 24 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 24 and Node_4[pnode[4]][15] == 23 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 25 and Node_4[pnode[4]][15] == 26 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == 26 and Node_4[pnode[4]][15] == 25 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == 27 and Node_4[pnode[4]][15] == 28 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 28 and Node_4[pnode[4]][15] == 27 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 51 and Node_4[pnode[4]][15] == 52 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == 52 and Node_4[pnode[4]][15] == 51 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == 53 and Node_4[pnode[4]][15] == 54 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == 54 and Node_4[pnode[4]][15] == 53 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17]) or (
                                                        Node_3[numNode_3][15] == 55 and Node_4[pnode[4]][15] == 56 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 56 and Node_4[pnode[4]][15] == 55 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 57 and Node_4[pnode[4]][15] == 58 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 58 and Node_4[pnode[4]][15] == 57 and
                                                        Node_3[numNode_3][16] == Node_4[pnode[4]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_4[pnode[4]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 1 and Node_5[pnode[5]][15] == 2 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == 1 and Node_5[pnode[5]][15] == 3 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == 2 and Node_5[pnode[5]][15] == 1 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == 2 and Node_5[pnode[5]][15] == 3 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 3 and Node_5[pnode[5]][15] == 2 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 3 and Node_5[pnode[5]][15] == 1 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 4 and Node_5[pnode[5]][15] == 6 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 4 and Node_5[pnode[5]][15] == 5 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == 5 and Node_5[pnode[5]][15] == 4 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == 5 and Node_5[pnode[5]][15] == 6 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 6 and Node_5[pnode[5]][15] == 4 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 6 and Node_5[pnode[5]][15] == 5 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 7 and Node_5[pnode[5]][15] == 9 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 7 and Node_5[pnode[5]][15] == 8 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == 8 and Node_5[pnode[5]][15] == 7 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == 8 and Node_5[pnode[5]][15] == 9 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 9 and Node_5[pnode[5]][15] == 8 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 9 and Node_5[pnode[5]][15] == 7 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 10 and Node_5[pnode[5]][15] == 11 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == 10 and Node_5[pnode[5]][15] == 12 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 11 and Node_5[pnode[5]][15] == 12 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 11 and Node_5[pnode[5]][15] == 10 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == 12 and Node_5[pnode[5]][15] == 11 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 21 and Node_5[pnode[5]][15] == 22 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == 12 and Node_5[pnode[5]][15] == 10 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 22 and Node_5[pnode[5]][15] == 21 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == 23 and Node_5[pnode[5]][15] == 24 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 24 and Node_5[pnode[5]][15] == 23 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 25 and Node_5[pnode[5]][15] == 26 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == 26 and Node_5[pnode[5]][15] == 25 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == 27 and Node_5[pnode[5]][15] == 28 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 28 and Node_5[pnode[5]][15] == 27 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 51 and Node_5[pnode[5]][15] == 52 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == 52 and Node_5[pnode[5]][15] == 51 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == 53 and Node_5[pnode[5]][15] == 54 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == 54 and Node_5[pnode[5]][15] == 53 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17]) or (
                                                        Node_3[numNode_3][15] == 55 and Node_5[pnode[5]][15] == 56 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 56 and Node_5[pnode[5]][15] == 55 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 57 and Node_5[pnode[5]][15] == 58 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 58 and Node_5[pnode[5]][15] == 57 and
                                                        Node_3[numNode_3][16] == Node_5[pnode[5]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_5[pnode[5]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 1 and Node_6[pnode[6]][15] == 2 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 1 and Node_6[pnode[6]][15] == 3 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 2 and Node_6[pnode[6]][15] == 1 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 2 and Node_6[pnode[6]][15] == 3 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 3 and Node_6[pnode[6]][15] == 2 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 3 and Node_6[pnode[6]][15] == 1 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 4 and Node_6[pnode[6]][15] == 6 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 4 and Node_6[pnode[6]][15] == 5 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 5 and Node_6[pnode[6]][15] == 4 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 5 and Node_6[pnode[6]][15] == 6 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 6 and Node_6[pnode[6]][15] == 4 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 6 and Node_6[pnode[6]][15] == 5 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 7 and Node_6[pnode[6]][15] == 9 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 7 and Node_6[pnode[6]][15] == 8 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 8 and Node_6[pnode[6]][15] == 7 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 8 and Node_6[pnode[6]][15] == 9 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 9 and Node_6[pnode[6]][15] == 8 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 9 and Node_6[pnode[6]][15] == 7 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 10 and Node_6[pnode[6]][15] == 11 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 10 and Node_6[pnode[6]][15] == 12 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 11 and Node_6[pnode[6]][15] == 12 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 11 and Node_6[pnode[6]][15] == 10 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 12 and Node_6[pnode[6]][15] == 11 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 21 and Node_6[pnode[6]][15] == 22 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 12 and Node_6[pnode[6]][15] == 10 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 22 and Node_6[pnode[6]][15] == 21 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 23 and Node_6[pnode[6]][15] == 24 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 24 and Node_6[pnode[6]][15] == 23 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 25 and Node_6[pnode[6]][15] == 26 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 26 and Node_6[pnode[6]][15] == 25 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 27 and Node_6[pnode[6]][15] == 28 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 28 and Node_6[pnode[6]][15] == 27 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 51 and Node_6[pnode[6]][15] == 52 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 52 and Node_6[pnode[6]][15] == 51 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 53 and Node_6[pnode[6]][15] == 54 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] - 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 54 and Node_6[pnode[6]][15] == 53 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] + 1 and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17]) or (
                                                        Node_3[numNode_3][15] == 55 and Node_6[pnode[6]][15] == 56 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 56 and Node_6[pnode[6]][15] == 55 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] + 1) or (
                                                        Node_3[numNode_3][15] == 57 and Node_6[pnode[6]][15] == 58 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] - 1) or (
                                                        Node_3[numNode_3][15] == 58 and Node_6[pnode[6]][15] == 57 and
                                                        Node_3[numNode_3][16] == Node_6[pnode[6]][16] and
                                                        Node_3[numNode_3][17] ==
                                                        Node_6[pnode[6]][17] + 1)):
                                                    if ((Node_1[numNode_1][15] == pnode[8] and Node_1[numNode_1][16] ==
                                                         pnode[9] and Node_1[numNode_1][17] == pnode[10]) or (
                                                            Node_1[numNode_1][15] == Node_1[pnode[1]][15] and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == Node_2[pnode[2]][15] and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == Node_3[pnode[3]][15] and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == Node_4[pnode[4]][15] and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == Node_5[pnode[5]][15] and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == Node_6[pnode[6]][15] and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 1 and pnode[8] == 2 and
                                                            Node_1[numNode_1][16] == pnode[9] - 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10]) or (
                                                            Node_1[numNode_1][15] == 1 and pnode[8] == 3 and
                                                            Node_1[numNode_1][16] == pnode[9] and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] - 1) or (
                                                            Node_1[numNode_1][15] == 2 and pnode[8] == 1 and
                                                            Node_1[numNode_1][16] == pnode[9] + 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10]) or (
                                                            Node_1[numNode_1][15] == 2 and pnode[8] == 3 and
                                                            Node_1[numNode_1][16] == pnode[9] + 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] - 1) or (
                                                            Node_1[numNode_1][15] == 3 and pnode[8] == 2 and
                                                            Node_1[numNode_1][16] == pnode[9] - 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] + 1) or (
                                                            Node_1[numNode_1][15] == 3 and pnode[8] == 1 and
                                                            Node_1[numNode_1][16] == pnode[9] and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] + 1) or (
                                                            Node_1[numNode_1][15] == 4 and pnode[8] == 6 and
                                                            Node_1[numNode_1][16] == pnode[9] - 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] - 1) or (
                                                            Node_1[numNode_1][15] == 4 and pnode[8] == 5 and
                                                            Node_1[numNode_1][16] == pnode[9] - 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10]) or (
                                                            Node_1[numNode_1][15] == 5 and pnode[8] == 4 and
                                                            Node_1[numNode_1][16] == pnode[9] + 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10]) or (
                                                            Node_1[numNode_1][15] == 5 and pnode[8] == 6 and
                                                            Node_1[numNode_1][16] == pnode[9] and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] - 1) or (
                                                            Node_1[numNode_1][15] == 6 and pnode[8] == 4 and
                                                            Node_1[numNode_1][16] == pnode[9] + 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] + 1) or (
                                                            Node_1[numNode_1][15] == 6 and pnode[8] == 5 and
                                                            Node_1[numNode_1][16] == pnode[9] and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] + 1) or (
                                                            Node_1[numNode_1][15] == 7 and pnode[8] == 9 and
                                                            Node_1[numNode_1][16] == pnode[9] - 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] + 1) or (
                                                            Node_1[numNode_1][15] == 7 and pnode[8] == 8 and
                                                            Node_1[numNode_1][16] == pnode[9] - 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10]) or (
                                                            Node_1[numNode_1][15] == 8 and pnode[8] == 7 and
                                                            Node_1[numNode_1][16] == pnode[9] + 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10]) or (
                                                            Node_1[numNode_1][15] == 8 and pnode[8] == 9 and
                                                            Node_1[numNode_1][16] == pnode[9] and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] + 1) or (
                                                            Node_1[numNode_1][15] == 9 and pnode[8] == 8 and
                                                            Node_1[numNode_1][16] == pnode[9] and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] - 1) or (
                                                            Node_1[numNode_1][15] == 9 and pnode[8] == 7 and
                                                            Node_1[numNode_1][16] == pnode[9] + 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] - 1) or (
                                                            Node_1[numNode_1][15] == 10 and pnode[8] == 11 and
                                                            Node_1[numNode_1][16] == pnode[9] - 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10]) or (
                                                            Node_1[numNode_1][15] == 10 and pnode[8] == 12 and
                                                            Node_1[numNode_1][16] == pnode[9] and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] + 1) or (
                                                            Node_1[numNode_1][15] == 11 and pnode[8] == 12 and
                                                            Node_1[numNode_1][16] == pnode[9] + 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] + 1) or (
                                                            Node_1[numNode_1][15] == 11 and pnode[8] == 10 and
                                                            Node_1[numNode_1][16] == pnode[9] + 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10]) or (
                                                            Node_1[numNode_1][15] == 12 and pnode[8] == 11 and
                                                            Node_1[numNode_1][16] == pnode[9] - 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] + 1) or (
                                                            Node_1[numNode_1][15] == 21 and pnode[8] == 22 and
                                                            Node_1[numNode_1][16] == pnode[9] - 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10]) or (
                                                            Node_1[numNode_1][15] == 12 and pnode[8] == 10 and
                                                            Node_1[numNode_1][16] == pnode[9] and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] - 1) or (
                                                            Node_1[numNode_1][15] == 22 and pnode[8] == 21 and
                                                            Node_1[numNode_1][16] == pnode[9] + 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10]) or (
                                                            Node_1[numNode_1][15] == 23 and pnode[8] == 24 and
                                                            Node_1[numNode_1][16] == pnode[9] and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] - 1) or (
                                                            Node_1[numNode_1][15] == 24 and pnode[8] == 23 and
                                                            Node_1[numNode_1][16] == pnode[9] and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] + 1) or (
                                                            Node_1[numNode_1][15] == 25 and pnode[8] == 26 and
                                                            Node_1[numNode_1][16] == pnode[9] - 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10]) or (
                                                            Node_1[numNode_1][15] == 26 and pnode[8] == 25 and
                                                            Node_1[numNode_1][16] == pnode[9] + 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10]) or (
                                                            Node_1[numNode_1][15] == 27 and pnode[8] == 28 and
                                                            Node_1[numNode_1][16] == pnode[9] and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] - 1) or (
                                                            Node_1[numNode_1][15] == 28 and pnode[8] == 27 and
                                                            Node_1[numNode_1][16] == pnode[9] and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] + 1) or (
                                                            Node_1[numNode_1][15] == 51 and pnode[8] == 52 and
                                                            Node_1[numNode_1][16] == pnode[9] - 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10]) or (
                                                            Node_1[numNode_1][15] == 52 and pnode[8] == 51 and
                                                            Node_1[numNode_1][16] == pnode[9] + 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10]) or (
                                                            Node_1[numNode_1][15] == 53 and pnode[8] == 54 and
                                                            Node_1[numNode_1][16] == pnode[9] - 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10]) or (
                                                            Node_1[numNode_1][15] == 54 and pnode[8] == 53 and
                                                            Node_1[numNode_1][16] == pnode[9] + 1 and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10]) or (
                                                            Node_1[numNode_1][15] == 55 and pnode[8] == 56 and
                                                            Node_1[numNode_1][16] == pnode[9] and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] - 1) or (
                                                            Node_1[numNode_1][15] == 56 and pnode[8] == 55 and
                                                            Node_1[numNode_1][16] == pnode[9] and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] + 1) or (
                                                            Node_1[numNode_1][15] == 57 and pnode[8] == 58 and
                                                            Node_1[numNode_1][16] == pnode[9] and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] - 1) or (
                                                            Node_1[numNode_1][15] == 58 and pnode[8] == 57 and
                                                            Node_1[numNode_1][16] == pnode[9] and Node_1[numNode_1][
                                                                17] ==
                                                            pnode[10] + 1) or (
                                                            Node_1[numNode_1][15] == 1 and Node_1[pnode[1]][15] == 2 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == 1 and Node_1[pnode[1]][15] == 3 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == 2 and Node_1[pnode[1]][15] == 1 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == 2 and Node_1[pnode[1]][15] == 3 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 3 and Node_1[pnode[1]][15] == 2 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 3 and Node_1[pnode[1]][15] == 1 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 4 and Node_1[pnode[1]][15] == 6 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 4 and Node_1[pnode[1]][15] == 5 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == 5 and Node_1[pnode[1]][15] == 4 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == 5 and Node_1[pnode[1]][15] == 6 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 6 and Node_1[pnode[1]][15] == 4 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 6 and Node_1[pnode[1]][15] == 5 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 7 and Node_1[pnode[1]][15] == 9 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 7 and Node_1[pnode[1]][15] == 8 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == 8 and Node_1[pnode[1]][15] == 7 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == 8 and Node_1[pnode[1]][15] == 9 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 9 and Node_1[pnode[1]][15] == 8 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 9 and Node_1[pnode[1]][15] == 7 and
                                                            Node_1[numNode_1][16] == Node_1[pnode[1]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 10 and Node_1[pnode[1]][
                                                        15] == 11 and Node_1[numNode_1][16] == Node_1[pnode[1]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == 10 and Node_1[pnode[1]][
                                                        15] == 12 and Node_1[numNode_1][16] == Node_1[pnode[1]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 11 and Node_1[pnode[1]][
                                                        15] == 12 and Node_1[numNode_1][16] == Node_1[pnode[1]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 11 and Node_1[pnode[1]][
                                                        15] == 10 and Node_1[numNode_1][16] == Node_1[pnode[1]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == 12 and Node_1[pnode[1]][
                                                        15] == 11 and Node_1[numNode_1][16] == Node_1[pnode[1]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 21 and Node_1[pnode[1]][
                                                        15] == 22 and Node_1[numNode_1][16] == Node_1[pnode[1]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == 12 and Node_1[pnode[1]][
                                                        15] == 10 and Node_1[numNode_1][16] == Node_1[pnode[1]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 22 and Node_1[pnode[1]][
                                                        15] == 21 and Node_1[numNode_1][16] == Node_1[pnode[1]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == 23 and Node_1[pnode[1]][
                                                        15] == 24 and Node_1[numNode_1][16] == Node_1[pnode[1]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 24 and Node_1[pnode[1]][
                                                        15] == 23 and Node_1[numNode_1][16] == Node_1[pnode[1]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 25 and Node_1[pnode[1]][
                                                        15] == 26 and Node_1[numNode_1][16] == Node_1[pnode[1]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == 26 and Node_1[pnode[1]][
                                                        15] == 25 and Node_1[numNode_1][16] == Node_1[pnode[1]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == 27 and Node_1[pnode[1]][
                                                        15] == 28 and Node_1[numNode_1][16] == Node_1[pnode[1]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 28 and Node_1[pnode[1]][
                                                        15] == 27 and Node_1[numNode_1][16] == Node_1[pnode[1]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 51 and Node_1[pnode[1]][
                                                        15] == 52 and Node_1[numNode_1][16] == Node_1[pnode[1]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == 52 and Node_1[pnode[1]][
                                                        15] == 51 and Node_1[numNode_1][16] == Node_1[pnode[1]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == 53 and Node_1[pnode[1]][
                                                        15] == 54 and Node_1[numNode_1][16] == Node_1[pnode[1]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == 54 and Node_1[pnode[1]][
                                                        15] == 53 and Node_1[numNode_1][16] == Node_1[pnode[1]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17]) or (
                                                            Node_1[numNode_1][15] == 55 and Node_1[pnode[1]][
                                                        15] == 56 and Node_1[numNode_1][16] == Node_1[pnode[1]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 56 and Node_1[pnode[1]][
                                                        15] == 55 and Node_1[numNode_1][16] == Node_1[pnode[1]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 57 and Node_1[pnode[1]][
                                                        15] == 58 and Node_1[numNode_1][16] == Node_1[pnode[1]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 58 and Node_1[pnode[1]][
                                                        15] == 57 and Node_1[numNode_1][16] == Node_1[pnode[1]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_1[pnode[1]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 1 and Node_2[pnode[2]][15] == 2 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == 1 and Node_2[pnode[2]][15] == 3 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == 2 and Node_2[pnode[2]][15] == 1 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == 2 and Node_2[pnode[2]][15] == 3 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 3 and Node_2[pnode[2]][15] == 2 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 3 and Node_2[pnode[2]][15] == 1 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 4 and Node_2[pnode[2]][15] == 6 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 4 and Node_2[pnode[2]][15] == 5 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == 5 and Node_2[pnode[2]][15] == 4 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == 5 and Node_2[pnode[2]][15] == 6 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 6 and Node_2[pnode[2]][15] == 4 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 6 and Node_2[pnode[2]][15] == 5 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 7 and Node_2[pnode[2]][15] == 9 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 7 and Node_2[pnode[2]][15] == 8 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == 8 and Node_2[pnode[2]][15] == 7 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == 8 and Node_2[pnode[2]][15] == 9 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 9 and Node_2[pnode[2]][15] == 8 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 9 and Node_2[pnode[2]][15] == 7 and
                                                            Node_1[numNode_1][16] == Node_2[pnode[2]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 10 and Node_2[pnode[2]][
                                                        15] == 11 and Node_1[numNode_1][16] == Node_2[pnode[2]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == 10 and Node_2[pnode[2]][
                                                        15] == 12 and Node_1[numNode_1][16] == Node_2[pnode[2]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 11 and Node_2[pnode[2]][
                                                        15] == 12 and Node_1[numNode_1][16] == Node_2[pnode[2]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 11 and Node_2[pnode[2]][
                                                        15] == 10 and Node_1[numNode_1][16] == Node_2[pnode[2]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == 12 and Node_2[pnode[2]][
                                                        15] == 11 and Node_1[numNode_1][16] == Node_2[pnode[2]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 21 and Node_2[pnode[2]][
                                                        15] == 22 and Node_1[numNode_1][16] == Node_2[pnode[2]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == 12 and Node_2[pnode[2]][
                                                        15] == 10 and Node_1[numNode_1][16] == Node_2[pnode[2]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 22 and Node_2[pnode[2]][
                                                        15] == 21 and Node_1[numNode_1][16] == Node_2[pnode[2]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == 23 and Node_2[pnode[2]][
                                                        15] == 24 and Node_1[numNode_1][16] == Node_2[pnode[2]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 24 and Node_2[pnode[2]][
                                                        15] == 23 and Node_1[numNode_1][16] == Node_2[pnode[2]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 25 and Node_2[pnode[2]][
                                                        15] == 26 and Node_1[numNode_1][16] == Node_2[pnode[2]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == 26 and Node_2[pnode[2]][
                                                        15] == 25 and Node_1[numNode_1][16] == Node_2[pnode[2]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == 27 and Node_2[pnode[2]][
                                                        15] == 28 and Node_1[numNode_1][16] == Node_2[pnode[2]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 28 and Node_2[pnode[2]][
                                                        15] == 27 and Node_1[numNode_1][16] == Node_2[pnode[2]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 51 and Node_2[pnode[2]][
                                                        15] == 52 and Node_1[numNode_1][16] == Node_2[pnode[2]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == 52 and Node_2[pnode[2]][
                                                        15] == 51 and Node_1[numNode_1][16] == Node_2[pnode[2]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == 53 and Node_2[pnode[2]][
                                                        15] == 54 and Node_1[numNode_1][16] == Node_2[pnode[2]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == 54 and Node_2[pnode[2]][
                                                        15] == 53 and Node_1[numNode_1][16] == Node_2[pnode[2]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17]) or (
                                                            Node_1[numNode_1][15] == 55 and Node_2[pnode[2]][
                                                        15] == 56 and Node_1[numNode_1][16] == Node_2[pnode[2]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 56 and Node_2[pnode[2]][
                                                        15] == 55 and Node_1[numNode_1][16] == Node_2[pnode[2]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 57 and Node_2[pnode[2]][
                                                        15] == 58 and Node_1[numNode_1][16] == Node_2[pnode[2]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 58 and Node_2[pnode[2]][
                                                        15] == 57 and Node_1[numNode_1][16] == Node_2[pnode[2]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_2[pnode[2]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 1 and Node_3[pnode[3]][15] == 2 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == 1 and Node_3[pnode[3]][15] == 3 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == 2 and Node_3[pnode[3]][15] == 1 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == 2 and Node_3[pnode[3]][15] == 3 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 3 and Node_3[pnode[3]][15] == 2 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 3 and Node_3[pnode[3]][15] == 1 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 4 and Node_3[pnode[3]][15] == 6 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 4 and Node_3[pnode[3]][15] == 5 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == 5 and Node_3[pnode[3]][15] == 4 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == 5 and Node_3[pnode[3]][15] == 6 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 6 and Node_3[pnode[3]][15] == 4 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 6 and Node_3[pnode[3]][15] == 5 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 7 and Node_3[pnode[3]][15] == 9 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 7 and Node_3[pnode[3]][15] == 8 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == 8 and Node_3[pnode[3]][15] == 7 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == 8 and Node_3[pnode[3]][15] == 9 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 9 and Node_3[pnode[3]][15] == 8 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 9 and Node_3[pnode[3]][15] == 7 and
                                                            Node_1[numNode_1][16] == Node_3[pnode[3]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 10 and Node_3[pnode[3]][
                                                        15] == 11 and Node_1[numNode_1][16] == Node_3[pnode[3]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == 10 and Node_3[pnode[3]][
                                                        15] == 12 and Node_1[numNode_1][16] == Node_3[pnode[3]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 11 and Node_3[pnode[3]][
                                                        15] == 12 and Node_1[numNode_1][16] == Node_3[pnode[3]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 11 and Node_3[pnode[3]][
                                                        15] == 10 and Node_1[numNode_1][16] == Node_3[pnode[3]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == 12 and Node_3[pnode[3]][
                                                        15] == 11 and Node_1[numNode_1][16] == Node_3[pnode[3]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 21 and Node_3[pnode[3]][
                                                        15] == 22 and Node_1[numNode_1][16] == Node_3[pnode[3]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == 12 and Node_3[pnode[3]][
                                                        15] == 10 and Node_1[numNode_1][16] == Node_3[pnode[3]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 22 and Node_3[pnode[3]][
                                                        15] == 21 and Node_1[numNode_1][16] == Node_3[pnode[3]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == 23 and Node_3[pnode[3]][
                                                        15] == 24 and Node_1[numNode_1][16] == Node_3[pnode[3]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 24 and Node_3[pnode[3]][
                                                        15] == 23 and Node_1[numNode_1][16] == Node_3[pnode[3]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 25 and Node_3[pnode[3]][
                                                        15] == 26 and Node_1[numNode_1][16] == Node_3[pnode[3]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == 26 and Node_3[pnode[3]][
                                                        15] == 25 and Node_1[numNode_1][16] == Node_3[pnode[3]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == 27 and Node_3[pnode[3]][
                                                        15] == 28 and Node_1[numNode_1][16] == Node_3[pnode[3]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 28 and Node_3[pnode[3]][
                                                        15] == 27 and Node_1[numNode_1][16] == Node_3[pnode[3]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 51 and Node_3[pnode[3]][
                                                        15] == 52 and Node_1[numNode_1][16] == Node_3[pnode[3]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == 52 and Node_3[pnode[3]][
                                                        15] == 51 and Node_1[numNode_1][16] == Node_3[pnode[3]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == 53 and Node_3[pnode[3]][
                                                        15] == 54 and Node_1[numNode_1][16] == Node_3[pnode[3]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == 54 and Node_3[pnode[3]][
                                                        15] == 53 and Node_1[numNode_1][16] == Node_3[pnode[3]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17]) or (
                                                            Node_1[numNode_1][15] == 55 and Node_3[pnode[3]][
                                                        15] == 56 and Node_1[numNode_1][16] == Node_3[pnode[3]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 56 and Node_3[pnode[3]][
                                                        15] == 55 and Node_1[numNode_1][16] == Node_3[pnode[3]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 57 and Node_3[pnode[3]][
                                                        15] == 58 and Node_1[numNode_1][16] == Node_3[pnode[3]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 58 and Node_3[pnode[3]][
                                                        15] == 57 and Node_1[numNode_1][16] == Node_3[pnode[3]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_3[pnode[3]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 1 and Node_4[pnode[4]][15] == 2 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == 1 and Node_4[pnode[4]][15] == 3 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == 2 and Node_4[pnode[4]][15] == 1 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == 2 and Node_4[pnode[4]][15] == 3 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 3 and Node_4[pnode[4]][15] == 2 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 3 and Node_4[pnode[4]][15] == 1 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 4 and Node_4[pnode[4]][15] == 6 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 4 and Node_4[pnode[4]][15] == 5 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == 5 and Node_4[pnode[4]][15] == 4 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == 5 and Node_4[pnode[4]][15] == 6 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 6 and Node_4[pnode[4]][15] == 4 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 6 and Node_4[pnode[4]][15] == 5 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 7 and Node_4[pnode[4]][15] == 9 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 7 and Node_4[pnode[4]][15] == 8 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == 8 and Node_4[pnode[4]][15] == 7 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == 8 and Node_4[pnode[4]][15] == 9 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 9 and Node_4[pnode[4]][15] == 8 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 9 and Node_4[pnode[4]][15] == 7 and
                                                            Node_1[numNode_1][16] == Node_4[pnode[4]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 10 and Node_4[pnode[4]][
                                                        15] == 11 and Node_1[numNode_1][16] == Node_4[pnode[4]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == 10 and Node_4[pnode[4]][
                                                        15] == 12 and Node_1[numNode_1][16] == Node_4[pnode[4]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 11 and Node_4[pnode[4]][
                                                        15] == 12 and Node_1[numNode_1][16] == Node_4[pnode[4]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 11 and Node_4[pnode[4]][
                                                        15] == 10 and Node_1[numNode_1][16] == Node_4[pnode[4]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == 12 and Node_4[pnode[4]][
                                                        15] == 11 and Node_1[numNode_1][16] == Node_4[pnode[4]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 21 and Node_4[pnode[4]][
                                                        15] == 22 and Node_1[numNode_1][16] == Node_4[pnode[4]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == 12 and Node_4[pnode[4]][
                                                        15] == 10 and Node_1[numNode_1][16] == Node_4[pnode[4]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 22 and Node_4[pnode[4]][
                                                        15] == 21 and Node_1[numNode_1][16] == Node_4[pnode[4]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == 23 and Node_4[pnode[4]][
                                                        15] == 24 and Node_1[numNode_1][16] == Node_4[pnode[4]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 24 and Node_4[pnode[4]][
                                                        15] == 23 and Node_1[numNode_1][16] == Node_4[pnode[4]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 25 and Node_4[pnode[4]][
                                                        15] == 26 and Node_1[numNode_1][16] == Node_4[pnode[4]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == 26 and Node_4[pnode[4]][
                                                        15] == 25 and Node_1[numNode_1][16] == Node_4[pnode[4]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == 27 and Node_4[pnode[4]][
                                                        15] == 28 and Node_1[numNode_1][16] == Node_4[pnode[4]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 28 and Node_4[pnode[4]][
                                                        15] == 27 and Node_1[numNode_1][16] == Node_4[pnode[4]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 51 and Node_4[pnode[4]][
                                                        15] == 52 and Node_1[numNode_1][16] == Node_4[pnode[4]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == 52 and Node_4[pnode[4]][
                                                        15] == 51 and Node_1[numNode_1][16] == Node_4[pnode[4]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == 53 and Node_4[pnode[4]][
                                                        15] == 54 and Node_1[numNode_1][16] == Node_4[pnode[4]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == 54 and Node_4[pnode[4]][
                                                        15] == 53 and Node_1[numNode_1][16] == Node_4[pnode[4]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17]) or (
                                                            Node_1[numNode_1][15] == 55 and Node_4[pnode[4]][
                                                        15] == 56 and Node_1[numNode_1][16] == Node_4[pnode[4]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 56 and Node_4[pnode[4]][
                                                        15] == 55 and Node_1[numNode_1][16] == Node_4[pnode[4]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 57 and Node_4[pnode[4]][
                                                        15] == 58 and Node_1[numNode_1][16] == Node_4[pnode[4]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 58 and Node_4[pnode[4]][
                                                        15] == 57 and Node_1[numNode_1][16] == Node_4[pnode[4]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_4[pnode[4]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 1 and Node_5[pnode[5]][15] == 2 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == 1 and Node_5[pnode[5]][15] == 3 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == 2 and Node_5[pnode[5]][15] == 1 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == 2 and Node_5[pnode[5]][15] == 3 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 3 and Node_5[pnode[5]][15] == 2 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 3 and Node_5[pnode[5]][15] == 1 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 4 and Node_5[pnode[5]][15] == 6 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 4 and Node_5[pnode[5]][15] == 5 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == 5 and Node_5[pnode[5]][15] == 4 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == 5 and Node_5[pnode[5]][15] == 6 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 6 and Node_5[pnode[5]][15] == 4 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 6 and Node_5[pnode[5]][15] == 5 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 7 and Node_5[pnode[5]][15] == 9 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 7 and Node_5[pnode[5]][15] == 8 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == 8 and Node_5[pnode[5]][15] == 7 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == 8 and Node_5[pnode[5]][15] == 9 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 9 and Node_5[pnode[5]][15] == 8 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 9 and Node_5[pnode[5]][15] == 7 and
                                                            Node_1[numNode_1][16] == Node_5[pnode[5]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 10 and Node_5[pnode[5]][
                                                        15] == 11 and Node_1[numNode_1][16] == Node_5[pnode[5]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == 10 and Node_5[pnode[5]][
                                                        15] == 12 and Node_1[numNode_1][16] == Node_5[pnode[5]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 11 and Node_5[pnode[5]][
                                                        15] == 12 and Node_1[numNode_1][16] == Node_5[pnode[5]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 11 and Node_5[pnode[5]][
                                                        15] == 10 and Node_1[numNode_1][16] == Node_5[pnode[5]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == 12 and Node_5[pnode[5]][
                                                        15] == 11 and Node_1[numNode_1][16] == Node_5[pnode[5]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 21 and Node_5[pnode[5]][
                                                        15] == 22 and Node_1[numNode_1][16] == Node_5[pnode[5]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == 12 and Node_5[pnode[5]][
                                                        15] == 10 and Node_1[numNode_1][16] == Node_5[pnode[5]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 22 and Node_5[pnode[5]][
                                                        15] == 21 and Node_1[numNode_1][16] == Node_5[pnode[5]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == 23 and Node_5[pnode[5]][
                                                        15] == 24 and Node_1[numNode_1][16] == Node_5[pnode[5]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 24 and Node_5[pnode[5]][
                                                        15] == 23 and Node_1[numNode_1][16] == Node_5[pnode[5]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 25 and Node_5[pnode[5]][
                                                        15] == 26 and Node_1[numNode_1][16] == Node_5[pnode[5]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == 26 and Node_5[pnode[5]][
                                                        15] == 25 and Node_1[numNode_1][16] == Node_5[pnode[5]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == 27 and Node_5[pnode[5]][
                                                        15] == 28 and Node_1[numNode_1][16] == Node_5[pnode[5]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 28 and Node_5[pnode[5]][
                                                        15] == 27 and Node_1[numNode_1][16] == Node_5[pnode[5]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 51 and Node_5[pnode[5]][
                                                        15] == 52 and Node_1[numNode_1][16] == Node_5[pnode[5]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == 52 and Node_5[pnode[5]][
                                                        15] == 51 and Node_1[numNode_1][16] == Node_5[pnode[5]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == 53 and Node_5[pnode[5]][
                                                        15] == 54 and Node_1[numNode_1][16] == Node_5[pnode[5]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == 54 and Node_5[pnode[5]][
                                                        15] == 53 and Node_1[numNode_1][16] == Node_5[pnode[5]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17]) or (
                                                            Node_1[numNode_1][15] == 55 and Node_5[pnode[5]][
                                                        15] == 56 and Node_1[numNode_1][16] == Node_5[pnode[5]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 56 and Node_5[pnode[5]][
                                                        15] == 55 and Node_1[numNode_1][16] == Node_5[pnode[5]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 57 and Node_5[pnode[5]][
                                                        15] == 58 and Node_1[numNode_1][16] == Node_5[pnode[5]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 58 and Node_5[pnode[5]][
                                                        15] == 57 and Node_1[numNode_1][16] == Node_5[pnode[5]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_5[pnode[5]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 1 and Node_6[pnode[6]][15] == 2 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 1 and Node_6[pnode[6]][15] == 3 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 2 and Node_6[pnode[6]][15] == 1 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 2 and Node_6[pnode[6]][15] == 3 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 3 and Node_6[pnode[6]][15] == 2 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 3 and Node_6[pnode[6]][15] == 1 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 4 and Node_6[pnode[6]][15] == 6 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 4 and Node_6[pnode[6]][15] == 5 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 5 and Node_6[pnode[6]][15] == 4 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 5 and Node_6[pnode[6]][15] == 6 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 6 and Node_6[pnode[6]][15] == 4 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 6 and Node_6[pnode[6]][15] == 5 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 7 and Node_6[pnode[6]][15] == 9 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 7 and Node_6[pnode[6]][15] == 8 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] - 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 8 and Node_6[pnode[6]][15] == 7 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 8 and Node_6[pnode[6]][15] == 9 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 9 and Node_6[pnode[6]][15] == 8 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 9 and Node_6[pnode[6]][15] == 7 and
                                                            Node_1[numNode_1][16] == Node_6[pnode[6]][16] + 1 and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 10 and Node_6[pnode[6]][
                                                        15] == 11 and Node_1[numNode_1][16] == Node_6[pnode[6]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 10 and Node_6[pnode[6]][
                                                        15] == 12 and Node_1[numNode_1][16] == Node_6[pnode[6]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 11 and Node_6[pnode[6]][
                                                        15] == 12 and Node_1[numNode_1][16] == Node_6[pnode[6]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 11 and Node_6[pnode[6]][
                                                        15] == 10 and Node_1[numNode_1][16] == Node_6[pnode[6]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 12 and Node_6[pnode[6]][
                                                        15] == 11 and Node_1[numNode_1][16] == Node_6[pnode[6]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 21 and Node_6[pnode[6]][
                                                        15] == 22 and Node_1[numNode_1][16] == Node_6[pnode[6]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 12 and Node_6[pnode[6]][
                                                        15] == 10 and Node_1[numNode_1][16] == Node_6[pnode[6]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 22 and Node_6[pnode[6]][
                                                        15] == 21 and Node_1[numNode_1][16] == Node_6[pnode[6]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 23 and Node_6[pnode[6]][
                                                        15] == 24 and Node_1[numNode_1][16] == Node_6[pnode[6]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 24 and Node_6[pnode[6]][
                                                        15] == 23 and Node_1[numNode_1][16] == Node_6[pnode[6]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 25 and Node_6[pnode[6]][
                                                        15] == 26 and Node_1[numNode_1][16] == Node_6[pnode[6]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 26 and Node_6[pnode[6]][
                                                        15] == 25 and Node_1[numNode_1][16] == Node_6[pnode[6]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 27 and Node_6[pnode[6]][
                                                        15] == 28 and Node_1[numNode_1][16] == Node_6[pnode[6]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 28 and Node_6[pnode[6]][
                                                        15] == 27 and Node_1[numNode_1][16] == Node_6[pnode[6]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 51 and Node_6[pnode[6]][
                                                        15] == 52 and Node_1[numNode_1][16] == Node_6[pnode[6]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 52 and Node_6[pnode[6]][
                                                        15] == 51 and Node_1[numNode_1][16] == Node_6[pnode[6]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 53 and Node_6[pnode[6]][
                                                        15] == 54 and Node_1[numNode_1][16] == Node_6[pnode[6]][
                                                                16] - 1 and Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 54 and Node_6[pnode[6]][
                                                        15] == 53 and Node_1[numNode_1][16] == Node_6[pnode[6]][
                                                                16] + 1 and Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17]) or (
                                                            Node_1[numNode_1][15] == 55 and Node_6[pnode[6]][
                                                        15] == 56 and Node_1[numNode_1][16] == Node_6[pnode[6]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 56 and Node_6[pnode[6]][
                                                        15] == 55 and Node_1[numNode_1][16] == Node_6[pnode[6]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] + 1) or (
                                                            Node_1[numNode_1][15] == 57 and Node_6[pnode[6]][
                                                        15] == 58 and Node_1[numNode_1][16] == Node_6[pnode[6]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] - 1) or (
                                                            Node_1[numNode_1][15] == 58 and Node_6[pnode[6]][
                                                        15] == 57 and Node_1[numNode_1][16] == Node_6[pnode[6]][16] and
                                                            Node_1[numNode_1][17] ==
                                                            Node_6[pnode[6]][17] + 1)):
                                                        if ((Node_2[numNode_2][15] == pnode[8] and Node_2[numNode_2][
                                                            16] == pnode[9] and Node_2[numNode_2][17] == pnode[10]) or (
                                                                Node_2[numNode_2][15] == Node_1[pnode[1]][15] and
                                                                Node_2[numNode_2][16] == Node_1[pnode[1]][16] and
                                                                Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == Node_2[pnode[2]][15] and
                                                                Node_2[numNode_2][16] == Node_2[pnode[2]][16] and
                                                                Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == Node_3[pnode[3]][15] and
                                                                Node_2[numNode_2][16] == Node_3[pnode[3]][16] and
                                                                Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == Node_4[pnode[4]][15] and
                                                                Node_2[numNode_2][16] == Node_4[pnode[4]][16] and
                                                                Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == Node_5[pnode[5]][15] and
                                                                Node_2[numNode_2][16] == Node_5[pnode[5]][16] and
                                                                Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == Node_6[pnode[6]][15] and
                                                                Node_2[numNode_2][16] == Node_6[pnode[6]][16] and
                                                                Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 1 and pnode[8] == 2 and
                                                                Node_2[numNode_2][16] == pnode[9] - 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10]) or (
                                                                Node_2[numNode_2][15] == 1 and pnode[8] == 3 and
                                                                Node_2[numNode_2][16] == pnode[9] and Node_2[numNode_2][
                                                                    17] ==
                                                                pnode[10] - 1) or (
                                                                Node_2[numNode_2][15] == 2 and pnode[8] == 1 and
                                                                Node_2[numNode_2][16] == pnode[9] + 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10]) or (
                                                                Node_2[numNode_2][15] == 2 and pnode[8] == 3 and
                                                                Node_2[numNode_2][16] == pnode[9] + 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10] - 1) or (
                                                                Node_2[numNode_2][15] == 3 and pnode[8] == 2 and
                                                                Node_2[numNode_2][16] == pnode[9] - 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10] + 1) or (
                                                                Node_2[numNode_2][15] == 3 and pnode[8] == 1 and
                                                                Node_2[numNode_2][16] == pnode[9] and Node_2[numNode_2][
                                                                    17] ==
                                                                pnode[10] + 1) or (
                                                                Node_2[numNode_2][15] == 4 and pnode[8] == 6 and
                                                                Node_2[numNode_2][16] == pnode[9] - 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10] - 1) or (
                                                                Node_2[numNode_2][15] == 4 and pnode[8] == 5 and
                                                                Node_2[numNode_2][16] == pnode[9] - 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10]) or (
                                                                Node_2[numNode_2][15] == 5 and pnode[8] == 4 and
                                                                Node_2[numNode_2][16] == pnode[9] + 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10]) or (
                                                                Node_2[numNode_2][15] == 5 and pnode[8] == 6 and
                                                                Node_2[numNode_2][16] == pnode[9] and Node_2[numNode_2][
                                                                    17] ==
                                                                pnode[10] - 1) or (
                                                                Node_2[numNode_2][15] == 6 and pnode[8] == 4 and
                                                                Node_2[numNode_2][16] == pnode[9] + 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10] + 1) or (
                                                                Node_2[numNode_2][15] == 6 and pnode[8] == 5 and
                                                                Node_2[numNode_2][16] == pnode[9] and Node_2[numNode_2][
                                                                    17] ==
                                                                pnode[10] + 1) or (
                                                                Node_2[numNode_2][15] == 7 and pnode[8] == 9 and
                                                                Node_2[numNode_2][16] == pnode[9] - 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10] + 1) or (
                                                                Node_2[numNode_2][15] == 7 and pnode[8] == 8 and
                                                                Node_2[numNode_2][16] == pnode[9] - 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10]) or (
                                                                Node_2[numNode_2][15] == 8 and pnode[8] == 7 and
                                                                Node_2[numNode_2][16] == pnode[9] + 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10]) or (
                                                                Node_2[numNode_2][15] == 8 and pnode[8] == 9 and
                                                                Node_2[numNode_2][16] == pnode[9] and Node_2[numNode_2][
                                                                    17] ==
                                                                pnode[10] + 1) or (
                                                                Node_2[numNode_2][15] == 9 and pnode[8] == 8 and
                                                                Node_2[numNode_2][16] == pnode[9] and Node_2[numNode_2][
                                                                    17] ==
                                                                pnode[10] - 1) or (
                                                                Node_2[numNode_2][15] == 9 and pnode[8] == 7 and
                                                                Node_2[numNode_2][16] == pnode[9] + 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10] - 1) or (
                                                                Node_2[numNode_2][15] == 10 and pnode[8] == 11 and
                                                                Node_2[numNode_2][16] == pnode[9] - 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10]) or (
                                                                Node_2[numNode_2][15] == 10 and pnode[8] == 12 and
                                                                Node_2[numNode_2][16] == pnode[9] and Node_2[numNode_2][
                                                                    17] ==
                                                                pnode[10] + 1) or (
                                                                Node_2[numNode_2][15] == 11 and pnode[8] == 12 and
                                                                Node_2[numNode_2][16] == pnode[9] + 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10] + 1) or (
                                                                Node_2[numNode_2][15] == 11 and pnode[8] == 10 and
                                                                Node_2[numNode_2][16] == pnode[9] + 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10]) or (
                                                                Node_2[numNode_2][15] == 12 and pnode[8] == 11 and
                                                                Node_2[numNode_2][16] == pnode[9] - 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10] + 1) or (
                                                                Node_2[numNode_2][15] == 21 and pnode[8] == 22 and
                                                                Node_2[numNode_2][16] == pnode[9] - 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10]) or (
                                                                Node_2[numNode_2][15] == 12 and pnode[8] == 10 and
                                                                Node_2[numNode_2][16] == pnode[9] and Node_2[numNode_2][
                                                                    17] ==
                                                                pnode[10] - 1) or (
                                                                Node_2[numNode_2][15] == 22 and pnode[8] == 21 and
                                                                Node_2[numNode_2][16] == pnode[9] + 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10]) or (
                                                                Node_2[numNode_2][15] == 23 and pnode[8] == 24 and
                                                                Node_2[numNode_2][16] == pnode[9] and Node_2[numNode_2][
                                                                    17] ==
                                                                pnode[10] - 1) or (
                                                                Node_2[numNode_2][15] == 24 and pnode[8] == 23 and
                                                                Node_2[numNode_2][16] == pnode[9] and Node_2[numNode_2][
                                                                    17] ==
                                                                pnode[10] + 1) or (
                                                                Node_2[numNode_2][15] == 25 and pnode[8] == 26 and
                                                                Node_2[numNode_2][16] == pnode[9] - 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10]) or (
                                                                Node_2[numNode_2][15] == 26 and pnode[8] == 25 and
                                                                Node_2[numNode_2][16] == pnode[9] + 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10]) or (
                                                                Node_2[numNode_2][15] == 27 and pnode[8] == 28 and
                                                                Node_2[numNode_2][16] == pnode[9] and Node_2[numNode_2][
                                                                    17] ==
                                                                pnode[10] - 1) or (
                                                                Node_2[numNode_2][15] == 28 and pnode[8] == 27 and
                                                                Node_2[numNode_2][16] == pnode[9] and Node_2[numNode_2][
                                                                    17] ==
                                                                pnode[10] + 1) or (
                                                                Node_2[numNode_2][15] == 51 and pnode[8] == 52 and
                                                                Node_2[numNode_2][16] == pnode[9] - 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10]) or (
                                                                Node_2[numNode_2][15] == 52 and pnode[8] == 51 and
                                                                Node_2[numNode_2][16] == pnode[9] + 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10]) or (
                                                                Node_2[numNode_2][15] == 53 and pnode[8] == 54 and
                                                                Node_2[numNode_2][16] == pnode[9] - 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10]) or (
                                                                Node_2[numNode_2][15] == 54 and pnode[8] == 53 and
                                                                Node_2[numNode_2][16] == pnode[9] + 1 and
                                                                Node_2[numNode_2][17] ==
                                                                pnode[10]) or (
                                                                Node_2[numNode_2][15] == 55 and pnode[8] == 56 and
                                                                Node_2[numNode_2][16] == pnode[9] and Node_2[numNode_2][
                                                                    17] ==
                                                                pnode[10] - 1) or (
                                                                Node_2[numNode_2][15] == 56 and pnode[8] == 55 and
                                                                Node_2[numNode_2][16] == pnode[9] and Node_2[numNode_2][
                                                                    17] ==
                                                                pnode[10] + 1) or (
                                                                Node_2[numNode_2][15] == 57 and pnode[8] == 58 and
                                                                Node_2[numNode_2][16] == pnode[9] and Node_2[numNode_2][
                                                                    17] ==
                                                                pnode[10] - 1) or (
                                                                Node_2[numNode_2][15] == 58 and pnode[8] == 57 and
                                                                Node_2[numNode_2][16] == pnode[9] and Node_2[numNode_2][
                                                                    17] ==
                                                                pnode[10] + 1) or (
                                                                Node_2[numNode_2][15] == 1 and Node_1[pnode[1]][
                                                            15] == 2 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == 1 and Node_1[pnode[1]][
                                                            15] == 3 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == 2 and Node_1[pnode[1]][
                                                            15] == 1 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == 2 and Node_1[pnode[1]][
                                                            15] == 3 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 3 and Node_1[pnode[1]][
                                                            15] == 2 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 3 and Node_1[pnode[1]][
                                                            15] == 1 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 4 and Node_1[pnode[1]][
                                                            15] == 6 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 4 and Node_1[pnode[1]][
                                                            15] == 5 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == 5 and Node_1[pnode[1]][
                                                            15] == 4 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == 5 and Node_1[pnode[1]][
                                                            15] == 6 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 6 and Node_1[pnode[1]][
                                                            15] == 4 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 6 and Node_1[pnode[1]][
                                                            15] == 5 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 7 and Node_1[pnode[1]][
                                                            15] == 9 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 7 and Node_1[pnode[1]][
                                                            15] == 8 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == 8 and Node_1[pnode[1]][
                                                            15] == 7 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == 8 and Node_1[pnode[1]][
                                                            15] == 9 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 9 and Node_1[pnode[1]][
                                                            15] == 8 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 9 and Node_1[pnode[1]][
                                                            15] == 7 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 10 and Node_1[pnode[1]][
                                                            15] == 11 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == 10 and Node_1[pnode[1]][
                                                            15] == 12 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 11 and Node_1[pnode[1]][
                                                            15] == 12 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 11 and Node_1[pnode[1]][
                                                            15] == 10 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == 12 and Node_1[pnode[1]][
                                                            15] == 11 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 21 and Node_1[pnode[1]][
                                                            15] == 22 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == 12 and Node_1[pnode[1]][
                                                            15] == 10 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 22 and Node_1[pnode[1]][
                                                            15] == 21 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == 23 and Node_1[pnode[1]][
                                                            15] == 24 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 24 and Node_1[pnode[1]][
                                                            15] == 23 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 25 and Node_1[pnode[1]][
                                                            15] == 26 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == 26 and Node_1[pnode[1]][
                                                            15] == 25 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == 27 and Node_1[pnode[1]][
                                                            15] == 28 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 28 and Node_1[pnode[1]][
                                                            15] == 27 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 51 and Node_1[pnode[1]][
                                                            15] == 52 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == 52 and Node_1[pnode[1]][
                                                            15] == 51 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == 53 and Node_1[pnode[1]][
                                                            15] == 54 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == 54 and Node_1[pnode[1]][
                                                            15] == 53 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17]) or (
                                                                Node_2[numNode_2][15] == 55 and Node_1[pnode[1]][
                                                            15] == 56 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 56 and Node_1[pnode[1]][
                                                            15] == 55 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 57 and Node_1[pnode[1]][
                                                            15] == 58 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 58 and Node_1[pnode[1]][
                                                            15] == 57 and Node_2[numNode_2][16] == Node_1[pnode[1]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_1[pnode[1]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 1 and Node_2[pnode[2]][
                                                            15] == 2 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == 1 and Node_2[pnode[2]][
                                                            15] == 3 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == 2 and Node_2[pnode[2]][
                                                            15] == 1 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == 2 and Node_2[pnode[2]][
                                                            15] == 3 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 3 and Node_2[pnode[2]][
                                                            15] == 2 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 3 and Node_2[pnode[2]][
                                                            15] == 1 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 4 and Node_2[pnode[2]][
                                                            15] == 6 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 4 and Node_2[pnode[2]][
                                                            15] == 5 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == 5 and Node_2[pnode[2]][
                                                            15] == 4 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == 5 and Node_2[pnode[2]][
                                                            15] == 6 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 6 and Node_2[pnode[2]][
                                                            15] == 4 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 6 and Node_2[pnode[2]][
                                                            15] == 5 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 7 and Node_2[pnode[2]][
                                                            15] == 9 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 7 and Node_2[pnode[2]][
                                                            15] == 8 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == 8 and Node_2[pnode[2]][
                                                            15] == 7 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == 8 and Node_2[pnode[2]][
                                                            15] == 9 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 9 and Node_2[pnode[2]][
                                                            15] == 8 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 9 and Node_2[pnode[2]][
                                                            15] == 7 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 10 and Node_2[pnode[2]][
                                                            15] == 11 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == 10 and Node_2[pnode[2]][
                                                            15] == 12 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 11 and Node_2[pnode[2]][
                                                            15] == 12 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 11 and Node_2[pnode[2]][
                                                            15] == 10 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == 12 and Node_2[pnode[2]][
                                                            15] == 11 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 21 and Node_2[pnode[2]][
                                                            15] == 22 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == 12 and Node_2[pnode[2]][
                                                            15] == 10 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 22 and Node_2[pnode[2]][
                                                            15] == 21 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == 23 and Node_2[pnode[2]][
                                                            15] == 24 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 24 and Node_2[pnode[2]][
                                                            15] == 23 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 25 and Node_2[pnode[2]][
                                                            15] == 26 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == 26 and Node_2[pnode[2]][
                                                            15] == 25 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == 27 and Node_2[pnode[2]][
                                                            15] == 28 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 28 and Node_2[pnode[2]][
                                                            15] == 27 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 51 and Node_2[pnode[2]][
                                                            15] == 52 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == 52 and Node_2[pnode[2]][
                                                            15] == 51 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == 53 and Node_2[pnode[2]][
                                                            15] == 54 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == 54 and Node_2[pnode[2]][
                                                            15] == 53 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17]) or (
                                                                Node_2[numNode_2][15] == 55 and Node_2[pnode[2]][
                                                            15] == 56 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 56 and Node_2[pnode[2]][
                                                            15] == 55 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 57 and Node_2[pnode[2]][
                                                            15] == 58 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 58 and Node_2[pnode[2]][
                                                            15] == 57 and Node_2[numNode_2][16] == Node_2[pnode[2]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_2[pnode[2]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 1 and Node_3[pnode[3]][
                                                            15] == 2 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == 1 and Node_3[pnode[3]][
                                                            15] == 3 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == 2 and Node_3[pnode[3]][
                                                            15] == 1 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == 2 and Node_3[pnode[3]][
                                                            15] == 3 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 3 and Node_3[pnode[3]][
                                                            15] == 2 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 3 and Node_3[pnode[3]][
                                                            15] == 1 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 4 and Node_3[pnode[3]][
                                                            15] == 6 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 4 and Node_3[pnode[3]][
                                                            15] == 5 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == 5 and Node_3[pnode[3]][
                                                            15] == 4 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == 5 and Node_3[pnode[3]][
                                                            15] == 6 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 6 and Node_3[pnode[3]][
                                                            15] == 4 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 6 and Node_3[pnode[3]][
                                                            15] == 5 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 7 and Node_3[pnode[3]][
                                                            15] == 9 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 7 and Node_3[pnode[3]][
                                                            15] == 8 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == 8 and Node_3[pnode[3]][
                                                            15] == 7 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == 8 and Node_3[pnode[3]][
                                                            15] == 9 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 9 and Node_3[pnode[3]][
                                                            15] == 8 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 9 and Node_3[pnode[3]][
                                                            15] == 7 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 10 and Node_3[pnode[3]][
                                                            15] == 11 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == 10 and Node_3[pnode[3]][
                                                            15] == 12 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 11 and Node_3[pnode[3]][
                                                            15] == 12 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 11 and Node_3[pnode[3]][
                                                            15] == 10 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == 12 and Node_3[pnode[3]][
                                                            15] == 11 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 21 and Node_3[pnode[3]][
                                                            15] == 22 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == 12 and Node_3[pnode[3]][
                                                            15] == 10 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 22 and Node_3[pnode[3]][
                                                            15] == 21 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == 23 and Node_3[pnode[3]][
                                                            15] == 24 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 24 and Node_3[pnode[3]][
                                                            15] == 23 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 25 and Node_3[pnode[3]][
                                                            15] == 26 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == 26 and Node_3[pnode[3]][
                                                            15] == 25 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == 27 and Node_3[pnode[3]][
                                                            15] == 28 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 28 and Node_3[pnode[3]][
                                                            15] == 27 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 51 and Node_3[pnode[3]][
                                                            15] == 52 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == 52 and Node_3[pnode[3]][
                                                            15] == 51 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == 53 and Node_3[pnode[3]][
                                                            15] == 54 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == 54 and Node_3[pnode[3]][
                                                            15] == 53 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17]) or (
                                                                Node_2[numNode_2][15] == 55 and Node_3[pnode[3]][
                                                            15] == 56 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 56 and Node_3[pnode[3]][
                                                            15] == 55 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 57 and Node_3[pnode[3]][
                                                            15] == 58 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 58 and Node_3[pnode[3]][
                                                            15] == 57 and Node_2[numNode_2][16] == Node_3[pnode[3]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_3[pnode[3]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 1 and Node_4[pnode[4]][
                                                            15] == 2 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == 1 and Node_4[pnode[4]][
                                                            15] == 3 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == 2 and Node_4[pnode[4]][
                                                            15] == 1 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == 2 and Node_4[pnode[4]][
                                                            15] == 3 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 3 and Node_4[pnode[4]][
                                                            15] == 2 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 3 and Node_4[pnode[4]][
                                                            15] == 1 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 4 and Node_4[pnode[4]][
                                                            15] == 6 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 4 and Node_4[pnode[4]][
                                                            15] == 5 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == 5 and Node_4[pnode[4]][
                                                            15] == 4 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == 5 and Node_4[pnode[4]][
                                                            15] == 6 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 6 and Node_4[pnode[4]][
                                                            15] == 4 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 6 and Node_4[pnode[4]][
                                                            15] == 5 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 7 and Node_4[pnode[4]][
                                                            15] == 9 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 7 and Node_4[pnode[4]][
                                                            15] == 8 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == 8 and Node_4[pnode[4]][
                                                            15] == 7 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == 8 and Node_4[pnode[4]][
                                                            15] == 9 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 9 and Node_4[pnode[4]][
                                                            15] == 8 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 9 and Node_4[pnode[4]][
                                                            15] == 7 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 10 and Node_4[pnode[4]][
                                                            15] == 11 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == 10 and Node_4[pnode[4]][
                                                            15] == 12 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 11 and Node_4[pnode[4]][
                                                            15] == 12 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 11 and Node_4[pnode[4]][
                                                            15] == 10 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == 12 and Node_4[pnode[4]][
                                                            15] == 11 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 21 and Node_4[pnode[4]][
                                                            15] == 22 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == 12 and Node_4[pnode[4]][
                                                            15] == 10 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 22 and Node_4[pnode[4]][
                                                            15] == 21 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == 23 and Node_4[pnode[4]][
                                                            15] == 24 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 24 and Node_4[pnode[4]][
                                                            15] == 23 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 25 and Node_4[pnode[4]][
                                                            15] == 26 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == 26 and Node_4[pnode[4]][
                                                            15] == 25 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == 27 and Node_4[pnode[4]][
                                                            15] == 28 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 28 and Node_4[pnode[4]][
                                                            15] == 27 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 51 and Node_4[pnode[4]][
                                                            15] == 52 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == 52 and Node_4[pnode[4]][
                                                            15] == 51 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == 53 and Node_4[pnode[4]][
                                                            15] == 54 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == 54 and Node_4[pnode[4]][
                                                            15] == 53 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17]) or (
                                                                Node_2[numNode_2][15] == 55 and Node_4[pnode[4]][
                                                            15] == 56 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 56 and Node_4[pnode[4]][
                                                            15] == 55 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 57 and Node_4[pnode[4]][
                                                            15] == 58 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 58 and Node_4[pnode[4]][
                                                            15] == 57 and Node_2[numNode_2][16] == Node_4[pnode[4]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_4[pnode[4]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 1 and Node_5[pnode[5]][
                                                            15] == 2 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == 1 and Node_5[pnode[5]][
                                                            15] == 3 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == 2 and Node_5[pnode[5]][
                                                            15] == 1 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == 2 and Node_5[pnode[5]][
                                                            15] == 3 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 3 and Node_5[pnode[5]][
                                                            15] == 2 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 3 and Node_5[pnode[5]][
                                                            15] == 1 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 4 and Node_5[pnode[5]][
                                                            15] == 6 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 4 and Node_5[pnode[5]][
                                                            15] == 5 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == 5 and Node_5[pnode[5]][
                                                            15] == 4 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == 5 and Node_5[pnode[5]][
                                                            15] == 6 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 6 and Node_5[pnode[5]][
                                                            15] == 4 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 6 and Node_5[pnode[5]][
                                                            15] == 5 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 7 and Node_5[pnode[5]][
                                                            15] == 9 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 7 and Node_5[pnode[5]][
                                                            15] == 8 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == 8 and Node_5[pnode[5]][
                                                            15] == 7 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == 8 and Node_5[pnode[5]][
                                                            15] == 9 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 9 and Node_5[pnode[5]][
                                                            15] == 8 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 9 and Node_5[pnode[5]][
                                                            15] == 7 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 10 and Node_5[pnode[5]][
                                                            15] == 11 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == 10 and Node_5[pnode[5]][
                                                            15] == 12 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 11 and Node_5[pnode[5]][
                                                            15] == 12 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 11 and Node_5[pnode[5]][
                                                            15] == 10 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == 12 and Node_5[pnode[5]][
                                                            15] == 11 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 21 and Node_5[pnode[5]][
                                                            15] == 22 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == 12 and Node_5[pnode[5]][
                                                            15] == 10 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 22 and Node_5[pnode[5]][
                                                            15] == 21 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == 23 and Node_5[pnode[5]][
                                                            15] == 24 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 24 and Node_5[pnode[5]][
                                                            15] == 23 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 25 and Node_5[pnode[5]][
                                                            15] == 26 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == 26 and Node_5[pnode[5]][
                                                            15] == 25 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == 27 and Node_5[pnode[5]][
                                                            15] == 28 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 28 and Node_5[pnode[5]][
                                                            15] == 27 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 51 and Node_5[pnode[5]][
                                                            15] == 52 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == 52 and Node_5[pnode[5]][
                                                            15] == 51 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == 53 and Node_5[pnode[5]][
                                                            15] == 54 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == 54 and Node_5[pnode[5]][
                                                            15] == 53 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17]) or (
                                                                Node_2[numNode_2][15] == 55 and Node_5[pnode[5]][
                                                            15] == 56 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 56 and Node_5[pnode[5]][
                                                            15] == 55 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 57 and Node_5[pnode[5]][
                                                            15] == 58 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 58 and Node_5[pnode[5]][
                                                            15] == 57 and Node_2[numNode_2][16] == Node_5[pnode[5]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_5[pnode[5]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 1 and Node_6[pnode[6]][
                                                            15] == 2 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 1 and Node_6[pnode[6]][
                                                            15] == 3 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 2 and Node_6[pnode[6]][
                                                            15] == 1 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 2 and Node_6[pnode[6]][
                                                            15] == 3 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 3 and Node_6[pnode[6]][
                                                            15] == 2 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 3 and Node_6[pnode[6]][
                                                            15] == 1 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 4 and Node_6[pnode[6]][
                                                            15] == 6 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 4 and Node_6[pnode[6]][
                                                            15] == 5 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 5 and Node_6[pnode[6]][
                                                            15] == 4 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 5 and Node_6[pnode[6]][
                                                            15] == 6 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 6 and Node_6[pnode[6]][
                                                            15] == 4 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 6 and Node_6[pnode[6]][
                                                            15] == 5 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 7 and Node_6[pnode[6]][
                                                            15] == 9 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 7 and Node_6[pnode[6]][
                                                            15] == 8 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 8 and Node_6[pnode[6]][
                                                            15] == 7 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 8 and Node_6[pnode[6]][
                                                            15] == 9 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 9 and Node_6[pnode[6]][
                                                            15] == 8 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 9 and Node_6[pnode[6]][
                                                            15] == 7 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 10 and Node_6[pnode[6]][
                                                            15] == 11 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 10 and Node_6[pnode[6]][
                                                            15] == 12 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 11 and Node_6[pnode[6]][
                                                            15] == 12 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 11 and Node_6[pnode[6]][
                                                            15] == 10 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 12 and Node_6[pnode[6]][
                                                            15] == 11 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 21 and Node_6[pnode[6]][
                                                            15] == 22 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 12 and Node_6[pnode[6]][
                                                            15] == 10 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 22 and Node_6[pnode[6]][
                                                            15] == 21 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 23 and Node_6[pnode[6]][
                                                            15] == 24 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 24 and Node_6[pnode[6]][
                                                            15] == 23 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 25 and Node_6[pnode[6]][
                                                            15] == 26 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 26 and Node_6[pnode[6]][
                                                            15] == 25 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 27 and Node_6[pnode[6]][
                                                            15] == 28 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 28 and Node_6[pnode[6]][
                                                            15] == 27 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 51 and Node_6[pnode[6]][
                                                            15] == 52 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 52 and Node_6[pnode[6]][
                                                            15] == 51 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 53 and Node_6[pnode[6]][
                                                            15] == 54 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] - 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 54 and Node_6[pnode[6]][
                                                            15] == 53 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] + 1 and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17]) or (
                                                                Node_2[numNode_2][15] == 55 and Node_6[pnode[6]][
                                                            15] == 56 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 56 and Node_6[pnode[6]][
                                                            15] == 55 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] + 1) or (
                                                                Node_2[numNode_2][15] == 57 and Node_6[pnode[6]][
                                                            15] == 58 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] - 1) or (
                                                                Node_2[numNode_2][15] == 58 and Node_6[pnode[6]][
                                                            15] == 57 and Node_2[numNode_2][16] == Node_6[pnode[6]][
                                                                    16] and Node_2[numNode_2][17] ==
                                                                Node_6[pnode[6]][17] + 1)):

                                                            pnodeInt = 1
                                                            break
                                if (pnodeInt ==0):
                                    print("1:",Node_1[numNode_1][15:18],"2:",Node_2[numNode_2][15:18],"3:",Node_3[numNode_3][15:18],"4:",Node_4[numNode_4][15:18],"5:",Node_5[numNode_5][15:18],"6:",Node_6[numNode_6][15:18],"7:",search6,x6,y6)
                                    Node_7.append(
                                        [Model_7.copy(), numNode_1, numNode_2,
                                         numNode_3,
                                         numNode_4, numNode_5, numNode_6, numNode_7, search6, x6, y6])
                                    numNode_7 += 1
                                    if (numNode_7 < 10):
                                        w = Canvas(
                                            f1,
                                            width=160,
                                            height=160,
                                            background="white"
                                        )
                                    elif (numNode_7 < 19):
                                        w = Canvas(
                                            f2,
                                            width=160,
                                            height=160,
                                            background="white"
                                        )
                                    elif (numNode_7 < 28):
                                        w = Canvas(
                                            f3,
                                            width=160,
                                            height=160,
                                            background="white"
                                        )
                                    elif (numNode_7 < 37):
                                        w = Canvas(
                                            f4,
                                            width=160,
                                            height=160,
                                            background="white"
                                        )
                                    elif (numNode_7 < 46):
                                        w = Canvas(
                                            f5,
                                            width=160,
                                            height=160,
                                            background="white"
                                        )
                                    elif (numNode_7 < 55):
                                        w = Canvas(
                                            f6,
                                            width=160,
                                            height=160,
                                            background="white"
                                        )
                                    else:
                                        w = Canvas(
                                            f7,
                                            width=160,
                                            height=160,
                                            background="white"
                                        )
                                    w.pack(side=LEFT, expand=YES)
                                    draw(Model_7, root, w)
            print(numNode_7)

def Openf():
    # fm2.destroy()
    f1.pack_forget()
    f2.pack_forget()
    f3.pack_forget()
    f4.pack_forget()
    f5.pack_forget()
    f6.pack_forget()
    f7.pack_forget()
    for widget in f1.winfo_children():
        widget.destroy()
    for widget in f2.winfo_children():
        widget.destroy()
    for widget in f3.winfo_children():
        widget.destroy()
    for widget in f4.winfo_children():
        widget.destroy()
    for widget in f5.winfo_children():
        widget.destroy()
    for widget in f6.winfo_children():
        widget.destroy()
    for widget in f7.winfo_children():
        widget.destroy()

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=1500,height=1000)



if __name__ == "__main__":
    root = Tk()
    Model = Model1.copy()
    root.title('Seven-piece Puzzle')
    Label1 = ttk.Label(root,
                 background="yellow",
                 relief="ridge",
                 borderwidth=10,
                 #文本
                 text = "小七巧",)
    Label1.pack(side = TOP ,expand = YES)
    mw, mh = root.maxsize()
    root.geometry('360x150+%d+%d' % ((mw - 360) / 2, (mh - 150) / 2))  # 窗口居中
    # 创建一个下拉列表
    # number = StringVar()#窗体自带的文本，新建一个值

    numberChosen = ttk.Combobox(root, width=40)
    comboxlist = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    numberChosen['values'] = comboxlist  # 设置下拉列表的值
    aChosen = ttk.Combobox(root, width=40)
    alist = ["DFS","BFS","A*","IDA"]
    aChosen['values'] = alist  # 设置下拉列表的值
    aChosen.pack(side=TOP, expand=YES)  # 设置其在界面中出现的位置
    aChosen["state"] = "readonly"
    aChosen.set("DFS")
    aChosen.bind("<<ComboboxSelected>>")  # 绑定事件
    numberChosen.pack(side=TOP, expand=YES)  # 设置其在界面中出现的位置
    numberChosen["state"] = "readonly"
    numberChosen.set(1)
    numberChosen.bind("<<ComboboxSelected>>")  # 绑定事件
   # R = numberChosen.get()
   # print(R)
    fm1 = Frame(root)
    OpenB = Button(fm1, text="清空页面", fg='green', activeforeground='yellow', command=Openf).pack(side=LEFT,
                                                                                                  expand=YES)  # 创建按钮
    CancelB = Button(fm1, text="退出", fg='green', activeforeground='yellow', command=root.quit).pack(side=LEFT,
                                                                                                    expand=YES)  # 创建按钮
    UpgradeB = Button(fm1, text="开始", fg='green', activeforeground='yellow', command=Upgrade).pack(side=LEFT,
                                                                                                      expand=YES)  # 创建按钮
    # B.pack()
    fm1.pack(ipadx=20, expand=YES)
    myframe = Frame(root, relief=GROOVE, width=50, height=100, bd=1)
    #myframe.place(x=10, y=10)
    myframe.pack(side=TOP)
    canvas = Canvas(myframe)
    frame = Frame(canvas)
    myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right", fill="y")
    canvas.pack(side="left")
    canvas.create_window((0, 0), window=frame, anchor='nw')
    frame.bind("<Configure>", myfunction)
    f1 = Frame(frame)
    f2 = Frame(frame)
    f3 = Frame(frame)
    f4 = Frame(frame)
    f5 = Frame(frame)
    f6 = Frame(frame)
    f7 = Frame(frame)
    # fm2.pack()
    root.update()
    root.mainloop()
