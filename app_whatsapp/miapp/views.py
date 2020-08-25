from django.shortcuts import render,HttpResponse

nombre = 'sergio'
datos = ['casa', 'habitacion', 'mesa', 'aire']

# Create your views here.
def index(request):
    html = "<ul>"
    year = 2021
    while year <= 2050:
        html += f"<li>{str(year)}</li>"
        year += 1
    html += "</ul>"
    return render(request ,'index.html', {
        'title': 'Inicio',
        'nombre':nombre,
        'datos':datos,
        'mi_variable': 'Soy un dato que esta en la vista'
    })

def filtro(request):
    return render(request, 'filtro.html')

def pagina(request):
    return render(request, 'pagina.html')


