from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Hashtag

from .forms import PostForm,Commentform

def home(request):
    posts = Post.objects.order_by('-created_at')
    return render(request,'home.html',{'posts':posts})

def new(request):
    form=PostForm()
    return render(request, 'new.html', {'form':form})

def create(request):
    form=PostForm(request.POST,request.FILES)
    if form.is_valid():
        new_deskresearch=form.save(commit=False)
        new_deskresearch.save()
        hashtags=request.POST['hashtags']
        hashtag_list=hashtags.split(', ')

        for tag in hashtag_list:
            tag = tag.strip()
            new_hashtag=Hashtag.objects.get_or_create(hashtag=tag)
            new_deskresearch.hashtag.add(new_hashtag[0])

        return redirect('deskresearch:detail',new_deskresearch.id)
    return redirect('deskresearch:home') #여기도 deskresearch:home 해줘야함

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    post_hashtag = post_detail.hashtag.all()
    return render(request, 'detail.html', {
        'post': post_detail,
        'hashtag': post_hashtag,
    })

def delete(request, post_id):
    delete_deskresearch = get_object_or_404(Post, pk=post_id)
    delete_deskresearch.delete()
    return redirect('deskresearch:home')

def update_page(request, post_id):
    update_deskresearch = get_object_or_404(Post, pk=post_id)
    hashtags = ', '.join([tag.hashtag for tag in update_deskresearch.hashtag.all()])

    return render(request, 'update.html', {
        'update_deskresearch': update_deskresearch,
        'hashtags': hashtags,
    })

def update_post(request, post_id):
    update_deskresearch=get_object_or_404(Post,pk=post_id)
    update_deskresearch.title=request.POST['title']
    update_deskresearch.content=request.POST['content']
    update_deskresearch.save()

    hashtags=request.POST['hashtags']
    hashtag_list=hashtags.split(', ')

    update_deskresearch.hashtag.clear()

    for tag in hashtag_list:
        tag = tag.strip()
        if tag:
            new_hashtag, created = Hashtag.objects.get_or_create(hashtag=tag)
            update_deskresearch.hashtag.add(new_hashtag)

    return redirect('deskresearch:home')

def add_comment(request, post_id):
    deskresearch = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = Commentform(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post= deskresearch
            comment.save()
            return redirect('deskresearch:detail',post_id)
        
    else:
        form = Commentform()
    return render(request,'add_comment.html',{'form':form})

def detail(request,post_id):
    post_detail = get_object_or_404(Post,pk=post_id)
    post_hashtag = post_detail.hashtag.all()
    return render(request, 'detail.html',{'post':post_detail,'hashtag':post_hashtag})