from django.db import models


class Menu(models.Model):
    """Класс меню. Дочерние пункты меню должны ссылатся на родителя (поле паррент)"""
    name = models.CharField(max_length=255, help_text='Name of menu item', null=False, unique=True)
    slug = models.SlugField(verbose_name='Слаг')
    description = models.TextField(verbose_name="Описание")
    parent = models.ForeignKey(to='self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    has_children = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            parent = type(self).objects.get(id=self.parent_id)
            parent.has_children = True
            parent.save()
            super().save(*args, **kwargs)
        except:
            print("Нету родительского меню")
            super().save(*args, **kwargs)





# Create your models here.
