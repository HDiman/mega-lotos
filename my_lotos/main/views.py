from django.shortcuts import render, redirect
from .models import Grid



# релокация
def relocate(request, id):
    return redirect('home')


# изменение базы данных по одной ячейке
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

        if id == 1 and len(userform_0) != 0:
            grid.item_0 = userform_0
        if len(userform_1) != 0:
            grid.item_1 = userform_1
        if len(userform_2) != 0:
            grid.item_2 = userform_2
        if len(userform_3) != 0:
            grid.item_3 = userform_3
        if len(userform_4) != 0:
            grid.item_4 = userform_4
        if len(userform_5) != 0:
            grid.item_5 = userform_5
        if len(userform_6) != 0:
            grid.item_6 = userform_6
        if len(userform_7) != 0:
            grid.item_7 = userform_7
        if len(userform_8) != 0:
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


def index(request):
    # блок замены листьев основного на центры сетки
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

    #  вызов данных с БД
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


# страница списка БД
def list(request):
    data = {"grid": Grid.objects.all()}
    return render(request, 'main/list.html', context=data)
