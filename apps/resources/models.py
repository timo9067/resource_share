from django.db import models
# from apps.user.models import User

from django.contrib.postgres.fields import ArrayField


from apps.core.models import CreatedModifiedDateTimeBase
from apps.resources import validators

# Create your models here.


class Tag(CreatedModifiedDateTimeBase):
    # id = None # If you don't want the default id to be created
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Category(CreatedModifiedDateTimeBase):
    cat = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.cat


class Resources(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey(
        "user.User", null=True, on_delete=models.SET_NULL)
    cat_id = models.ForeignKey(
        "resources.Category", default=1, on_delete=models.SET_DEFAULT)

    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=500)
    tags = models.ManyToManyField("resources.Tag", through="ResourcesTag")
    # rate = ArrayField(base_field=models.IntegerField())  # INT ARRAY

    class Meta:
        verbose_name_plural = 'Resourses'

    def __str__(self) -> str:
        return f"{self.user_id.username} - {self.title}"

    @property
    def username(self):
        return self.user_id.username

    def user_title(self):
        return self.user_id.title

    def all_tags(self):
        return ', '.join([tag.name for tag in self.tags.all()])


class ResourcesTag(CreatedModifiedDateTimeBase):
    modified_at = None
    resources_id = models.ForeignKey(
        "resources.Resources", on_delete=models.CASCADE)
    tag_id = models.ForeignKey("resources.Tag", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                'resources_id',
                'tag_id',
                name='resource_tag_unique',
                violation_error_message='Tag already exists for resource',
            )
        ]

    def title(self):
        return self.resources_id.title

    def tag(self):
        return self.tag_id.name

    def __str__(self) -> str:
        return f'{self.resources_id.title}: {self.tag_id}'


class Review(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey(
        "user.User", null=True, on_delete=models.SET_NULL)
    resources_id = models.ForeignKey(
        "resources.Resources", on_delete=models.CASCADE)
    body = models.TextField(max_length=100)

    def __str__(self) -> str:
        return f"{self.user_id.username} - {self.resources_id.title}"

    def username(self):
        return self.user_id.username

    def title(self):
        return self.resources_id.title

    def get_body(self):
        return self.body[:50]


class ResourcesRating(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey(
        'user.User', null=True, on_delete=models.SET_NULL)
    resources_id = models.ForeignKey(
        'resources.Resources', on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[validators.check_rating_range])

    def username(self):
        return self.user_id.username

    def title(self):
        return self.resources_id.title

    def __str__(self) -> str:
        return f'{self.user_id.username}:{self.rate}'
