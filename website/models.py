from pyexpat import model
from django.db import models, transaction
from datetime import datetime
from .utils import weeksSinceStart

class UserInfoManager(models.Manager):
    def create_user_info(self, e):
        new = self.create(email=e)
        return new

# Create your models here.
class UserInfo(models.Model):
    email = models.CharField(max_length=255)#user email
    anonymous = models.BooleanField(default=False)#does user want to be anonymous
    assets = models.TextField(default="", blank=True)#string of assets
    cash = models.DecimalField(decimal_places=50, max_digits=500, default=weeksSinceStart()*10000)#current amount of cash
    added_cash = models.DecimalField(decimal_places=50, max_digits=500, default=weeksSinceStart()*10000)#amount of cash given
    leaderboard_portfolio_value = models.DecimalField(decimal_places=50, max_digits=500, default=weeksSinceStart()*10000)#last updated portfolio value
    price_history = models.TextField(default=str(weeksSinceStart()*10000))
    objects = UserInfoManager()

    def get_queryset(self):
        return self.__class__.objects.filter(id=self.id)

    @transaction.atomic()
    def addPriceHistory(self, s):
        obj = self.get_queryset().select_for_update().get()
        hist = obj.price_history.split(";")
        if(len(hist) == 50):
            hist.append(str(s))
            obj.price_history = ";".join(hist[1:])
        else:
            obj.price_history += ";" + str(s)
            obj.save()

    @transaction.atomic()
    def updateAnonymous(self, b):
        obj = self.get_queryset().select_for_update().get()
        obj.anonymous = b
        obj.save()
    
    @transaction.atomic()
    def updateAssets(self, s):
        obj = self.get_queryset().select_for_update().get()
        obj.assets = s
        obj.save()
    
    @transaction.atomic()
    def updateCash(self, a):
        obj = self.get_queryset().select_for_update().get()
        obj.cash = a
        obj.save()
    
    @transaction.atomic()
    def addCash(self, a):
        obj = self.get_queryset().select_for_update().get()
        obj.cash += a
        obj.save()
    
    @transaction.atomic()
    def updateAddedCash(self, a):
        obj = self.get_queryset().select_for_update().get()
        obj.added_cash = a
        obj.save()

    @transaction.atomic()
    def addAddedCash(self, a):
        obj = self.get_queryset().select_for_update().get()
        obj.added_cash += a
        obj.save()
    
    @transaction.atomic()
    def updateLeaderboardPortfolioValue(self, a):
        obj = self.get_queryset().select_for_update().get()
        obj.leaderboard_portfolio_value = a
        obj.save()