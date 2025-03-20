from pyautocad import Autocad, APoint
import re
import math
import example
import door






# 打开cad文件
# 自动连接上cad，只要cad是开着的，就创建了一个<pyautocad.api.Autocad> 对象。这个对象连接最近打开的cad文件。
# 如果此时还没有打开cad，将会创建一个新的dwg文件，并自动开启cad软件
acad = Autocad(create_if_not_exists=True)
# acad.prompt() 用来在cad控制台中打印文字
acad.prompt("Hello, Autocad from Python")
# acad.doc.Name储存着cad最近打开的图形名
#//acad.doc.Application.Documents.Open("D:\CAD\demo\three.dxf")
print(acad.doc.Name)

total_width = float(input("请输入门宽度: ")) # 总宽
total_high = float(input("请输入门高度: ")) # 总高
standard_small_door_width = float(input("请输入小门宽度: "))# 小门宽度
standard_small_door_high = float(input("请输入小门高度: ")) # 小门高度
flag = 1
is_mirror = 0  # 是否镜像

#standard_small_door_width = 840  ##标准小门宽
#standard_small_door_high = 2400 ## 标准小门高

door_jamb_up_x = total_width / 2 - standard_small_door_width - 25 - 2 + 48 + 27.3
door_jamb_up_y = total_high
door_jamb_up_y2 = standard_small_door_high + 11

doorframe3_x = standard_small_door_width - 4 + 29.3 + 44 + 31
doorframe3_y = standard_small_door_high - 5

doorframe5_x = standard_small_door_width - 4 + 75 + 75
doorframe5_y = standard_small_door_high - 5

doorframe4_x = standard_small_door_width - 2 + 11 + 29.3
doorframe4_y = total_high - doorframe3_y

doorframe6_x = standard_small_door_width - 2 + 11 + 75
doorframe6_y = total_high - doorframe5_y

doorframe1_x = standard_small_door_width + 26 +  64.3 + 70.3
doorframe1_y = doorframe3_y + 15

doorframe2_x = standard_small_door_width - 6 +  64.3 + 75
doorframe2_y = doorframe5_y + 15

doorframe7_x = standard_small_door_width + 28 + 11 + 70.3
doorframe7_y = total_high - doorframe1_y

doorframe8_x = standard_small_door_width - 4  + 11 + 70
doorframe8_y = total_high - doorframe2_y

door_jamb_down_x = door_jamb_up_x - 15 + 52.7
door_jamb_down_y = total_high
door_jamb_down_y2 = total_high - doorframe7_y + 2


# p = APoint(-129775.2359 + 10000, -131949.2087)
# #example.create_Door_jamb_up(p, 708.3, 3000,2411)
# example.create_Door_jamb_up(p, door_jamb_up_x, door_jamb_up_y, door_jamb_up_y2)
#
# p = APoint(-129780.2359 + 10000, -135699.2087)
# #example.create_Door_jamb_down(p, 746, 3000,2412)
# example.create_Door_jamb_down(p, door_jamb_down_x, door_jamb_down_y, door_jamb_down_y2)
#
# p3 = APoint(-128150.1108 + 10000,-131949.2087)
# # example.create_doorframe3(p,940.3,2395)
# example.create_doorframe3(p3, doorframe3_x, doorframe3_y,flag)
#
# #p = APoint(-128150.1108 + 10000,-129554.2087 )
# #example.create_doorframe4(p,878.3,605)
# p4 = APoint(p3.x,p3.y + doorframe3_y )
# example.create_doorframe4(p4,doorframe4_x, doorframe4_y)
#
# p5 = APoint(-127950.1108+ 10000  ,-131939.2087)
# #example.create_doorframe5(p,986,2395)
# example.create_doorframe5(p5,doorframe5_x, doorframe5_y)
#
# # p = APoint(-127026.1108,-129554.2087 )
# p6 = APoint(p5.x + doorframe5_x - 62,p5.y + doorframe5_y - 10)
# #example.create_doorframe6(p,924,605)
# example.create_doorframe6(p6,doorframe6_x, doorframe6_y)
#
# p1= APoint(-128150.1108 + 10000, -135899.2087)
# #example.create_doorframe1(p,1000.6,2410)
# example.create_doorframe1(p1,doorframe1_x, doorframe1_y)
#
#
# p2= APoint(-126976.8108 + 10000, -135899.2087)
# #example.create_doorframe2(pp,973.3,2410)
# example.create_doorframe2(p2,doorframe2_x, doorframe2_y,flag)

# p7 = APoint(-128150.1108+ 10000 , -133289.2087)  #输入起始点的坐标
# example.create_doorframe7(p7,949.3,590)
# p7 = APoint(p1.x,p1.y + doorframe1_y )
# example.create_doorframe7(p7,doorframe7_x, doorframe7_y)

p8 = APoint(-127028.1108 + 10000, -133289.2087 )
example.create_doorframe8(p8,917,590)
# p8 = APoint(p2.x - doorframe2_x + 5 + 10 + 2 + 58 - 70 + doorframe8_x, p2.y + doorframe2_y)
# example.create_doorframe8(p8,doorframe8_x, doorframe8_y)



# if(is_mirror == 1):
#     mirror_line_start = APoint(-126976.8108 + 1000,-135899.2087 - 100)
#     mirror_line_end = APoint(-126976.8108 + 1000,-128949.2087  + 100)
#     # 遍历模型空间中的所有对象并进行镜像
#     for obj in acad.model:
#         try:
#             # 执行镜像操作
#             #obj.TransformBy(mirror_matrix)
#             obj.Mirror(mirror_line_start, mirror_line_end)
#             print(f"Object {obj.ObjectID} mirrored.")
#         except Exception as e:
#             print(f"Failed to mirror object {obj.ObjectID}: {str(e)}")


# file_path = r"D:\CAD\new.dxf"
# acad.doc.SaveAs(file_path,13)