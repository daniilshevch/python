from django.shortcuts import render, get_object_or_404, redirect
from Lab3.models import PassengerCarriage
from .forms import PassengerCarriageForm
def passenger_carriage_list(request):
    carriages = PassengerCarriage.objects.all()
    return render(request, 'representation/passenger_carriage_list.html', {'carriages': carriages})
def passenger_carriage_detail(request, pk):
    carriage = get_object_or_404(PassengerCarriage, pk=pk)
    return render(request, 'representation/passenger_carriage_detail.html', {'carriage': carriage})
def passenger_carriage_add(request, pk):
    if request.method == 'POST':
        form = PassengerCarriageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('passenger_carriage_list')
    else:
        form = PassengerCarriageForm()
    return render(request, 'representation/passenger_carriage_form.html', {'form': form})
def passenger_carriage_edit(request, pk):
    carriage = get_object_or_404(PassengerCarriage, pk=pk)
    if request.method == 'POST':
        form = PassengerCarriageForm(request.POST, instance=carriage)
        if form.is_valid():
            form.save()
            return redirect('passenger_carriage_list')
    else:
        form = PassengerCarriageForm(instance=carriage)
    return render(request, 'representation/passenger_carriage_form.html', {'form': form})
