from django.shortcuts import render

from Cars.models import Car

from django.shortcuts import redirect

# Create your views here.

def Cars(request):
    if request.method == 'POST':
        data = request.POST

        Car_name = data.get('Car_name')
        About_car = data.get('About_car')
        Car_image = request.FILES.get('Car_image')

        # print(Car_name)
        # print(About_car)
        # print(Car_image)

        Car.objects.create(
            Car_name = Car_name,
            About_car = About_car,
            Car_image = Car_image
        )
        return redirect('Cars')
    queryset = Car.objects.all()
    context = {"Cars" : queryset}

    # def __str__(self):
    #         return self.Car_name
    # for car in Cars:
    #         print(f"The car name is {car.Car_name}.")
    
    return render(request, 'Cars.html', context)


def delete_car(request, id):
    queryset = Car.objects.get(id = id)
    queryset.delete()
    return redirect('Cars')

def update_car(request, id):
    queryset = Car.objects.get(id = id)

    if request.method == 'POST':
        data = request.POST

        Car_name = data.get('Car_name')
        About_car = data.get('About_car')
        Car_image = request.FILES.get('Car_image')

        queryset.Car_name = Car_name
        queryset.About_car = About_car

        if Car_image:
            queryset.Car_image = Car_image

        queryset.save()
        return redirect('Cars')
    context = {'Cars':queryset}
    return render(request, 'update_car.html', context)