
cnt = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        for z in range(-100, 100):
            if x + y != 0 and z + x != 0 and z + y != 0 :
                if (z / (x + y) + y / (z + x) + x / (z + y) == 4):
                    cnt += 1
                    print(x, y, z)
                
print("Broj rješenja: ", cnt)
                