from django.shortcuts import render, get_object_or_404, redirect
from Lab3.models import PassengerCarriage, RailwayBranch, Station, TrainSquad, TrainRouteWithSquadOnDate
from Lab3.repositories import PassengerCarriageRepository, RailwayBranchRepository, StationRepository, TrainRouteRepository, TrainSquadRepository, TrainRouteWithSquadOnDateRepository
from .forms import PassengerCarriageForm, RailwayBranchForm, StationForm, TrainRouteForm, TrainRoute, TrainSquadForm, TrainRouteWithSquadOnDateForm

## Main Page
def index(request):
    return render(request, 'representation/index.html')
def graph_menu_view(request):
    return render(request, 'representation/graph_menu.html')

def menu_view(request):
    return render(request, 'representation/menu.html')
##PassengerCarriage
def carriages_operations(request):
    return render(request, 'representation/carriages_templates/carriages.html')
def passenger_carriage_detail(request, pk):
    carriage = get_object_or_404(PassengerCarriage, pk=pk)
    return render(request, 'representation/carriages_templates/passenger_carriage_detail.html', {'carriage': carriage})

def passenger_carriage_add(request):
    if request.method == 'POST':
        form = PassengerCarriageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carriages_get')
    else:
        form = PassengerCarriageForm()
    return render(request, 'representation/carriages_templates/passenger_carriage_form.html', {'form': form})


def passenger_carriage_edit(request, pk):
    carriage = get_object_or_404(PassengerCarriage, pk=pk)
    if request.method == 'POST':
        form = PassengerCarriageForm(request.POST, instance=carriage)
        if form.is_valid():
            form.save()
            return redirect('carriages_get')
    else:
        form = PassengerCarriageForm(instance=carriage)
    return render(request, 'representation/carriages_templates/passenger_carriage_form.html', {'form': form})


def carriages_get(request):
    carriages = PassengerCarriage.objects.all()
    return render(request, 'representation/carriages_templates/carriages_get.html', {'carriages': carriages})

def carriages_get_by_id(request):
    carriage = None
    error = None

    if request.method == 'GET':
        carriage_id = request.GET.get('id')
        if carriage_id:
            carriage = PassengerCarriageRepository.get(carriage_id)
            if not carriage:
                error = 'Вагон не знайдено'

    return render(request, 'representation/carriages_templates/carriages_get_id.html', {'carriage': carriage, 'error': error})

def carriages_post(request):
    if request.method == 'POST':
        form = PassengerCarriageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carriages_get')
    else:
        form = PassengerCarriageForm()
    return render(request, 'representation/carriages_templates/passenger_carriage_form.html', {'form': form})

def carriages_put(request):
    error = None
    form = None

    if request.method == 'POST':
        carriage_id = request.POST.get('id')
        carriage = PassengerCarriageRepository.get(carriage_id)

        if carriage:
            form = PassengerCarriageForm(request.POST, instance=carriage)
            if form.is_valid():
                form.save()
                return redirect('carriages_get')
        else:
            error = 'Вагон не знайдено'

    if not form:
        form = PassengerCarriageForm()

    return render(
        request,
        'representation/carriages_templates/carriages_put.html',
        {'form': form, 'error': error}
    )
def carriages_delete(request):
    if request.method == 'POST':
        carriage_id = request.POST.get('id')
        carriage = PassengerCarriageRepository.get(carriage_id)
        if carriage:
            PassengerCarriageRepository.delete(carriage_id)
            return redirect('carriages_get')
        else:
            return render(request, 'representation/carriages_templates/carriages_delete.html', {'error': 'Вагон не знайдено'})
    return render(request, 'representation/carriages_templates/carriages_delete.html')

##RailwayBranch
def railway_branches_operations(request):
    return render(request, 'representation/railway_branches_templates/railway_branches.html')

def railway_branch_detail(request, pk):
    branch = get_object_or_404(RailwayBranch, pk=pk)
    return render(request, 'representation/railway_branches_templates/railway_branch_detail.html', {'branch': branch})

def railway_branch_add(request):
    if request.method == 'POST':
        form = RailwayBranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('railway_branches_get')
    else:
        form = RailwayBranchForm()
    return render(request, 'representation/railway_branches_templates/railway_branch_form.html', {'form': form})

def railway_branch_edit(request, pk):
    branch = get_object_or_404(RailwayBranch, pk=pk)
    if request.method == 'POST':
        form = RailwayBranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('railway_branches_get')
    else:
        form = RailwayBranchForm(instance=branch)
    return render(request, 'representation/railway_branches_templates/railway_branch_form.html', {'form': form})

def railway_branches_get(request):
    branches = RailwayBranch.objects.all()
    return render(request, 'representation/railway_branches_templates/railway_branch_get.html', {'branches': branches})

def railway_branches_get_by_id(request):
    branch = None
    error = None
    if request.method == 'GET':
        branch_id = request.GET.get('id')
        if branch_id:
            branch = RailwayBranchRepository.get(branch_id)
            if not branch:
                error = 'Філія не знайдена'
    return render(request, 'representation/railway_branches_templates/railway_branches_get_id.html', {'branch': branch, 'error': error})

def railway_branches_post(request):
    if request.method == 'POST':
        form = RailwayBranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('railway_branches_get')
    else:
        form = RailwayBranchForm()
    return render(request, 'representation/railway_branches_templates/railway_branch_form.html', {'form': form})

def railway_branches_put(request):
    error = None
    form = None
    if request.method == 'POST':
        branch_id = request.POST.get('id')
        branch = RailwayBranchRepository.get(branch_id)
        if branch:
            form = RailwayBranchForm(request.POST, instance=branch)
            if form.is_valid():
                form.save()
                return redirect('railway_branches_get')
        else:
            error = 'Філія не знайдена'
    if not form:
        form = RailwayBranchForm()
    return render(
        request,
        'representation/railway_branches_templates/railway_branches_put.html',
        {'form': form, 'error': error}
    )

def railway_branches_delete(request):
    if request.method == 'POST':
        branch_id = request.POST.get('id')
        branch = RailwayBranchRepository.get(branch_id)
        if branch:
            RailwayBranchRepository.delete(branch_id)
            return redirect('railway_branches_get')
        else:
            return render(request, 'representation/railway_branches_templates/railway_branches_delete.html', {'error': 'Філія не знайдена'})
    return render(request, 'representation/railway_branches_templates/railway_branches_delete.html')

 ##Station

def stations_operations(request):
    return render(request, 'representation/stations_templates/stations.html')


def station_detail(request, pk):
    station = get_object_or_404(Station, pk=pk)
    return render(request, 'representation/stations_templates/station_detail.html', {'station': station})


def station_add(request):
    if request.method == 'POST':
        form = StationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stations_get')
    else:
        form = StationForm()
    return render(request, 'representation/stations_templates/station_form.html', {'form': form})


def station_edit(request, pk):
    station = get_object_or_404(Station, pk=pk)
    if request.method == 'POST':
        form = StationForm(request.POST, instance=station)
        if form.is_valid():
            form.save()
            return redirect('stations_get')
    else:
        form = StationForm(instance=station)
    return render(request, 'representation/stations_templates/station_form.html', {'form': form})


def stations_get(request):
    stations = Station.objects.all()
    return render(request, 'representation/stations_templates/stations_get.html', {'stations': stations})


def stations_get_by_id(request):
    station = None
    error = None

    if request.method == 'GET':
        station_id = request.GET.get('id')
        if station_id:
            station = StationRepository.get(station_id)
            if not station:
                error = 'Станцію не знайдено'

    return render(request, 'representation/stations_templates/stations_get_id.html',
                  {'station': station, 'error': error})


def stations_post(request):
    if request.method == 'POST':
        form = StationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stations_get')
    else:
        form = StationForm()
    return render(request, 'representation/stations_templates/station_form.html', {'form': form})


def stations_put(request):
    error = None
    form = None

    if request.method == 'POST':
        station_id = request.POST.get('id')
        station = StationRepository.get(station_id)

        if station:
            form = StationForm(request.POST, instance=station)
            if form.is_valid():
                form.save()
                return redirect('stations_get')
        else:
            error = 'Станцію не знайдено'

    if not form:
        form = StationForm()

    return render(
        request,
        'representation/stations_templates/stations_put.html',
        {'form': form, 'error': error}
    )


def stations_delete(request):
    if request.method == 'POST':
        station_id = request.POST.get('id')
        station = StationRepository.get(station_id)
        if station:
            StationRepository.delete(station_id)
            return redirect('stations_get')
        else:
            return render(request, 'representation/stations_templates/stations_delete.html',
                          {'error': 'Станцію не знайдено'})
    return render(request, 'representation/stations_templates/stations_delete.html')

##TrainRoute
def train_routes_operations(request):
    return render(request, 'representation/train_routes_templates/train_routes.html')

def train_route_detail(request, pk):
    route = get_object_or_404(TrainRoute, pk=pk)
    return render(request, 'representation/train_routes_templates/train_routes_detail.html', {'route': route})

def train_route_add(request):
    if request.method == 'POST':
        form = TrainRouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('train_routes_get')
    else:
        form = TrainRouteForm()
    return render(request, 'representation/train_routes_templates/train_routes_form.html', {'form': form})

def train_route_edit(request, pk):
    route = get_object_or_404(TrainRoute, pk=pk)
    if request.method == 'POST':
        form = TrainRouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            return redirect('train_routes_get')
    else:
        form = TrainRouteForm(instance=route)
    return render(request, 'representation/train_routes_templates/train_routes_form.html', {'form': form})

def train_routes_get(request):
    routes = TrainRoute.objects.all()
    return render(request, 'representation/train_routes_templates/train_routes_get.html', {'routes': routes})

def train_routes_get_by_id(request):
    route = None
    error = None
    if request.method == 'GET':
        route_id = request.GET.get('id')
        if route_id:
            route = TrainRouteRepository.get(route_id)
            if not route:
                error = 'Маршрут не знайдено'
    return render(request, 'representation/train_routes_templates/train_routes_get_id.html', {'route': route, 'error': error})

def train_routes_post(request):
    if request.method == 'POST':
        form = TrainRouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('train_routes_get')
    else:
        form = TrainRouteForm()
    return render(request, 'representation/train_routes_templates/train_routes_form.html', {'form': form})

def train_routes_put(request):
    error = None
    form = None
    if request.method == 'POST':
        route_id = request.POST.get('id')
        route = TrainRouteRepository.get(route_id)
        if route:
            form = TrainRouteForm(request.POST, instance=route)
            if form.is_valid():
                form.save()
                return redirect('train_routes_get')
        else:
            error = 'Маршрут не знайдено'
    if not form:
        form = TrainRouteForm()
    return render(request, 'representation/train_routes_templates/train_routes_put.html', {'form': form, 'error': error})

def train_routes_delete(request):
    if request.method == 'POST':
        route_id = request.POST.get('id')
        route = TrainRouteRepository.get(route_id)
        if route:
            TrainRouteRepository.delete(route_id)
            return redirect('train_routes_get')
        else:
            return render(request, 'representation/train_routes_templates/train_routes_delete.html', {'error': 'Маршрут не знайдено'})
    
    return render(request, 'representation/train_routes_templates/train_routes_delete.html')

##TrainSquad
def train_squads_operations(request):
    return render(request, 'representation/train_squads_templates/train_squads.html')


def train_squad_detail(request, pk):
    train_squad = get_object_or_404(TrainSquad, pk=pk)
    return render(request, 'representation/train_squads_templates/train_squad_detail.html', {'train_squad': train_squad})


def train_squad_add(request):
    if request.method == 'POST':
        form = TrainSquadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('train_squads_get')
    else:
        form = TrainSquadForm()
    return render(request, 'representation/train_squads_templates/train_squad_form.html', {'form': form})


def train_squad_edit(request, pk):
    train_squad = get_object_or_404(TrainSquad, pk=pk)
    if request.method == 'POST':
        form = TrainSquadForm(request.POST, instance=train_squad)
        if form.is_valid():
            form.save()
            return redirect('train_squads_get')
    else:
        form = TrainSquadForm(instance=train_squad)
    return render(request, 'representation/train_squads_templates/train_squad_form.html', {'form': form})


def train_squads_get(request):
    train_squads = TrainSquad.objects.all()
    return render(request, 'representation/train_squads_templates/train_squads_get.html', {'train_squads': train_squads})


def train_squads_get_by_id(request):
    train_squad = None
    error = None

    if request.method == 'GET':
        train_squad_id = request.GET.get('id')
        if train_squad_id:
            try:
                train_squad = TrainSquad.objects.get(pk=train_squad_id)
            except TrainSquad.DoesNotExist:
                error = 'Склад не знайдено'

    return render(request, 'representation/train_squads_templates/train_squads_get_id.html',
                  {'train_squad': train_squad, 'error': error})


def train_squads_post(request):
    if request.method == 'POST':
        form = TrainSquadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('train_squads_get')
    else:
        form = TrainSquadForm()
    return render(request, 'representation/train_squads_templates/train_squad_form.html', {'form': form})


def train_squads_put(request):
    error = None
    form = None

    if request.method == 'POST':
        train_squad_id = request.POST.get('id')
        try:
            train_squad = TrainSquad.objects.get(pk=train_squad_id)
            form = TrainSquadForm(request.POST, instance=train_squad)
            if form.is_valid():
                form.save()
                return redirect('train_squads_get')
        except TrainSquad.DoesNotExist:
            error = 'Склад не знайдено'

    if not form:
        form = TrainSquadForm()

    return render(
        request,
        'representation/train_squads_templates/train_squads_put.html',
        {'form': form, 'error': error}
    )


def train_squads_delete(request):
    if request.method == 'POST':
        train_squad_id = request.POST.get('id')
        try:
            train_squad = TrainSquad.objects.get(pk=train_squad_id)
            train_squad.delete()
            return redirect('train_squads_get')
        except TrainSquad.DoesNotExist:
            return render(request, 'representation/train_squads_templates/train_squads_delete.html',
                          {'error': 'Склад не знайдено'})
        except:
            return render(request,
                          'representation/train_routes_with_squads_templates/train_routes_with_squads_delete.html', {
                              'error': 'Заборонена операція'
                          })
    return render(request, 'representation/train_squads_templates/train_squads_delete.html')

def train_route_with_squads_operations(request):
    return render(request, 'representation/train_routes_with_squads_templates/train_routes_with_squads.html')


def train_route_with_squad_detail(request, pk):
    train_route_with_squad = get_object_or_404(TrainRouteWithSquadOnDate, pk=pk)
    return render(request, 'representation/train_routes_with_squads_templates/train_route_with_squad_detail.html', {
        'train_route_with_squad': train_route_with_squad
    })


def train_route_with_squad_add(request):
    if request.method == 'POST':
        form = TrainRouteWithSquadOnDateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('train_routes_with_squads_get')
    else:
        form = TrainRouteWithSquadOnDateForm()
    return render(request, 'representation/train_routes_with_squads_templates/train_route_with_squad_form.html', {
        'form': form
    })


def train_route_with_squad_edit(request, pk):
    train_route_with_squad = get_object_or_404(TrainRouteWithSquadOnDate, pk=pk)
    if request.method == 'POST':
        form = TrainRouteWithSquadOnDateForm(request.POST, instance=train_route_with_squad)
        if form.is_valid():
            form.save()
            return redirect('train_routes_with_squads_get')
    else:
        form = TrainRouteWithSquadOnDateForm(instance=train_route_with_squad)
    return render(request, 'representation/train_routes_with_squads_templates/train_route_with_squad_form.html', {
        'form': form
    })


def train_routes_with_squads_get(request):
    train_routes_with_squads = TrainRouteWithSquadOnDate.objects.all()
    return render(request, 'representation/train_routes_with_squads_templates/train_routes_with_squads_get.html', {
        'train_routes_with_squads': train_routes_with_squads
    })


def train_routes_with_squads_get_by_id(request):
    train_route_with_squad = None
    error = None

    if request.method == 'GET':
        route_id = request.GET.get('id')
        if route_id:
            try:
                train_route_with_squad = TrainRouteWithSquadOnDate.objects.get(pk=route_id)
            except TrainRouteWithSquadOnDate.DoesNotExist:
                error = 'Запис не знайдено'

    return render(request, 'representation/train_routes_with_squads_templates/train_routes_with_squads_get_id.html', {
        'train_route_with_squad': train_route_with_squad,
        'error': error
    })


def train_routes_with_squads_post(request):
    if request.method == 'POST':
        form = TrainRouteWithSquadOnDateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('train_routes_with_squads_get')
    else:
        form = TrainRouteWithSquadOnDateForm()
    return render(request, 'representation/train_routes_with_squads_templates/train_route_with_squad_form.html', {
        'form': form
    })


def train_routes_with_squads_put(request):
    error = None
    form = None

    if request.method == 'POST':
        route_id = request.POST.get('id')
        try:
            train_route_with_squad = TrainRouteWithSquadOnDate.objects.get(pk=route_id)
            form = TrainRouteWithSquadOnDateForm(request.POST, instance=train_route_with_squad)
            if form.is_valid():
                form.save()
                return redirect('train_routes_with_squads_get')
        except TrainRouteWithSquadOnDate.DoesNotExist:
            error = 'Запис не знайдено'

    if not form:
        form = TrainRouteWithSquadOnDateForm()

    return render(request, 'representation/train_routes_with_squads_templates/train_routes_with_squads_put.html', {
        'form': form,
        'error': error
    })


def train_routes_with_squads_delete(request):
    if request.method == 'POST':
        route_id = request.POST.get('id')
        try:
            train_route_with_squad = TrainRouteWithSquadOnDate.objects.get(pk=route_id)
            train_route_with_squad.delete()
            return redirect('train_routes_with_squads_get')
        except TrainRouteWithSquadOnDate.DoesNotExist:
            return render(request, 'representation/train_routes_with_squads_templates/train_routes_with_squads_delete.html', {
                'error': 'Запис не знайдено'
            })
        except:
            return render(request,
                          'representation/train_routes_with_squads_templates/train_routes_with_squads_delete.html', {
                              'error': 'Заборонена операція'
                          })
    return render(request, 'representation/train_routes_with_squads_templates/train_routes_with_squads_delete.html')