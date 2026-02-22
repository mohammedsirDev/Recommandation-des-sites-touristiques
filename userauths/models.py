from django.contrib.auth.models import AbstractUser
from django.db import models



USER_TYPE=(
    ("Voyageur","Voyageur"),
    ("administrateur","administrateur")
)
class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=120, null=True,blank=True)
    user_type=models.CharField(max_length=50, choices=USER_TYPE, null=True,blank=True, default=True)
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS =["username"]

    def __str__(self):
        return self.username
   
    def save(self,*args,**kwargs):
        email_username ,_ = self.email.split("@")
        if self.username =="" or self.username== None:
            self.username=email_username
        super(User,self).save(*args,**kwargs)

