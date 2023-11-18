

# =====================================================================================================================

def index(request):

        grid_0 = Grid.objects.all()[0]
        grid_1 = Grid.objects.all()[1]
        grid_2 = Grid.objects.all()[2]
        grid_3 = Grid.objects.all()[3]
        grid_4 = Grid.objects.all()[4]
        grid_5 = Grid.objects.all()[5]
        grid_6 = Grid.objects.all()[6]
        grid_7 = Grid.objects.all()[7]
        grid_8 = Grid.objects.all()[8]

        grid_1.item_0 = grid_0.item_1
        grid_2.item_0 = grid_0.item_2
        grid_3.item_0 = grid_0.item_3
        grid_4.item_0 = grid_0.item_4
        grid_5.item_0 = grid_0.item_5
        grid_6.item_0 = grid_0.item_6
        grid_7.item_0 = grid_0.item_7
        grid_8.item_0 = grid_0.item_8

        grid_1.save()
        grid_2.save()
        grid_3.save()
        grid_4.save()
        grid_5.save()
        grid_6.save()
        grid_7.save()
        grid_8.save()

        data = {
                'grid_0': Grid.objects.all()[0],
                'grid_1': Grid.objects.all()[1],
                'grid_2': Grid.objects.all()[2],
                'grid_3': Grid.objects.all()[3],
                'grid_4': Grid.objects.all()[4],
                'grid_5': Grid.objects.all()[5],
                'grid_6': Grid.objects.all()[6],
                'grid_7': Grid.objects.all()[7],
                'grid_8': Grid.objects.all()[8],
        }

        return render(request, 'main/index.html', context=data)


# список данных в grid
def list(request):
        grid = Grid.objects.all()
        data = {"grid": grid}
        return render(request, 'main/list.html', context=data)


# =====================================================================================================================

# листья центра становятся центрами листьев
def leaf():
        grid_0 = Grid.objects.all()[0]
        grid_1 = Grid.objects.all()[1]
        grid_2 = Grid.objects.all()[2]
        grid_3 = Grid.objects.all()[3]
        grid_4 = Grid.objects.all()[4]
        grid_5 = Grid.objects.all()[5]
        grid_6 = Grid.objects.all()[6]
        grid_7 = Grid.objects.all()[7]
        grid_8 = Grid.objects.all()[8]

        # grid[1][0] = grid[0][1]
        # grid[2][0] = grid[0][2]
        # grid[3][0] = grid[0][3]
        # grid[4][0] = grid[0][4]
        # grid[5][0] = grid[0][5]
        # grid[6][0] = grid[0][6]
        # grid[7][0] = grid[0][7]
        # grid[8][0] = grid[0][8]
        # grid.save()

        for j in range(1, 9):
                globals()['grid_%s' % j].item_0 = 'Проверка0'
                globals()['grid_%s' % j].item_0 = 'Проверка0'
                globals()['grid_%s' % j].item_0 = 'Проверка0'
                globals()['grid_%s' % j].item_0 = 'Проверка0'
                globals()['grid_%s' % j].item_0 = 'Проверка0'
                globals()['grid_%s' % j].item_0 = 'Проверка0'
                globals()['grid_%s' % j].item_0 = 'Проверка0'
                globals()['grid_%s' % j].item_0 = 'Проверка0'
                globals()['grid_%s' % j].item_0 = 'Проверка0'

        for i in range(9):
                globals()['grid_%s' % i].save()



# =====================================================================================================================

# листья центра становятся центрами листьев
def leaf():
        grid = Grid.objects.all()

        # grid[1][0] = grid[0][1]
        # grid[2][0] = grid[0][2]
        # grid[3][0] = grid[0][3]
        # grid[4][0] = grid[0][4]
        # grid[5][0] = grid[0][5]
        # grid[6][0] = grid[0][6]
        # grid[7][0] = grid[0][7]
        # grid[8][0] = grid[0][8]
        # grid.save()

# =====================================================================================================================

# def edit(request, id):
#         grid = Grid.objects.get(id=id)
#         if request.method == 'POST':
#                 userform_0 = request.POST.get('item_0')
#                 userform_1 = request.POST.get('item_1')
#                 userform_2 = request.POST.get('item_2')
#                 userform_3 = request.POST.get('item_3')
#                 userform_4 = request.POST.get('item_4')
#                 userform_5 = request.POST.get('item_5')
#                 userform_6 = request.POST.get('item_6')
#                 userform_7 = request.POST.get('item_7')
#                 userform_8 = request.POST.get('item_8')
#
#                 # if userform_0 == True:
#                 grid.item_0 = userform_0
#                 # if userform_1 == True:
#                 grid.item_1 = userform_1
#                 # if userform_2 == True:
#                 grid.item_2 = userform_2
#                 # if userform_3 == True:
#                 grid.item_3 = userform_3
#                 # if userform_4 == True:
#                 grid.item_4 = userform_4
#                 # if userform_5 == True:
#                 grid.item_5 = userform_5
#                 # if userform_6 == True:
#                 grid.item_6 = userform_6
#                 # if userform_7 == True:
#                 grid.item_7 = userform_7
#                 # if userform_8 == True:
#                 grid.item_8 = userform_8
#         grid.save()
#         return redirect('home')
#         else:
#              data = {
#                 'id': id,
#                 'grid_0': Grid.objects.all()[0],
#                 'grid_1': Grid.objects.all()[1],
#                 'grid_2': Grid.objects.all()[2],
#                 'grid_3': Grid.objects.all()[3],
#                 'grid_4': Grid.objects.all()[4],
#                 'grid_5': Grid.objects.all()[5],
#                 'grid_6': Grid.objects.all()[6],
#                 'grid_7': Grid.objects.all()[7],
#                 'grid_8': Grid.objects.all()[8],
#                 }
#         return render(request, 'main/edit.html', context=data)


# =====================================================================================================================


# изменение данных в бд
# как сделать, чтобы он не переписывал

def edit(request, id):
        grid = Grid.objects.get(id=id)
        if request.method == 'POST':
                userform_0 = request.POST.get('item_0')
                userform_1 = request.POST.get('item_1')
                userform_2 = request.POST.get('item_2')
                userform_3 = request.POST.get('item_3')
                userform_4 = request.POST.get('item_4')
                userform_5 = request.POST.get('item_5')
                userform_6 = request.POST.get('item_6')
                userform_7 = request.POST.get('item_7')
                userform_8 = request.POST.get('item_8')

                if userform_0 == True:
                        grid.item_0 = userform_0
                if userform_1 == True:
                        grid.item_1 = userform_1
                if userform_2 == True:
                        grid.item_2 = userform_2
                if userform_3 == True:
                        grid.item_3 = userform_3
                if userform_4 == True:
                        grid.item_4 = userform_4
                if userform_5 == True:
                        grid.item_5 = userform_5
                if userform_6 == True:
                        grid.item_6 = userform_6
                if userform_7 == True:
                        grid.item_7 = userform_7
                if userform_8 == True:
                        grid.item_8 = userform_8
                grid.save()
                return redirect('home')
        else:
                data = {
                        'id': id,
                        'grid_0': Grid.objects.all()[0],
                        'grid_1': Grid.objects.all()[1],
                        'grid_2': Grid.objects.all()[2],
                        'grid_3': Grid.objects.all()[3],
                        'grid_4': Grid.objects.all()[4],
                        'grid_5': Grid.objects.all()[5],
                        'grid_6': Grid.objects.all()[6],
                        'grid_7': Grid.objects.all()[7],
                        'grid_8': Grid.objects.all()[8],
                }
                return render(request, 'main/edit.html', context=data)






# =====================================================================================================================


# изменение данных в бд + валидация данных
def edit(request, id):
        grid = Grid.objects.get(id=id)
        if request.method == 'POST':
                form = UserForms(request.POST)
                if form.is_valid():
                        grid.item_0 = form.cleaned_data['item_0']
                        grid.item_1 = form.cleaned_data['item_1']
                        grid.item_2 = form.cleaned_data['item_2']
                        grid.item_3 = form.cleaned_data['item_3']
                        grid.item_4 = form.cleaned_data['item_4']
                        grid.item_5 = form.cleaned_data['item_5']
                        grid.item_6 = form.cleaned_data['item_6']
                        grid.item_7 = form.cleaned_data['item_7']
                        grid.item_8 = form.cleaned_data['item_8']
                        grid.save()
                return redirect('home')
        else:
                data = {
                        'id': id,
                        'grid_0': Grid.objects.all()[0],
                        'grid_1': Grid.objects.all()[1],
                        'grid_2': Grid.objects.all()[2],
                        'grid_3': Grid.objects.all()[3],
                        'grid_4': Grid.objects.all()[4],
                        'grid_5': Grid.objects.all()[5],
                        'grid_6': Grid.objects.all()[6],
                        'grid_7': Grid.objects.all()[7],
                        'grid_8': Grid.objects.all()[8],
                }
                return render(request, 'main/edit.html', context=data)


# =====================================================================================================================

# изменение данных в бд
def edit(request, id):
        grid = Grid.objects.get(id=id)
        if request.method == 'POST':
                form = UserForms(request.POST)
                if form.is_valid():
                        grid.item_0 = form.cleaned_data['item_0']
                        grid.item_1 = form.cleaned_data['item_1']
                        grid.item_2 = form.cleaned_data['item_2']
                        grid.item_3 = form.cleaned_data['item_3']
                        grid.item_4 = form.cleaned_data['item_4']
                        grid.item_5 = form.cleaned_data['item_5']
                        grid.item_6 = form.cleaned_data['item_6']
                        grid.item_7 = form.cleaned_data['item_7']
                        grid.item_8 = form.cleaned_data['item_8']
                        grid.save()
                return redirect('home')
        else:
                data = {
                        'id': id,
                        'grid_0': Grid.objects.all()[0],
                        'grid_1': Grid.objects.all()[1],
                        'grid_2': Grid.objects.all()[2],
                        'grid_3': Grid.objects.all()[3],
                        'grid_4': Grid.objects.all()[4],
                        'grid_5': Grid.objects.all()[5],
                        'grid_6': Grid.objects.all()[6],
                        'grid_7': Grid.objects.all()[7],
                        'grid_8': Grid.objects.all()[8],
                }
                return render(request, 'main/edit.html', context=data)

# =====================================================================================================================

# изменение данных в бд
def edit(request, id):
        grid = Grid.objects.get(id=id)
        if request.method == 'POST':
                form = UserForms(request.POST)
                if form.is_valid():
                        grid.item_0 = form.cleaned_data['item_0']
                        grid.item_1 = form.cleaned_data['item_1']
                        grid.item_2 = form.cleaned_data['item_2']
                        grid.item_3 = form.cleaned_data['item_3']
                        grid.item_4 = form.cleaned_data['item_4']
                        grid.item_5 = form.cleaned_data['item_5']
                        grid.item_6 = form.cleaned_data['item_6']
                        grid.item_7 = form.cleaned_data['item_7']
                        grid.item_8 = form.cleaned_data['item_8']
                grid.save()
                return redirect('home')
        else:
                data = {
                        'id': id,
                        'grid_0': Grid.objects.all()[0],
                        'grid_1': Grid.objects.all()[1],
                        'grid_2': Grid.objects.all()[2],
                        'grid_3': Grid.objects.all()[3],
                        'grid_4': Grid.objects.all()[4],
                        'grid_5': Grid.objects.all()[5],
                        'grid_6': Grid.objects.all()[6],
                        'grid_7': Grid.objects.all()[7],
                        'grid_8': Grid.objects.all()[8],
                }
                return render(request, 'main/edit.html', context=data)



# =====================================================================================================================

userform_0 = UserForms(request.POST.get('item_0'))
userform_1 = UserForms(request.POST.get('item_1'))
userform_2 = UserForms(request.POST.get('item_2'))
userform_3 = UserForms(request.POST.get('item_3'))
userform_4 = UserForms(request.POST.get('item_4'))
userform_5 = UserForms(request.POST.get('item_5'))
userform_6 = UserForms(request.POST.get('item_6'))
userform_7 = UserForms(request.POST.get('item_7'))
userform_8 = UserForms(request.POST.get('item_8'))

# =====================================================================================================================


# изменение данных в бд
def edit(request, id):
        grid = Grid.objects.get(id=id)
        if request.method == 'POST':
                userform_0 = request.POST.get('item_0')
                userform_1 = request.POST.get('item_1')
                userform_2 = request.POST.get('item_2')
                userform_3 = request.POST.get('item_3')
                userform_4 = request.POST.get('item_4')
                userform_5 = request.POST.get('item_5')
                userform_6 = request.POST.get('item_6')
                userform_7 = request.POST.get('item_7')
                userform_8 = request.POST.get('item_8')

                if userform_0.is_valid():
                        grid.item_0 = userform_0
                if userform_1.is_valid():
                        grid.item_1 = userform_1
                if userform_2.is_valid():
                        grid.item_2 = userform_2
                if userform_3.is_valid():
                        grid.item_3 = userform_3
                if userform_4.is_valid():
                        grid.item_4 = userform_4
                if userform_5.is_valid():
                        grid.item_5 = userform_5
                if userform_6.is_valid():
                        grid.item_6 = userform_6
                if userform_7.is_valid():
                        grid.item_7 = userform_7
                if userform_8.is_valid():
                        grid.item_8 = userform_8
                grid.save()
                return redirect('home')
        else:
                data = {
                        'id': id,
                        'grid_0': Grid.objects.all()[0],
                        'grid_1': Grid.objects.all()[1],
                        'grid_2': Grid.objects.all()[2],
                        'grid_3': Grid.objects.all()[3],
                        'grid_4': Grid.objects.all()[4],
                        'grid_5': Grid.objects.all()[5],
                        'grid_6': Grid.objects.all()[6],
                        'grid_7': Grid.objects.all()[7],
                        'grid_8': Grid.objects.all()[8],
                }
                return render(request, 'main/edit.html', context=data)


# =====================================================================================================================


if 'item_1' is not None:
        grid.item_1 = request.POST.get('item_1')
if 'item_2' is not None:
        grid.item_2 = request.POST.get('item_2')
if 'item_3' is not None:
        grid.item_3 = request.POST.get('item_3')
if 'item_4' is not None:
        grid.item_4 = request.POST.get('item_4')
if 'item_5' is not None:
        grid.item_5 = request.POST.get('item_5')
if 'item_6' is not None:
        grid.item_6 = request.POST.get('item_6')
if 'item_7' is not None:
        grid.item_7 = request.POST.get('item_7')
if 'item_8' is not None:
        grid.item_8 = request.POST.get('item_8')

# =====================================================================================================================


# изменение данных
def change(request):
        grid = Grid.objects.get(id=3)
        if request.method == 'POST':
                grid.item_0 = request.POST.get('item_0')
                grid.item_1 = request.POST.get('item_1')
                grid.item_2 = request.POST.get('item_2')
                grid.item_3 = request.POST.get('item_3')
                grid.item_4 = request.POST.get('item_4')
                grid.item_5 = request.POST.get('item_5')
                grid.item_6 = request.POST.get('item_6')
                grid.item_7 = request.POST.get('item_7')
                grid.item_8 = request.POST.get('item_8')
                grid.save()
        return redirect('home')


# =====================================================================================================================


# сохранение данных в бд
def create(request):
        if request.method == 'POST':
                grid = Grid()
                grid.item_0 = request.POST.get('item_0')
                grid.item_1 = request.POST.get('item_1')
                grid.item_2 = request.POST.get('item_2')
                grid.item_3 = request.POST.get('item_3')
                grid.item_4 = request.POST.get('item_4')
                grid.item_5 = request.POST.get('item_5')
                grid.item_6 = request.POST.get('item_6')
                grid.item_7 = request.POST.get('item_7')
                grid.item_8 = request.POST.get('item_8')
                grid.save()
        return redirect('home')



# =====================================================================================================================

from django.shortcuts import render, redirect
# from .data_base import data
from .models import Grid

grid_0 = Grid.objects.all()[0]
grid_1 = Grid.objects.all()[1]
grid_2 = Grid.objects.all()[2]
grid_3 = Grid.objects.all()[3]
grid_4 = Grid.objects.all()[4]
grid_5 = Grid.objects.all()[5]
grid_6 = Grid.objects.all()[6]
grid_7 = Grid.objects.all()[7]
grid_8 = Grid.objects.all()[8]

item = {0: ['Москва', 'Профи', 'Сарафан', 'Кодинг', 'Обучение', 'Планирование', 'Питание', 'Здоровье', 'Достависта',],
        1: ['Профи', 'Поиск заказов', 'Переписка', 'Продажа', 'Ремонт', 'Инструмент', 'Запчасти', '-', '-',],
        2: ['Сарафан', '-', '-', '-', '-', '-', '-', '-', '-',],
        3: ['Кодинг', '-', '-', '-', '-', '-', '-', '-', '-',],
        4: ['Обучение', '-', '-', '-', '-', '-', '-', '-', '-',],
        5: ['Планирование', '-', '-', '-', '-', '-', '-', '-', '-',],
        6: ['Питание', '-', '-', '-', '-', '-', '-', '-', '-',],
        7: ['Здоровье', '-', '-', '-', '-', '-', '-', '-', '-',],
        8: ['Достависта', '-', '-', '-', '-', '-', '-', '-', '-',],
        }

item1 = {0: ['Профи', 'Поиск заказов', 'Переписка', 'Продажа', 'Ремонт', 'Инструмент', 'Запчасти', '-', '-',],
         1: ['Поиск заказов', '-', '-', '-', '-', '-', '-', '-', '-',],
         2: ['Переписка', '-', '-', '-', '-', '-', '-', '-', '-',],
         3: ['Продажа', '-', '-', '-', '-', '-', '-', '-', '-',],
         4: ['Ремонт', '-', '-', '-', '-', '-', '-', '-', '-',],
         5: ['Инструмент', '-', '-', '-', '-', '-', '-', '-', '-',],
         6: ['Запчасти', '-', '-', '-', '-', '-', '-', '-', '-',],
         7: ['-', '-', '-', '-', '-', '-', '-', '-', '-',],
         8: ['-', '-', '-', '-', '-', '-', '-', '-', '-',],
         }

def rlc_1(request):
        for j in range(9):
                globals()['grid_%s' % j].item_0 = '-'
                globals()['grid_%s' % j].item_1 = '-'
                globals()['grid_%s' % j].item_2 = '-'
                globals()['grid_%s' % j].item_3 = '-'
                globals()['grid_%s' % j].item_4 = '-'
                globals()['grid_%s' % j].item_5 = '-'
                globals()['grid_%s' % j].item_6 = '-'
                globals()['grid_%s' % j].item_7 = '-'
                globals()['grid_%s' % j].item_8 = '-'

        for j in range(9):
                globals()['grid_%s' % j].item_0 = item1[j][0]
                globals()['grid_%s' % j].item_1 = item1[j][1]
                globals()['grid_%s' % j].item_2 = item1[j][2]
                globals()['grid_%s' % j].item_3 = item1[j][3]
                globals()['grid_%s' % j].item_4 = item1[j][4]
                globals()['grid_%s' % j].item_5 = item1[j][5]
                globals()['grid_%s' % j].item_6 = item1[j][6]
                globals()['grid_%s' % j].item_7 = item1[j][7]
                globals()['grid_%s' % j].item_8 = item1[j][8]

        for i in range(9):
                globals()['grid_%s' % i].save()

        # second.item_0 = 'Django'
        # second.item_1 = 'инструкции'
        # second.item_2 = 'проекты'
        # second.item_3 = 'text'
        # second.item_4 = 'text'
        # second.item_5 = 'text'
        # second.item_6 = 'text'
        # second.item_7 = 'text'
        # second.item_8 = 'text'
        #
        # second.save(using="second_db")

        return redirect('home')


# написать код по возврату к изначальному виду
def rlc_0(request):
        for j in range(9):
                globals()['grid_%s' % j].item_0 = item[j][0]
                globals()['grid_%s' % j].item_1 = item[j][1]
                globals()['grid_%s' % j].item_2 = item[j][2]
                globals()['grid_%s' % j].item_3 = item[j][3]
                globals()['grid_%s' % j].item_4 = item[j][4]
                globals()['grid_%s' % j].item_5 = item[j][5]
                globals()['grid_%s' % j].item_6 = item[j][6]
                globals()['grid_%s' % j].item_7 = item[j][7]
                globals()['grid_%s' % j].item_8 = item[j][8]

        for i in range(9):
                globals()['grid_%s' % i].save()

        return redirect('home')


def index(request):
        data = {
                'item0_0': grid_0.item_0,
                'item0_1': grid_0.item_1,
                'item0_2': grid_0.item_2,
                'item0_3': grid_0.item_3,
                'item0_4': grid_0.item_4,
                'item0_5': grid_0.item_5,
                'item0_6': grid_0.item_6,
                'item0_7': grid_0.item_7,
                'item0_8': grid_0.item_8,

                'item1_0': grid_1.item_0,
                'item1_1': grid_1.item_1,
                'item1_2': grid_1.item_2,
                'item1_3': grid_1.item_3,
                'item1_4': grid_1.item_4,
                'item1_5': grid_1.item_5,
                'item1_6': grid_1.item_6,
                'item1_7': grid_1.item_7,
                'item1_8': grid_1.item_8,

                'item2_0': grid_2.item_0,
                'item2_1': grid_2.item_1,
                'item2_2': grid_2.item_2,
                'item2_3': grid_2.item_3,
                'item2_4': grid_2.item_4,
                'item2_5': grid_2.item_5,
                'item2_6': grid_2.item_6,
                'item2_7': grid_2.item_7,
                'item2_8': grid_2.item_8,

                'item3_0': grid_3.item_0,
                'item3_1': grid_3.item_1,
                'item3_2': grid_3.item_2,
                'item3_3': grid_3.item_3,
                'item3_4': grid_3.item_4,
                'item3_5': grid_3.item_5,
                'item3_6': grid_3.item_6,
                'item3_7': grid_3.item_7,
                'item3_8': grid_3.item_8,

                'item4_0': grid_4.item_0,
                'item4_1': grid_4.item_1,
                'item4_2': grid_4.item_2,
                'item4_3': grid_4.item_3,
                'item4_4': grid_4.item_4,
                'item4_5': grid_4.item_5,
                'item4_6': grid_4.item_6,
                'item4_7': grid_4.item_7,
                'item4_8': grid_4.item_8,

                'item5_0': grid_5.item_0,
                'item5_1': grid_5.item_1,
                'item5_2': grid_5.item_2,
                'item5_3': grid_5.item_3,
                'item5_4': grid_5.item_4,
                'item5_5': grid_5.item_5,
                'item5_6': grid_5.item_6,
                'item5_7': grid_5.item_7,
                'item5_8': grid_5.item_8,

                'item6_0': grid_6.item_0,
                'item6_1': grid_6.item_1,
                'item6_2': grid_6.item_2,
                'item6_3': grid_6.item_3,
                'item6_4': grid_6.item_4,
                'item6_5': grid_6.item_5,
                'item6_6': grid_6.item_6,
                'item6_7': grid_6.item_7,
                'item6_8': grid_6.item_8,

                'item7_0': grid_7.item_0,
                'item7_1': grid_7.item_1,
                'item7_2': grid_7.item_2,
                'item7_3': grid_7.item_3,
                'item7_4': grid_7.item_4,
                'item7_5': grid_7.item_5,
                'item7_6': grid_7.item_6,
                'item7_7': grid_7.item_7,
                'item7_8': grid_7.item_8,

                'item8_0': grid_8.item_0,
                'item8_1': grid_8.item_1,
                'item8_2': grid_8.item_2,
                'item8_3': grid_8.item_3,
                'item8_4': grid_8.item_4,
                'item8_5': grid_8.item_5,
                'item8_6': grid_8.item_6,
                'item8_7': grid_8.item_7,
                'item8_8': grid_8.item_8,
        }

        return render(request, 'main/index.html', context=data)

# =====================================================================================================================

def rlc_1(request):
        for j in range(9):
                for i in range(9):
                        globals()['grid_%s' % j].item_5 = 'text'

        for i in range(9):
                globals()['grid_%s' % i].save()

        return redirect('home')



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


cell = {0: 'item_0', 1: 'item_1', 2: 'item_2', 3: 'item_3', 4: 'item_4', 5: 'item_5', 6: 'item_6',7: 'item_7', 8:'item_8',}

cell = {'item_0', 'item_1', 'item_2', 'item_3', 'item_4', 'item_5', 'item_6','item_7', 'item_8' }

# =====================================================================================================================

# from django.shortcuts import render, redirect
# # from . data_base import data
# import copy
#
#
# r = 1
#
# def rlc_1(request):
#     return redirect('home')
#
#
#
# def index(request):
#
#     # Переход листка в центр
#     def replace(item_0, n):
#         item_copy = copy.deepcopy(item_0)
#         for i in item_copy:
#             for j in range(9):
#                 item_copy[i][j] = ''
#
#         item_copy[0] = item_0[n]
#         item_copy[1][0] = item_copy[0][1]
#         item_copy[2][0] = item_copy[0][2]
#         item_copy[3][0] = item_copy[0][3]
#         item_copy[4][0] = item_copy[0][4]
#         item_copy[5][0] = item_copy[0][5]
#         item_copy[6][0] = item_copy[0][6]
#         item_copy[7][0] = item_copy[0][7]
#         item_copy[8][0] = item_copy[0][8]
#
#         item_0 = copy.deepcopy(item_copy)
#         return item_0
#
#     item = {0: ['Москва', 'Профи', 'Сарафан', 'Кодинг', 'Обучение', 'Планирование', 'Питание', 'Здоровье', 'Достависта',],
#             1: ['Профи', 'Поиск заказов', 'Переписка', 'Продажа', 'Ремонт', 'Инструмент', 'Запчасти', 'item1_7', 'item1_8',],
#             2: ['Сарафан', 'item2_1', 'item2_2', 'item2_3', 'item2_4', 'item2_5', 'item2_6', 'item2_7', 'item2_8',],
#             3: ['Кодинг', 'item3_1', 'item3_2', 'item3_3', 'item3_4', 'item3_5', 'item3_6', 'item3_7', 'item3_8',],
#             4: ['Обучение', 'item4_1', 'item4_2', 'item4_3', 'item4_4', 'item4_5', 'item4_6', 'item4_7', 'item4_8',],
#             5: ['Планирование', 'item5_1', 'item5_2', 'item5_3', 'item5_4', 'item5_5', 'item5_6', 'item5_7', 'item5_8',],
#             6: ['Питание', 'item6_1', 'item6_2', 'item6_3', 'item6_4', 'item6_5', 'item6_6', 'item6_7', 'item6_8',],
#             7: ['Здоровье', 'item7_1', 'item7_2', 'item7_3', 'item7_4', 'item7_5', 'item7_6', 'item7_7', 'item7_8',],
#             8: ['Достависта', 'item8_1', 'item8_2', 'item8_3', 'item8_4', 'item8_5', 'item8_6', 'item8_7', 'item8_8',],
#             }
#
#     if r == 1:
#         item = replace(item, 1)
#
#
#     data = {
#         'item0_0': item[0][0],
#         'item0_1': item[0][1],
#         'item0_2': item[0][2],
#         'item0_3': item[0][3],
#         'item0_4': item[0][4],
#         'item0_5': item[0][5],
#         'item0_6': item[0][6],
#         'item0_7': item[0][7],
#         'item0_8': item[0][8],
#
#         'item1_0': item[1][0],
#         'item1_1': item[1][1],
#         'item1_2': item[1][2],
#         'item1_3': item[1][3],
#         'item1_4': item[1][4],
#         'item1_5': item[1][5],
#         'item1_6': item[1][6],
#         'item1_7': item[1][7],
#         'item1_8': item[1][8],
#
#         'item2_0': item[2][0],
#         'item2_1': item[2][1],
#         'item2_2': item[2][2],
#         'item2_3': item[2][3],
#         'item2_4': item[2][4],
#         'item2_5': item[2][5],
#         'item2_6': item[2][6],
#         'item2_7': item[2][7],
#         'item2_8': item[2][8],
#
#         'item3_0': item[3][0],
#         'item3_1': item[3][1],
#         'item3_2': item[3][2],
#         'item3_3': item[3][3],
#         'item3_4': item[3][4],
#         'item3_5': item[3][5],
#         'item3_6': item[3][6],
#         'item3_7': item[3][7],
#         'item3_8': item[3][8],
#
#         'item4_0': item[4][0],
#         'item4_1': item[4][1],
#         'item4_2': item[4][2],
#         'item4_3': item[4][3],
#         'item4_4': item[4][4],
#         'item4_5': item[4][5],
#         'item4_6': item[4][6],
#         'item4_7': item[4][7],
#         'item4_8': item[4][8],
#
#         'item5_0': item[5][0],
#         'item5_1': item[5][1],
#         'item5_2': item[5][2],
#         'item5_3': item[5][3],
#         'item5_4': item[5][4],
#         'item5_5': item[5][5],
#         'item5_6': item[5][6],
#         'item5_7': item[5][7],
#         'item5_8': item[5][8],
#
#         'item6_0': item[6][0],
#         'item6_1': item[6][1],
#         'item6_2': item[6][2],
#         'item6_3': item[6][3],
#         'item6_4': item[6][4],
#         'item6_5': item[6][5],
#         'item6_6': item[6][6],
#         'item6_7': item[6][7],
#         'item6_8': item[6][8],
#
#         'item7_0': item[7][0],
#         'item7_1': item[7][1],
#         'item7_2': item[7][2],
#         'item7_3': item[7][3],
#         'item7_4': item[7][4],
#         'item7_5': item[7][5],
#         'item7_6': item[7][6],
#         'item7_7': item[7][7],
#         'item7_8': item[7][8],
#
#         'item8_0': item[8][0],
#         'item8_1': item[8][1],
#         'item8_2': item[8][2],
#         'item8_3': item[8][3],
#         'item8_4': item[8][4],
#         'item8_5': item[8][5],
#         'item8_6': item[8][6],
#         'item8_7': item[8][7],
#         'item8_8': item[8][8],
#     }
#
#     return render(request, 'main/index.html', context=data)
