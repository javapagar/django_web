from blog.forms import CommentForm
from blog.models import Comment, Post
from django.shortcuts import render

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-created_on')
    context ={
        "nbar":"blog",
        "posts":posts
    }
   
    return render(request,'posts_list.html',context)

def detalle_post(request,pk):
    post=Post.objects.get(pk=pk)

    form=CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body= form.cleaned_data["body"],
                post=post
            )

            comment.save()

    comments=Comment.objects.filter(post=post).order_by('-created_on')
    
    context={
        "post":post,
        "comments":comments,
        "form":form
    }
    return render(request,"detalle_post.html",context)

def post_category(request,category):
    posts= Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'#el simbolo - significa orden ascendente
    )
    context = {
        "category":category,
        "posts":posts
    }
    return render(request,"posts_category.html",context)