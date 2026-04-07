from django.db import models

class Hashtag(models.Model):
    hashtag = models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag

class Post(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500)
    hashtag = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title
    #def 안에 써야함! 밖에썼더니 제목이 post object(1)이렇게 나옴..ㅎㅎ

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = 'comments',on_delete=models.CASCADE)
    username= models.CharField(max_length=20)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def approve(self):
        self.save()
        
    def __str__(self):
        return self.comment_text

