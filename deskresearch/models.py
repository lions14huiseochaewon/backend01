from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.title
    #def 안에 써야함! 밖에썼더니 제목이 post object(1)이렇게 나옴..ㅎㅎ

