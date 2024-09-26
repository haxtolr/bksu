from django.shortcuts import render, redirect
from .forms import ProductForm
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
<<<<<<< HEAD
from rest_framework.response import Response
from rest_framework import status
=======
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127

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
<<<<<<< HEAD
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
=======
    serializer_class = ProductSerializer
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127
