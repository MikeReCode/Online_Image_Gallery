from . import views
from django.urls import path, reverse_lazy

app_name = 'image_gallery'
urlpatterns = [
    path('', views.Gallery.as_view(), name='all'),
    path('register/', views.RegisterView.as_view(success_url = reverse_lazy('image_gallery:all')), name='register'),
    path('image/<int:pk>', views.DetailImage.as_view(), name='image_detail'),
    path('create/', views.AddImages.as_view(success_url=reverse_lazy('image_gallery:all')), name='image_create'),
    path('image/<int:pk>/delete', views.DeleteImage.as_view(success_url=reverse_lazy('image_gallery:all')), name='image_delete'),

]