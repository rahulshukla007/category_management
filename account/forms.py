from django import forms

class CustomerRegistration(forms.Form):
    firstname    = forms.CharField(min_length = 2, max_length = 50)
    lastname     = forms.CharField(min_length = 5, max_length = 50)
    email        = forms.EmailField()
    password     = forms.CharField(widget = forms.PasswordInput)
    rpassword    = forms.CharField(label = 'Confirm Password' , widget = forms.PasswordInput)
    

    def clean(self):
        cleaned_data = super().clean()
        fpass = self.cleaned_data['password']
        spass = self.cleaned_data['rpassword']

        if fpass != spass:
            raise forms.ValidationError('password not matched')


class Customerlogin(forms.Form):
    email       = forms.EmailField()
    password    = forms.CharField(widget = forms.PasswordInput)
    

class CategoryForm(forms.Form):
    category_name       = forms.CharField(label = 'Category name')

class ProductForm(forms.Form):
    categoty_id         = forms.CharField()
    product_name        = forms.CharField()
    tags                = forms.CharField()
    Description         = forms.CharField()
    Image               = forms.ImageField()


