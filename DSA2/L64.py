inp = input().split(" ")
one = list(map(int,(inp[0].strip("()")).split(",")))
two = list(map(int,(inp[1].strip("()")).split(",")))
three = list(map(int,(inp[2].strip("()")).split(",")))
four = list(map(int,(inp[3].strip("()")).split(",")))
bl_x1 = one[0] 
bl_y1 = one[1]
tr_x1 = two[0] 
tr_y1 = two[1]
bl_x2 = three[0]
bl_y2 = three[1]
tr_x2 = four[0] 
tr_y2 = four[1]
# x_1 = abs(bl_x1 - tr_x1)
# y_1 = abs(bl_y1 - tr_y1)
# area1 = x_1*y_1
x_2 = max(0,min(tr_x1, tr_x2) - max(bl_x1, bl_x2)) 
y_2 = max(0,min(tr_y1, tr_y2) - max(bl_y1, bl_y2))
area2 = x_2*y_2
print(area2)