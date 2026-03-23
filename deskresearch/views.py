from django.shortcuts import render,get_object_or_404,redirect
from .models import Post

from .forms import PostForm

def home(request):
    posts = Post.objects.order_by('-created_at')
    return render(request,'home.html',{'Posts':posts})

def new(request):
    form=PostForm()
    return render(request, 'new.html', {'form':form})

def create(request):
    form=PostForm(request.POST,request.FILES)
    if form.is_valid():
        new_deskresearch=form.save(commit=False)
        new_deskresearch.save()
        return redirect('deskresearch:detail',new_deskresearch.id)
    return redirect('deskresearch:home') #여기도 deskresearch:home 해줘야함

def detail(request,post_id):
    post_detail=get_object_or_404(Post, pk=post_id)
    return render(request,'detail.html',{'post':post_detail})

def delete(request, post_id):
    delete_deskresearch = get_object_or_404(Post, pk=post_id)
    delete_deskresearch.delete()
    return redirect('deskresearch:home')

def update_page(request, post_id):
    update_deskresearch=get_object_or_404(Post,pk=post_id)
    return render(request,'update.html',{'update_deskresearch':update_deskresearch})

def update_post(request, post_id):
    update_deskresearch=get_object_or_404(Post,pk=post_id)
    update_deskresearch.title=request.POST['title']
    update_deskresearch.content=request.POST['content']
    update_deskresearch.save()
    return redirect('deskresearch:home')