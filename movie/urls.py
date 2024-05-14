from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import MovieDeleteView

app_name='setadmin'

urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('addmovie/', views.AddMovies.as_view(), name='addmovie'),
    path('setmovie/', views.SetMovies.as_view(), name='setmovie'),
    path('adminlogin/', views.LoginAdmin.as_view(), name='adminlogin'),
    path('logout/', views.adminLogout, name='logout'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)