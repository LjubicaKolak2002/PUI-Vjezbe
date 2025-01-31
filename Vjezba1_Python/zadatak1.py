
def addition(vector1, vector2):
    result = []
    if len(vector1) != len(vector2):
        print("Vektori moraju biti jednake duljine")
    else:
        for i in range(len(vector1)):
            result.append(vector1[i] + vector2[i])
    return result


def multipy_num(vector, num):
    result = []
    for element in vector:
        result.append(element * num)
    return result


def multiply1(vector1, vector2):
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result
    
def multiply2(vector1, vector2):
    matrix = []
    for i in range(len(vector1)):
        arr = []
        for j in range(len(vector2)):
            arr.append(vector1[i] * vector2[j])
        matrix.append(arr)
    return matrix
            
            

def main():
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]
    print("Zbroj: ", addition(vector1, vector2))
    print("Umnožak vektora i broja: ", multipy_num(vector1, 2))
    print("Umnožak1: ", multiply1(vector1, vector2))
    print("Umnožak2: ", multiply2(vector1, vector2))

if __name__ == '__main__':
    main()

