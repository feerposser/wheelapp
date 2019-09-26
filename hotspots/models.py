from django.db import models


class ModelCategories(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categoria"

    def __str__(self):
        return self.name


class ModelHotspots(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(ModelCategories, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    lat = models.FloatField()
    lng = models.FloatField()
    user = models.CharField(default="Herbert Vianna", max_length=100)

    class Meta:
        verbose_name = "Hostpot"
        verbose_name_plural = "Hotspots"

    def __str__(self):
        return self.title
