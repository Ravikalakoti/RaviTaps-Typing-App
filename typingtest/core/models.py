from django.db import models

class TypingResult(models.Model):
    username = models.CharField(max_length=100)
    wpm = models.FloatField()
    accuracy = models.FloatField()
    time_taken = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    test_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.wpm:.2f} WPM"
