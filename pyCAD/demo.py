from pyautocad import Autocad, APoint
import re
import math

# 打开cad文件
# 自动连接上cad，只要cad是开着的，就创建了一个<pyautocad.api.Autocad> 对象。这个对象连接最近打开的cad文件。
# 如果此时还没有打开cad，将会创建一个新的dwg文件，并自动开启cad软件
acad = Autocad(create_if_not_exists=True)
# acad.prompt() 用来在cad控制台中打印文字
acad.prompt("Hello, Autocad from Python")
# acad.doc.Name储存着cad最近打开的图形名
#//acad.doc.Application.Documents.Open("D:\CAD\demo\three.dxf")
print(acad.doc.Name)

    ### 找到两点######
v = []
for obj in acad.iter_objects('PolyLine'):
    if(obj.Color==3):
        v = obj.Coordinates

print(v)
p=[]
for i in range(0,len(v),2):
    p.append(APoint(v[i],v[i+1]))

# for i in range(len(p)-1):
#     line = acad.model.AddLine(p[i],p[i+1])
#     line.Color = i+1;

#################找到圆心#####################
circle_list = []
for obj in acad.iter_objects('Circle'):
    if(obj.Color==3):
        circle_list.append(obj)

print(circle_list)
bia_y = p[2].y - circle_list[0].Center[1]
bia_x = p[2].x - circle_list[0].Center[0]


newpoint_list = []
newpoint_list.append(p[0])

def create_newPoint(p,len_x,len_y):
    new_p = APoint(p.x+len_x,p.y+len_y)
    return new_p

l = 300
newpoint_list.append(create_newPoint(newpoint_list[0],0,l))
newpoint_list.append(create_newPoint(newpoint_list[1],p[2].x-p[1].x,0))
newpoint_list.append(create_newPoint(newpoint_list[2],0,p[3].y-p[2].y))
newpoint_list.append(create_newPoint(newpoint_list[3],p[4].x-p[3].x,0))
len4 = newpoint_list[3].y - newpoint_list[0].y - (p[5].y - p[0].y)
newpoint_list.append(create_newPoint(newpoint_list[4],0,-len4))
newpoint_list.append(create_newPoint(newpoint_list[5],p[6].x-p[5].x,0))
newpoint_list.append(create_newPoint(newpoint_list[6],0,p[7].y-p[6].y))
newpoint_list.append(create_newPoint(newpoint_list[7],p[8].x-p[7].x,0))
newpoint_list.append(create_newPoint(newpoint_list[8],0,p[9].y-p[8].y))

# def change_len(newpoint_list,len):
#     newpoint_list[1].y = newpoint_list[0].y+len
#     newpoint_list[4].y = newpoint_list[5].y+len
#
#
# change_len(newpoint_list,1000)
for i in range(len(newpoint_list)-1):
    line = acad.model.AddLine(newpoint_list[i],newpoint_list[i+1])
    line.Color = 4;
circle_center = APoint(newpoint_list[2].x-bia_x,newpoint_list[2].y-bia_y)
cir = acad.model.AddCircle(circle_center,4.2)
cir.Color = 5
# selectline = []
# for i in range(len(p)-1):
#     if((p[i].x==p[i+1].x) and abs(p[i].y-p[i+1].y)>300):
#         selectline.append(p[i])
#         selectline.append(p[i+1])
# print(selectline)
#
#
# def changelength(selectline,len):
#     p1 = selectline[0]
#     p2 = selectline[1]
#     if(p1.y<p2.y):
#         p2.y = p1.y+len
#         selectline[1].y = p2.y
#     else :
#         p1.y = p2.y+len
#         selectline[0].y = p1.y
# # changelength(selectline,500)
# line = acad.model.AddLine(selectline[0],selectline[1])
# line.Color= 1

# #################找到圆心#####################
# circle_list = []
# for obj in acad.iter_objects('Circle'):
#     if(obj.Color==3):
#         circle_list.append(obj)
#
# print(circle_list)

# # 选择所有的线条
# lines = [obj for obj in acad.iter_objects('Line')]
#
# # 打印选中的所有线条
# #for line in lines:
# #    print(f"Line found: {line.StartPoint} to {line.EndPoint}")
#
# # 选择其中的一条线（例如选择第一个线条）
# if lines:
#     selected_line = lines[0]
#     print(f"Selected line: {selected_line.StartPoint} to {selected_line.EndPoint}")
#
#     # 对选中的线条进行操作（例如：改变颜色、删除、修改等）
#     selected_line.Color = 2  # 设置线条颜色为红色（AutoCAD中的颜色编号为1）
#   #  acad.doc.Regen()  # 刷新显示
# else:
#     print("没有找到线条！")