from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    category = models.CharField(
        max_length=50,
        blank=False,
        choices=(
            ("tv", "TV"),
            ("mobile phone", "Mobile Phone"),
            ("tablet", "Tablet"),
            ("tv accessories", "TV Accessories"),
            ("mobile phone accessories", "Mobile Phone Accessories"),
            ("tablet accessories", "Tablet Accessories")
        )
    )
    rating = models.PositiveSmallIntegerField(
        blank=False,
        choices=(
            (1, "1"),
            (2, "2"),
            (3, "3"),
            (4, "4"),
            (5, "5"),
        )
    )
    image = models.ImageField(
        upload_to='images/', default='../default_category', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
