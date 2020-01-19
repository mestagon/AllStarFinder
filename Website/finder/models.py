from django.db import models

# Create your models here.
class PlayerStats(models.Model):
    ID = models.IntegerField(primary_key = True, unique = True)

    Player = models.CharField(max_length = 32)

    G = models.IntegerField() 

    GS = models.IntegerField()

    MP = models.DecimalField(max_digits = 3, decimal_places = 1)

    FG = models.DecimalField(max_digits = 3, decimal_places = 1)

    FGA = models.DecimalField(max_digits = 3, decimal_places = 1)

    eFG = models.DecimalField(max_digits = 4, decimal_places = 3)

    TRB = models.DecimalField(max_digits = 3, decimal_places = 1)

    AST = models.DecimalField(max_digits = 3, decimal_places = 1)

    STL = models.DecimalField(max_digits = 3, decimal_places = 1)

    BLK = models.DecimalField(max_digits = 3, decimal_places = 1)

    PF = models.DecimalField(max_digits = 2, decimal_places = 1)

    PTS = models.DecimalField(max_digits = 3, decimal_places = 1)

    Prediction = models.BooleanField()

    Actual = models.BooleanField()

    class Meta:
        verbose_name_plural = "PlayerStats"

    def __str__(self):
        return self.Player

class PredictedAllStars(models.Model):
    Player = models.OneToOneField(PlayerStats, on_delete = models.CASCADE, primary_key = True)

    class Meta:
        verbose_name_plural = "PredictedAllStars"

    def __str__(self):
        return (f"{self.Player}")

class ActualAllStars(models.Model):
    Player = models.OneToOneField(PlayerStats, on_delete = models.CASCADE, primary_key = True)

    class Meta:
        verbose_name_plural = "ActualAllStars"

    def __str__(self):
        return (f"{self.Player}")
