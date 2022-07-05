from django.db import models as m


class Task(m.Model):
    title = m.CharField(max_length=100)
    description = m.TextField(default='')
    deadline = m.DateTimeField()
    done = m.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['id']
