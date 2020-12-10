from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

# Import the Category and Page models
from rango.models import Category, Page, UserProfile
from django.contrib.auth.models import User

""" # A helper method
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):

    visits = int(get_server_side_cookie(request, 'visits', '1'))

    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    
    # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).days > 0:
        visits += 1
        # update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())
    else:
        visits = 1
        # set the last visit cookie
        request.session['last_visit'] = last_visit_cookie
    
    # Update/set the visits cookie
    request.session['visits'] = visits


def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.

    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}

    # Obtain our Response object early so we can add cookie information.
    response =  render(request, 'rango/index.html', context=context_dict)

    #Call function to handle the cookies
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    # Return response back to the user, updating any cookies that need change.
    return response """

class IndexView(ListView):
    template_name = 'rango/index.html'
    context_object_name = 'pages'
    queryset = Page.objects.order_by('-views')[:5] 

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = Category.objects.order_by('-likes')[:5]
        return context

def about(request):
    context_dict = {}
    #visitor_cookie_handler(request)
    #context_dict['visits'] = request.session['visits']
    return render(request, 'rango/about.html', context_dict)

class PageListView(ListView):
    template_name = "rango/category.html"
    context_object_name = "pages"

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category_name_slug'])
        return Page.objects.filter(category=self.category).order_by('-views')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

def track_url(request):
    page_id = None
    url = 'rango/index/'

    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']

            try:
                page = Page.objects.get(id=page_id)
                page.views += 1
                page.save()
                url = page.url
            except:
                pass
                
    return redirect(url)

class AddCategoryView(CreateView):
    template_name = 'rango/add_category.html'
    model = Category
    fields = ['name']

class AddPageView(CreateView):
    template_name = 'rango/add_page.html'
    model = Page
    fields = ['title', 'url']

    def form_valid(self, form, **kwargs):
        form.instance.category = get_object_or_404(Category, slug=self.kwargs['category_name_slug'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.kwargs['category_name_slug'])
        return context

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@method_decorator(login_required, name='dispatch')
class RegisterProfileView(CreateView):
    template_name = 'rango/profile_registration.html'
    model = UserProfile
    fields = ['website', 'picture']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):
    template_name = 'rango/profile.html'
    model = UserProfile
    fields = ['website', 'picture']
    slug_field = 'user_slug'
    slug_url_kwarg = 'user_slug'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        user = User.objects.get(username=self.kwargs['user_slug'])
        user_profile = UserProfile.objects.get(user=user)
        context = super().get_context_data(**kwargs)
        context['user_profile'] = user_profile
        context['selected_user'] = user
        return context

@method_decorator(login_required, name='dispatch')
class UserListView(ListView):
    model = UserProfile
    template_name = 'rango/users.html'
    context_object_name = 'user_profiles'

@login_required
def like_category(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id']
        likes = 0
        if cat_id:
            cat = Category.objects.get(id=int(cat_id))
            if cat:
                likes = cat.likes + 1
                cat.likes = likes
                cat.save()
    return HttpResponse(likes)

def get_category_list(max_results=0, starts_with=''):
    cat_list = []
    if starts_with:
        cat_list = Category.objects.filter(name__istartswith=starts_with)

    if max_results > 0:
        if len(cat_list) > max_results:
            cat_list = cat_list[:max_results]
    return cat_list

def suggest_category(request):
    cat_list = []
    starts_with = ''

    if request.method == 'GET':
        starts_with = request.GET['suggestion']
    cat_list = get_category_list(8, starts_with)

    if len(cat_list) == 0:
            cat_list = Category.objects.order_by('-likes')

    return render(request, 'rango/cats.html', {'cats': cat_list })
