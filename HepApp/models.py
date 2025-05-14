from django.db import models

class HepatitisRecord(models.Model):
    AST = models.FloatField()
    ALT = models.FloatField()
    CHE = models.FloatField()
    ALP = models.FloatField()
    BIL = models.FloatField()
    GGT = models.FloatField()
    Age = models.FloatField()
    ALB = models.FloatField()
    prediction_result = models.CharField(max_length=100)  
    def __str__(self):
        return f"Hepatitis Record - Age: {self.Age}, Prediction: {self.prediction_result}"