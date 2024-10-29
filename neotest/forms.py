from django.forms import ModelForm
from datetime import datetime
from django_neomodel import DjangoNode
from neomodel import StructuredNode, StringProperty, DateTimeProperty, UniqueIdProperty

class Book(DjangoNode):
    uid = UniqueIdProperty()
    title = StringProperty(unique_index=True)
    status = StringProperty(choices=(
            ('Available', 'A'),
            ('On loan', 'L'),
            ('Damaged', 'D'),
        ), default='Available')
    created = DateTimeProperty(default=datetime.now())

    class Meta:
        app_label = 'library'
        
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'status']        