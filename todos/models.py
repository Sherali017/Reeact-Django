from django.db import models

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'todo'
        verbose_name_plural = 'todos'
