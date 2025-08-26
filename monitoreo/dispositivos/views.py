from django.shortcuts import render
from django.http import HttpResponse

# Vista de inicio
def inicio(request):
    return HttpResponse("Hola desde Django")

# Vista del panel de dispositivos
def panel(request):
    # Datos simulados de dispositivos
    dispositivos = [
        {"nombre": "Aire acondicionado", "consumo": 120, "limite": 100},
        {"nombre": "Refrigerador", "consumo": 80, "limite": 100},
        {"nombre": "Computadora", "consumo": 50, "limite": 60},
        {"nombre": "Calefactor", "consumo": 110, "limite": 90},
    ]
    # Se calcula si el consumo está dentro del límite
    for d in dispositivos:
        d["estado"] = "Dentro del límite" if d["consumo"] <= d["limite"] else "Excede el límite"
    return render(request, "panel.html", {"dispositivos": dispositivos})