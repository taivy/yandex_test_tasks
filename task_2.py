# Задача:
# Дан массив целых чисел. Нужно удалить из него нули. 
# Можно использовать только О(1) дополнительной памяти. 


def remove_zeros(arr):
    read_ptr = 0
    write_ptr = 0
    n = len(arr)

    # Перебираем все элементы массива
    while read_ptr < n:
        # Если текущий элемент не является нулем
        if arr[read_ptr] != 0:
            # Копируем его на позицию write_ptr
            arr[write_ptr] = arr[read_ptr]
            write_ptr += 1
        
        read_ptr += 1

    # Возвращаем обрезанный до новой длины массив
    return arr[:write_ptr]
