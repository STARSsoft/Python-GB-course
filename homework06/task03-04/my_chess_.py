
EMD="_"
QUN="Q"
TGT="•"

def create_desk():
    desk = [EMD] * 8    # число строк
    for i in range(8):
        desk[i] = [EMD] * 8  # число столцов
    return desk


def print_desk(desk):
    "рисуем доску в консоли"
    for i in range(len(desk)):
        print(i+1, end="  ")
        for j in range(len(desk[0])):
            print(desk[i][j], end=" ")
        print()


def set_queen(cord, desk):
    '''
    поставить 1 ферзя на доску
    '''
    def set_target(g, v):
        desk[g][v] = TGT

    g = cord[0]
    v = cord[1]
    for i in range(len(desk)):
        set_target(g, i)
        set_target(i, v)
        gd, vd = g+i, v+i
        if 0 <= gd < len(desk) and 0 <= vd < len(desk) and desk[gd][vd]==EMD:
            set_target(gd, vd)
        gd, vd = g-i, v+i
        if 0 <= gd < len(desk) and 0 <= vd < len(desk) and desk[gd][vd]==EMD:
            set_target(gd, vd)
        gd, vd = g+i, v-i
        if 0 <= gd < len(desk) and 0 <= vd < len(desk) and desk[gd][vd]==EMD:
            set_target(gd, vd)
        gd, vd = g-i, v-i
        if 0 <= gd < len(desk) and 0 <= vd < len(desk) and desk[gd][vd]==EMD:
            set_target(gd, vd)
    desk[g][v] = QUN


def check_desk(cord, desk):
    """
    проверка, бьется ли клетка на доске
    """
    g = cord[0]
    v = cord[1]
    if desk[g][v] == EMD:
        return True
    else:
        return False


def check_cords(*args):
    """
    принимаем лист со значениями ([g1,v1],[g2,v2],....)
    проверяем, есть ли пересечения
    """
    is_good = True
    desk = create_desk()
    for cord in args:
        g, v = cord[0]-1, cord[1]-1
        if check_desk([g, v], desk):
            set_queen([g, v], desk)
        else:
            set_queen([g, v], desk)
            is_good = False
    return is_good

def not_solution():
    desk=create_desk()
    my_list=[]
    set_queen([0,3],desk)
    my_list.append([1,4])
    for i in range(len(desk)):
        for j in range(len(desk[0])):
            if check_desk([i,j],desk):
                set_queen([i,j],desk)
                my_list.append([i+1,j+1])
    # print_desk(desk)
    return my_list

def set_queens(*args):
    desk = create_desk()
    for cord in args:
        g, v = cord[0]-1, cord[1]-1
        set_queen([g, v], desk)
    return desk


if __name__=="__main__":
    print("это не решение")
    print(check_cords(*not_solution()))
    
    print(not_solution())
