from django.contrib import admin
from apps.resources import models

# Register your models here.


class CustomResources(admin.ModelAdmin):
    list_display = (
        'username',
        'user_title',
        'title',
        'link',
        'all_tags',
        'description'
    )

    @admin.display(description='Tags')
    def get_tags(self):
        return ', '.join([tag.name for tag in self.tags.all()])


class CustomRating(admin.ModelAdmin):
    list_display = (
        'username',
        'title',
        'rating',
    )

    def rating(self, obj):
        return obj.rate


class CustomResourcesTag(admin.ModelAdmin):
    list_display = (
        'title',
        'tag',
    )


class CustomReview(admin.ModelAdmin):
    list_display = (
        'username',
        'title',
        'get_body',
    )


@admin.display(description='body')
def get_body(self, obj):
    if len(obj.body) > 50:
        return f"{obj.body[:50]}..."
    else:
        return obj.body


admin.site.register(models.Tag)
admin.site.register(models.Category)
admin.site.register(models.Resources, CustomResources)
admin.site.register(models.Review, CustomReview)
admin.site.register(models.ResourcesTag, CustomResourcesTag)
admin.site.register(models.ResourcesRating, CustomRating)
