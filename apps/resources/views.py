from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count, Avg
from django.contrib.auth.decorators import login_required

from .models import Resources, Review, ResourcesRating
from apps.user.models import User
from .utils import generate_cat_count_list
from .form import PostResourceForm
# Create your views here.


def home_page(request):
    cnt = Resources.objects.all().count()
    user_cnt = User.objects.filter(is_active=True).count()
    res_per_cat = Resources.objects.values(
        'cat_id__cat').annotate(cnt=Count('cat_id'))
 
    context = {
        "cnt": cnt,
        "user_cnt": user_cnt,
        "res_per_cat": res_per_cat,
    }

    return render(
        request=request,
        template_name='resources/home.html',
        context=context
    )


def home_page_old(request):
    cnt = Resources.objects.all().count()
    user_cnt = User.objects.filter(is_active=True).count()
    res_per_cat = Resources.objects.values(
        'cat_id__cat').annotate(cnt=Count('cat_id'))
    response = f"""
        <html>
            <h1>Welcome to the ResourceShare</h1>
            <h3>All Users</h3>
            <p>{user_cnt} and counting!</p>
            
            <p>{cnt} resources and counting!</p>
            
            <h3>Resources per category</h3>
            <ol>
                {generate_cat_count_list(res_per_cat)}
            </ol>
        </html>"""
    return HttpResponse(response)

@login_required
def resource_detail(request, id):
    max_viewed_resources = 5
    
    viewed_resources = request.session.get("viewed_resources", [])
    
    res = (
        Resources.objects.select_related('user_id', 'cat_id')
        .prefetch_related('tags')
        .get(pk=id)
    )
    # prepare data
    viewed_resource = [id, res.title]
    
    # check if that data exists already and remove it
    
    if viewed_resource in viewed_resources:
        viewed_resources.remove(viewed_resource)
    
    viewed_resources.insert(0, viewed_resource)
    
    # get limit
    viewed_resources = viewed_resources[:max_viewed_resources]
    
    # add it back to our session
    request.session["viewed_resources"] = viewed_resources
    
    
    
    rev_count = Review.objects.filter(resources_id_id=id).count()
    avg_rating = ResourcesRating.objects.filter(resources_id_id=id).aggregate(Avg('rate'))
    
    
    context = {
        "res": res, 
        "rev_count": rev_count,
        "avg_rating": avg_rating['rate__avg'],
        
    }
    return render(
        request=request,
        template_name='resources/resource_details.html',
        context=context
    )


def resource_detail_old(request, id):
    res = (
        Resources.objects.select_related('user_id', 'cat_id')
        .prefetch_related('tags')
        .get(pk=id)
    )

    response = f"""
        <html>
            <h1>{res.title}</h1>
            <p><b>User: </b>{res.user_id.username}</p>
            <p><b>Link: </b>{res.link}</p>
            <p><b>Description: </b>{res.description}</p>
            <p><b>Category: </b>{res.cat_id.cat}</p>
            <p><b>Tags: </b>{res.all_tags()}</p>
            
        </html>    
        """
    return HttpResponse(response)

@login_required
def resource_post(request):
    # Unbound # user made a GET request
    if request.method == 'GET':
        form = PostResourceForm()
        return render(
            request,
            'resources/resource_post.html',
            {'form': form},
        )
    else:
        # Bound # user made a POST request
        form = PostResourceForm(request.POST)
        
        # validation
        # .is_valid() method
        # .cleaned_data attribute
        
        if form.is_valid():
            
            data = form.cleaned_data
            #TODO: manually add a user id 
            #TODO: save it to the DB
            #TODO: Redirect the user to the home page 
        else: 
            pass


class HomePage(TemplateView):
    template_name = 'home_page.html'
