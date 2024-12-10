from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm

# Vista de Formulario
def formulario(request):
    return render(request, 'Formulario/formulario_view.html')

# Vista de Asignaciones
def asignaciones(request):
    return render(request, 'Asignaciones/asignaciones_view.html')

# Vista de Realimentacion
def realimentacion(request):
    return render(request, 'Realimentacion/realimentacio_view.html')

# Vista de Usuarios
def usuarios(request):
    return render(request, 'Usuarios/usuarios_view.html')




# Vista para listar los items
def item_list(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items})

# Vista para crear un nuevo item
def item_create(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'items/item_form.html', {'form': form})

# Vista para editar un item existente
def item_update(request, id):
    item = get_object_or_404(Item, id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'items/item_form.html', {'form': form})

# Vista para eliminar un item
def item_delete(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'items/item_confirm_delete.html', {'item': item})
