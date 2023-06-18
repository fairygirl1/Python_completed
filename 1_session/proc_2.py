"""
Напишите 2 функции
Первая должна принимать ширину, длинну и высоты комнаты и 
записывать в файл площадь комнаты из 4 стен.
Вторая должна записать в тот же файл расход краски исходя 
из соотношения 5л/кв.м.
"""
import multiprocessing

def params(width, length, high, queue):
    area = high*length*2 + high*width*2
    queue.put(area)    

def consumption(area, queue):
    result = area*5
    queue.put(result)

if __name__ == '__main__':
    width = 3
    length = 4
    high = 5

    queue = multiprocessing.Queue()

    params_proc = multiprocessing.Process(target=params, args=(width, length, high, queue))
    params_proc.start()
    params_proc.join()
    area = queue.get()
    
    consumption_proc = multiprocessing.Process(target=consumption, args=(area, queue))
    consumption_proc.start()
    consumption_proc.join()
    result = queue.get()

    with open ('room.txt', 'w') as f:
        f.write(f'ширина: {width}\n длина: {length} \n высота: {high}\n'
                f'площадь комнаты: {area} \n расход краски: {result}')
        
    print('результаты в файле')