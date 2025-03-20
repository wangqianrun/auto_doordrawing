from pyautocad import Autocad, APoint
import re
import math
import array




# 打开cad文件
# 自动连接上cad，只要cad是开着的，就创建了一个<pyautocad.api.Autocad> 对象。这个对象连接最近打开的cad文件。
# 如果此时还没有打开cad，将会创建一个新的dwg文件，并自动开启cad软件
acad = Autocad(create_if_not_exists=True)
# acad.prompt() 用来在cad控制台中打印文字
acad.prompt("Hello, Autocad from Python")
# acad.doc.Name储存着cad最近打开的图形名
#//acad.doc.Application.Documents.Open("D:\CAD\demo\three.dxf")
print(acad.doc.Name)
def create_arc(x,y,radius,start_angle,end_angle):
    center_point = APoint(x,y)
    start_angle = math.radians(start_angle)
    end_angle = math.radians(end_angle)
    arc = acad.model.AddArc(center_point,radius,start_angle,end_angle)
    arc.Color = 1
    # mirror_line_start = APoint(9189.1276,(-213923.8392-214200.8392)/2)
    # mirror_line_end = APoint(10662.1276,(-213923.8392-214200.8392)/2)
    # arc.Mirror(mirror_line_start,mirror_line_end)


    return arc

def create_line(x1,y1,x2,y2):
    p1 = APoint(x1,y1)
    p2 = APoint(x2,y2)
    line = acad.model.AddLine(p1,p2)
    line.Color = 1
    # mirror_line_start = APoint(9189.1276,(-213923.8392-214200.8392)/2)
    # mirror_line_end = APoint(10662.1276,(-213923.8392-214200.8392)/2)
    # line.Mirror(mirror_line_start,mirror_line_end)

    return line

def create_capsule_circle(center_point_x,center_point_y):
    center_point2_x = center_point_x
    center_point2_y = center_point_y + 38
    create_arc(center_point_x,center_point_y,10,-180,0)
    create_arc(center_point2_x,center_point2_y,10,0,180)
    create_line(center_point_x-10,center_point_y,center_point_x-10,center_point_y+38)
    create_line(center_point_x+10,center_point_y,center_point_x+10,center_point_y+38)

    return



def create_candy(base_point_x,base_point_y):  ## 以最右边类圆的下圆圆心为基点
    create_arc(base_point_x,base_point_y,3,-180,0)
    create_arc(base_point_x,base_point_y + 10,3,0,180)
    create_line(base_point_x-3,base_point_y,base_point_x-3,base_point_y + 10)
    create_line(base_point_x + 3, base_point_y, base_point_x + 3, base_point_y + 10)

    create_arc(base_point_x - 49,base_point_y,3,-180,0)
    create_arc(base_point_x - 49,base_point_y + 10,3,0,180)
    create_line(base_point_x - 49 -3,base_point_y,base_point_x -49 -3,base_point_y + 10)
    create_line(base_point_x -49 + 3, base_point_y, base_point_x -49 + 3, base_point_y + 10)

    create_arc(base_point_x - 16.5, base_point_y, 7, -90, 0)
    create_arc(base_point_x - 32.5,base_point_y,7,-180,-90)
    create_arc(base_point_x - 16.5, base_point_y + 10, 7, 0, 90)
    create_arc(base_point_x - 32.5,base_point_y + 10,7,90,180)
    create_line(base_point_x - 16.5 + 7, base_point_y,base_point_x - 16.5 + 7, base_point_y + 10)
    create_line(base_point_x - 32.5 - 7, base_point_y, base_point_x - 32.5 - 7, base_point_y + 10)
    create_line(base_point_x - 16.5, base_point_y-7, base_point_x - 32.5, base_point_y -7)
    create_line(base_point_x - 16.5, base_point_y + 10 + 7, base_point_x - 32.5, base_point_y + 10 + 7)


#create_candy(10633.6276,-214173.8392)

def left_1(base_point_x,base_point_y,door_width,small_door_width,tp):   # 以最左侧最上第一个点为基点

    obj = []

    x1 = (door_width / 2 - 25 - small_door_width - 20.5) # 门边板支撑宽度
    x2 = (small_door_width - 7.5)   # 门头板支撑宽度

    if(tp==1):  ## 如果是类型1  支撑的下侧固定长度一个为260 一个为530
        x3 = 260
        x4 = 530
        bia_x3 = 159  # 长度260的口距离下衔接左侧点的距离
        bia_x4 = (x2 + 2) / 2 - ( x4 / 2 )  # 长度530的口距离下衔接右侧点的距离
    else:
        x3 = 320
        x4 = 620
        bia_x3 = 154.5
        bia_x4 = (x2 + 2) / 2 - ( x4 / 2 )

    incise_line = []  # 切割标记线

    incise_line.append(base_point_x)
    incise_line.append(base_point_y)
    incise_line.append(base_point_x + 2)
    incise_line.append(base_point_y)

    incise_line.append(base_point_x + 2 + (door_width / 2 - 25 - small_door_width - 20.5) + 5 + (small_door_width - 7.5) + 2 )
    incise_line.append(base_point_y)
    incise_line.append(base_point_x + 2 + (door_width / 2 - 25 - small_door_width - 20.5) + 5 + (small_door_width - 7.5) + 2 - 2)
    incise_line.append(base_point_y)

    incise_line.append(base_point_x)
    incise_line.append(base_point_y - 74)
    incise_line.append(base_point_x + 2)
    incise_line.append(base_point_y - 74)

    incise_line.append(base_point_x + 2 + (door_width / 2 - 25 - small_door_width - 20.5) + 5 + (small_door_width - 7.5) + 2 + 17)
    incise_line.append(base_point_y - 74)
    incise_line.append(base_point_x + 2 + (door_width / 2 - 25 - small_door_width - 20.5) + 5 + (small_door_width - 7.5) + 2 + 17 - 2)
    incise_line.append(base_point_y - 74)

    for i in range(0, len(incise_line), 4):
        line = create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3])
        obj.append(line)

    coords = []

    coords.append(base_point_x)
    coords.append(base_point_y)

    coords.append(base_point_x + 2)
    coords.append(base_point_y + 14.5)

    coords.append(coords[2] + x1)
    coords.append(coords[3])

    coords.append(coords[4])
    coords.append(coords[5] - 24.5)

    obj.append(create_arc(coords[6]+2,coords[7],2,-180,-90))
    obj.append(create_line(coords[6]+2,coords[7] - 2,coords[6] + 2 + 1,coords[7] - 2))
    obj.append(create_arc(coords[6] + 2 + 1, coords[7], 2, -90, 0))

    coords2 = []

    coords2.append(coords[6] + 2 + 1 + 2)
    coords2.append(coords[7])

    coords2.append(coords2[0])
    coords2.append(coords2[1] + 24.5)

    coords2.append(coords2[2] + x2)
    coords2.append(coords2[3])

    coords2.append(coords2[4] + 2)
    coords2.append(coords2[5] - 14.5)

    coords2.append(coords2[6])
    coords2.append(coords2[7] - 69)

    coords2.append(coords2[8] + 1.2)
    coords2.append(coords2[9])

    coords2.append(coords2[10])
    coords2.append(coords2[11] + 5)

    coords2.append(coords2[12] + 13.8)
    coords2.append(coords2[13])

    obj.append(create_arc(coords2[14],coords2[15] - 2 ,2,0,90))
    obj.append(create_line(coords2[14] + 2,coords2[15] - 2,coords2[14] + 2,coords2[15] - 2 - 8))

    coords3 = []
    coords3.append(base_point_x)
    coords3.append(base_point_y - 74)

    coords3.append(coords3[0] + 2)
    coords3.append(coords3[1] - 14.5)

    if(tp == 1):
        coords3.append(coords3[2] + x1 + 15 - bia_x3 - x3)
    else:
        coords3.append(coords3[2] + bia_x3)
    coords3.append(coords3[3])

    coords3.append(coords3[4])
    coords3.append(coords3[5] + 15)

    coords3.append(coords3[6] + x3)
    coords3.append(coords3[7])

    coords3.append(coords3[8])
    coords3.append(coords3[9] - 15)

    if(tp == 1):
        coords3.append(coords3[10] + bia_x3)
    else:
        coords3.append(coords3[10] + x1 + 15 - bia_x3 - x3)

    coords3.append(coords3[11])

    coords3.append(coords3[12])
    coords3.append(coords3[13] + 24.5)

    obj.append(create_arc(coords3[14] + 2,coords3[15],2,90,180))
    obj.append(create_line(coords3[14] + 2,coords3[15] + 2,coords3[14] + 2 + 1,coords3[15] + 2))
    obj.append(create_arc(coords3[14] + 2 + 1, coords3[15], 2, 0, 90))

    coords4 = []
    coords4.append(coords3[14] + 2 + 1 + 2)
    coords4.append(coords3[15])

    coords4.append(coords4[0])
    coords4.append(coords4[1] - 24.5)

    coords4.append(coords4[2] + bia_x4)
    coords4.append(coords4[3])

    coords4.append(coords4[4])
    coords4.append(coords4[5] + 15)

    coords4.append(coords4[6] + x4)
    coords4.append(coords4[7])

    coords4.append(coords4[8])
    coords4.append(coords4[9] - 15)

    coords4.append(coords4[2] + x2 + 2 - 2)
    coords4.append(coords4[11])

    coords4.append(coords4[12] + 2)
    coords4.append(coords4[13] + 14.5)

    new_line1 = acad.model.AddLightWeightPolyline(array.array("d", coords))
    new_line1.Color = 1
    new_line1.Closed = False
    obj.append(new_line1)
    #new_line1.Mirror(mirror_line_start,mirror_line_end)


    new_line2 = acad.model.AddLightWeightPolyline(array.array("d", coords2))
    new_line2.Color = 1
    new_line2.Closed = False
    obj.append(new_line2)
    #new_line2.Mirror(mirror_line_start, mirror_line_end)



    new_line3 = acad.model.AddLightWeightPolyline(array.array("d", coords3))
    new_line3.Color = 1
    new_line3.Closed = False
    obj.append(new_line3)
    #new_line3.Mirror(mirror_line_start, mirror_line_end)


    new_line4 = acad.model.AddLightWeightPolyline(array.array("d", coords4))
    new_line4.Color = 1
    new_line4.Closed = False
    obj.append(new_line4)
   #new_line4.Mirror(mirror_line_start, mirror_line_end)

    y1 = base_point_y - 7.4196
    y2 = base_point_y - 74 + 7.4196
    bia_cy = (y2 - y1) / 2
    bia_cx = 30 * math.sin(math.radians(10))



    ##绘制左侧圆口
    obj.append(create_arc(base_point_x + bia_cx, (y1+y2)/2, 30,-100,100))
    start_point = obj[-1].StartPoint  # 圆弧的起点
    end_point = obj[-1].EndPoint  # 圆弧的终点
    obj.append(create_line(base_point_x,base_point_y,end_point[0],end_point[1]))
    obj.append(create_line(base_point_x, base_point_y - 74, start_point[0], start_point[1]))


    mirror_line_start = APoint(base_point_x ,base_point_y - 138.5)
    mirror_line_end = APoint(base_point_x + 100 ,base_point_y - 138.5)
    for i in range(len(obj)):
        obj[i].Mirror(mirror_line_start,mirror_line_end)


    create_candy(base_point_x + 2 + 5 + x1 + x2 + 2 - 11.5, 2 * mirror_line_start.y -base_point_y + 27)


    return

# left_1(9189.1276 ,-213923.8392,3000,840,1)
# left_1(9160.0982 ,-215936.9578,3000,840,0)

left_1(-3343.8337, 171.4765,840,1,1)













def right_1(base_point_x,base_point_y,door_width,small_door_width,tp):  # 以最右侧最上第一个点为基点

    obj = []

    x1 = (door_width / 2 - 25 - small_door_width - 20.5)  # 门边板支撑宽度
    x2 = (small_door_width + 24.5)  # 门头板支撑宽度


    if(tp==1):  ## 如果是类型1  支撑的下侧固定长度一个为260 一个为530
        x3 = 260
        x4 = 530
        bia_x3 = 159  # 长度260的口距离下衔接左侧点的距离
        bia_x4 = (small_door_width - 3.9) / 2 - (x4 / 2)  # 长度530的口距离下衔接右侧点的距离
    else:
        x3 = 320
        x4 = 620
        bia_x3 = 154.5
        bia_x4 = (small_door_width - 3.9) / 2 - (x4 / 2)

    incise_line = []  # 切割标记线

    incise_line.append(base_point_x)
    incise_line.append(base_point_y)
    incise_line.append(base_point_x - 2)
    incise_line.append(base_point_y)

    incise_line.append(base_point_x - 2 - (door_width / 2 - 25 - small_door_width - 2 - 20.5) - 5 - (small_door_width + 24.5) -2 )
    incise_line.append(base_point_y)
    incise_line.append(base_point_x - 2 - (door_width / 2 - 25 - small_door_width - 2 - 20.5) - 5 - (small_door_width + 24.5) -2 + 2)
    incise_line.append(base_point_y)

    incise_line.append(base_point_x)
    incise_line.append(base_point_y - 74)
    incise_line.append(base_point_x - 2)
    incise_line.append(base_point_y - 74)

    incise_line.append(base_point_x - 2 - (door_width / 2 - 25 - small_door_width - 2 - 20.5) - 5 - (small_door_width + 24.5) - 2 + 15.4)
    incise_line.append(base_point_y - 74)
    incise_line.append(base_point_x - 2 - (door_width / 2 - 25 - small_door_width - 2 - 20.5) - 5 - (small_door_width + 24.5) -2 + 15.4 + 2)
    incise_line.append(base_point_y - 74)

    for i in range(0, len(incise_line), 4):
        obj.append(create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3]))

    coords = []

    coords.append(base_point_x)
    coords.append(base_point_y)

    coords.append(base_point_x - 2)
    coords.append(base_point_y + 14.5)

    coords.append(coords[2] - x1)
    coords.append(coords[3])

    coords.append(coords[4])
    coords.append(coords[5] - 24.5)

    obj.append(create_arc(coords[6] - 2, coords[7], 2, -90, 0))
    obj.append(create_line(coords[6] - 2, coords[7] - 2, coords[6] - 2 - 1, coords[7] - 2))
    obj.append(create_arc(coords[6] - 2 - 1, coords[7], 2, -180, -90))

    coords2 = []

    coords2.append(coords[6] - 2 - 1 - 2)
    coords2.append(coords[7])

    coords2.append(coords2[0])
    coords2.append(coords2[1] + 24.5)

    coords2.append(coords2[2] - x2)
    coords2.append(coords2[3])

    coords2.append(coords2[4] - 2)
    coords2.append(coords2[5] - 14.5)

    coords2.append(coords2[6])
    coords2.append(coords2[7] - 51)

    obj.append(create_arc(coords2[8] + 2, coords2[9], 2, -180, -90))

    coords3 = []
    coords3.append(base_point_x)
    coords3.append(base_point_y - 74)

    coords3.append(coords3[0] - 2)
    coords3.append(coords3[1] - 14.5)

    if(tp==1):
        coords3.append(coords3[2] - (x1 + 15 - bia_x3 - x3))
    else:
        coords3.append(coords3[2] - bia_x3)
    coords3.append(coords3[3])

    coords3.append(coords3[4])
    coords3.append(coords3[5] + 15)

    coords3.append(coords3[6] - x3)
    coords3.append(coords3[7])

    coords3.append(coords3[8])
    coords3.append(coords3[9] - 15)

    if(tp == 1):
        coords3.append(coords3[10] - bia_x3)
    else:
        coords3.append(coords3[10] - (x1 + 15 - bia_x3 - x3))
    coords3.append(coords3[11])

    coords3.append(coords3[12])
    coords3.append(coords3[13] + 24.5)

    obj.append(create_arc(coords3[14] - 2, coords3[15], 2, 0, 90))
    obj.append(create_line(coords3[14] - 2, coords3[15] + 2, coords3[14] - 2 - 1, coords3[15] + 2))
    obj.append(create_arc(coords3[14] - 2 - 1, coords3[15], 2, 90, 180))

    coords4 = []
    coords4.append(coords3[14] - 2 - 1 - 2)
    coords4.append(coords3[15])

    coords4.append(coords4[0])
    coords4.append(coords4[1] - 24.5)

    coords4.append(coords4[2] - bia_x4)
    coords4.append(coords4[3])

    coords4.append(coords4[4])
    coords4.append(coords4[5] + 15)

    coords4.append(coords4[6] - x4)
    coords4.append(coords4[7])

    coords4.append(coords4[8])
    coords4.append(coords4[9] - 15)

    coords4.append(coords4[2] - (small_door_width - 3.9) + 2)
    coords4.append(coords4[11])

    coords4.append(coords4[12] - 2)
    coords4.append(coords4[13] + 14.5)

    coords4.append(coords4[14])
    coords4.append(coords4[15] + 26)

    coords4.append(coords4[16] - 1.6)
    coords4.append(coords4[17])

    coords4.append(coords4[18])
    coords4.append(coords4[19]- 5)

    coords4.append(coords4[20] - 11.8)
    coords4.append(coords4[21])

    new_line1 = acad.model.AddLightWeightPolyline(array.array("d", coords))
    new_line1.Color = 1
    new_line1.Closed = False
    obj.append(new_line1)
    # new_line1.Mirror(mirror_line_start,mirror_line_end)

    new_line2 = acad.model.AddLightWeightPolyline(array.array("d", coords2))
    new_line2.Color = 1
    new_line2.Closed = False
    obj.append(new_line2)
    # new_line2.Mirror(mirror_line_start, mirror_line_end)

    new_line3 = acad.model.AddLightWeightPolyline(array.array("d", coords3))
    new_line3.Color = 1
    new_line3.Closed = False
    obj.append(new_line3)
    # new_line3.Mirror(mirror_line_start, mirror_line_end)

    new_line4 = acad.model.AddLightWeightPolyline(array.array("d", coords4))
    new_line4.Color = 1
    new_line4.Closed = False
    obj.append(new_line4)
    # new_line4.Mirror(mirror_line_start, mirror_line_end)

    ##绘制左侧圆口
    create_line(base_point_x, base_point_y, base_point_x, base_point_y - 7.4196)
    create_line(base_point_x, base_point_y - 74, base_point_x, base_point_y - 74 + 7.4196)
    create_arc(base_point_x - 5, base_point_y - 37, 30, 80, 280)

    mirror_line_start = APoint(base_point_x,base_point_y - 138.5)
    mirror_line_end = APoint(base_point_x - 100,base_point_y - 138.5)
    for i in range(len(obj)):
        obj[i].Mirror(mirror_line_start,mirror_line_end)

    create_line(base_point_x, 2 * mirror_line_start.y - base_point_y, base_point_x, 2 * mirror_line_start.y - (base_point_y - 74))

    create_candy(base_point_x - 2 - 5 - x1 - x2 - 2 + 74.5 , 2 * mirror_line_start.y - base_point_y + 31.5)

    create_line(base_point_x - 2 - 5 - x1 - x2 - 2 + 39.85,base_point_y - 26.35,base_point_x - 2 - 5 - x1 - x2 - 2 + 39.85 + 20.3 ,base_point_y - 26.35)
    create_line(base_point_x - 2 - 5 - x1 - x2 - 2 + 39.85, base_point_y - 26.35,base_point_x - 2 - 5 - x1 - x2 - 2 + 39.85, base_point_y - 26.35 - 20.3)
    create_line(base_point_x - 2 - 5 - x1 - x2 - 2 + 39.85 , base_point_y - 26.35 - 20.3,base_point_x - 2 - 5 - x1 - x2 - 2 + 39.85 + 20.3, base_point_y - 26.35 - 20.3)
    create_line(base_point_x - 2 - 5 - x1 - x2 - 2 + 39.85 + 20.3, base_point_y - 26.35,base_point_x - 2 - 5 - x1 - x2 - 2 + 39.85 + 20.3, base_point_y - 26.35 - 20.3)

    return

# right_1(12433.1276 ,-213923.8392,3000,840,1)
# right_1(12404.0982  ,-215936.9578,3000,840,0)


def left_3(base_point_x,base_point_y, width,tp):  ## 左下第一个支撑  门边板下边支撑  以左上侧折弯点的左顶点为基点

    obj = []

    # 宽度计算公式  width = x1 + 3
    if(tp == 1):
        x3 = 260
        bia_x3 = 145
    else:
        x3 = 320
        bia_x3 = 154.5


    incise_line = []  # 切割标记线

    incise_line.append(base_point_x)
    incise_line.append(base_point_y)
    incise_line.append(base_point_x + 2)
    incise_line.append(base_point_y)

    incise_line.append(base_point_x)
    incise_line.append(base_point_y - 74)
    incise_line.append(base_point_x + 2)
    incise_line.append(base_point_y - 74)

    incise_line.append(base_point_x + width)
    incise_line.append(base_point_y - 74)
    incise_line.append(base_point_x + width - 2)
    incise_line.append(base_point_y - 74)

    incise_line.append(base_point_x + width + 15)
    incise_line.append(base_point_y)
    incise_line.append(base_point_x + width + 15 - 2)
    incise_line.append(base_point_y)

    for i in range(0, len(incise_line), 4):
        obj.append(create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3]))



    coords = []
    coords.append(base_point_x)
    coords.append(base_point_y)

    coords.append(base_point_x + 2)
    coords.append(base_point_y + 14.5)

    if(tp == 1):
        coords.append(coords[2] + width - x3 - bia_x3 - 2)
    else:
        coords.append(coords[2] + bia_x3)
    coords.append(coords[3])

    coords.append(coords[4])
    coords.append(coords[5] - 15)

    coords.append(coords[6] + x3)
    coords.append(coords[7])

    coords.append(coords[8])
    coords.append(coords[9] + 15)

    if(tp == 1):
        coords.append(coords[10] + bia_x3 + 13)
    else:
        coords.append(coords[10] + width - 2 - x3 - bia_x3 + 13)
    coords.append(coords[11])

    coords.append(coords[12] + 2)
    coords.append(coords[13] - 14.5)

    coords.append(coords[14])
    coords.append(coords[15] - 8)

    obj.append(create_arc(coords[16] -2 ,coords[17],2,-90,0))

    coords2 = []
    coords2.append(coords[16] - 2)
    coords2.append(coords[17] - 2)

    coords2.append(coords2[0] - 11.8)
    coords2.append(coords2[1])

    coords2.append(coords2[2])
    coords2.append(coords2[3] + 5)

    coords2.append(coords2[4] - 1.2)
    coords2.append(coords2[5])

    coords2.append(coords2[6])
    coords2.append(coords2[7] - 69)

    coords2.append(coords2[8] - 2)
    coords2.append(coords2[9] - 14.5)

    obj.append(create_arc(coords2[8] - 34,coords2[9] + 32, 9.75, -90,90))
    obj.append(create_arc(coords2[8] - 34 - 66, coords2[9] + 32, 9.75, 90, 270))
    obj.append(create_line(coords2[8] - 34,coords2[9] + 32 - 9.75,coords2[8] - 34 - 66,coords2[9] + 32 - 9.75))
    obj.append(create_line(coords2[8] - 34, coords2[9] + 32 + 9.75, coords2[8] - 34 - 66, coords2[9] + 32 + 9.75))

    obj.append(create_line(base_point_x,base_point_y,base_point_x,base_point_y- 7.4196))
    obj.append(create_line(base_point_x, base_point_y - 74, base_point_x, base_point_y - 74 + 7.4196))
    obj.append(create_arc(base_point_x + 5, base_point_y - 37, 30,-100,100))

    coords3 = []
    coords3.append(base_point_x)
    coords3.append(base_point_y - 74)

    coords3.append(coords3[0] + 2)
    coords3.append(coords3[1] - 14.5)

    coords3.append(coords3[2] + width - 2 - 2)
    coords3.append(coords3[3])

    new_line1 = acad.model.AddLightWeightPolyline(array.array("d", coords))
    new_line1.Color = 1
    new_line1.Closed = False
    obj.append(new_line1)

    new_line2 = acad.model.AddLightWeightPolyline(array.array("d", coords2))
    new_line2.Color = 1
    new_line2.Closed = False
    obj.append(new_line2)

    new_line3 = acad.model.AddLightWeightPolyline(array.array("d", coords3))
    new_line3.Color = 1
    new_line3.Closed = False
    obj.append(new_line3)

    mirror_line_start = APoint((12488.6276 +9133.6276 )/2,base_point_y)
    mirror_line_end = APoint((12488.6276 +9133.6276 )/2,base_point_y - 50)
    for i in range(len(obj)):
        obj[i].Mirror(mirror_line_start,mirror_line_end)


    return

# left_3(9133.6276, -214429.8392,617.5,1)
# left_3( 9104.5982 , -216442.9578,617.5,0)


def left_4(base_point_x,base_point_y,width,tp):  ## 左下角支撑 以左上焊点左侧端点为基点   门边板外支撑

    obj = []

    # 宽度计算公式  width = x1 + 3   宽度为left3的宽度数值
    if(tp == 1):
        x3 = 260
        bia_x3 = 145
    else:
        x3 = 320
        bia_x3 = 65.5

    changeable_width = width - 55.5 - x3 - bia_x3 - 35.5

    incise_line = []  # 切割标记线

    incise_line.append(base_point_x)
    incise_line.append(base_point_y)
    incise_line.append(base_point_x + 2)
    incise_line.append(base_point_y)

    incise_line.append(base_point_x + 35.5 + changeable_width + x3 + bia_x3 + 15)
    incise_line.append(base_point_y)
    incise_line.append(base_point_x + 35.5 + changeable_width + x3 + bia_x3 + 15 - 2)
    incise_line.append(base_point_y)

    incise_line.append(base_point_x)
    incise_line.append(base_point_y - 74)
    incise_line.append(base_point_x + 2)
    incise_line.append(base_point_y - 74)

    incise_line.append(base_point_x + 35.5 + changeable_width + x3 + bia_x3)
    incise_line.append(base_point_y - 74)
    incise_line.append(base_point_x + 35.5 + changeable_width + x3 + bia_x3 - 2)
    incise_line.append(base_point_y - 74)

    for i in range(0, len(incise_line), 4):
        obj.append(create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3]))

    coords = []

    coords.append(base_point_x)
    coords.append(base_point_y + 14.5)

    coords.append(coords[0] + 6.5)
    coords.append(coords[1])

    coords.append(coords[2] + 14.5)
    coords.append(coords[3] - 14.5)

    obj.append(create_line(coords[4],coords[5], coords[4], coords[5] - 2 ))
    obj.append(create_line(coords[4], coords[5] - 9, coords[4], coords[5]-34))
    obj.append(create_line(coords[4], coords[5]-42, coords[4], coords[5]-68))
    obj.append(create_line(coords[4], coords[5] - 72, coords[4], coords[5] - 74))

    coords.append(coords[4] + 14.5)
    coords.append(coords[5] + 14.5)

    if(tp == 1):
        coords.append(coords[6] + changeable_width)
    else:
        coords.append(coords[6] + bia_x3)
    coords.append(coords[7])

    coords.append(coords[8])
    coords.append(coords[9] - 15)

    coords.append(coords[10] + x3)
    coords.append(coords[11])

    coords.append(coords[12])
    coords.append(coords[13] + 15)

    if(tp == 1):
        coords.append(coords[14] + bia_x3 + 13)
    else:
        coords.append(coords[14] + changeable_width + 13)
    coords.append(coords[15])

    coords.append(coords[16] + 2)
    coords.append(coords[17] - 14.5)

    coords.append(coords[18])
    coords.append(coords[19] - 8)

    obj.append(create_arc(coords[20] - 2,coords[21],2,-90,0))

    coords2 = []
    coords2.append(base_point_x)
    coords2.append(base_point_y - 88.5)

    coords2.append(coords2[0] + 6.5)
    coords2.append(coords2[1])

    coords2.append(coords2[2] + 14.5)
    coords2.append(coords2[3] + 14.5)

    coords2.append(coords2[4] + 14.5)
    coords2.append(coords2[5] - 14.5)

    coords2.append(coords2[6] + changeable_width + x3 + bia_x3 - 2)
    coords2.append(coords2[7])

    coords2.append(coords2[8] + 2)
    coords2.append(coords2[9] + 14.5)

    coords2.append(coords2[10])
    coords2.append(coords2[11] + 69)

    coords2.append(coords2[12] + 1.2 )
    coords2.append(coords2[13])

    coords2.append(coords2[14])
    coords2.append(coords2[15] - 5)

    coords2.append(coords2[16] + 11.8)
    coords2.append(coords2[17])

    ## 绘制左侧内部孔
    obj.append(create_arc(base_point_x + 57,base_point_y - 37,6,90,270))
    obj.append(create_arc(base_point_x + 57 + 12.5,base_point_y - 37,7.5,-127,127))
    obj.append(create_line(base_point_x + 57,base_point_y - 37 + 6,base_point_x + 57 + 8,base_point_y - 37 + 6))
    obj.append(create_line(base_point_x + 57, base_point_y - 37 - 6, base_point_x + 57 + 8, base_point_y - 37 - 6))

    ## 绘制右侧内部孔
    obj.append(create_arc(coords2[10] - 34,coords2[11] + 32,6.75,-90,90))
    obj.append(create_arc(coords2[10] - 34 - 56, coords2[11] + 32, 6.75, 90, 270))
    obj.append(create_line(coords2[10] - 34, coords2[11] + 32 + 6.75,coords2[10] - 34 - 56, coords2[11] + 32 + 6.75))
    obj.append(create_line(coords2[10] - 34, coords2[11] + 32 - 6.75, coords2[10] - 34 - 27, coords2[11] + 32 - 6.75))
    obj.append(create_line(coords2[10] - 34 - 27, coords2[11] + 32 - 6.75, coords2[10] - 34 - 27 - 1, coords2[11] + 32 - 6.75 - 2))
    obj.append(create_line(coords2[10] - 34 - 27 -2, coords2[11] + 32 - 6.75, coords2[10] - 34 - 27 - 1,coords2[11] + 32 - 6.75 - 2))
    obj.append(create_line(coords2[10] - 34 - 29, coords2[11] + 32 - 6.75, coords2[10] - 34 - 56, coords2[11] + 32 - 6.75))

    obj.append(create_line(base_point_x, base_point_y + 14.5,base_point_x,base_point_y - 88.5))

    new_line1 = acad.model.AddLightWeightPolyline(array.array("d", coords))
    new_line1.Color = 1
    new_line1.Closed = False
    obj.append(new_line1)

    new_line2 = acad.model.AddLightWeightPolyline(array.array("d", coords2))
    new_line2.Color = 1
    new_line2.Closed = False
    obj.append(new_line2)

    mirror_line_start = APoint((9189.1276+12433.1276 )/2,-214632.8392)
    mirror_line_end = APoint((9189.1276 +12433.1276)/2,-214532.8392)
    for i in range(len(obj)):
        obj[i].Mirror(mirror_line_start,mirror_line_end)

    return


# left_4(9189.1276,-214632.8392,617.5,1)
# left_4(9160.0982 ,-216645.9578,617.5,0)

def left_5(base_point_x,base_point_y, width,tp):# 以左上侧折弯点左端点为基点   左侧小门支撑

    obj = []

    if(tp == 1):
        x4 = 530
        bia_x4 = (width + 2.6) / 2 - (x4 / 2) - 2

    else:
        x4 = 620
        bia_x4 = (width + 2.6) / 2 - (x4 / 2) - 2

    changeable_width = width - 16.4 - bia_x4 - x4

    incise_line = []  # 切割标记线
    incise_line.append(base_point_x)
    incise_line.append(base_point_y)
    incise_line.append(base_point_x + 2)
    incise_line.append(base_point_y)

    coords = []

    coords.append(base_point_x)
    coords.append(base_point_y - 45)

    obj.append(create_arc(coords[0]+2,coords[1],2,180,270))

    coords.append(base_point_x)
    coords.append(base_point_y)

    coords.append(base_point_x + 2)
    coords.append(base_point_y + 14.5)

    coords.append(coords[4] + width - 2 - 2)
    coords.append(coords[5])

    coords.append(coords[6] + 2)
    coords.append(coords[7] - 14.5)

    incise_line.append(coords[8])
    incise_line.append(coords[9])
    incise_line.append(coords[8] - 2)
    incise_line.append(coords[9])

    ##绘制右侧孔
    obj.append(create_arc(coords[8] - 34,coords[9]-32,6.75,-90,90))
    obj.append(create_arc(coords[8] - 34 - 56, coords[9]-32, 6.75, 90, 270))
    obj.append(create_line(coords[8] - 34, coords[9]-32 - 6.75,coords[8] - 34 - 56, coords[9]-32 - 6.75))
    obj.append(create_line(coords[8] - 34, coords[9]-32 + 6.75, coords[8] - 34 - 27, coords[9]-32 + 6.75))
    obj.append(create_line(coords[8] - 34 - 27, coords[9]-32 + 6.75, coords[8] - 34 - 27 - 1, coords[9]-32 + 6.75 + 2))
    obj.append(create_line(coords[8] - 34 - 27 -2, coords[9]-32 + 6.75, coords[8] - 34 - 27 - 1,coords[9]-32 + 6.75 + 2))
    obj.append(create_line(coords[8] - 34 - 29, coords[9]-32 + 6.75, coords[8] - 34 - 56, coords[9]-32 + 6.75))



    coords.append(coords[8])
    coords.append(coords[9] - 69)

    coords.append(coords[10] + 1.2)
    coords.append(coords[11])

    coords.append(coords[12])
    coords.append(coords[13] + 5)

    coords.append(coords[14] + 13.8)
    coords.append(coords[15])

    obj.append(create_arc(coords[16],coords[17]-2,2,0,90))

    coords2 = []

    coords2.append(coords[0] + 2)
    coords2.append(coords[1] - 2)

    coords2.append(coords2[0] + 10.8)
    coords2.append(coords2[1])

    coords2.append(coords2[2])
    coords2.append(coords2[3] + 5)

    coords2.append(coords2[4] + 1.6)
    coords2.append(coords2[5])

    coords2.append(coords2[6])
    coords2.append(coords2[7] - 32)

    incise_line.append(coords2[8])
    incise_line.append(coords2[9])
    incise_line.append(coords2[8] + 2)
    incise_line.append(coords2[9])

    coords2.append(coords2[8] + 2)
    coords2.append(coords2[9] - 14.5)

    coords2.append(coords2[10] + bia_x4)
    coords2.append(coords2[11])

    coords2.append(coords2[12])
    coords2.append(coords2[13] + 15)

    coords2.append(coords2[14] + x4)
    coords2.append(coords2[15])

    coords2.append(coords2[16])
    coords2.append(coords2[17] - 15)

    coords2.append(coords2[8] + width + 2.6 - 2)
    coords2.append(coords2[19])

    coords2.append(coords2[20] + 2)
    coords2.append(coords2[21] + 14.5)

    incise_line.append(coords2[22])
    incise_line.append(coords2[23])
    incise_line.append(coords2[22] - 2)
    incise_line.append(coords2[23])

    coords2.append(coords2[22])
    coords2.append(coords2[23] + 8)

    for i in range(0, len(incise_line), 4):
        obj.append(create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3]))

    new_line1 = acad.model.AddLightWeightPolyline(array.array("d", coords))
    new_line1.Color = 1
    new_line1.Closed = False
    obj.append(new_line1)

    new_line2 = acad.model.AddLightWeightPolyline(array.array("d", coords2))
    new_line2.Color = 1
    new_line2.Closed = False
    obj.append(new_line2)

    mirror_line_start = APoint(9812.1276 ,(-214429.8392 -214706.8392)/2)
    mirror_line_end = APoint(10645.1276 ,(-214429.8392 -214706.8392)/2)
    for i in range(len(obj)):
        obj[i].Mirror(mirror_line_start,mirror_line_end)


    return

# left_5(9812.1276 ,-214429.8392,833,1)
# left_5(9783.0982 ,-216442.9578,833,0)

def right_2(base_point_x,base_point_y,width,tp):## 以左上折弯点左端点为基点    小门支撑，长

    obj = []

    if(tp == 1):
        x4 = 530
        bia_x4 = (width - 29.8) / 2 - (x4 / 2) - 2
    else:
        x4 = 620
        bia_x4 = (width - 29.8) / 2 - (x4 / 2) - 2

    changeable_width = width - 16.4 - x4 - bia_x4 - 17.4

    incise_line = []  # 切割标记线
    incise_line.append(base_point_x)
    incise_line.append(base_point_y)
    incise_line.append(base_point_x + 2)
    incise_line.append(base_point_y)

    coords = []

    coords.append(base_point_x)
    coords.append(base_point_y - 51)

    obj.append(create_arc(coords[0]+2,coords[1],2,180,270))

    coords.append(base_point_x)
    coords.append(base_point_y)

    coords.append(base_point_x + 2)
    coords.append(base_point_y + 14.5)

    coords.append(coords[4] + width - 2 - 2)
    coords.append(coords[5])

    coords.append(coords[6] + 2)
    coords.append(coords[7] - 14.5)

    incise_line.append(coords[8])
    incise_line.append(coords[9])
    incise_line.append(coords[8] - 2)
    incise_line.append(coords[9])

    coords.append(coords[8])
    coords.append(coords[9] - 45)

    obj.append(create_arc(coords[10] - 2, coords[11], 2, -90, 0))

    coords2 = []

    coords2.append(coords[0] + 2)
    coords2.append(coords[1] - 2)

    coords2.append(coords2[0] + 11.8)
    coords2.append(coords2[1])

    coords2.append(coords2[2])
    coords2.append(coords2[3] + 5)

    coords2.append(coords2[4] + 1.6)
    coords2.append(coords2[5])

    coords2.append(coords2[6])
    coords2.append(coords2[7] - 26)

    incise_line.append(coords2[8])
    incise_line.append(coords2[9])
    incise_line.append(coords2[8] + 2)
    incise_line.append(coords2[9])

    coords2.append(coords2[8] + 2)
    coords2.append(coords2[9] - 14.5)

    coords2.append(coords2[10] + bia_x4)
    coords2.append(coords2[11])

    coords2.append(coords2[12])
    coords2.append(coords2[13] + 15)

    coords2.append(coords2[14] + x4)
    coords2.append(coords2[15])

    coords2.append(coords2[16])
    coords2.append(coords2[17] - 15)

    coords2.append(coords2[8] + width - 29.8 - 2)
    coords2.append(coords2[19] )

    coords2.append(coords2[20] + 2)
    coords2.append(coords2[21] + 14.5)

    incise_line.append(coords2[22])
    incise_line.append(coords2[23])
    incise_line.append(coords2[22] - 2)
    incise_line.append(coords2[23])

    coords2.append(coords2[22])
    coords2.append(coords2[23] + 32)

    coords2.append(coords2[24] + 1.6)
    coords2.append(coords2[25])

    coords2.append(coords2[26])
    coords2.append(coords2[27] - 5)

    coords2.append(coords2[28] + 10.8)
    coords2.append(coords2[29])

    ##绘制左侧孔
    obj.append(create_arc(base_point_x + 47,base_point_y-35,6.75,90,270))
    obj.append(create_arc(base_point_x + 47 + 56, base_point_y - 35, 6.75, -90, 90))
    obj.append(create_line(base_point_x + 47,base_point_y-35-6.75,base_point_x + 47 + 56, base_point_y-35-6.75))
    obj.append(create_line(base_point_x + 47,base_point_y-35+6.75, base_point_x + 47 + 27,base_point_y-35+6.75))
    obj.append(create_line(base_point_x + 47 + 27, base_point_y-35+6.75, base_point_x + 47 + 27 + 1, base_point_y-35+6.75+2))
    obj.append(create_line(base_point_x + 47 + 27 + 1, base_point_y-35+6.75+2, base_point_x + 47 + 27 + 2, base_point_y-35+6.75))
    obj.append(create_line(base_point_x + 47 + 27 + 2,base_point_y-35+6.75, base_point_x + 47 + 27 + 2 + 27,base_point_y-35+6.75))

    for i in range(0, len(incise_line), 4):
        obj.append(create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3]))

    new_line1 = acad.model.AddLightWeightPolyline(array.array("d", coords))
    new_line1.Color = 1
    new_line1.Closed = False
    obj.append(new_line1)

    new_line2 = acad.model.AddLightWeightPolyline(array.array("d", coords2))
    new_line2.Color = 1
    new_line2.Closed = False
    obj.append(new_line2)

    mirror_line_start = APoint(10945.1276 ,(-214429.8392 -214706.8392)/2)
    mirror_line_end = APoint(11810.1276 ,(-214429.8392 -214706.8392)/2)
    for i in range(len(obj)):
        obj[i].Mirror(mirror_line_start,mirror_line_end)

    return

# right_2(10945.1276,-214429.8392,865,1)
# right_2(10916.0982,-216442.9578,865,0)


































































































































































































































