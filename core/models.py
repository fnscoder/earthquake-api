from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "cities"


class SearchResult(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="results")
    start_date = models.DateField()
    end_date = models.DateField()
    earthquake_date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.city} - {self.earthquake_date} - {self.title}"

    class Meta:
        verbose_name = "Search result"
        verbose_name_plural = "Search results"
