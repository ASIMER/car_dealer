from django.db import models


class Car(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_PUBLISHED = 'published'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
            (STATUS_PENDING, "Pending"),
            (STATUS_PUBLISHED, "Published"),
            (STATUS_SOLD, "Sold"),
            (STATUS_ARCHIVED, "Archived"),
            )

    views = models.PositiveIntegerField(default=0, editable=False)
    slug = models.SlugField(max_length=75)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_PENDING, blank=True)
    dealer = models.ForeignKey('Dealer', on_delete=models.CASCADE, related_name='cars')

    model = models.ForeignKey(to='CarModel', on_delete=models.SET_NULL, null=True)
    extra_title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Title second part'))

    # other fields ...
    #

    @property
    def auto_title(self):
        return f'{self.model.brand} {self.extra_title or ""}'  # do not show None

    def __str__(self):
        return self.auto_title

    class Meta:
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')

        indexes = [
                Index(fields=['status', ])
                ]
