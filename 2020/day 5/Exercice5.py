import os

def UpdateRowFromZone(min_x, max_x, zone) :
    mid = (min_x + max_x) // 2
    if (zone == 'F') | (zone == 'L') :
        return min_x, mid
    elif (zone == 'B') | (zone == 'R'):
        return mid + 1, max_x
    else :
        print('error')
        return 0,0

def GetRowColFromBordingPass(BordingPass) :
    min_row, max_row = 0, 127
    min_col, max_col = 0, 7

    for z in BordingPass[:7] :
        min_row, max_row = UpdateRowFromZone(min_row, max_row, z)

    for z in BordingPass[7:] :
        min_col, max_col = UpdateRowFromZone(min_col, max_col, z)

    return min_row, min_col, min_row * 8 + min_col


with open('day 5/input.txt') as f:
    lines = [line.rstrip() for line in f]

plane = [ [0] * 8 for i1 in range(128) ] #[[0] * 8] * 128
print(plane[0])
print(len(plane))

max_id = 0
for line in lines :
    row_seat, col_seat, id_seat = GetRowColFromBordingPass(line)

    #print(f'{line} ==> row = {row_seat}, col = {col_seat} --> id : {id_seat}')
    #print(plane[row_seat][col_seat])

    plane[row_seat][col_seat] = id_seat

    #print(plane[row_seat][col_seat])

    if max_id < id_seat :
        max_id = id_seat


print(F'MAX ID : {max_id}')

def getXYFromId(id) :
    y = id % 8
    x = id // 8
    return x,y

#get empty row
list_res = []
for i in range(1, 127) :
    for j in range(8) :
        id_test = plane[i][j]

        if id_test  == 0 :
            #) &
            id_real = i * 8 + j
            #print(id_real)
            i_m_1, j_m_1 = getXYFromId(id_real - 1)
            i_p_1, j_p_1 = getXYFromId(id_real + 1)

            id_less = plane[i_m_1][j_m_1]
            id_more = plane[i_p_1][j_p_1]

            if (id_less > 0) & (id_more > 0) :
                print('###' ,id_real)

#print(list_res)
