from django.shortcuts import render
from . import convert


def home(request):
    if request.method == 'GET':
        return render(request, 'converter/home.html')
    else:
        test1 = request.POST['test']
        # test2 = request.POST['fileList']
        # test3 = request.POST['studio']
        test4 = convert.test_funk(test1)
        return render(request, 'converter/home.html', {'test': test4})


def about(request):
    return render(request, 'converter/about.html')
