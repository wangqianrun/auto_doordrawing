import pyautocad
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

# file_path = r"D:\CAD\new.dxf"
# acad.doc.SaveAs(file_path,13)

# mirror_line_start = APoint(-126976.8108 + 1000,-135899.2087 - 100)
# mirror_line_end = APoint(-126976.8108 + 1000,-128949.2087  + 100)
# # for obj in acad.model:
# #     if(obj.Color == 5):
# #         try:
# #         # 执行镜像操作
# #             acad.doc.SendCommand(f'Mirror {obj.ObjectID} {mirror_line_start.x},{mirror_line_start.y} {mirror_line_end.x},{mirror_line_end.y} No\n')
# #             print(f"Object {obj.ObjectID} mirrored.")
# #         except Exception as e:
# #             print(f"Failed to mirror object {obj.ObjectID}: {str(e)}")
#
#
# # 遍历模型空间中的所有对象并进行镜像
# for obj in acad.model:
#     try:
#         # 执行镜像操作
#         #obj.TransformBy(mirror_matrix)
#         obj.Mirror(mirror_line_start, mirror_line_end)
#         print(f"Object {obj.ObjectID} mirrored.")
#     except Exception as e:
#         print(f"Failed to mirror object {obj.ObjectID}: {str(e)}")

def create_arc(x,y,radius,start_angle,end_angle):
    center_point = APoint(x,y)
    start_angle = math.radians(start_angle)
    end_angle = math.radians(end_angle)
    arc = acad.model.AddArc(center_point,radius,start_angle,end_angle)
    arc.Color = 1
    return

def create_line(x1,y1,x2,y2):
    p1 = APoint(x1,y1)
    p2 = APoint(x2,y2)
    line = acad.model.AddLine(p1,p2)
    line.Color = 1


def create_rectangle(base_point_x,base_point_y,len_x,len_y): ##以左下角为基点
    coords = []
    coords.append(base_point_x)
    coords.append(base_point_y)
    coords.append(base_point_x)
    coords.append(base_point_y + len_y)
    coords.append(base_point_x + len_x)
    coords.append(base_point_y + len_y)
    coords.append(base_point_x + len_x)
    coords.append(base_point_y)
    new_line = acad.model.AddLightWeightPolyline(array.array("d", coords))
    new_line.Color = 1
    new_line.Closed = True

    return




def create_four_rounded_rectangle(base_point_x,base_point_y,len_x,len_y):  #四角圆角矩形 以左下角圆心为基点
       create_arc(base_point_x,base_point_y,2,180,270)
       create_arc(base_point_x + len_x, base_point_y, 2, -90, 0)
       create_arc(base_point_x, base_point_y + len_y, 2, 90, 180)
       create_arc(base_point_x + len_x, base_point_y + len_y, 2, 0, 90)
       create_line(base_point_x, base_point_y - 2, base_point_x + len_x, base_point_y - 2)
       create_line(base_point_x - 2, base_point_y, base_point_x - 2, base_point_y + len_y)
       create_line(base_point_x, base_point_y + len_y + 2, base_point_x + len_x, base_point_y + len_y + 2)
       create_line(base_point_x + len_x + 2, base_point_y, base_point_x + len_x + 2, base_point_y + len_y)

       return


def create_two_rounded_rectangle_up(base_point_x,base_point_y,len_x,len_y):  # 上两角圆角矩形 以左上角圆心为基点
    create_arc(base_point_x, base_point_y, 1, 90, 180)
    create_arc(base_point_x + len_x, base_point_y, 1, 0, 90)
    create_line(base_point_x,base_point_y + 1, base_point_x + len_x, base_point_y + 1)
    create_line(base_point_x -1, base_point_y, base_point_x - 1 , base_point_y - len_y)
    create_line(base_point_x -1, base_point_y - len_y, base_point_x + len_x + 1, base_point_y - len_y)
    create_line(base_point_x + len_x + 1,base_point_y, base_point_x + len_x + 1, base_point_y - len_y)

    return



def create_two_rounded_rectangle_down(base_point_x, base_point_y, len_x, len_y):  # 下两角圆角矩形 以左下角圆心为基点
    create_arc(base_point_x, base_point_y, 1, 180, 270)
    create_arc(base_point_x + len_x, base_point_y, 1, -90, 0)
    create_line(base_point_x, base_point_y - 1, base_point_x + len_x, base_point_y - 1)
    create_line(base_point_x -1, base_point_y + len_y, base_point_x + len_x + 1, base_point_y +len_y)
    create_line(base_point_x - 1, base_point_y, base_point_x - 1, base_point_y +len_y)
    create_line(base_point_x + len_x + 1, base_point_y, base_point_x + len_x + 1, base_point_y +len_y)

    return
# create_four_rounded_rectangle(-128288.9108 ,-135635.2087,34.5,176.5 )
# create_two_rounded_rectangle_up(-128211.6608,-134519.9587,38.5,144.25)
# create_two_rounded_rectangle_down(-128211.6608,-135118.4587,38.5,134.25)

def create_Cylinder_hole_down(center_point_x,center_point_y):
    c_p = [-128520.3188, -134802.8228, -128498.3929, -134804.6264, -128503.3188, -134819.3228, -128504.6940,
           -134834.2596, -128520.3188, -134825.3228, -128535.9436, -134834.2596, -128537.3188, -134819.3228,
           -128542.2447, -134804.6264]
    bia = []
    for i in range(0,len(c_p),2):
        bia.append(c_p[i]-c_p[0])
        bia.append(c_p[i+1]-c_p[1])

    start_angle = [-5, 175, -95, 85, -150, 30, 109, -71]
    end_angle = [185, 251, 71, 150, -30, 95, 276, 5]
    radius = [13.5, 8.5, 7, 8, 10, 8, 7, 8.5]
    for i in range(len(start_angle)):
        create_arc(center_point_x + bia[i*2], center_point_y+bia[i * 2 + 1], radius[i], start_angle[i], end_angle[i])

    return
# create_Cylinder_hole_down(-127830.1108 , -130893.7087)


def create_Cylinder_hole_up(center_point_x,center_point_y):
    c_p = [-128498.0816,-134681.4235,-128503.0076,-134666.7270,-128504.3828,-134651.7902,-128520.0076,-134660.7270,-128535.6323,-134651.7902,-128537.0076,-134666.7270,-128541.9335,-134681.4235,-128520.0076,-134683.2270]
    bia = []
    for i in range(0,len(c_p),2):
        bia.append(c_p[i]-c_p[14])
        bia.append(c_p[i+1]-c_p[15])

    start_angle = [109, -71, -150, 30, -95, 85, -5, -185]
    end_angle = [185, 95, -85, 150, -30, 251, 71, 5]
    radius = [8.5, 7, 8, 10, 8, 7, 8.5, 13.5]
    for i in range(len(start_angle)):
        create_arc(center_point_x + bia[i*2], center_point_y+bia[i * 2 + 1], radius[i], start_angle[i], end_angle[i])
# create_Cylinder_hole_up(-127830.1108,-130844.7087)

def create_capsule_circle(center_point_x,center_point_y):
    center_point2_x = center_point_x
    center_point2_y = center_point_y + 38
    create_arc(center_point_x,center_point_y,10,-180,0)
    create_arc(center_point2_x,center_point2_y,10,0,180)
    create_line(center_point_x-10,center_point_y,center_point_x-10,center_point_y+38)
    create_line(center_point_x+10,center_point_y,center_point_x+10,center_point_y+38)

    return



def create_hinge_circle(left_center_point):
    cpoint = []
    cpoint.append(left_center_point.x)
    cpoint.append(left_center_point.y)
    cpoint.append(left_center_point.x+2)
    cpoint.append(left_center_point.y)
    start_angle = [90, -90]
    end_angle = [270, 90]
    radius = [5.5, 5.5]
    for i in range(len(start_angle)):
        create_arc(cpoint[i * 2], cpoint[i * 2 + 1], radius[i], start_angle[i], end_angle[i])
    p1 = APoint(left_center_point.x, left_center_point.y+5.5)
    p2 = APoint(p1.x+2,p1.y)
    line1 = acad.model.AddLine(p1, p2)
    line1.Color = 1
    p3 = APoint(left_center_point.x, left_center_point.y-5.5)
    p4 = APoint(p3.x+2, p3.y)
    line2 = acad.model.AddLine(p3, p4)
    line2.Color = 1
    return


def create_hinge_rectangle(circle_center_point,direction):
    bia_x = -129172.8042 - (-129173.3667)
    bia_y = -133652.9203 - (-133655.4203)
    if(direction == 0):    ## 缺口朝向左边
        create_arc(circle_center_point.x, circle_center_point.y, 2.56, -77, 77)
        p1 = APoint(circle_center_point.x + bia_x, circle_center_point.y + bia_y)
        p2 = APoint(p1.x - 15, p1.y)
        p3 = APoint(p1.x, p1.y - 5)
        p4 = APoint(p3.x - 15, p3.y)
        line1 = acad.model.AddLine(p1, p2)
        line2 = acad.model.AddLine(p3, p4)
        line1.Color = 1
        line2.Color = 1
    else:
        create_arc(circle_center_point.x, circle_center_point.y, 2.56, 103, 257 )
        p1 = APoint(circle_center_point.x - bia_x, circle_center_point.y + bia_y)
        p2 = APoint(p1.x + 15, p1.y)
        p3 = APoint(p1.x, p1.y - 5)
        p4 = APoint(p3.x + 15, p3.y)
        line1 = acad.model.AddLine(p1, p2)
        line2 = acad.model.AddLine(p3, p4)
        line1.Color = 1
        line2.Color = 1


def create_hinge1(base_point,direction):
    bia_y = -135624.9587 - (-135899.2087)
    bia_x = -129127.4108 - (-129150.7108)
    bia_x2 = -129125.5983 - (-129150.7108)
    bia_y2 = -135600.9587 - (-135899.2087)
    p = []
    if(direction == 0):   #在基准点的右边绘制
        p1 = APoint(base_point.x+bia_x, base_point.y+bia_y)
        p.append(p1)
        p2 = APoint(p1.x+27, p1.y)
        p.append(p2)
        p.append(APoint(p1.x, p1.y + 47))
        p.append(APoint(p1.x, p1.y + 94))
        p.append(APoint(p2.x, p2.y + 47))
        p.append(APoint(p2.x, p2.y + 94))
        for i in range(len(p)):
            create_hinge_circle(p[i])

        p3 = APoint(base_point.x+bia_x2, base_point.y+bia_y2)
        create_hinge_rectangle(p3,1)
        b_x = -129100.7233 - (-129125.5983)
        b_y = -135554.9587 - (-135600.9587)
        p4 = APoint(p3.x+b_x, p3.y+b_y)
        create_hinge_rectangle(p4,0)


    if(direction == 1):   #在基准点的左边绘制
        p1 = APoint(base_point.x-bia_x - 2, base_point.y+bia_y)
        p.append(p1)
        p2 = APoint(p1.x-27, p1.y)
        p.append(p2)
        p.append(APoint(p1.x, p1.y + 47))
        p.append(APoint(p1.x, p1.y + 94))
        p.append(APoint(p2.x, p2.y + 47))
        p.append(APoint(p2.x, p2.y + 94))
        for i in range(len(p)):
            create_hinge_circle(p[i])

        p3 = APoint(base_point.x-bia_x2, base_point.y+bia_y2)
        create_hinge_rectangle(p3,0)
        b_x = -129100.7233 - (-129125.5983)
        b_y = -135554.9587 - (-135600.9587)
        p4 = APoint(p3.x-b_x, p3.y+b_y)
        create_hinge_rectangle(p4,1)

        return



def create_hinge2(base_point,direction):
    bia_x = -129127.4108 - (-129150.7108)
    bia_y = -133640.9587 - (-133489.2087)
    bia_x2 = -129100.7233 - (-129150.7108)
    bia_y2 = -133664.9587 - (-133489.2087)
    p = []
    if(direction == 0):   #在基准点的右边绘制
        p1 = APoint(base_point.x+bia_x, base_point.y+bia_y)
        p.append(p1)
        p2 = APoint(p1.x+27, p1.y)
        p.append(p2)
        p.append(APoint(p1.x, p1.y - 47))
        p.append(APoint(p1.x, p1.y - 94))
        p.append(APoint(p2.x, p2.y - 47))
        p.append(APoint(p2.x, p2.y - 94))
        for i in range(len(p)):
            create_hinge_circle(p[i])

        p3 = APoint(base_point.x+bia_x2, base_point.y+bia_y2)
        create_hinge_rectangle(p3,0)
        b_x = -129125.5983 - (-129100.7233)
        b_y = -133710.9587 - (-133664.9587)
        p4 = APoint(p3.x+b_x, p3.y+b_y)
        create_hinge_rectangle(p4,1)


    if(direction == 1):   #在基准点的左边绘制
        p1 = APoint(base_point.x - bia_x - 2, base_point.y+bia_y)
        p.append(p1)
        p2 = APoint(p1.x-27 , p1.y)
        p.append(p2)
        p.append(APoint(p1.x, p1.y - 47))
        p.append(APoint(p1.x, p1.y - 94))
        p.append(APoint(p2.x, p2.y - 47))
        p.append(APoint(p2.x, p2.y - 94))
        for i in range(len(p)):
            create_hinge_circle(p[i])

        p3 = APoint(base_point.x-bia_x2, base_point.y+bia_y2)
        create_hinge_rectangle(p3,1)
        b_x = -129125.5983 - (-129100.7233)
        b_y = -133710.9587 - (-133664.9587)
        p4 = APoint(p3.x-b_x, p3.y+b_y)
        create_hinge_rectangle(p4,0)

        return


def create_Door_jamb_up(base_point,len_x,len_y,len_y2):   ## 以右下角为基点

    incise_line = []  # 切割标记线
    incise_line.append(base_point.x - 14.3)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - 14.3)
    incise_line.append(base_point.y + 2)

    incise_line.append(base_point.x - 27.3)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - 27.3)
    incise_line.append(base_point.y + 2)

    incise_line.append(base_point.x - len_x + 11)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - len_x + 11)
    incise_line.append(base_point.y + 2)

    incise_line.append(base_point.x - len_x + 48)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - len_x + 48)
    incise_line.append(base_point.y + 2)

    incise_line.append(base_point.x - 14.3)
    incise_line.append(base_point.y + len_y2)
    incise_line.append(base_point.x - 14.3)
    incise_line.append(base_point.y + len_y2 - 2)

    incise_line.append(base_point.x - 16.3 - 11)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - 16.3 - 11)
    incise_line.append(base_point.y + len_y - 2)

    incise_line.append(base_point.x - len_x + 11)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - len_x + 11)
    incise_line.append(base_point.y + len_y - 2)

    incise_line.append(base_point.x - len_x + 48)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - len_x + 48)
    incise_line.append(base_point.y + len_y - 2)

    incise_line.append(base_point.x - len_x + 11)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - len_x + 11)
    incise_line.append(base_point.y + 2)

    incise_line.append(base_point.x - len_x + 48)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - len_x + 48)
    incise_line.append(base_point.y + 2)

    for i in range(0, len(incise_line), 4):
        create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3])


    coords = []
    coords.append(base_point.x)
    coords.append(base_point.y)

    coords.append(base_point.x)
    coords.append(base_point.y + len_y2)

    coords.append(base_point.x - 16.3)
    coords.append(base_point.y + len_y2)

    coords.append(base_point.x - 16.3)
    coords.append(base_point.y + len_y)

    coords.append(base_point.x - len_x)
    coords.append(base_point.y + len_y)

    new_line = acad.model.AddLightWeightPolyline(array.array("d", coords))
    new_line.Color = 1
    new_line.Closed = False

    create_line(coords[8],coords[9],coords[8],coords[9] - 142)
    create_line(coords[8]-10, coords[9]-140, coords[8], coords[9] - 140)
    create_line(base_point.x-len_x,base_point.y + 107, base_point.x -len_x, base_point.y)
    create_line(base_point.x - len_x, base_point.y + 105, base_point.x - len_x - 10, base_point.y + 105)
    create_line(base_point.x - len_x - 10, base_point.y + 105, base_point.x - len_x - 10, base_point.y + len_y/2 - 9.5 - 65.5528)
    create_line(base_point.x - len_x - 10, base_point.y + len_y/2 - 9.5 - 65.5528,base_point.x - len_x - 10 + 9, base_point.y + len_y/2 - 9.5 - 65.5528)
    create_line(base_point.x - len_x - 10 + 9, base_point.y + len_y/2 - 9.5 - 65.5528,base_point.x - len_x - 10 + 9, base_point.y + len_y/2 - 9.5)
    create_arc(base_point.x - len_x - 10 + 9 - 1, base_point.y + len_y/2, 9.5,-84,84)
    create_line(base_point.x - len_x - 10 + 9, base_point.y + len_y / 2 + 9.5 + 65.5528, base_point.x - len_x - 10 + 9,base_point.y + len_y / 2 + 9.5)
    create_line(base_point.x - len_x - 10 + 9, base_point.y + len_y / 2 + 9.5 + 65.5528,base_point.x - len_x - 10, base_point.y + len_y / 2 + 9.5 + 65.5528)
    create_line(base_point.x - len_x - 10, base_point.y + len_y / 2 + 9.5 + 65.5528,base_point.x - len_x - 10, base_point.y + len_y - 140)
    create_line(base_point.x,base_point.y,base_point.x - len_x,base_point.y)

    return
#
# p = APoint(-129775.2359, -131949.2087)
# create_Door_jamb_up(p, 708.3, 3000,2411)

def create_Door_jamb_down(base_point,len_x,len_y,len_y2):  ##右下为基点
    incise_line = []  # 切割标记线
    incise_line.append(base_point.x - 70)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - 70)
    incise_line.append(base_point.y + 2)

    incise_line.append(base_point.x - len_x + 10 + 48)
    incise_line.append(base_point.y + 25)
    incise_line.append(base_point.x - len_x + 10 + 48)
    incise_line.append(base_point.y + 25 + 2)

    incise_line.append(base_point.x - len_x + 10 + 11)
    incise_line.append(base_point.y + 25)
    incise_line.append(base_point.x - len_x + 10 + 11)
    incise_line.append(base_point.y + 25 + 2)

    incise_line.append(base_point.x + 5 - 64 - 11)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x + 5 - 64 - 11)
    incise_line.append(base_point.y + len_y - 2)

    incise_line.append(base_point.x - len_x + 10 + 11)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - len_x + 10 + 11)
    incise_line.append(base_point.y + len_y - 2)

    incise_line.append(base_point.x - len_x + 10 + 11 + 37)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - len_x + 10 + 11 + 37)
    incise_line.append(base_point.y + len_y - 2)

    for i in range(0, len(incise_line), 4):
        create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3])

    coords = []
    coords.append(base_point.x)
    coords.append(base_point.y)

    coords.append(base_point.x)
    coords.append(base_point.y + 55)

    coords.append(base_point.x + 5)
    coords.append(base_point.y + 55)

    coords.append(base_point.x + 5)
    coords.append(base_point.y + len_y2)

    coords.append(base_point.x + 5 - 64)
    coords.append(base_point.y + len_y2)

    coords.append(base_point.x + 5 - 64)
    coords.append(base_point.y + len_y)

    coords.append(base_point.x - len_x + 10)
    coords.append(base_point.y + len_y)

    new_line = acad.model.AddLightWeightPolyline(array.array("d", coords))
    new_line.Color = 1
    new_line.Closed = False


    create_line(base_point.x,base_point.y,base_point.x - len_x + 10 + 123 + 3,base_point.y)
    create_arc(base_point.x - len_x + 10 + 123 + 3,base_point.y + 3, 3,180,270)
    create_line(base_point.x - len_x + 10 + 123,base_point.y + 3,base_point.x - len_x + 10 + 123,base_point.y + 3 + 22)
    create_line(base_point.x - len_x + 10 + 123,base_point.y + 3 + 22,base_point.x - len_x + 10,base_point.y + 3 + 22)
    create_line(base_point.x - len_x + 10, base_point.y + 3 + 22, base_point.x - len_x + 10,base_point.y + 3 + 22 + 82)
    create_line(base_point.x - len_x + 10, base_point.y + 3 + 22 + 80, base_point.x - len_x, base_point.y + 3 + 22 + 80)

    create_line(base_point.x - len_x, base_point.y + 3 + 22 + 80, base_point.x - len_x, base_point.y + len_y/2 - 9.5 - 65.5528)
    create_line(base_point.x - len_x + 9, base_point.y + len_y / 2 - 9.5 - 65.5528, base_point.x - len_x,base_point.y + len_y / 2 - 9.5 - 65.5528)
    create_line(base_point.x - len_x + 9, base_point.y + len_y / 2 - 9.5 - 65.5528, base_point.x - len_x + 9,base_point.y + len_y / 2 - 9.5)
    create_arc(base_point.x - len_x + 9 -1, base_point.y + len_y / 2, 9.5, -84, 84)

    create_line(base_point.x - len_x + 9, base_point.y + len_y / 2 + 9.5 + 65.5528, base_point.x - len_x + 9,base_point.y + len_y / 2 + 9.5)
    create_line(base_point.x - len_x + 9, base_point.y + len_y / 2 + 9.5 + 65.5528, base_point.x - len_x,base_point.y + len_y / 2 + 9.5 + 65.5528)
    create_line(base_point.x - len_x,base_point.y + len_y / 2 + 9.5 + 65.5528,base_point.x - len_x,base_point.y + len_y - 140 )
    create_line(base_point.x - len_x,base_point.y + len_y - 140,base_point.x - len_x + 10,base_point.y + len_y - 140)
    create_line(base_point.x - len_x + 10,base_point.y + len_y - 140 - 2,base_point.x - len_x + 10,base_point.y + len_y)


    create_rectangle(base_point.x - 73 ,base_point.y + 136.5, 54,251)
    create_rectangle(base_point.x - 73, base_point.y + len_y2 - 385.5, 54, 251)

    create_line(base_point.x - 20, base_point.y + 462,base_point.x - 20 - 34.5, base_point.y + 462)
    create_line(base_point.x - 20 + 2, base_point.y + 462 + 2, base_point.x - 20 + 2, base_point.y + 462 + 2 + 176.5)
    create_line(base_point.x - 20 - 34.5, base_point.y + 462 + 2 + 176.5 + 2, base_point.x - 20, base_point.y + 462 + 2 + 176.5 + 2)
    create_line(base_point.x - 20 - 34.5 - 2, base_point.y + 462 + 2 + 176.5, base_point.x - 20 - 34.5 - 2, base_point.y + 462 + 2)
    create_arc(base_point.x - 20,base_point.y + 462 + 2,2,-90,0)
    create_arc(base_point.x - 20, base_point.y + 462 + 2 + 176.5, 2, 0, 90)
    create_arc(base_point.x - 20 - 34.5, base_point.y + 462 + 2 + 176.5, 2, 90, 180)
    create_arc(base_point.x - 20 - 34.5, base_point.y + 462 + 2, 2, 180, 270)


    return


# p = APoint(-129780.2359, -135699.2087)
# create_Door_jamb_down(p, 746, 3000,2412)


# create_capsule_circle(-128001.0573,-130966.7993)

def create_doorframe6(base_point,len_x,len_y):

    incise_line = [] #切割标记线
    incise_line.append(base_point.x - 11)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - 11)
    incise_line.append(base_point.y + 2)

    incise_line.append(base_point.x - len_x + 50 + 5 + 1 + 19)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - len_x + 50 + 5 + 1 + 19)
    incise_line.append(base_point.y + 2)

    incise_line.append(base_point.x - 11)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - 11)
    incise_line.append(base_point.y + len_y - 2)

    incise_line.append(base_point.x - len_x + 50 + 25)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - len_x + 50 + 25)
    incise_line.append(base_point.y +len_y - 2)

    for i in range(0,len(incise_line),4):
        create_line(incise_line[i],incise_line[i+1],incise_line[i+2],incise_line[i+3])


    coords = []
    coords.append(base_point.x)
    coords.append(base_point.y)

    coords.append(base_point.x)
    coords.append(base_point.y + len_y)

    coords.append(base_point.x - len_x + 50)
    coords.append(base_point.y + len_y)

    coords.append(base_point.x - len_x + 50)
    coords.append(base_point.y + len_y - 10)

    coords.append(base_point.x - len_x)
    coords.append(base_point.y + len_y - 10)

    coords.append(base_point.x - len_x)
    coords.append(base_point.y + 10 + 14 + 1)

    coords.append(base_point.x - len_x + 50)
    coords.append(base_point.y + 10 + 14 + 1)

    coords.append(base_point.x - len_x + 50)
    coords.append(base_point.y + 14 + 1)

    coords.append(base_point.x - len_x + 50 + 5)
    coords.append(base_point.y + 14 + 1)

    coords.append(base_point.x - len_x + 50 + 5)
    coords.append(base_point.y + 1)

    new_line = acad.model.AddLightWeightPolyline(array.array("d", coords))
    new_line.Color = 1
    new_line.Closed = False

    cen_point = APoint(base_point.x - len_x + 111.2, base_point.y +len_y - 25.8)
    new_circle = acad.model.AddCircle(cen_point,4.2)
    new_circle.Color = 1

    create_arc(base_point.x - len_x + 50 + 5 + 1, base_point.y + 1, 1, 180, 270)

    return
# p = APoint(-127026.1108,-129554.2087 )
# create_doorframe6(p,924,605)


def create_doorframe5(base_point,len_x,len_y):   ## 以左下角为基点

    incise_line = [] #切割标记线
    incise_line.append(base_point.x + 75)
    incise_line.append(base_point.y - 10)
    incise_line.append(base_point.x + 75)
    incise_line.append(base_point.y - 10 + 2)
    incise_line.append(base_point.x + len_x - 75)
    incise_line.append(base_point.y - 10)
    incise_line.append(base_point.x + len_x - 75)
    incise_line.append(base_point.y - 10 + 2)

    incise_line.append(base_point.x + 75)
    incise_line.append(base_point.y + len_y - 10)
    incise_line.append(base_point.x + 75)
    incise_line.append(base_point.y + len_y - 10 - 2)
    incise_line.append(base_point.x + len_x - 75)
    incise_line.append(base_point.y + len_y - 10)
    incise_line.append(base_point.x + len_x - 75)
    incise_line.append(base_point.y +len_y - 10 - 2)

    for i in range(0,len(incise_line),4):
        create_line(incise_line[i],incise_line[i+1],incise_line[i+2],incise_line[i+3])

    coords = []
    coords.append(base_point.x)
    coords.append(base_point.y)

    coords.append(base_point.x)
    coords.append(base_point.y + len_y - 10 - 10)

    coords.append(base_point.x + 50)
    coords.append(base_point.y + len_y - 10 - 10)

    coords.append(base_point.x + 50)
    coords.append(base_point.y + len_y - 10 )

    coords.append(base_point.x + len_x - 44)
    coords.append(base_point.y + len_y - 10)

    coords.append(base_point.x + len_x - 44)
    coords.append(base_point.y + len_y - 10 - 10)

    coords.append(base_point.x + len_x)
    coords.append(base_point.y + len_y - 10 - 10)

    coords.append(base_point.x + len_x)
    coords.append(base_point.y)

    coords.append(base_point.x + len_x - 44)
    coords.append(base_point.y)

    coords.append(base_point.x + len_x - 44)
    coords.append(base_point.y - 10)

    coords.append(base_point.x + 50)
    coords.append(base_point.y - 10)

    coords.append(base_point.x + 50)
    coords.append(base_point.y)

    new_line = acad.model.AddLightWeightPolyline(array.array("d", coords))
    new_line.Color = 1
    new_line.Closed = True

    coords2 = []
    coords2.append(base_point.x + 5)
    coords2.append(base_point.y + 745)
    coords2.append(base_point.x + 5)
    coords2.append(base_point.y + 745 + 320)
    coords2.append(base_point.x + 5 + 42)
    coords2.append(base_point.y + 745 + 320)
    coords2.append(base_point.x + 5 + 42)
    coords2.append(base_point.y + 745)
    new_line = acad.model.AddLightWeightPolyline(array.array("d", coords2))
    new_line.Color = 1
    new_line.Closed = True

    coords2.clear()
    coords2.append(base_point.x + 5)
    coords2.append(base_point.y + 745 + 10 + 320)
    coords2.append(base_point.x + 5)
    coords2.append(base_point.y + 745 + 320 + 10 + 320)
    coords2.append(base_point.x + 5 + 42)
    coords2.append(base_point.y + 745 + 320 + 10 + 320)
    coords2.append(base_point.x + 5 + 42)
    coords2.append(base_point.y + 745 + 10 + 320)
    new_line = acad.model.AddLightWeightPolyline(array.array("d", coords2))
    new_line.Color = 1
    new_line.Closed = True

    create_capsule_circle(base_point.x + 120, base_point.y + 961 - 8)
    create_capsule_circle(base_point.x + 120, base_point.y + 961 + 196 - 8)
    create_Cylinder_hole_up(base_point.x + 120, base_point.y + 961 + 141.5 - 8)
    create_Cylinder_hole_down(base_point.x + 120, base_point.y + 961 + 92.5 - 8)


    return
#
# p = APoint(-127950.1108 ,-131939.2087)
# create_doorframe5(p,986,2395)

def create_doorframe4(base_point,len_x,len_y):
    incise_line = [] #切割标记线
    incise_line.append(base_point.x - 16.3)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - 16.3)
    incise_line.append(base_point.y + 2)
    incise_line.append(base_point.x - 29.3)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - 29.3)
    incise_line.append(base_point.y + 2)
    incise_line.append(base_point.x - len_x + 11)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - len_x + 11)
    incise_line.append(base_point.y + 2)

    incise_line.append(base_point.x - 16.3)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - 16.3)
    incise_line.append(base_point.y + len_y - 2)
    incise_line.append(base_point.x - 29.3)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - 29.3)
    incise_line.append(base_point.y + len_y - 2)
    incise_line.append(base_point.x - len_x + 11)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - len_x + 11)
    incise_line.append(base_point.y +len_y - 2)
    for i in range(0,len(incise_line),4):
        create_line(incise_line[i],incise_line[i+1],incise_line[i+2],incise_line[i+3])


    coords = []
    coords.append(base_point.x)
    coords.append(base_point.y)
    coords.append(base_point.x)
    coords.append(base_point.y + len_y)
    coords.append(base_point.x - len_x)
    coords.append(base_point.y + len_y)
    coords.append(base_point.x - len_x)
    coords.append(base_point.y)
    new_line = acad.model.AddLightWeightPolyline(array.array("d", coords))
    new_line.Color = 1
    new_line.Closed = False

    cen_point = APoint(coords[2] - 65.5,coords[3] - 25.8)
    new_circle = acad.model.AddCircle(cen_point,4.2)
    new_circle.Color = 1

    return
p = APoint(-128150.1108,-129554.2087 )
create_doorframe4(p,878.3,605)




#
# p = APoint(-126976.8108,-133489.2087)
# create_hinge2(p,1)
# #############################################################






def create_doorframe3(base_point,len_x,len_y,flag):  ##flag为1则画圆

    incise_line = [] #切割标记线
    incise_line.append(base_point.x - 16.3)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - 16.3)
    incise_line.append(base_point.y + 2)
    incise_line.append(base_point.x - 29.3)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - 29.3)
    incise_line.append(base_point.y + 2)
    incise_line.append(base_point.x - len_x + 44 + 31)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - len_x + 44 + 31)
    incise_line.append(base_point.y + 2)

    incise_line.append(base_point.x - 16.3)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - 16.3)
    incise_line.append(base_point.y + len_y - 2)
    incise_line.append(base_point.x - 29.3)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - 29.3)
    incise_line.append(base_point.y + len_y - 2)
    incise_line.append(base_point.x - len_x + 44 + 31)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - len_x + 44 + 31)
    incise_line.append(base_point.y +len_y - 2)

    for i in range(0,len(incise_line),4):
        create_line(incise_line[i],incise_line[i+1],incise_line[i+2],incise_line[i+3])

    coords = []
    coords.append(base_point.x)
    coords.append(base_point.y)
    coords.append(base_point.x - len_x + 44)
    coords.append(base_point.y)
    coords.append(base_point.x - len_x + 44)
    coords.append(base_point.y + 10)
    coords.append(base_point.x - len_x)
    coords.append(base_point.y + 10)
    coords.append(base_point.x - len_x)
    coords.append(base_point.y + len_y - 10)
    coords.append(base_point.x - len_x + 44)
    coords.append(base_point.y + len_y - 10)
    coords.append(base_point.x - len_x + 44)
    coords.append(base_point.y + len_y)
    coords.append(base_point.x)
    coords.append(base_point.y + len_y)

    new_line = acad.model.AddLightWeightPolyline(array.array("d", coords))
    new_line.Color = 1
    new_line.Closed = True

    if(flag == 1):
        cen_point1 = APoint(base_point.x - 88.3,base_point.y + 963)
        cen_point2 = APoint(base_point.x - 88.3,base_point.y + 963 + 234)
        new_circle1 = acad.model.AddCircle(cen_point1,10)
        new_circle1.Color = 1
        new_circle2 = acad.model.AddCircle(cen_point2,10)
        new_circle2.Color = 1


    return
#
# p = APoint(-128150.1108,-131949.2087)
# create_doorframe3(p,940.3,2395)


def create_doorframe1(base_point,len_x,len_y):  #以右下角为基点
    incise_line = [] #切割标记线
    incise_line.append(base_point.x - 14.3)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - 14.3)
    incise_line.append(base_point.y + 2)
    incise_line.append(base_point.x - 70.3)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - 70.3)
    incise_line.append(base_point.y + 2)
    incise_line.append(base_point.x - len_x + 14.3)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - len_x + 14.3)
    incise_line.append(base_point.y + 2)
    incise_line.append(base_point.x - len_x + 64.3)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - len_x + 64.3)
    incise_line.append(base_point.y + 2)

    incise_line.append(base_point.x - 14.3)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - 14.3)
    incise_line.append(base_point.y + len_y - 2)
    incise_line.append(base_point.x - 70.3)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - 70.3)
    incise_line.append(base_point.y + len_y - 2)
    incise_line.append(base_point.x - len_x + 14.3)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - len_x + 14.3)
    incise_line.append(base_point.y + len_y - 2)
    incise_line.append(base_point.x - len_x + 64.3)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - len_x + 64.3)
    incise_line.append(base_point.y + len_y - 2)

    for i in range(0,len(incise_line),4):
        create_line(incise_line[i],incise_line[i+1],incise_line[i+2],incise_line[i+3])

    coords = []
    coords.append(base_point.x)
    coords.append(base_point.y)
    coords.append(base_point.x - len_x)
    coords.append(base_point.y)
    coords.append(base_point.x - len_x)
    coords.append(base_point.y + len_y)
    coords.append(base_point.x)
    coords.append(base_point.y + len_y)
    new_line = acad.model.AddLightWeightPolyline(array.array("d", coords))
    new_line.Color = 1
    new_line.Closed = True

    create_hinge1(APoint(base_point.x - len_x,base_point.y),0) # 23.3 274.25
    create_hinge2(APoint(base_point.x - len_x, base_point.y +len_y), 0) # 23.3 151.75
    create_capsule_circle(base_point.x - 129.3,base_point.y + 963)
    create_capsule_circle(base_point.x - 129.3, base_point.y + 963 + 196)
    create_Cylinder_hole_up(base_point.x - 129.3,base_point.y + 963 + 141.5)
    create_Cylinder_hole_down(base_point.x - 129.3,base_point.y + 963 + 92.5)
    create_rectangle(base_point.x - 62.55,base_point.y + 925,40.5,145)
    create_rectangle(base_point.x - 62.55,base_point.y + 925 + 155,40.5,145)

    create_four_rounded_rectangle(base_point.x - 138.8  ,base_point.y + 264,34.5,176.5 )
    create_two_rounded_rectangle_up(base_point.x - 61.55  ,base_point.y + 780.75 + 598.5,38.5,144.25)
    create_two_rounded_rectangle_down(base_point.x - 61.55  ,base_point.y + 780.75,38.5,134.25)

    if(len_y<= 2200):
        create_four_rounded_rectangle(base_point.x - 138.8, base_point.y + len_y - 265 - 2 - 176.5, 34.5, 176.5)
    elif(len_y <= 2400):
        create_four_rounded_rectangle(base_point.x - 138.8, base_point.y + len_y - 465 - 2 - 176.5, 34.5, 176.5)
    else:
        create_four_rounded_rectangle(base_point.x - 138.8, base_point.y + len_y - 265 - 2 - 176.5 + len_y - 2400, 34.5, 176.5)

    return
#
# p= APoint(-128150.1108 , -135899.2087)
# create_doorframe1(p,1000.6,2410)
#
#
def create_doorframe2(base_point,len_x,len_y,flag):   # 以右下角为基点  flag为1则画圆
    incise_line = [] #切割标记线
    incise_line.append(base_point.x - 14.3)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - 14.3)
    incise_line.append(base_point.y + 2)
    incise_line.append(base_point.x - 64.3)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - 64.3)
    incise_line.append(base_point.y + 2)
    incise_line.append(base_point.x - len_x + 5 + 70)
    incise_line.append(base_point.y)
    incise_line.append(base_point.x - len_x + 5 + 70)
    incise_line.append(base_point.y + 2)


    incise_line.append(base_point.x - 14.3)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - 14.3)
    incise_line.append(base_point.y + len_y - 2)
    incise_line.append(base_point.x - 64.3)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - 64.3)
    incise_line.append(base_point.y + len_y - 2)
    incise_line.append(base_point.x - len_x + 5 + 10 + 2 + 58)
    incise_line.append(base_point.y + len_y)
    incise_line.append(base_point.x - len_x + 5 + 10 + 2 + 58)
    incise_line.append(base_point.y + len_y - 2)


    for i in range(0,len(incise_line),4):
        create_line(incise_line[i],incise_line[i+1],incise_line[i+2],incise_line[i+3])

    coords = []
    coords.append(base_point.x)
    coords.append(base_point.y)
    coords.append(base_point.x - len_x + 5)
    coords.append(base_point.y)
    coords.append(base_point.x - len_x + 5)
    coords.append(base_point.y + 20)
    coords.append(base_point.x - len_x)
    coords.append(base_point.y + 20)
    coords.append(base_point.x - len_x)
    coords.append(base_point.y + len_y - 2 - 13 - 20)
    coords.append(base_point.x - len_x + 5)
    coords.append(base_point.y + len_y - 2 - 13 - 20)
    coords.append(base_point.x - len_x + 5)
    coords.append(base_point.y + len_y - 2 - 13)
    coords.append(base_point.x - len_x + 5 + 10)
    coords.append(base_point.y + len_y - 2 - 13)
    coords.append(base_point.x - len_x + 5 + 10)
    coords.append(base_point.y + len_y - 2)

    new_line = acad.model.AddLightWeightPolyline(array.array("d", coords))
    new_line.Color = 1
    new_line.Closed = False

    create_arc(base_point.x - len_x + 5 + 10 + 2,base_point.y + len_y - 2,2,90,180)

    coords2 = []
    coords2.append(base_point.x)
    coords2.append(base_point.y)
    coords2.append(base_point.x)
    coords2.append(base_point.y + len_y)
    coords2.append(base_point.x - 64.3 + 2 + 11)
    coords2.append(base_point.y + len_y)
    new_line2 = acad.model.AddLightWeightPolyline(array.array("d", coords2))
    new_line2.Color = 1
    new_line2.Closed = False

    create_hinge1(APoint(base_point.x,base_point.y),1)
    create_hinge2(APoint(base_point.x,base_point.y +len_y), 1)

    if(flag == 1):
        cen_point1 = APoint(base_point.x - len_x + 5 +114,base_point.y + 963)
        cen_point2 = APoint(base_point.x - len_x + 5 + 114,base_point.y + 963 + 234)
        new_circle1 = acad.model.AddCircle(cen_point1,10)
        new_circle1.Color = 1
        new_circle2 = acad.model.AddCircle(cen_point2,10)
        new_circle2.Color = 1

    create_rectangle(base_point.x - len_x + 24.75, base_point.y + 925,40.5,145)
    create_rectangle(base_point.x - len_x + 24.75, base_point.y + 925 + 155 ,40.5,145)

    create_four_rounded_rectangle(base_point.x - len_x + 5 + 20  ,base_point.y + 264,34.5,176.5 )
    create_two_rounded_rectangle_up(base_point.x - len_x + 5 + 20.75  ,base_point.y + 780.75 + 598.5,38.5,144.25)
    create_two_rounded_rectangle_down(base_point.x - len_x + 5 + 20.75  ,base_point.y + 780.75,38.5,134.25)

    if(len_y <= 2200):  ##有问题
        create_four_rounded_rectangle(base_point.x - len_x + 5 + 20, base_point.y + len_y - 265 - 2 - 176.5, 34.5, 176.5)
    elif(len_y <= 2400):
        create_four_rounded_rectangle(base_point.x - len_x + 5 + 20, base_point.y + len_y - 465 - 2 - 176.5, 34.5, 176.5)
    else:
        create_four_rounded_rectangle(base_point.x - len_x + 5 + 20, base_point.y + len_y - 265 - 2 - 176.5 -(len_y - 2400), 34.5, 176.5)


    return
#
# pp= APoint(-126976.8108 , -135899.2087)
# create_doorframe2(pp,973.3,2400,1)

# #####  绘制图形 #############
# cenpoint = [-129173.3667,-133655.4203]
# create_arc(cenpoint[0],cenpoint[1],2.56,-77,77)
# bia_x = -129172.8042 - (-129173.3667)
# bia_y = -133652.9203 - (-133655.4203)
# p1 = APoint(cenpoint[0]+bia_x,cenpoint[1]+bia_y)
# p2 = APoint(p1.x - 15,p1.y)
# p3 = APoint(p1.x,p1.y-5)
# p4 = APoint(p3.x - 15,p3.y)
# line1 = acad.model.AddLine(p1,p2)
# line2 = acad.model.AddLine(p3,p4)
# line1.Color = 1
# line2.Color = 1



#####################  创建铰链 ##########################
# def create_hinge_circle(left_center_point):
#     cpoint = []
#     cpoint.append(left_center_point.x)
#     cpoint.append(left_center_point.y)
#     cpoint.append(left_center_point.x+2)
#     cpoint.append(left_center_point.y)
#     start_angle = [90, -90]
#     end_angle = [270, 90]
#     radius = [5.5, 5.5]
#     for i in range(len(start_angle)):
#         create_arc(cpoint[i * 2], cpoint[i * 2 + 1], radius[i], start_angle[i], end_angle[i])
#     p1 = APoint(left_center_point.x, left_center_point.y+5.5)
#     p2 = APoint(p1.x+2,p1.y)
#     line1 = acad.model.AddLine(p1, p2)
#     line1.Color = 1
#     p3 = APoint(left_center_point.x, left_center_point.y-5.5)
#     p4 = APoint(p3.x+2, p3.y)
#     line2 = acad.model.AddLine(p3, p4)
#     line2.Color = 1
#     return


# def create_hinge_rectangle(circle_center_point,direction):
#     bia_x = -129172.8042 - (-129173.3667)
#     bia_y = -133652.9203 - (-133655.4203)
#     if(direction == 0):    ## 缺口朝向左边
#         create_arc(circle_center_point.x, circle_center_point.y, 2.56, -77, 77)
#         p1 = APoint(circle_center_point.x + bia_x, circle_center_point.y + bia_y)
#         p2 = APoint(p1.x - 15, p1.y)
#         p3 = APoint(p1.x, p1.y - 5)
#         p4 = APoint(p3.x - 15, p3.y)
#         line1 = acad.model.AddLine(p1, p2)
#         line2 = acad.model.AddLine(p3, p4)
#         line1.Color = 1
#         line2.Color = 1
#     else:
#         create_arc(circle_center_point.x, circle_center_point.y, 2.56, 103, 257 )
#         p1 = APoint(circle_center_point.x - bia_x, circle_center_point.y + bia_y)
#         p2 = APoint(p1.x + 15, p1.y)
#         p3 = APoint(p1.x, p1.y - 5)
#         p4 = APoint(p3.x + 15, p3.y)
#         line1 = acad.model.AddLine(p1, p2)
#         line2 = acad.model.AddLine(p3, p4)
#         line1.Color = 1
#         line2.Color = 1
#
#


# p = APoint(-126976.8108,-135899.2087)
# create_hinge(p,1)
# ##############################################################


# v = [(1.0,2.0),(3.0,4.0),(5.0,6.0)]
# new_line = acad.model.AddLightWeightPolyline(v)
# new_line.Color = 1

# v = []
# for obj in acad.iter_objects('PolyLine'):
#     if(obj.Color==3):
#         v = obj.Coordinates
#         print(v)
#
# p1 = APoint(v[0],v[1])
# p2 = APoint(v[2],v[3])
# l = acad.model.AddLine(p1,p2)
# l.Color = 1

# def move(obj,x,y):
#     start_point = APoint(obj.Coordinates[0], obj.Coordinates[1])
#     move_vector = APoint(x,y)
#     obj.Move(start_point,start_point+move_vector)
#
# i = 0
# for obj in acad.iter_objects():
#     if(obj.Color == 3):
#         i = i + 1
#         move(obj,100,0)
#         print('success ',i)


# # 定义弧线的起点和终点（使用坐标点）
# start_point = pyautocad.aDouble(-129292.8653, -134844.8154)  # 起点
# end_point = pyautocad.aDouble(-129242.8653, -134844.8154)  # 终点


#######       绘制图形   ##########
# def create_arc(x,y,radius,start_angle,end_angle):
#     center_point = APoint(x,y)
#     start_angle = math.radians(start_angle)
#     end_angle = math.radians(end_angle)
#     arc = acad.model.AddArc(center_point,radius,start_angle,end_angle)
#     arc.Color = 1
#     return
#
# cpoint = [-129182.3305, -133636.9365, -129180.3305, -133636.9365]
# start_angle = [90, -90]
# end_angle = [270, 90]
# radius = [5.5,5.5]
# for i in range(len(start_angle)):
#     create_arc(cpoint[i * 2], cpoint[i * 2 + 1], radius[i], start_angle[i], end_angle[i])
#
#
#
# p1 = APoint(-129182.3305, -133631.4365)
# p2 = APoint(-129180.3305, -133631.4365)
# line1 = acad.model.AddLine(p1, p2)
# line1.Color = 1
# p3 = APoint(-129182.3305, -133642.4365)
# p4 = APoint(-129180.3305, -133642.4365)
# line2 = acad.model.AddLine(p3, p4)
# line2.Color = 1


# # c_p = [-128498.0816,-134681.4235,-128503.0076,-134666.7270,-128504.3828,-134651.7902,-128520.0076,-134660.7270,-128535.6323,-134651.7902,-128537.0076,-134666.7270,-128541.9335,-134681.4235,-128520.0076,-134683.2270]
# # start_angle = [109,-71,-150,30,-95,85,-5,-185]
# # end_angle = [185,95,-85,150,-30,251,71,5]
# # radius = [8.5,7,8,10,8,7,8.5,13.5]
# # for i in range(len(start_angle)):
# #     create_arc(c_p[i*2],c_p[i*2+1],radius[i],-end_angle[i],-start_angle[i])
#
# c_p = [-128520.3188,-134802.8228,-128498.3929,-134804.6264,-128503.3188,-134819.3228, -128504.6940,-134834.2596,-128520.3188,-134825.3228,-128535.9436,-134834.2596,-128537.3188,-134819.3228,-128542.2447,-134804.6264]
# start_angle = [-5,175,-95,85,-150,30,109,-71]
# end_angle = [185,251,71,150,-30,95,276,5]
# radius = [13.5,8.5,7,8,10,8,7,8.5]
# for i in range(len(start_angle)):
#     create_arc(c_p[i*2],c_p[i*2+1],radius[i],start_angle[i],end_angle[i])
# # # 定义弧线的中心点
# # center_point = APoint(-129267.8653, -134844.8154)  # 圆心
# # radius = 50
# # start_angle = math.radians(109)
# # end_angle = math.radians(185)
# # # 使用起点、终点和圆心绘制弧线
# # # arc = acad.ActiveDocument.ModelSpace.AddArc(center_point, start_point, end_point)
# # arc = acad.model.AddArc(center_point, 8.5, start_angle,end_angle)



#############   绘制2  ########################
def change_point(p,x,y):
    statr_point = APoint(p.x+x,p.y)
    end_point = APoint(p.x+x,p.y+y)
    new_line = acad.model.Addline(statr_point,end_point)
    new_line.Color = 1
    return

def create_doorframe8(p0,len_x,len_y):
    coords = []

    coords.append(p0.x)
    coords.append(p0.y)

    coords.append(p0.x)
    coords.append(p0.y+len_y)

    coords.append(p0.x-len_x)
    coords.append(p0.y+len_y)

    coords.append(p0.x-len_x)
    coords.append(p0.y+len_y-20)

    coords.append(p0.x-len_x - 5)
    coords.append(p0.y+len_y-20)

    coords.append(p0.x-len_x-5)
    coords.append(p0.y+20)

    coords.append(p0.x-len_x)
    coords.append(p0.y+20)

    coords.append(p0.x-len_x)
    coords.append(p0.y)



    new_line = acad.model.AddLightWeightPolyline(array.array("d", coords))
    new_line.Color = 1
    new_line.Closed = True

    p = []
    for i in range(len(coords)):
        if(i % 2 == 0):
            p.append(APoint(coords[i],coords[i+1]))

    change_point(p[0],-11,2)
    change_point(p[7],70,2)
    change_point(p[2],70,-2)
    change_point(p[1],-11,-2)

    return
#
# p0 = APoint(-125945.1107585265, -133289.2086799392)
# test2(p0,1037,590)


        # new_coords = []
        # for i, coord in enumerate(v):
        #     if i % 2 == 0:  # X 坐标
        #         new_coords.append(coord - 40)
        #     else:  # Y 坐标
        #         new_coords.append(coord)
        # new_coords[5] = new_coords[5] + 30
        # new_coords[7] = new_coords[7] + 30
        # #acad.ActiveDocument.ModelSpace.AddLightWeightPolyline(tuple(new_coords))
        # new_line = acad.model.AddLightWeightPolyline(array.array("d",new_coords))
        # new_line.Color = 5
        # new_line.Closed = True


# new_line_coords = [-128150.1107585265, -133289.2086799392, -129099.4107585266, -133289.2086799392, -129099.4107585266, -132699.2086799391, -128150.1107585265, -132699.2086799391]
# p = []
# for i in range(len(new_line_coords)):
#     if(i % 2 == 0):
#         new_line_coords[i] += 3000
#         p.append(APoint(new_line_coords[i],new_line_coords[i+1]))


# ################    绘制1    ############################
# def change_point(p,x,y):
#     statr_point = APoint(p.x+x,p.y)
#     end_point = APoint(p.x+x,p.y+y)
#     new_line = acad.model.Addline(statr_point,end_point)
#     new_line.Color = 5
#     return
#
def create_doorframe7(p0,len_x,len_y):
    coords = []
    p1_x = p0.x
    p1_y = p0.y + len_y
#    p2 = p0
    p2_x = p1_x - len_x
    p2_y = p1_y
#    p3=p0
    p3_x = p0.x - len_x
    p3_y = p0.y
    print(p1_x,p1_y,p2_x,p2_y,p3_x,p3_y)
    coords.append(p0.x)
    coords.append(p0.y)
    coords.append(p1_x)
    coords.append(p1_y)
    coords.append(p2_x)
    coords.append(p2_y)
    coords.append(p3_x)
    coords.append(p3_y)
 #   print(coords)
    new_line = acad.model.AddLightWeightPolyline(array.array("d", coords))
    new_line.Color = 1
    new_line.Closed = False
    p = []
    for i in range(len(coords)):
        if(i % 2 == 0):
            p.append(APoint(coords[i],coords[i+1]))
    change_point(p[2], 11, -2)
    change_point(p[3], 11, 2)
    change_point(p[1], -14.3, -2)
    change_point(p[1], -70.3, -2)
    change_point(p[0], -14.3, 2)
    change_point(p[0], -70.3, 2)
    return
#
# p0 = APoint(-123150.1107585265, -133289.2086799392)
# test1(p0,800,600)
# print('success')






