from django.db import models


# Create your models here.


class var_key(models.Model):
    customer_name = models.CharField(max_length=32)
    tag = models.CharField(max_length=32, blank=True, null=True)
    keywords_insearch = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = u"标记信息"

    def __str__(self):
        return self.customer_name


class szgbModels(models.Model):
    site = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    updated_time = models.DateTimeField(max_length=32)

    status = models.BooleanField(max_length=32)

    class Meta:
        verbose_name_plural = u"前端展示信息"
