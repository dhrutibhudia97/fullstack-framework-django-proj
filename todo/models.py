from django.db import models
# we have inherited class functionality from models class...

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    #null=false prevents items without a name being created.
    # blank=false makes the field required on forms.   
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
        #returns item classes name attribute (name put into form)



