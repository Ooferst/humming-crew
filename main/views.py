from django.shortcuts import render
# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'Humming Crew',
        'npm' : '2406432406',
        'name': 'Hafiz Nathan Vesaputra',
        'class': 'PBP F',
    }

    return render(request, "main.html", context)