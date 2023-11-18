import copy



item = {0: ['Москва', 'Профи', 'Сарафан', 'Кодинг', 'Обучение', 'Планирование', 'Питание', 'Здоровье', 'Достависта',],
        1: ['Профи', 'Поиск заказов', 'Переписка', 'Продажа', 'Ремонт', 'Инструмент', 'Запчасти', 'item1_7', 'item1_8',],
        2: ['Сарафан', 'item2_1', 'item2_2', 'item2_3', 'item2_4', 'item2_5', 'item2_6', 'item2_7', 'item2_8',],
        3: ['Кодинг', 'item3_1', 'item3_2', 'item3_3', 'item3_4', 'item3_5', 'item3_6', 'item3_7', 'item3_8',],
        4: ['Обучение', 'item4_1', 'item4_2', 'item4_3', 'item4_4', 'item4_5', 'item4_6', 'item4_7', 'item4_8',],
        5: ['Планирование', 'item5_1', 'item5_2', 'item5_3', 'item5_4', 'item5_5', 'item5_6', 'item5_7', 'item5_8',],
        6: ['Питание', 'item6_1', 'item6_2', 'item6_3', 'item6_4', 'item6_5', 'item6_6', 'item6_7', 'item6_8',],
        7: ['Здоровье', 'item7_1', 'item7_2', 'item7_3', 'item7_4', 'item7_5', 'item7_6', 'item7_7', 'item7_8',],
        8: ['Достависта', 'item8_1', 'item8_2', 'item8_3', 'item8_4', 'item8_5', 'item8_6', 'item8_7', 'item8_8',],
        }

# Переход листка в центр
def replace(item_0, n):
    item_copy = copy.deepcopy(item_0)
    for i in item_copy:
        for j in range(9):
            item_copy[i][j] = ''

    item_copy[0] = item_0[n]
    item_copy[1][0] = item_copy[0][1]
    item_copy[2][0] = item_copy[0][2]
    item_copy[3][0] = item_copy[0][3]
    item_copy[4][0] = item_copy[0][4]
    item_copy[5][0] = item_copy[0][5]
    item_copy[6][0] = item_copy[0][6]
    item_copy[7][0] = item_copy[0][7]
    item_copy[8][0] = item_copy[0][8]

    item_0 = copy.deepcopy(item_copy)
    return item_0


# Сделать ссылки выбора через клик и возврат обратно если нужно
# num = int(input('Выберите блок: '))
# item = replace(item, num)


data = {
    'item0_0': item[0][0],
    'item0_1': item[0][1],
    'item0_2': item[0][2],
    'item0_3': item[0][3],
    'item0_4': item[0][4],
    'item0_5': item[0][5],
    'item0_6': item[0][6],
    'item0_7': item[0][7],
    'item0_8': item[0][8],

    'item1_0': item[1][0],
    'item1_1': item[1][1],
    'item1_2': item[1][2],
    'item1_3': item[1][3],
    'item1_4': item[1][4],
    'item1_5': item[1][5],
    'item1_6': item[1][6],
    'item1_7': item[1][7],
    'item1_8': item[1][8],

    'item2_0': item[2][0],
    'item2_1': item[2][1],
    'item2_2': item[2][2],
    'item2_3': item[2][3],
    'item2_4': item[2][4],
    'item2_5': item[2][5],
    'item2_6': item[2][6],
    'item2_7': item[2][7],
    'item2_8': item[2][8],

    'item3_0': item[3][0],
    'item3_1': item[3][1],
    'item3_2': item[3][2],
    'item3_3': item[3][3],
    'item3_4': item[3][4],
    'item3_5': item[3][5],
    'item3_6': item[3][6],
    'item3_7': item[3][7],
    'item3_8': item[3][8],

    'item4_0': item[4][0],
    'item4_1': item[4][1],
    'item4_2': item[4][2],
    'item4_3': item[4][3],
    'item4_4': item[4][4],
    'item4_5': item[4][5],
    'item4_6': item[4][6],
    'item4_7': item[4][7],
    'item4_8': item[4][8],

    'item5_0': item[5][0],
    'item5_1': item[5][1],
    'item5_2': item[5][2],
    'item5_3': item[5][3],
    'item5_4': item[5][4],
    'item5_5': item[5][5],
    'item5_6': item[5][6],
    'item5_7': item[5][7],
    'item5_8': item[5][8],

    'item6_0': item[6][0],
    'item6_1': item[6][1],
    'item6_2': item[6][2],
    'item6_3': item[6][3],
    'item6_4': item[6][4],
    'item6_5': item[6][5],
    'item6_6': item[6][6],
    'item6_7': item[6][7],
    'item6_8': item[6][8],

    'item7_0': item[7][0],
    'item7_1': item[7][1],
    'item7_2': item[7][2],
    'item7_3': item[7][3],
    'item7_4': item[7][4],
    'item7_5': item[7][5],
    'item7_6': item[7][6],
    'item7_7': item[7][7],
    'item7_8': item[7][8],

    'item8_0': item[8][0],
    'item8_1': item[8][1],
    'item8_2': item[8][2],
    'item8_3': item[8][3],
    'item8_4': item[8][4],
    'item8_5': item[8][5],
    'item8_6': item[8][6],
    'item8_7': item[8][7],
    'item8_8': item[8][8],
}


