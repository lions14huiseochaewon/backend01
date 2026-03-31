from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model=Post #기반으로 사용할 모델명 form에 받을 필드명
        fields=['title','content']
        #모델 필드를 모두 사용하는 경우 '__all__'로 작성할 건데 이부분 일단 잘 모르겠으니까 
        
class Commentform(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['username','comment_text']
