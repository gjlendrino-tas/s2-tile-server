import mercantile

id = 'S2A_31PCK_20220915_0_L2A'
#31/P/CK/2022/9
print(id[4:6])
print(id[6:7])
print(id[7:9])
print(id[10:14])
print(int(id[14:16]))
t = mercantile.tile(-105.0, 40.0, 1)
print(t)
print(mercantile.tile(2.120361328125, 8.254982704877875, 14))
x, y = mercantile.xy(2.120361328125, 8.254982704877875)
print(x)
print(y)
print(mercantile.tile((168.45251984367613 + 168.459511241736)/2.0, (-17.557596404471102 - 17.54927007461763)/2.0, 15))
for x in range (0, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            x = int(x)
            y = int(y)
            z = int(z)
            tile_bbox = mercantile.bounds(x, y, z)
            print(tile_bbox)