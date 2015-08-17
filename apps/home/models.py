from django.db import models



# Students Modal
class Students(models.Model):
    name = models.CharField(max_length=50,verbose_name="Student Name")
    address = models.TextField(verbose_name="Student Address",null=True,blank=True)


    def __unicode__(self):
        return str(self.id)+ "-"+self.name

    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Students")

