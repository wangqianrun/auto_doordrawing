import sys
print("Python executable:", sys.executable)
import door


def create_door(total_width, total_height, small_door_width, small_door_height,flag,bloster_type):
    total_width = float(total_width)
    total_height = float(total_height)
    small_door_width = float(small_door_width)
    small_door_height = float(small_door_height)
    flag = int(flag)  # 假设flag是整数类型
    bloster_type = int(bloster_type)  # 假设bloster_type也是整数类型
    d = door.Door(total_width, total_height, small_door_width, small_door_height, flag, bloster_type)
    d.run()
    print('successful')


if __name__ == "__main__":
    total_width = sys.argv[1]
    total_height = sys.argv[2]
    small_door_width = sys.argv[3]
    small_door_height = sys.argv[4]
    flag = sys.argv[5]
    bloster_type = sys.argv[6]

    create_door(total_width, total_height, small_door_width, small_door_height,flag,bloster_type)
