from django.db import models

class Diary(models.Model):
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    learning_time = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)

    def __str__(self):
        return self.text
