from django.shortcuts import render
from django.http import HttpResponse

def calcular(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operacion = request.POST['operacion']

        if operacion == 'sumar':
            resultado = num1 + num2
        elif operacion == 'restar':
            resultado = num1 - num2
        elif operacion == 'multiplicar':
            resultado = num1 * num2
        elif operacion == 'dividir':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = 'Error: División por cero'
        else:
            resultado = 'Operación no válida'

        return render(request, 'index.html', {'resultado': resultado})

    return render(request, 'index.html')

# Create your views here.
