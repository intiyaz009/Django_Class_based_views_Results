from django.db import models

# Create your models here.
class StudResults(models.Model):
    sname = models.CharField(max_length=40)
    maths = models.IntegerField()
    physics = models.IntegerField()
    biology = models.IntegerField()
    social = models.IntegerField()
    english = models.IntegerField()
    total = models.IntegerField(editable=False)

    def save(self,*args,**kwargs):
        self.total = self.maths+self.physics+self.biology+self.social+self.english
        super().save(*args,**kwargs)