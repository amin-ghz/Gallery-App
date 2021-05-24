from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import PictureFilter

def home(request):
    pictures = Picture.objects.all()
    categories = CategoryTag.objects.all()
    category_count = categories.count()
    category = request.GET.get('category')

    myFilter = PictureFilter(request.GET, queryset=pictures)

    pictures = myFilter.qs  

    paginator = Paginator(pictures, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {'pictures': pictures,
    'category': category,
    'category_count': category_count,
    'categories':categories,
    'myFilter': myFilter,
    'page_obj': page_obj,
}
    return render(request, 'image_app/display.html', context)


def add(request):

    categories = CategoryTag.objects.all()

    if request.method == 'POST':
        # form = ImageForm(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()

        data = request.POST
        category_id = data.get('category')
        create_category = data.get('create_category')

        if category_id != 'none':
            category = CategoryTag.objects.get(id=category_id)

        elif create_category != '':
            category, created = CategoryTag.objects.get_or_create(category=create_category)

        else:
            category = None

        pictures = Picture.objects.create(
            description=data.get('description'),
            picture=request.FILES.get('image'),
            categories=category,
        )
           
        return redirect('/?category=all')
            
    
    return render(request, 'image_app/add.html', {'categories': categories,})


def detail(request,pk):
    picture = Picture.objects.get(id=pk)


    return render(request, 'image_app/detail.html', {'picture': picture})