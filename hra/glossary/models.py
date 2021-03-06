from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet

from hra.utils.models import ListingFields, SocialFields


@register_snippet
class GlossaryTerm(index.Indexed, models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()
    is_noun = models.BooleanField("Noun", default=False)

    panels = [
        FieldPanel('name', classname='full title'),
        FieldPanel('description', classname='full'),
        FieldPanel('is_noun'),
    ]

    search_fields = [
        index.SearchField('name', partial_match=True, boost=10),
        index.SearchField('description', partial_match=True),
    ]

    def __str__(self):
        return self.name


class GlossaryIndex(Page, SocialFields, ListingFields):
    promote_panels = (
        Page.promote_panels +
        SocialFields.promote_panels +
        ListingFields.promote_panels
    )
