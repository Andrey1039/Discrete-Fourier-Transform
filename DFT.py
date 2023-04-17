import cmath

def DFT(x: list, N: int) -> list:
    '''
    Дискретное преобразование Фурье
    '''
    receive_data = []
    for k in range(N):
        X = 0
        for n in range(N):
            X += x[n] * cmath.exp(-2j*cmath.pi*k*n/N)
        receive_data.append(X/N)

    return receive_data[1:][:6]

def int_round(num: int) -> int:
    '''
    Округление чисел
    '''
    return int(num + (0.5 if num > 0 else -0.5))

def result(data: list) -> list:
    '''
    Окончательные преобразования
    '''
    result = []
    for i in range(len(data)):
        root = cmath.sqrt(pow(data[i].real, 2)+pow(data[i].imag, 2)).real * 2
        root = int_round(root)
        result.append(chr(root))
    
    return result

def write_file(data: list) -> None:
    '''
    Запись результатов в файл
    '''
    output = str("".join(data))
    file = open("result.txt","w+")
    file.writelines(output)
    file.close()

def read_file(filename: str) -> list:
    '''
    Чтение данных из файла
    '''
    data = open(filename, 'r')
    data = [float(x) for x in data.read().replace(',','.').split()]

    return data

if __name__ == "__main__":
    '''
    Главная программа
    '''
    FILENAME = '2.txt'
    data = read_file(FILENAME)
    data = DFT(data, len(data))
    data = result(data)
    write_file(data)






# f = open('1.txt', 'r')
# group_data = [float(x) for x in f.read().replace(',','.').split()]

# X = DFT(group_data, len(group_data))#[:7][1:]

# result = []
# for i in range(len(X)):
#    result.append(chr(int_round(cmath.sqrt(pow(X[i].real,2)+pow(X[i].imag,2)).real * 2)))


# #X = [cmath.sqrt(pow(X[i].real,2)+pow(X[i].imag,2)) for i in range(len(group_data)-1)]

# output = str("".join(result))
# file = open("result.txt","w+")
# file.writelines(output)
# file.close()