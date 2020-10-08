from django.shortcuts import render ,redirect
from .models import Post
 
from .form import Post_form
# Create your views here.

def post_list(request):
    all_posts = Post.objects.all
    return render(request,'Post/postlist.html',{'posts':all_posts})

def post_details(request , post_id):
    
    post_details = Post.objects.get(id= post_id)
    return render(request , 'Post/postdetails.html', {'single_post':post_details})

def new_post (request):
    if request.method == 'POST':
        print("in if")
        form = Post_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else: form =Post_form

    return render(request,"Post/new_post.html",{'form_new_post': form })

def post_delete(request,post_id):

    post= Post.objects.get(id=post_id)
    post.delete()
    return redirect ('/bloge')


