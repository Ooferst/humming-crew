from django.forms import ModelForm
from main.models import Products
from django.utils.html import strip_tags

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ["name", "description", "category", "thumbnail", "is_featured", "price", "size", "stocks", ]
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_content(self):
        content = self.cleaned_data["content"]
        return strip_tags(content)
    