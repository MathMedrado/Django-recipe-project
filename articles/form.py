from distutils.command.clean import clean
from django import forms

class ArticleForm(forms.Form):
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
        if title.lower().strip() == "code geass":
            self.add_error('title', "this title is taken.")
            #raise forms.ValidationError('This title is taken.')
        return cleaned_data