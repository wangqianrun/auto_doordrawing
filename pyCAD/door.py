from pyautocad import Autocad, APoint
import math
import array

class Door:
    def __init__(self,total_width,total_height,small_door_width,small_door_height,flag,bloster_type):
        self.total_width = total_width
        self.total_height = total_height
        self.small_door_width = small_door_width
        self.small_door_height = small_door_height
        self.flag = flag    #flag==1，代表小门画小圆孔
        self.bloster_type = bloster_type  # 若其值为1，代表支撑缺口长度为530和260
        self.acad = Autocad(create_if_not_exists=True)
        self.acad.prompt("Hello, Autocad from Python")
        print(self.acad.doc.Name)
        self.w = {'left1':(self.total_width / 2 - 25 - self.small_door_width - 20.5) + (self.small_door_width - 7.5) +2+5+2,
                  'right1':(self.total_width / 2 - 25 - self.small_door_width - 20.5) + (self.small_door_width + 24.5) +2+5+2,
                  'left3':(self.total_width / 2 - 25 - self.small_door_width - 20.5) + 3,
                  'left5':self.small_door_width-7,
                  'right2':self.small_door_width+25,
                  'left4':(self.total_width / 2 - 25 - self.small_door_width - 20.5) + 3- 55.5}

        self.doorsize = {
            'door_jamb_down_x': self.total_width / 2 - self.small_door_width - 25 - 2 + 48 + 27.3 - 15 + 52.7,
            'door_jamb_down_y': self.total_height,
            'door_jamb_down_y2': self.total_height - (self.total_height - (self.small_door_height - 5 + 15)) + 2,
            'door_jamb_up_x': self.total_width / 2 - self.small_door_width - 25 - 2 + 48 + 27.3,
            'door_jamb_up_y': self.total_height,
            'door_jambb_up_y2': self.small_door_height + 11,
            'doorframe6_x': self.small_door_width - 2 + 11 + 75,
            'doorframe6_y': self.total_height - (self.small_door_height - 5),
            'doorframe5_x': self.small_door_width - 4 + 75 + 75,
            'doorframe5_y': self.small_door_height - 5,
            'doorframe4_x': self.small_door_width - 2 + 11 + 29.3,
            'doorframe4_y': self.total_height - (self.small_door_height - 5),
            'doorframe3_x': self.small_door_width - 4 + 29.3 + 44 + 31,
            'doorframe3_y': self.small_door_height - 5,
            'doorframe1_x': self.small_door_width + 26 + 64.3 + 70.3,
            'doorframe1_y': self.small_door_height - 5 + 15,
            'doorframe2_x': self.small_door_width - 6 + 64.3 + 75,
            'doorframe2_y': self.small_door_height - 5 + 15,
            'doorframe8_x': self.small_door_width - 4 + 11 + 70,
            'doorframe8_y': self.total_height - (self.small_door_height - 5 + 15),
            'doorframe7_x': self.small_door_width + 28 + 11 + 70.3,
            'doorframe7_y': self.total_height - (self.small_door_height - 5 + 15)}





    def create_arc(self, x, y, radius, start_angle, end_angle):
        """绘制弧线"""
        center_point = APoint(x, y)
        start_angle = math.radians(start_angle)
        end_angle = math.radians(end_angle)
        arc = self.acad.model.AddArc(center_point, radius, start_angle, end_angle)
        arc.Color = 1
        return arc

    def create_line(self, x1, y1, x2, y2):
        """绘制直线"""
        p1 = APoint(x1, y1)
        p2 = APoint(x2, y2)
        line = self.acad.model.AddLine(p1, p2)
        line.Color = 1
        return line

    def create_capsule_circle(self, center_point_x, center_point_y):
        """绘制胶囊形圆"""
        center_point2_x = center_point_x
        center_point2_y = center_point_y + 38
        self.create_arc(center_point_x, center_point_y, 10, -180, 0)
        self.create_arc(center_point2_x, center_point2_y, 10, 0, 180)
        self.create_line(center_point_x - 10, center_point_y, center_point_x - 10, center_point_y + 38)
        self.create_line(center_point_x + 10, center_point_y, center_point_x + 10, center_point_y + 38)

    def create_candy(self, base_point_x, base_point_y):
        """绘制糖果形状"""
        self.create_arc(base_point_x, base_point_y, 3, -180, 0)
        self.create_arc(base_point_x, base_point_y + 10, 3, 0, 180)
        self.create_line(base_point_x - 3, base_point_y, base_point_x - 3, base_point_y + 10)
        self.create_line(base_point_x + 3, base_point_y, base_point_x + 3, base_point_y + 10)

        self.create_arc(base_point_x - 49, base_point_y, 3, -180, 0)
        self.create_arc(base_point_x - 49, base_point_y + 10, 3, 0, 180)
        self.create_line(base_point_x - 49 - 3, base_point_y, base_point_x - 49 - 3, base_point_y + 10)
        self.create_line(base_point_x - 49 + 3, base_point_y, base_point_x - 49 + 3, base_point_y + 10)

        self.create_arc(base_point_x - 16.5, base_point_y, 7, -90, 0)
        self.create_arc(base_point_x - 32.5, base_point_y, 7, -180, -90)
        self.create_arc(base_point_x - 16.5, base_point_y + 10, 7, 0, 90)
        self.create_arc(base_point_x - 32.5, base_point_y + 10, 7, 90, 180)
        self.create_line(base_point_x - 16.5 + 7, base_point_y, base_point_x - 16.5 + 7, base_point_y + 10)
        self.create_line(base_point_x - 32.5 - 7, base_point_y, base_point_x - 32.5 - 7, base_point_y + 10)
        self.create_line(base_point_x - 16.5, base_point_y - 7, base_point_x - 32.5, base_point_y - 7)
        self.create_line(base_point_x - 16.5, base_point_y + 10 + 7, base_point_x - 32.5, base_point_y + 10 + 7)

    def create_rectangle(self, base_point_x, base_point_y, len_x, len_y):
        """创建矩形（左下角为基点）"""
        coords = [base_point_x, base_point_y, base_point_x, base_point_y + len_y,
                  base_point_x + len_x, base_point_y + len_y, base_point_x + len_x, base_point_y]
        new_line = self.acad.model.AddLightWeightPolyline(array.array("d", coords))
        new_line.Color = 1
        new_line.Closed = True

    def create_four_rounded_rectangle(self, base_point_x, base_point_y, len_x, len_y):
        """创建四角圆角矩形（左下角圆心为基点）"""
        self.create_arc(base_point_x, base_point_y, 2, 180, 270)
        self.create_arc(base_point_x + len_x, base_point_y, 2, -90, 0)
        self.create_arc(base_point_x, base_point_y + len_y, 2, 90, 180)
        self.create_arc(base_point_x + len_x, base_point_y + len_y, 2, 0, 90)
        self.create_line(base_point_x, base_point_y - 2, base_point_x + len_x, base_point_y - 2)
        self.create_line(base_point_x - 2, base_point_y, base_point_x - 2, base_point_y + len_y)
        self.create_line(base_point_x, base_point_y + len_y + 2, base_point_x + len_x, base_point_y + len_y + 2)
        self.create_line(base_point_x + len_x + 2, base_point_y, base_point_x + len_x + 2, base_point_y + len_y)

    def create_two_rounded_rectangle_up(self, base_point_x, base_point_y, len_x, len_y):
        """创建上两角圆角矩形（左上角圆心为基点）"""
        self.create_arc(base_point_x, base_point_y, 1, 90, 180)
        self.create_arc(base_point_x + len_x, base_point_y, 1, 0, 90)
        self.create_line(base_point_x, base_point_y + 1, base_point_x + len_x, base_point_y + 1)
        self.create_line(base_point_x - 1, base_point_y, base_point_x - 1, base_point_y - len_y)
        self.create_line(base_point_x - 1, base_point_y - len_y, base_point_x + len_x + 1, base_point_y - len_y)
        self.create_line(base_point_x + len_x + 1, base_point_y, base_point_x + len_x + 1, base_point_y - len_y)

    def create_two_rounded_rectangle_down(self, base_point_x, base_point_y, len_x, len_y):
        """创建下两角圆角矩形（左下角圆心为基点）"""
        self.create_arc(base_point_x, base_point_y, 1, 180, 270)
        self.create_arc(base_point_x + len_x, base_point_y, 1, -90, 0)
        self.create_line(base_point_x, base_point_y - 1, base_point_x + len_x, base_point_y - 1)
        self.create_line(base_point_x - 1, base_point_y + len_y, base_point_x + len_x + 1, base_point_y + len_y)
        self.create_line(base_point_x - 1, base_point_y, base_point_x - 1, base_point_y + len_y)
        self.create_line(base_point_x + len_x + 1, base_point_y, base_point_x + len_x + 1, base_point_y + len_y)


    def create_Cylinder_hole_down(self, center_point_x, center_point_y):
        """创建向下的圆柱孔"""
        c_p = [-128520.3188, -134802.8228, -128498.3929, -134804.6264, -128503.3188, -134819.3228, -128504.6940,
               -134834.2596, -128520.3188, -134825.3228, -128535.9436, -134834.2596, -128537.3188, -134819.3228,
               -128542.2447, -134804.6264]
        bia = [(c_p[i] - c_p[0], c_p[i + 1] - c_p[1]) for i in range(0, len(c_p), 2)]
        start_angle = [-5, 175, -95, 85, -150, 30, 109, -71]
        end_angle = [185, 251, 71, 150, -30, 95, 276, 5]
        radius = [13.5, 8.5, 7, 8, 10, 8, 7, 8.5]
        for i in range(len(start_angle)):
            self.create_arc(center_point_x + bia[i][0], center_point_y + bia[i][1], radius[i], start_angle[i], end_angle[i])

    def create_Cylinder_hole_up(self, center_point_x, center_point_y):
        """创建向上的圆柱孔"""
        c_p = [-128498.0816, -134681.4235, -128503.0076, -134666.7270, -128504.3828, -134651.7902, -128520.0076, -134660.7270,
               -128535.6323, -134651.7902, -128537.0076, -134666.7270, -128541.9335, -134681.4235, -128520.0076, -134683.2270]
        bia = [(c_p[i] - c_p[14], c_p[i + 1] - c_p[15]) for i in range(0, len(c_p), 2)]
        start_angle = [109, -71, -150, 30, -95, 85, -5, -185]
        end_angle = [185, 95, -85, 150, -30, 251, 71, 5]
        radius = [8.5, 7, 8, 10, 8, 7, 8.5, 13.5]
        for i in range(len(start_angle)):
            self.create_arc(center_point_x + bia[i][0], center_point_y + bia[i][1], radius[i], start_angle[i], end_angle[i])

    def create_hinge_circle(self,left_center_point):
        cpoint = []
        cpoint.append(left_center_point.x)
        cpoint.append(left_center_point.y)
        cpoint.append(left_center_point.x + 2)
        cpoint.append(left_center_point.y)
        start_angle = [90, -90]
        end_angle = [270, 90]
        radius = [5.5, 5.5]
        for i in range(len(start_angle)):
            self.create_arc(cpoint[i * 2], cpoint[i * 2 + 1], radius[i], start_angle[i], end_angle[i])
        p1 = APoint(left_center_point.x, left_center_point.y + 5.5)
        p2 = APoint(p1.x + 2, p1.y)
        line1 = self.acad.model.AddLine(p1, p2)
        line1.Color = 1
        p3 = APoint(left_center_point.x, left_center_point.y - 5.5)
        p4 = APoint(p3.x + 2, p3.y)
        line2 = self.acad.model.AddLine(p3, p4)
        line2.Color = 1
        return

    def create_hinge_rectangle(self,circle_center_point, direction):
        bia_x = -129172.8042 - (-129173.3667)
        bia_y = -133652.9203 - (-133655.4203)
        if (direction == 0):  ## 缺口朝向左边
            self.create_arc(circle_center_point.x, circle_center_point.y, 2.56, -77, 77)
            p1 = APoint(circle_center_point.x + bia_x, circle_center_point.y + bia_y)
            p2 = APoint(p1.x - 15, p1.y)
            p3 = APoint(p1.x, p1.y - 5)
            p4 = APoint(p3.x - 15, p3.y)
            line1 = self.acad.model.AddLine(p1, p2)
            line2 = self.acad.model.AddLine(p3, p4)
            line1.Color = 1
            line2.Color = 1
        else:
            self.create_arc(circle_center_point.x, circle_center_point.y, 2.56, 103, 257)
            p1 = APoint(circle_center_point.x - bia_x, circle_center_point.y + bia_y)
            p2 = APoint(p1.x + 15, p1.y)
            p3 = APoint(p1.x, p1.y - 5)
            p4 = APoint(p3.x + 15, p3.y)
            line1 = self.acad.model.AddLine(p1, p2)
            line2 = self.acad.model.AddLine(p3, p4)
            line1.Color = 1
            line2.Color = 1

    def change_point(self,p, x, y):
        statr_point = APoint(p.x + x, p.y)
        end_point = APoint(p.x + x, p.y + y)
        new_line = self.acad.model.Addline(statr_point, end_point)
        new_line.Color = 1
        return

    def create_hinge1(self, base_point, direction):
        """创建铰链（左侧或右侧）"""

        bia_y = -135624.9587 - (-135899.2087)
        bia_x = -129127.4108 - (-129150.7108)
        bia_x2 = -129125.5983 - (-129150.7108)
        bia_y2 = -135600.9587 - (-135899.2087)
        p = []
        if direction == 0:  # 在基准点的右边绘制
            p1 = APoint(base_point.x + bia_x, base_point.y + bia_y)
            p.append(p1)
            p2 = APoint(p1.x + 27, p1.y)
            p.append(p2)
            p.append(APoint(p1.x, p1.y + 47))
            p.append(APoint(p1.x, p1.y + 94))
            p.append(APoint(p2.x, p2.y + 47))
            p.append(APoint(p2.x, p2.y + 94))

            # 创建铰链圆形
            for point in p:
                self.create_hinge_circle(point)

            p3 = APoint(base_point.x + bia_x2, base_point.y + bia_y2)
            self.create_hinge_rectangle(p3, 1)
            b_x = -129100.7233 - (-129125.5983)
            b_y = -135554.9587 - (-135600.9587)
            p4 = APoint(p3.x + b_x, p3.y + b_y)
            self.create_hinge_rectangle(p4, 0)

        if direction == 1:  # 在基准点的左边绘制
            p1 = APoint(base_point.x - bia_x - 2, base_point.y + bia_y)
            p.append(p1)
            p2 = APoint(p1.x - 27, p1.y)
            p.append(p2)
            p.append(APoint(p1.x, p1.y + 47))
            p.append(APoint(p1.x, p1.y + 94))
            p.append(APoint(p2.x, p2.y + 47))
            p.append(APoint(p2.x, p2.y + 94))

            # 创建铰链圆形
            for point in p:
                self.create_hinge_circle(point)

            p3 = APoint(base_point.x - bia_x2, base_point.y + bia_y2)
            self.create_hinge_rectangle(p3, 0)
            b_x = -129100.7233 - (-129125.5983)
            b_y = -135554.9587 - (-135600.9587)
            p4 = APoint(p3.x - b_x, p3.y + b_y)
            self.create_hinge_rectangle(p4, 1)

        return

    def create_hinge2(self,base_point, direction):
        bia_x = -129127.4108 - (-129150.7108)
        bia_y = -133640.9587 - (-133489.2087)
        bia_x2 = -129100.7233 - (-129150.7108)
        bia_y2 = -133664.9587 - (-133489.2087)
        p = []
        if (direction == 0):  # 在基准点的右边绘制
            p1 = APoint(base_point.x + bia_x, base_point.y + bia_y)
            p.append(p1)
            p2 = APoint(p1.x + 27, p1.y)
            p.append(p2)
            p.append(APoint(p1.x, p1.y - 47))
            p.append(APoint(p1.x, p1.y - 94))
            p.append(APoint(p2.x, p2.y - 47))
            p.append(APoint(p2.x, p2.y - 94))
            for i in range(len(p)):
                self.create_hinge_circle(p[i])

            p3 = APoint(base_point.x + bia_x2, base_point.y + bia_y2)
            self.create_hinge_rectangle(p3, 0)
            b_x = -129125.5983 - (-129100.7233)
            b_y = -133710.9587 - (-133664.9587)
            p4 = APoint(p3.x + b_x, p3.y + b_y)
            self.create_hinge_rectangle(p4, 1)

        if (direction == 1):  # 在基准点的左边绘制
            p1 = APoint(base_point.x - bia_x - 2, base_point.y + bia_y)
            p.append(p1)
            p2 = APoint(p1.x - 27, p1.y)
            p.append(p2)
            p.append(APoint(p1.x, p1.y - 47))
            p.append(APoint(p1.x, p1.y - 94))
            p.append(APoint(p2.x, p2.y - 47))
            p.append(APoint(p2.x, p2.y - 94))
            for i in range(len(p)):
                self.create_hinge_circle(p[i])

            p3 = APoint(base_point.x - bia_x2, base_point.y + bia_y2)
            self.create_hinge_rectangle(p3, 1)
            b_x = -129125.5983 - (-129100.7233)
            b_y = -133710.9587 - (-133664.9587)
            p4 = APoint(p3.x - b_x, p3.y + b_y)
            self.create_hinge_rectangle(p4, 0)

            return

    def create_Door_jamb_up(self,base_point):  ## 以右下角为基点    上门边板

        len_x = self.total_width / 2 - self.small_door_width - 25 - 2 + 48 + 27.3
        len_y = self.total_height
        len_y2 = self.small_door_height + 11

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
            self.create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3])

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

        new_line = self.acad.model.AddLightWeightPolyline(array.array("d", coords))
        new_line.Color = 1
        new_line.Closed = False

        self.create_line(coords[8], coords[9], coords[8], coords[9] - 142)
        self.create_line(coords[8] - 10, coords[9] - 140, coords[8], coords[9] - 140)
        self.create_line(base_point.x - len_x, base_point.y + 107, base_point.x - len_x, base_point.y)
        self.create_line(base_point.x - len_x, base_point.y + 105, base_point.x - len_x - 10, base_point.y + 105)
        self.create_line(base_point.x - len_x - 10, base_point.y + 105, base_point.x - len_x - 10,
                    base_point.y + len_y / 2 - 9.5 - 65.5528)
        self.create_line(base_point.x - len_x - 10, base_point.y + len_y / 2 - 9.5 - 65.5528, base_point.x - len_x - 10 + 9,
                    base_point.y + len_y / 2 - 9.5 - 65.5528)
        self.create_line(base_point.x - len_x - 10 + 9, base_point.y + len_y / 2 - 9.5 - 65.5528,
                    base_point.x - len_x - 10 + 9, base_point.y + len_y / 2 - 9.5)
        self.create_arc(base_point.x - len_x - 10 + 9 - 1, base_point.y + len_y / 2, 9.5, -84, 84)
        self.create_line(base_point.x - len_x - 10 + 9, base_point.y + len_y / 2 + 9.5 + 65.5528,
                    base_point.x - len_x - 10 + 9, base_point.y + len_y / 2 + 9.5)
        self.create_line(base_point.x - len_x - 10 + 9, base_point.y + len_y / 2 + 9.5 + 65.5528, base_point.x - len_x - 10,
                    base_point.y + len_y / 2 + 9.5 + 65.5528)
        self.create_line(base_point.x - len_x - 10, base_point.y + len_y / 2 + 9.5 + 65.5528, base_point.x - len_x - 10,
                    base_point.y + len_y - 140)
        self.create_line(base_point.x, base_point.y, base_point.x - len_x, base_point.y)

        return

    def create_Door_jamb_down(self,base_point):  ##右下为基点   下门边板

        len_x = self.total_width / 2 - self.small_door_width - 25 - 2 + 48 + 27.3 - 15 + 52.7  # 基点到最左侧的宽度
        len_y = self.total_height                                                              # 最下到最上
        len_y2 = self.total_height - (self.total_height - (self.small_door_height - 5 + 15)) + 2  #以基点为底

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
            self.create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3])

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

        new_line = self.acad.model.AddLightWeightPolyline(array.array("d", coords))
        new_line.Color = 1
        new_line.Closed = False

        self.create_line(base_point.x, base_point.y, base_point.x - len_x + 10 + 123 + 3, base_point.y)
        self.create_arc(base_point.x - len_x + 10 + 123 + 3, base_point.y + 3, 3, 180, 270)
        self.create_line(base_point.x - len_x + 10 + 123, base_point.y + 3, base_point.x - len_x + 10 + 123,
                    base_point.y + 3 + 22)
        self.create_line(base_point.x - len_x + 10 + 123, base_point.y + 3 + 22, base_point.x - len_x + 10,
                    base_point.y + 3 + 22)
        self.create_line(base_point.x - len_x + 10, base_point.y + 3 + 22, base_point.x - len_x + 10,
                    base_point.y + 3 + 22 + 82)
        self.create_line(base_point.x - len_x + 10, base_point.y + 3 + 22 + 80, base_point.x - len_x,
                    base_point.y + 3 + 22 + 80)

        self.create_line(base_point.x - len_x, base_point.y + 3 + 22 + 80, base_point.x - len_x,
                    base_point.y + len_y / 2 - 9.5 - 65.5528)
        self.create_line(base_point.x - len_x + 9, base_point.y + len_y / 2 - 9.5 - 65.5528, base_point.x - len_x,
                    base_point.y + len_y / 2 - 9.5 - 65.5528)
        self.create_line(base_point.x - len_x + 9, base_point.y + len_y / 2 - 9.5 - 65.5528, base_point.x - len_x + 9,
                    base_point.y + len_y / 2 - 9.5)
        self.create_arc(base_point.x - len_x + 9 - 1, base_point.y + len_y / 2, 9.5, -84, 84)

        self.create_line(base_point.x - len_x + 9, base_point.y + len_y / 2 + 9.5 + 65.5528, base_point.x - len_x + 9,
                    base_point.y + len_y / 2 + 9.5)
        self.create_line(base_point.x - len_x + 9, base_point.y + len_y / 2 + 9.5 + 65.5528, base_point.x - len_x,
                    base_point.y + len_y / 2 + 9.5 + 65.5528)
        self.create_line(base_point.x - len_x, base_point.y + len_y / 2 + 9.5 + 65.5528, base_point.x - len_x,
                    base_point.y + len_y - 140)
        self.create_line(base_point.x - len_x, base_point.y + len_y - 140, base_point.x - len_x + 10,
                    base_point.y + len_y - 140)
        self.create_line(base_point.x - len_x + 10, base_point.y + len_y - 140 - 2, base_point.x - len_x + 10,
                    base_point.y + len_y)

        self.create_rectangle(base_point.x - 73, base_point.y + 136.5, 54, 251)
        self.create_rectangle(base_point.x - 73, base_point.y + len_y2 - 385.5, 54, 251)

        self.create_line(base_point.x - 20, base_point.y + 462, base_point.x - 20 - 34.5, base_point.y + 462)
        self.create_line(base_point.x - 20 + 2, base_point.y + 462 + 2, base_point.x - 20 + 2,
                    base_point.y + 462 + 2 + 176.5)
        self.create_line(base_point.x - 20 - 34.5, base_point.y + 462 + 2 + 176.5 + 2, base_point.x - 20,
                    base_point.y + 462 + 2 + 176.5 + 2)
        self.create_line(base_point.x - 20 - 34.5 - 2, base_point.y + 462 + 2 + 176.5, base_point.x - 20 - 34.5 - 2,
                    base_point.y + 462 + 2)
        self.create_arc(base_point.x - 20, base_point.y + 462 + 2, 2, -90, 0)
        self.create_arc(base_point.x - 20, base_point.y + 462 + 2 + 176.5, 2, 0, 90)
        self.create_arc(base_point.x - 20 - 34.5, base_point.y + 462 + 2 + 176.5, 2, 90, 180)
        self.create_arc(base_point.x - 20 - 34.5, base_point.y + 462 + 2, 2, 180, 270)

        return

    def create_doorframe6(self,base_point):  ## 右下角为基点  右侧正面门头板

        len_x = self.small_door_width - 2 + 11 + 75               # 基点到最左侧宽度
        len_y = self.total_height - (self.small_door_height - 5)  # 高度

        incise_line = []  # 切割标记线
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
        incise_line.append(base_point.y + len_y - 2)

        for i in range(0, len(incise_line), 4):
            self.create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3])

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

        new_line = self.acad.model.AddLightWeightPolyline(array.array("d", coords))
        new_line.Color = 1
        new_line.Closed = False

        cen_point = APoint(base_point.x - len_x + 111.2, base_point.y + len_y - 25.8)
        new_circle = self.acad.model.AddCircle(cen_point, 4.2)
        new_circle.Color = 1

        self.create_arc(base_point.x - len_x + 50 + 5 + 1, base_point.y + 1, 1, 180, 270)

        return

    def create_doorframe5(self,base_point):  ## 以左下角为基点   右侧正面小门板

        len_x = self.small_door_width - 4 + 75 + 75   # 最左到最右宽度
        len_y = self.small_door_height - 5            # 高度

        incise_line = []  # 切割标记线
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
        incise_line.append(base_point.y + len_y - 10 - 2)

        for i in range(0, len(incise_line), 4):
            self.create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3])

        coords = []
        coords.append(base_point.x)
        coords.append(base_point.y)

        coords.append(base_point.x)
        coords.append(base_point.y + len_y - 10 - 10)

        coords.append(base_point.x + 50)
        coords.append(base_point.y + len_y - 10 - 10)

        coords.append(base_point.x + 50)
        coords.append(base_point.y + len_y - 10)

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

        new_line = self.acad.model.AddLightWeightPolyline(array.array("d", coords))
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
        new_line = self.acad.model.AddLightWeightPolyline(array.array("d", coords2))
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
        new_line = self.acad.model.AddLightWeightPolyline(array.array("d", coords2))
        new_line.Color = 1
        new_line.Closed = True

        self.create_capsule_circle(base_point.x + 120, base_point.y + 961 - 8)
        self.create_capsule_circle(base_point.x + 120, base_point.y + 961 + 196 - 8)
        self.create_Cylinder_hole_up(base_point.x + 120, base_point.y + 961 + 141.5 - 8)
        self.create_Cylinder_hole_down(base_point.x + 120, base_point.y + 961 + 92.5 - 8)

        return

    def create_doorframe4(self,base_point):   ## 以右下角为基点   左侧正面门头板

        len_x = self.small_door_width - 2 + 11 + 29.3             # 最左侧到最右侧宽度
        len_y = self.total_height - (self.small_door_height- 5)   # 最下到最上高度


        incise_line = []  # 切割标记线
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
        incise_line.append(base_point.y + len_y - 2)
        for i in range(0, len(incise_line), 4):
            self.create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3])

        coords = []
        coords.append(base_point.x)
        coords.append(base_point.y)
        coords.append(base_point.x)
        coords.append(base_point.y + len_y)
        coords.append(base_point.x - len_x)
        coords.append(base_point.y + len_y)
        coords.append(base_point.x - len_x)
        coords.append(base_point.y)
        new_line = self.acad.model.AddLightWeightPolyline(array.array("d", coords))
        new_line.Color = 1
        new_line.Closed = False

        cen_point = APoint(coords[2] - 65.5, coords[3] - 25.8)
        new_circle = self.acad.model.AddCircle(cen_point, 4.2)
        new_circle.Color = 1

        return


    def create_doorframe3(self,base_point):  ##右下为基点

        len_x = self.small_door_width - 4 + 29.3 + 44 + 31   # 最左到最右宽度
        len_y = self.small_door_height - 5                   # 最下到最上高度

        incise_line = []  # 切割标记线
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
        incise_line.append(base_point.y + len_y - 2)

        for i in range(0, len(incise_line), 4):
            self.create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3])

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

        new_line = self.acad.model.AddLightWeightPolyline(array.array("d", coords))
        new_line.Color = 1
        new_line.Closed = True

        if (self.flag == 1):
            cen_point1 = APoint(base_point.x - 88.3, base_point.y + 963)
            cen_point2 = APoint(base_point.x - 88.3, base_point.y + 963 + 234)
            new_circle1 = self.acad.model.AddCircle(cen_point1, 10)
            new_circle1.Color = 1
            new_circle2 = self.acad.model.AddCircle(cen_point2, 10)
            new_circle2.Color = 1

        return

    def create_doorframe1(self,base_point):  # 以右下角为基点   左侧背面小门板

        len_x = self.small_door_width + 26 +  64.3 + 70.3  # 最左侧到最右宽度
        len_y = self.small_door_height - 5 + 15            # 最下到最上高度


        incise_line = []  # 切割标记线
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

        for i in range(0, len(incise_line), 4):
            self.create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3])

        coords = []
        coords.append(base_point.x)
        coords.append(base_point.y)
        coords.append(base_point.x - len_x)
        coords.append(base_point.y)
        coords.append(base_point.x - len_x)
        coords.append(base_point.y + len_y)
        coords.append(base_point.x)
        coords.append(base_point.y + len_y)
        new_line = self.acad.model.AddLightWeightPolyline(array.array("d", coords))
        new_line.Color = 1
        new_line.Closed = True

        self.create_hinge1(APoint(base_point.x - len_x, base_point.y), 0)  # 23.3 274.25
        self.create_hinge2(APoint(base_point.x - len_x, base_point.y + len_y), 0)  # 23.3 151.75
        self.create_capsule_circle(base_point.x - 129.3, base_point.y + 963)
        self.create_capsule_circle(base_point.x - 129.3, base_point.y + 963 + 196)
        self.create_Cylinder_hole_up(base_point.x - 129.3, base_point.y + 963 + 141.5)
        self.create_Cylinder_hole_down(base_point.x - 129.3, base_point.y + 963 + 92.5)
        self.create_rectangle(base_point.x - 62.55, base_point.y + 925, 40.5, 145)
        self.create_rectangle(base_point.x - 62.55, base_point.y + 925 + 155, 40.5, 145)

        self.create_four_rounded_rectangle(base_point.x - 138.8, base_point.y + 264, 34.5, 176.5)
        self.create_two_rounded_rectangle_up(base_point.x - 61.55, base_point.y + 780.75 + 598.5, 38.5, 144.25)
        self.create_two_rounded_rectangle_down(base_point.x - 61.55, base_point.y + 780.75, 38.5, 134.25)

        if (self.small_door_height <= 2200):
            self.create_four_rounded_rectangle(base_point.x - 138.8, base_point.y + len_y - 265 - 2 - 176.5, 34.5, 176.5)
        elif (self.small_door_height <= 2400):
            self.create_four_rounded_rectangle(base_point.x - 138.8, base_point.y + len_y - 465 - 2 - 176.5, 34.5, 176.5)
        else:
            self.create_four_rounded_rectangle(base_point.x - 138.8, base_point.y + len_y - 265 - 2 - 176.5 + len_y - 2400,
                                          34.5, 176.5)

        return

    def create_doorframe2(self,base_point):  # 以右下角为基点  右侧背面小门板

        len_x = self.small_door_width - 6 +  64.3 + 75  # 最左侧到最右宽度
        len_y = self.small_door_height - 5 + 15           # 最下到最上高度

        incise_line = []  # 切割标记线
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

        for i in range(0, len(incise_line), 4):
            self.create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3])

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

        new_line = self.acad.model.AddLightWeightPolyline(array.array("d", coords))
        new_line.Color = 1
        new_line.Closed = False

        self.create_arc(base_point.x - len_x + 5 + 10 + 2, base_point.y + len_y - 2, 2, 90, 180)

        coords2 = []
        coords2.append(base_point.x)
        coords2.append(base_point.y)
        coords2.append(base_point.x)
        coords2.append(base_point.y + len_y)
        coords2.append(base_point.x - 64.3 + 2 + 11)
        coords2.append(base_point.y + len_y)
        new_line2 = self.acad.model.AddLightWeightPolyline(array.array("d", coords2))
        new_line2.Color = 1
        new_line2.Closed = False

        self.create_hinge1(APoint(base_point.x, base_point.y), 1)
        self.create_hinge2(APoint(base_point.x, base_point.y + len_y), 1)

        if (self.flag == 1):
            cen_point1 = APoint(base_point.x - len_x + 5 + 114, base_point.y + 963)
            cen_point2 = APoint(base_point.x - len_x + 5 + 114, base_point.y + 963 + 234)
            new_circle1 = self.acad.model.AddCircle(cen_point1, 10)
            new_circle1.Color = 1
            new_circle2 = self.acad.model.AddCircle(cen_point2, 10)
            new_circle2.Color = 1

        self.create_rectangle(base_point.x - len_x + 24.75, base_point.y + 925, 40.5, 145)
        self.create_rectangle(base_point.x - len_x + 24.75, base_point.y + 925 + 155, 40.5, 145)

        self.create_four_rounded_rectangle(base_point.x - len_x + 5 + 20, base_point.y + 264, 34.5, 176.5)
        self.create_two_rounded_rectangle_up(base_point.x - len_x + 5 + 20.75, base_point.y + 780.75 + 598.5, 38.5, 144.25)
        self.create_two_rounded_rectangle_down(base_point.x - len_x + 5 + 20.75, base_point.y + 780.75, 38.5, 134.25)

        if (self.small_door_height <= 2200):
            self.create_four_rounded_rectangle(base_point.x - len_x + 5 + 20, base_point.y + len_y - 265 - 2 - 176.5, 34.5,
                                          176.5)
        elif (self.small_door_height <= 2400):
            self.create_four_rounded_rectangle(base_point.x - len_x + 5 + 20, base_point.y + len_y - 465 - 2 - 176.5, 34.5,
                                          176.5)
        else:
            self.create_four_rounded_rectangle(base_point.x - len_x + 5 + 20,
                                          base_point.y + len_y - 265 - 2 - 176.5 - (len_y - 2400), 34.5, 176.5)

        return

    def create_doorframe8(self,p0):  ## 右下角为基点  右侧背面门头板

        len_x = self.small_door_width - 4  + 11 + 70                    # 基点到最下最左侧宽度
        len_y = self.total_height - (self.small_door_height - 5 + 15)   # 最下到最上高度

        coords = []

        coords.append(p0.x)
        coords.append(p0.y)

        coords.append(p0.x)
        coords.append(p0.y + len_y)

        coords.append(p0.x - len_x)
        coords.append(p0.y + len_y)

        coords.append(p0.x - len_x)
        coords.append(p0.y + len_y - 20)

        coords.append(p0.x - len_x - 5)
        coords.append(p0.y + len_y - 20)

        coords.append(p0.x - len_x - 5)
        coords.append(p0.y + 20)

        coords.append(p0.x - len_x)
        coords.append(p0.y + 20)

        coords.append(p0.x - len_x)
        coords.append(p0.y)

        new_line = self.acad.model.AddLightWeightPolyline(array.array("d", coords))
        new_line.Color = 1
        new_line.Closed = True

        p = []
        for i in range(len(coords)):
            if (i % 2 == 0):
                p.append(APoint(coords[i], coords[i + 1]))

        self.change_point(p[0], -11, 2)
        self.change_point(p[7], 70, 2)
        self.change_point(p[2], 70, -2)
        self.change_point(p[1], -11, -2)

        return

    def create_doorframe7(self,p0):  #右下角为基点  左侧背面门头板

        len_x = self.small_door_width + 28 + 11 + 70.3                  # 最左到最右宽度
        len_y = self.total_height - (self.small_door_height - 5 + 15)   # 最下到最上高度


        coords = []
        p1_x = p0.x
        p1_y = p0.y + len_y
        #    p2 = p0
        p2_x = p1_x - len_x
        p2_y = p1_y
        #    p3=p0
        p3_x = p0.x - len_x
        p3_y = p0.y

        coords.append(p0.x)
        coords.append(p0.y)
        coords.append(p1_x)
        coords.append(p1_y)
        coords.append(p2_x)
        coords.append(p2_y)
        coords.append(p3_x)
        coords.append(p3_y)
        #   print(coords)
        new_line = self.acad.model.AddLightWeightPolyline(array.array("d", coords))
        new_line.Color = 1
        new_line.Closed = False
        p = []
        for i in range(len(coords)):
            if (i % 2 == 0):
                p.append(APoint(coords[i], coords[i + 1]))
        self.change_point(p[2], 11, -2)
        self.change_point(p[3], 11, 2)
        self.change_point(p[1], -14.3, -2)
        self.change_point(p[1], -70.3, -2)
        self.change_point(p[0], -14.3, 2)
        self.change_point(p[0], -70.3, 2)
        return

    def left_1(self,base_point_x, base_point_y):  # 以最左侧最上第一个点为基点

        obj = []

        x1 = (self.total_width / 2 - 25 - self.small_door_width - 20.5)  # 门边板支撑宽度
        x2 = (self.small_door_width - 7.5)  # 门头板支撑宽度

        if (self.bloster_type == 1):  ## 如果是类型1  支撑的下侧固定长度一个为260 一个为530
            x3 = 260
            x4 = 530
            bia_x3 = 159  # 长度260的口距离下衔接左侧点的距离
            bia_x4 = (x2 + 2) / 2 - (x4 / 2)  # 长度530的口距离下衔接右侧点的距离
        else:
            x3 = 320
            x4 = 620
            bia_x3 = 154.5
            bia_x4 = (x2 + 2) / 2 - (x4 / 2)

        incise_line = []  # 切割标记线

        incise_line.append(base_point_x)
        incise_line.append(base_point_y)
        incise_line.append(base_point_x + 2)
        incise_line.append(base_point_y)

        incise_line.append(
            base_point_x + 2 + x1 + 5 + x2 + 2)
        incise_line.append(base_point_y)
        incise_line.append(
            base_point_x + 2 + x1 + 5 + x2 + 2 - 2)
        incise_line.append(base_point_y)

        incise_line.append(base_point_x)
        incise_line.append(base_point_y - 74)
        incise_line.append(base_point_x + 2)
        incise_line.append(base_point_y - 74)

        incise_line.append(
            base_point_x + 2 + x1 + 5 + x2 + 2 + 17)
        incise_line.append(base_point_y - 74)
        incise_line.append(base_point_x + 2 + x1 + 5 + x2 + 2 + 17 - 2)
        incise_line.append(base_point_y - 74)

        for i in range(0, len(incise_line), 4):
            line = self.create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3])
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

        obj.append(self.create_arc(coords[6] + 2, coords[7], 2, -180, -90))
        obj.append(self.create_line(coords[6] + 2, coords[7] - 2, coords[6] + 2 + 1, coords[7] - 2))
        obj.append(self.create_arc(coords[6] + 2 + 1, coords[7], 2, -90, 0))

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

        obj.append(self.create_arc(coords2[14], coords2[15] - 2, 2, 0, 90))
        obj.append(self.create_line(coords2[14] + 2, coords2[15] - 2, coords2[14] + 2, coords2[15] - 2 - 8))

        coords3 = []
        coords3.append(base_point_x)
        coords3.append(base_point_y - 74)

        coords3.append(coords3[0] + 2)
        coords3.append(coords3[1] - 14.5)

        if (self.bloster_type == 1):
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

        if (self.bloster_type == 1):
            coords3.append(coords3[10] + bia_x3)
        else:
            coords3.append(coords3[10] + x1 + 15 - bia_x3 - x3)

        coords3.append(coords3[11])

        coords3.append(coords3[12])
        coords3.append(coords3[13] + 24.5)

        obj.append(self.create_arc(coords3[14] + 2, coords3[15], 2, 90, 180))
        obj.append(self.create_line(coords3[14] + 2, coords3[15] + 2, coords3[14] + 2 + 1, coords3[15] + 2))
        obj.append(self.create_arc(coords3[14] + 2 + 1, coords3[15], 2, 0, 90))

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

        new_line1 = self.acad.model.AddLightWeightPolyline(array.array("d", coords))
        new_line1.Color = 1
        new_line1.Closed = False
        obj.append(new_line1)
        # new_line1.Mirror(mirror_line_start,mirror_line_end)

        new_line2 = self.acad.model.AddLightWeightPolyline(array.array("d", coords2))
        new_line2.Color = 1
        new_line2.Closed = False
        obj.append(new_line2)
        # new_line2.Mirror(mirror_line_start, mirror_line_end)

        new_line3 = self.acad.model.AddLightWeightPolyline(array.array("d", coords3))
        new_line3.Color = 1
        new_line3.Closed = False
        obj.append(new_line3)
        # new_line3.Mirror(mirror_line_start, mirror_line_end)

        new_line4 = self.acad.model.AddLightWeightPolyline(array.array("d", coords4))
        new_line4.Color = 1
        new_line4.Closed = False
        obj.append(new_line4)
        # new_line4.Mirror(mirror_line_start, mirror_line_end)

        ##绘制左侧圆口
        obj.append(self.create_line(base_point_x, base_point_y, base_point_x, base_point_y - 7.4196))
        obj.append(self.create_line(base_point_x, base_point_y - 74, base_point_x, base_point_y - 74 + 7.4196))
        obj.append(self.create_arc(base_point_x + 5, base_point_y - 37, 30, -100, 100))

        mirror_line_start = APoint(base_point_x, base_point_y - 138.5)
        mirror_line_end = APoint(base_point_x + 100, base_point_y - 138.5)
        for i in range(len(obj)):
            obj[i].Mirror(mirror_line_start, mirror_line_end)

        self.create_candy(base_point_x + 2 + 5 + x1 + x2 + 2 - 11.5, 2 * mirror_line_start.y - base_point_y + 27)

        return

    def right_1(self,base_point_x, base_point_y):  # 以最右侧最上第一个点为基点

        obj = []

        x1 = (self.total_width / 2 - 25 - self.small_door_width - 20.5)  # 门边板支撑宽度
        x2 = (self.small_door_width + 24.5)  # 门头板支撑宽度


        if (self.bloster_type == 1):  ## 如果是类型1  支撑的下侧固定长度一个为260 一个为530
            x3 = 260
            x4 = 530
            bia_x3 = 159  # 长度260的口距离下衔接左侧点的距离
            bia_x4 = (self.small_door_width - 3.9) / 2 - (x4 / 2)  # 长度530的口距离下衔接右侧点的距离
        else:
            x3 = 320
            x4 = 620
            bia_x3 = 154.5
            bia_x4 = (self.small_door_width - 3.9) / 2 - (x4 / 2)

        incise_line = []  # 切割标记线

        incise_line.append(base_point_x)
        incise_line.append(base_point_y)
        incise_line.append(base_point_x - 2)
        incise_line.append(base_point_y)

        incise_line.append(
            base_point_x - 2 - (self.total_width / 2 - 25 - self.small_door_width - 2 - 20.5) - 5 - (self.small_door_width + 24.5) - 2)
        incise_line.append(base_point_y)
        incise_line.append(base_point_x - 2 - (self.total_width / 2 - 25 - self.small_door_width - 2 - 20.5) - 5 - (
                    self.small_door_width + 24.5) - 2 + 2)
        incise_line.append(base_point_y)

        incise_line.append(base_point_x)
        incise_line.append(base_point_y - 74)
        incise_line.append(base_point_x - 2)
        incise_line.append(base_point_y - 74)

        incise_line.append(base_point_x - 2 - (self.total_width / 2 - 25 - self.small_door_width - 2 - 20.5) - 5 - (
                    self.small_door_width + 24.5) - 2 + 15.4)
        incise_line.append(base_point_y - 74)
        incise_line.append(base_point_x - 2 - (self.total_width / 2 - 25 - self.small_door_width - 2 - 20.5) - 5 - (
                    self.small_door_width + 24.5) - 2 + 15.4 + 2)
        incise_line.append(base_point_y - 74)

        for i in range(0, len(incise_line), 4):
            obj.append(self.create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3]))

        coords = []

        coords.append(base_point_x)
        coords.append(base_point_y)

        coords.append(base_point_x - 2)
        coords.append(base_point_y + 14.5)

        coords.append(coords[2] - x1)
        coords.append(coords[3])

        coords.append(coords[4])
        coords.append(coords[5] - 24.5)

        obj.append(self.create_arc(coords[6] - 2, coords[7], 2, -90, 0))
        obj.append(self.create_line(coords[6] - 2, coords[7] - 2, coords[6] - 2 - 1, coords[7] - 2))
        obj.append(self.create_arc(coords[6] - 2 - 1, coords[7], 2, -180, -90))

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

        obj.append(self.create_arc(coords2[8] + 2, coords2[9], 2, -180, -90))

        coords3 = []
        coords3.append(base_point_x)
        coords3.append(base_point_y - 74)

        coords3.append(coords3[0] - 2)
        coords3.append(coords3[1] - 14.5)

        if (self.bloster_type == 1):
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

        if (self.bloster_type == 1):
            coords3.append(coords3[10] - bia_x3)
        else:
            coords3.append(coords3[10] - (x1 + 15 - bia_x3 - x3))
        coords3.append(coords3[11])

        coords3.append(coords3[12])
        coords3.append(coords3[13] + 24.5)

        obj.append(self.create_arc(coords3[14] - 2, coords3[15], 2, 0, 90))
        obj.append(self.create_line(coords3[14] - 2, coords3[15] + 2, coords3[14] - 2 - 1, coords3[15] + 2))
        obj.append(self.create_arc(coords3[14] - 2 - 1, coords3[15], 2, 90, 180))

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

        coords4.append(coords4[2] - (self.small_door_width - 3.9) + 2)
        coords4.append(coords4[11])

        coords4.append(coords4[12] - 2)
        coords4.append(coords4[13] + 14.5)

        coords4.append(coords4[14])
        coords4.append(coords4[15] + 26)

        coords4.append(coords4[16] - 1.6)
        coords4.append(coords4[17])

        coords4.append(coords4[18])
        coords4.append(coords4[19] - 5)

        coords4.append(coords4[20] - 11.8)
        coords4.append(coords4[21])

        new_line1 = self.acad.model.AddLightWeightPolyline(array.array("d", coords))
        new_line1.Color = 1
        new_line1.Closed = False
        obj.append(new_line1)
        # new_line1.Mirror(mirror_line_start,mirror_line_end)

        new_line2 = self.acad.model.AddLightWeightPolyline(array.array("d", coords2))
        new_line2.Color = 1
        new_line2.Closed = False
        obj.append(new_line2)
        # new_line2.Mirror(mirror_line_start, mirror_line_end)

        new_line3 = self.acad.model.AddLightWeightPolyline(array.array("d", coords3))
        new_line3.Color = 1
        new_line3.Closed = False
        obj.append(new_line3)
        # new_line3.Mirror(mirror_line_start, mirror_line_end)

        new_line4 = self.acad.model.AddLightWeightPolyline(array.array("d", coords4))
        new_line4.Color = 1
        new_line4.Closed = False
        obj.append(new_line4)
        # new_line4.Mirror(mirror_line_start, mirror_line_end)

        ##绘制左侧圆口
        self.create_line(base_point_x, base_point_y, base_point_x, base_point_y - 7.4196)
        self.create_line(base_point_x, base_point_y - 74, base_point_x, base_point_y - 74 + 7.4196)
        self.create_arc(base_point_x - 5, base_point_y - 37, 30, 80, 280)

        mirror_line_start = APoint(base_point_x, base_point_y - 138.5)
        mirror_line_end = APoint(base_point_x - 100, base_point_y - 138.5)
        for i in range(len(obj)):
            obj[i].Mirror(mirror_line_start, mirror_line_end)

        self.create_line(base_point_x, 2 * mirror_line_start.y - base_point_y, base_point_x,
                    2 * mirror_line_start.y - (base_point_y - 74))

        self.create_candy(base_point_x - 2 - 5 - x1 - x2 - 2 + 74.5, 2 * mirror_line_start.y - base_point_y + 31.5)

        self.create_line(base_point_x - 2 - 5 - x1 - x2 - 2 + 39.85, base_point_y - 26.35,
                    base_point_x - 2 - 5 - x1 - x2 - 2 + 39.85 + 20.3, base_point_y - 26.35)
        self.create_line(base_point_x - 2 - 5 - x1 - x2 - 2 + 39.85, base_point_y - 26.35,
                    base_point_x - 2 - 5 - x1 - x2 - 2 + 39.85, base_point_y - 26.35 - 20.3)
        self.create_line(base_point_x - 2 - 5 - x1 - x2 - 2 + 39.85, base_point_y - 26.35 - 20.3,
                    base_point_x - 2 - 5 - x1 - x2 - 2 + 39.85 + 20.3, base_point_y - 26.35 - 20.3)
        self.create_line(base_point_x - 2 - 5 - x1 - x2 - 2 + 39.85 + 20.3, base_point_y - 26.35,
                    base_point_x - 2 - 5 - x1 - x2 - 2 + 39.85 + 20.3, base_point_y - 26.35 - 20.3)

        return

    def left_3(self,base_point_x, base_point_y):  ## 左下第一个支撑  门边板下边支撑  以左上侧折弯点的左顶点为基点

        obj = []

        width = (self.total_width / 2 - 25 - self.small_door_width - 20.5) + 3
        if (self.bloster_type == 1):
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
            obj.append(self.create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3]))

        coords = []
        coords.append(base_point_x)
        coords.append(base_point_y)

        coords.append(base_point_x + 2)
        coords.append(base_point_y + 14.5)

        if (self.bloster_type == 1):
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

        if (self.bloster_type == 1):
            coords.append(coords[10] + bia_x3 + 13)
        else:
            coords.append(coords[10] + width - 2 - x3 - bia_x3 + 13)
        coords.append(coords[11])

        coords.append(coords[12] + 2)
        coords.append(coords[13] - 14.5)

        coords.append(coords[14])
        coords.append(coords[15] - 8)

        obj.append(self.create_arc(coords[16] - 2, coords[17], 2, -90, 0))

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

        obj.append(self.create_arc(coords2[8] - 34, coords2[9] + 32, 9.75, -90, 90))
        obj.append(self.create_arc(coords2[8] - 34 - 66, coords2[9] + 32, 9.75, 90, 270))
        obj.append(self.create_line(coords2[8] - 34, coords2[9] + 32 - 9.75, coords2[8] - 34 - 66, coords2[9] + 32 - 9.75))
        obj.append(self.create_line(coords2[8] - 34, coords2[9] + 32 + 9.75, coords2[8] - 34 - 66, coords2[9] + 32 + 9.75))

        obj.append(self.create_line(base_point_x, base_point_y, base_point_x, base_point_y - 7.4196))
        obj.append(self.create_line(base_point_x, base_point_y - 74, base_point_x, base_point_y - 74 + 7.4196))
        obj.append(self.create_arc(base_point_x + 5, base_point_y - 37, 30, -100, 100))

        coords3 = []
        coords3.append(base_point_x)
        coords3.append(base_point_y - 74)

        coords3.append(coords3[0] + 2)
        coords3.append(coords3[1] - 14.5)

        coords3.append(coords3[2] + width - 2 - 2)
        coords3.append(coords3[3])

        new_line1 = self.acad.model.AddLightWeightPolyline(array.array("d", coords))
        new_line1.Color = 1
        new_line1.Closed = False
        obj.append(new_line1)

        new_line2 = self.acad.model.AddLightWeightPolyline(array.array("d", coords2))
        new_line2.Color = 1
        new_line2.Closed = False
        obj.append(new_line2)

        new_line3 = self.acad.model.AddLightWeightPolyline(array.array("d", coords3))
        new_line3.Color = 1
        new_line3.Closed = False
        obj.append(new_line3)

        start = base_point_x + self.w['left3'] + 61 + self.w['left5'] + 300 + self.w['right2'] + 61 + self.w['left3']

        mirror_line_start = APoint((base_point_x + start) / 2, base_point_y)
        mirror_line_end = APoint((base_point_x + start) / 2, base_point_y - 50)
        for i in range(len(obj)):
            obj[i].Mirror(mirror_line_start, mirror_line_end)

        return

    def left_4(self,base_point_x, base_point_y):  ## 左下角支撑 以左上焊点左侧端点为基点   门边板外支撑

        obj = []

        width = (self.total_width / 2 - 25 - self.small_door_width - 20.5)  + 3
        if (self.bloster_type == 1):
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
            obj.append(self.create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3]))

        coords = []

        coords.append(base_point_x)
        coords.append(base_point_y + 14.5)

        coords.append(coords[0] + 6.5)
        coords.append(coords[1])

        coords.append(coords[2] + 14.5)
        coords.append(coords[3] - 14.5)

        obj.append(self.create_line(coords[4], coords[5], coords[4], coords[5] - 2))
        obj.append(self.create_line(coords[4], coords[5] - 9, coords[4], coords[5] - 34))
        obj.append(self.create_line(coords[4], coords[5] - 42, coords[4], coords[5] - 68))
        obj.append(self.create_line(coords[4], coords[5] - 72, coords[4], coords[5] - 74))

        coords.append(coords[4] + 14.5)
        coords.append(coords[5] + 14.5)

        if (self.bloster_type == 1):
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

        if (self.bloster_type == 1):
            coords.append(coords[14] + bia_x3 + 13)
        else:
            coords.append(coords[14] + changeable_width + 13)
        coords.append(coords[15])

        coords.append(coords[16] + 2)
        coords.append(coords[17] - 14.5)

        coords.append(coords[18])
        coords.append(coords[19] - 8)

        obj.append(self.create_arc(coords[20] - 2, coords[21], 2, -90, 0))

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

        coords2.append(coords2[12] + 1.2)
        coords2.append(coords2[13])

        coords2.append(coords2[14])
        coords2.append(coords2[15] - 5)

        coords2.append(coords2[16] + 11.8)
        coords2.append(coords2[17])

        ## 绘制左侧内部孔
        obj.append(self.create_arc(base_point_x + 57, base_point_y - 37, 6, 90, 270))
        obj.append(self.create_arc(base_point_x + 57 + 12.5, base_point_y - 37, 7.5, -127, 127))
        obj.append(self.create_line(base_point_x + 57, base_point_y - 37 + 6, base_point_x + 57 + 8, base_point_y - 37 + 6))
        obj.append(self.create_line(base_point_x + 57, base_point_y - 37 - 6, base_point_x + 57 + 8, base_point_y - 37 - 6))

        ## 绘制右侧内部孔
        obj.append(self.create_arc(coords2[10] - 34, coords2[11] + 32, 6.75, -90, 90))
        obj.append(self.create_arc(coords2[10] - 34 - 56, coords2[11] + 32, 6.75, 90, 270))
        obj.append(
           self.create_line(coords2[10] - 34, coords2[11] + 32 + 6.75, coords2[10] - 34 - 56, coords2[11] + 32 + 6.75))
        obj.append(
            self.create_line(coords2[10] - 34, coords2[11] + 32 - 6.75, coords2[10] - 34 - 27, coords2[11] + 32 - 6.75))
        obj.append(self.create_line(coords2[10] - 34 - 27, coords2[11] + 32 - 6.75, coords2[10] - 34 - 27 - 1,
                               coords2[11] + 32 - 6.75 - 2))
        obj.append(self.create_line(coords2[10] - 34 - 27 - 2, coords2[11] + 32 - 6.75, coords2[10] - 34 - 27 - 1,
                               coords2[11] + 32 - 6.75 - 2))
        obj.append(
            self.create_line(coords2[10] - 34 - 29, coords2[11] + 32 - 6.75, coords2[10] - 34 - 56, coords2[11] + 32 - 6.75))

        obj.append(self.create_line(base_point_x, base_point_y + 14.5, base_point_x, base_point_y - 88.5))

        new_line1 = self.acad.model.AddLightWeightPolyline(array.array("d", coords))
        new_line1.Color = 1
        new_line1.Closed = False
        obj.append(new_line1)

        new_line2 = self.acad.model.AddLightWeightPolyline(array.array("d", coords2))
        new_line2.Color = 1
        new_line2.Closed = False
        obj.append(new_line2)

        start = base_point_x + self.w['left4'] + 61 + self.w['left5'] + 300 + self.w['right2'] + 61 + self.w['left4']

        mirror_line_start = APoint((base_point_x + start) / 2, base_point_y)
        mirror_line_end = APoint((base_point_x + start) / 2, base_point_y - 50)
        for i in range(len(obj)):
            obj[i].Mirror(mirror_line_start, mirror_line_end)

        return

    def left_5(self,base_point_x, base_point_y):  # 以左上侧折弯点左端点为基点   左侧小门支撑

        obj = []

        width = self.small_door_width - 7

        if (self.bloster_type == 1):
            x4 = 530
            bia_x4 = (width + 2.6) / 2 - (x4 / 2) - 2

        else:
            x4 = 620
            bia_x4 = (width + 2.6) / 2 - (x4 / 2) - 2

        # changeable_width = width - 16.4 - bia_x4 - x4

        incise_line = []  # 切割标记线
        incise_line.append(base_point_x)
        incise_line.append(base_point_y)
        incise_line.append(base_point_x + 2)
        incise_line.append(base_point_y)

        coords = []

        coords.append(base_point_x)
        coords.append(base_point_y - 45)

        obj.append(self.create_arc(coords[0] + 2, coords[1], 2, 180, 270))

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
        obj.append(self.create_arc(coords[8] - 34, coords[9] - 32, 6.75, -90, 90))
        obj.append(self.create_arc(coords[8] - 34 - 56, coords[9] - 32, 6.75, 90, 270))
        obj.append(self.create_line(coords[8] - 34, coords[9] - 32 - 6.75, coords[8] - 34 - 56, coords[9] - 32 - 6.75))
        obj.append(self.create_line(coords[8] - 34, coords[9] - 32 + 6.75, coords[8] - 34 - 27, coords[9] - 32 + 6.75))
        obj.append(
            self.create_line(coords[8] - 34 - 27, coords[9] - 32 + 6.75, coords[8] - 34 - 27 - 1, coords[9] - 32 + 6.75 + 2))
        obj.append(self.create_line(coords[8] - 34 - 27 - 2, coords[9] - 32 + 6.75, coords[8] - 34 - 27 - 1,
                               coords[9] - 32 + 6.75 + 2))
        obj.append(self.create_line(coords[8] - 34 - 29, coords[9] - 32 + 6.75, coords[8] - 34 - 56, coords[9] - 32 + 6.75))

        coords.append(coords[8])
        coords.append(coords[9] - 69)

        coords.append(coords[10] + 1.2)
        coords.append(coords[11])

        coords.append(coords[12])
        coords.append(coords[13] + 5)

        coords.append(coords[14] + 13.8)
        coords.append(coords[15])

        obj.append(self.create_arc(coords[16], coords[17] - 2, 2, 0, 90))

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
            obj.append(self.create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3]))

        new_line1 = self.acad.model.AddLightWeightPolyline(array.array("d", coords))
        new_line1.Color = 1
        new_line1.Closed = False
        obj.append(new_line1)

        new_line2 = self.acad.model.AddLightWeightPolyline(array.array("d", coords2))
        new_line2.Color = 1
        new_line2.Closed = False
        obj.append(new_line2)

        mirror_line_start = APoint(base_point_x, base_point_y + (-214429.8392 - 214706.8392) / 2 - (-214429.8392))
        mirror_line_end = APoint(base_point_x + width, base_point_y + (-214429.8392 - 214706.8392) / 2 - (-214429.8392))
        for i in range(len(obj)):
            obj[i].Mirror(mirror_line_start, mirror_line_end)

        return

    def right_2(self,base_point_x, base_point_y):  ## 以左上折弯点左端点为基点    小门支撑，长

        obj = []

        width = self.small_door_width + 25

        if (self.bloster_type == 1):
            x4 = 530
            bia_x4 = (width - 29.8) / 2 - (x4 / 2) - 2
        else:
            x4 = 620
            bia_x4 = (width - 29.8) / 2 - (x4 / 2) - 2

        # changeable_width = width - 16.4 - x4 - bia_x4 - 17.4

        incise_line = []  # 切割标记线
        incise_line.append(base_point_x)
        incise_line.append(base_point_y)
        incise_line.append(base_point_x + 2)
        incise_line.append(base_point_y)

        coords = []

        coords.append(base_point_x)
        coords.append(base_point_y - 51)

        obj.append(self.create_arc(coords[0] + 2, coords[1], 2, 180, 270))

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

        obj.append(self.create_arc(coords[10] - 2, coords[11], 2, -90, 0))

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
        coords2.append(coords2[19])

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
        obj.append(self.create_arc(base_point_x + 47, base_point_y - 35, 6.75, 90, 270))
        obj.append(self.create_arc(base_point_x + 47 + 56, base_point_y - 35, 6.75, -90, 90))
        obj.append(
            self.create_line(base_point_x + 47, base_point_y - 35 - 6.75, base_point_x + 47 + 56, base_point_y - 35 - 6.75))
        obj.append(
            self.create_line(base_point_x + 47, base_point_y - 35 + 6.75, base_point_x + 47 + 27, base_point_y - 35 + 6.75))
        obj.append(self.create_line(base_point_x + 47 + 27, base_point_y - 35 + 6.75, base_point_x + 47 + 27 + 1,
                               base_point_y - 35 + 6.75 + 2))
        obj.append(self.create_line(base_point_x + 47 + 27 + 1, base_point_y - 35 + 6.75 + 2, base_point_x + 47 + 27 + 2,
                               base_point_y - 35 + 6.75))
        obj.append(self.create_line(base_point_x + 47 + 27 + 2, base_point_y - 35 + 6.75, base_point_x + 47 + 27 + 2 + 27,
                               base_point_y - 35 + 6.75))

        for i in range(0, len(incise_line), 4):
            obj.append(self.create_line(incise_line[i], incise_line[i + 1], incise_line[i + 2], incise_line[i + 3]))

        new_line1 = self.acad.model.AddLightWeightPolyline(array.array("d", coords))
        new_line1.Color = 1
        new_line1.Closed = False
        obj.append(new_line1)

        new_line2 = self.acad.model.AddLightWeightPolyline(array.array("d", coords2))
        new_line2.Color = 1
        new_line2.Closed = False
        obj.append(new_line2)

        mirror_line_start = APoint(base_point_x, base_point_y + ((-214429.8392 - 214706.8392) / 2 - (-214429.8392) ))
        mirror_line_end = APoint(base_point_x + width, base_point_y + ((-214429.8392 - 214706.8392) / 2 - (-214429.8392) ))
        for i in range(len(obj)):
            obj[i].Mirror(mirror_line_start, mirror_line_end)

        return

    def run(self):
        self.left_1(0, 0)
        self.right_1(self.w['left1'] + 300 + self.w['right1'], 0)
        self.right_2(self.w['left1'] + 300, -506)
        self.left_5(self.w['left1']-self.w['left5'], -506)
        self.left_4(self.w['left1']-self.w['left5'] - 61 - self.w['left4'], - 506 - 203)
        self.left_3(self.w['left1']-self.w['left5'] - 61 - self.w['left3'], - 506)
        self.create_Door_jamb_down(APoint(self.doorsize['door_jamb_down_x'],1000))
        self.create_Door_jamb_up(APoint(10 + self.doorsize['door_jamb_up_x'],1750 + self.doorsize['door_jamb_down_y']))
        doorframe7_x = self.doorsize['door_jamb_down_x'] + 680 + self.doorsize['doorframe7_x']
        doorframe7_y = self.doorsize['door_jamb_down_y2'] + 1000
        self.create_doorframe7(APoint(doorframe7_x,doorframe7_y))
        self.create_doorframe1(APoint(doorframe7_x,doorframe7_y - self.doorsize['doorframe1_y']))
        self.create_doorframe8(APoint(doorframe7_x + 205 + self.doorsize['doorframe8_x'],doorframe7_y))
        self.create_doorframe2(APoint(doorframe7_x + 205 + self.doorsize['doorframe2_x'],doorframe7_y - self.doorsize['doorframe2_y']))
        self.create_doorframe3(APoint(doorframe7_x,doorframe7_y + self.doorsize['doorframe7_y'] + 750))
        self.create_doorframe4(APoint(doorframe7_x,doorframe7_y + 750 + self.doorsize['doorframe3_y'] + self.doorsize['doorframe7_y']))
        self.create_doorframe5(APoint(doorframe7_x+200,doorframe7_y  + self.doorsize['doorframe7_y'] + 750 + 10))
        self.create_doorframe6(APoint(doorframe7_x + 200 + self.doorsize['doorframe6_x'],doorframe7_y + 750 + self.doorsize['doorframe5_y'] + self.doorsize['doorframe7_y']))











