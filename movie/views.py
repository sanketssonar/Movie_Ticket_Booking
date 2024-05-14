from django.shortcuts import render, redirect
from django.views import generic
from . import models
from .models import SetMovie, MovieMaster
from . import forms
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from movie_user.models import BookedSeatsModel
from django.http import JsonResponse
from django.db.models import Q
from django.urls import reverse
from django.views.generic import DeleteView
from .models import MovieMaster
# Create your views here.

############ADmin login page######################
class LoginAdmin(View):
    template_name = "movie/admin_login.html"

    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name)

    def post(self,request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            superusers = User.objects.get(username = username)
            print("-------------------------------------")
            print(superusers.username)
            print(superusers.is_superuser)
            print("--------------------------------------")
            if superusers.is_superuser == True:
                login(request, user)
                return redirect('../dashboard/')

        else:
            return render(request, self.template_name)


def adminLogout(request):
    logout(request)
    return redirect('../login/')


##########ADmin dashboard page##########
class Dashboard(generic.ListView):
    model = MovieMaster
    template_name = "movie/dashboard.html"
    context_object_name = 'movies'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(Q(m_name__icontains=search_query))
        return queryset

########This page will be used by admin for adding movies to system when then will be used for setting shows####################
class AddMovies(generic.CreateView):  
    form_class = forms.AddMovieForm
    model = models.MovieMaster
    template_name = "movie/addmovies.html"
    # fields = '__all__'

    
    ###############From the list of movies added admin can set show for particular movie############################
class SetMovies(generic.CreateView):
    form_class = forms.SetMovieForm
    model = models.SetMovie
    # context_object_name = 'movies'
    # def post(self, request, *args, **kwargs): 
    #     if request.method == 'POST':
    #         request.POST['']
    #         models.MovieGraphCount(m_name=)
    
    template_name = "movie/setmovies.html"
    
class MovieDeleteView(DeleteView):
    model = MovieMaster
    template_name = 'movie/delete_movie.html'

    def get_success_url(self):
        return reverse('setadmin:dashboard')

