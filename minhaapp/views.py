from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def lista_itens(request):
    itens = Item.objects.all()
    return render(request, 'minhaapp/lista_itens.html', {'itens': itens})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_itens')
    else:
        form = ItemForm()
    return render(request, 'minhaapp/add_item.html', {'form': form})