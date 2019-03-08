from django.shortcuts import render


# render page 1
def index(request):
    return render(request, 'cwApp/index.html')


# render page 2
def page_two(request):
    return render(request, 'cwApp/pageTwo.html')


# render page 3
def page_three(request):
    return render(request, 'cwApp/pageThree.html')
