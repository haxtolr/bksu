from django.shortcuts import render, redirect
from .forms import ProductForm
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

def upload_image(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image')
    else:
        form = ProductForm()
    return render(request, 'upload.html', {'form': form})

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer