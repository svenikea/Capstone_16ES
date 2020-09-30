from django.db import models

# Create your models here.


class CPU(models.Model):
    name = models.CharField(max_length=15)
    platform = models.CharField(max_length=15)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'CPU'
        verbose_name = 'CPU'
        verbose_name_plural = 'CPU'

    def __str__(self):
        return self.platform


class x86(models.Model):
    family = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    memory = models.DecimalField(max_digits=4, decimal_places=0)
    description = models.TextField()
    platform = models.ForeignKey(CPU, on_delete=models.CASCADE)
    quanity = models.DecimalField(max_digits=4, decimal_places=0)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'x86'
        verbose_name = 'x86'
        verbose_name_plural = 'x86'

    def __str__(self):
        return self.name


class arm(models.Model):
    family = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    memory = models.DecimalField(max_digits=4, decimal_places=0)
    description = models.TextField()
    platform = models.ForeignKey(CPU, on_delete=models.CASCADE)
    quanity = models.DecimalField(max_digits=4, decimal_places=0)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'arm'
        verbose_name = 'arm'
        verbose_name_plural = 'arm'

    def __str__(self):
        return self.name


class Language(models.Model):
    language = models.CharField(max_length=10)

    def __str__(self):
        return self.language

    class Meta:
        db_table = 'language'
        verbose_name = 'language'
        verbose_name_plural = 'languages'


class Framework(models.Model):
    framework = models.CharField(max_length=10)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.framework

    class Meta:
        db_table = 'Framework'
        verbose_name = 'Framework'
        verbose_name_plural = 'Frameworks'


class Shoes_Brand(models.Model):
    brand = models.CharField(max_length=15)

    class Meta:
        db_table = 'Brand'
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.brand


class Shoe(models.Model):
    name = models.CharField(max_length=15)
    foot_size = models.DecimalField(max_digits=3, decimal_places=1)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    quanity = models.DecimalField(max_digits=3, decimal_places=0)
    available = models.BooleanField(default=False)
    brand = models.ManyToManyField(Shoes_Brand, related_name="Shoes_Brand")

    def __str__(self):
        return self.name
