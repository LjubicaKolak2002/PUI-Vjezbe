import math

def polygon_perimeter(lst):
    result = 0
    for i in range(len(lst)):
        if i < len(lst) - 1:
            index = i + 1
        else:
            index = 0 
        distance = math.sqrt((lst[index][0] - lst[i][0])**2 + (lst[index][1] - lst[i][1])**2)
        result += distance
    return result
        

def center(lst):
    x, y = 0, 0
    for element in lst:
        x += (element[0]) / len(lst)
        y += (element[1]) / len(lst)
    return (x, y)

def min_radius(lst):
    my_center = center(lst)
    distances = []
    for element in lst:
        distances.append(math.sqrt((element[0] - my_center[0])**2 + (element[1] - my_center[1])**2))
    #print(distances)
    return max(distances)
    


def main():
    lst = [(0, 0), (3, 0), (1, 1), (2, 3), (2, 1)]
    print("Opseg: ", polygon_perimeter(lst))
    print("Centar: ", center(lst))
    print("Minimalni radijus: ", min_radius(lst))

if __name__ == '__main__':
    main()
    
