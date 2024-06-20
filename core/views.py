# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Text
from .forms import TextForm

# Página principal
def index(request):
    return render(request, 'index.html')

# Lista de textos
def listText(request):
    textos = Text.objects.all().order_by('-created_at')  # Ordena do mais recente para o mais antigo
    return render(request, 'listText.html', {'textos': textos})

# Publicar texto
def postText(request):
    if request.method == 'POST':
        form = TextForm(request.POST, request.FILES)  # request.FILES para mostrar a imagem no card
        if form.is_valid():
            form.save()
            return redirect('listText')
    else:
        form = TextForm()
    return render(request, 'postText.html', {'form': form})

# Página para ler o texto
def detailText(request, texto_id):
    texto = get_object_or_404(Text, pk=texto_id)
    return render(request, 'detailText.html', {'texto': texto})

# Excluir texto
def deleteText(request, texto_id):
    texto = get_object_or_404(Text, pk=texto_id)
    texto.delete()
    return redirect('listText')

# Editar texto
def editText(request, texto_id):
    texto = get_object_or_404(Text, pk=texto_id)
    if request.method == 'POST':
        form = TextForm(request.POST, request.FILES, instance=texto)
        if form.is_valid():
            form.save()
            return redirect('listText')
    else:
        form = TextForm(instance=texto)
    return render(request, 'editText.html', {'form': form, 'texto': texto})
