import re

from django import forms

from Basic_CRUD_exam.main.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'username',
            'email',
            'age',
        )
        age = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        super(CreateProfileForm, self).__init__(*args, **kwargs)
        self.fields['age'].required = False

    def clean_username(self):
        super(CreateProfileForm, self).clean()
        username = self.cleaned_data['username']
        if 2 >= len(username):
            msg = f'Username must contain at least 2 characters.'
            self._errors['username'] = self.error_class([msg])
        if not re.match(r'^[A-Za-z0-9_]*$', username):
            msg = "Ensure this value contains only letters, numbers, and underscore."
            self._errors['username'] = self.error_class([msg])
        return username

    def clean_age(self):
        super(CreateProfileForm, self).clean()
        age = self.cleaned_data['age']
        if not age:
            return age

        if not 0 < age:
            msg = "Age must be positive"
            self._errors['age'] = self.error_class([msg])
        return self.cleaned_data


class CreateAlbumForm(forms.ModelForm):
    CHOICES = (
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    )

    class Meta:
        model = Album
        fields = '__all__'

    genre = forms.ChoiceField(choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super(CreateAlbumForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False

    def clean_album_name(self):
        new_name = self.cleaned_data['album_name']
        album_name = Album.objects.filter(album_name=new_name)
        if album_name:
            self._errors['new_name'] = self.error_class([f"{new_name} - This album already exists"])
        if len(album_name) > 30:
            self._errors['new_name'] = self.error_class(['Name must have less than 30 characters.'])
        return new_name

    def clean_price(self):
        price = self.cleaned_data['price']
        if 0 > price:
            self._errors['price'] = self.error_class(['Price cannot be negative.'])
        return price


class EditAlbumForm(CreateAlbumForm):
    def clean_album_name(self):
        current = self.instance.id
        new_name = self.cleaned_data['album_name']
        album_name = Album.objects.filter(album_name=new_name)
        if not current == album_name[0].id:

            if album_name:
                self._errors['new_name'] = self.error_class([f"{new_name}- This album already exists"])
            if len(album_name) > 30:
                self._errors['new_name'] = self.error_class(['Name must have less than 30 characters.'])
        return new_name


class DeleteAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DeleteAlbumForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
