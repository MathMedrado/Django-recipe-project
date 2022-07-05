from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
    
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f" \"{title}\" is already taken by other article, Please choice another title.")

        return data




class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    
    # def clean_title(self):
    #     cleaned_data = self.cleaned_data #dictornary
    #     print(cleaned_data)
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == "code geass":
    #         raise forms.ValidationError('This tittle is taken.')
    #     print("title: ", title)
    #     return title

    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data', cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == "code geass":
            self.add_error('title', "this title is taken.")
            #raise forms.ValidationError('This title is taken.')
        if  "geass" in content or "geass" in title.lower():
            self.add_error('content', "geass cannot be in the content")
            raise forms.ValidationError('Geass is not allowed')
        return cleaned_data