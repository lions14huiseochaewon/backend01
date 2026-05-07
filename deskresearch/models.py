from django.db import models

RENTAL_AVAILABLITY = (
    (1, "AVAILABLE"),
    (2, "UNAVAILABLE"),

)

RENTAL_RECORD=(
    (1, "RENTED"),
    (2, "RETURNED"),
    (3, "OVERDUE"),
)


class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    rental = models.IntegerField(choices=RENTAL_AVAILABLITY,null=True, blank=True)

    def __str__(self):
        return self.title

class Record(models.Model):
    post=models.ForeignKey(Post,related_name='records', on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    record_text=models.IntegerField(choices=RENTAL_RECORD,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.get_record_text_display()}"