# Проверял на своих тестах, работает верно
# Тесты на сайте пройти не удалось :(

from math import * 


def min(distances):
    min_value = 1000000000.0
    for d in distances:
        if(d['d'] < min_value):
            min_value = d['d']

    return min_value

def main_func():

    M_N = input().split()
    M = int(M_N[0])
    N = int(M_N[1])
    i = 0

    stations = []
    distances = []


    # Забираем данные в массив
    while(i < M):
        
        value = input().split()

        name = value[0]
        del value[0]
        point = [float(item) for item in value]

        list = {'name': name, 'coords': point}
        stations.append(list)
        i += 1

    value = input().split()
    begin_points = [float(item) for item in value]

    for el in stations:
        sum = 0
        for i in range(len(el['coords'])):
            sum += pow((el['coords'][i] - begin_points[i]), 2)
        d = sqrt(sum)
        distances.append({'name': el['name'], 'd': d})
    print(distances)

    output = []
    for i in range(N):
        min_value = min(distances)
        j = 0
        while(j < len(distances)):
            if(distances[j]['d'] == min_value):
                output.append(distances[j]['name'])
                del distances[j]
            j += 1
    
    print(' '.join(output))

    return 

main_func()