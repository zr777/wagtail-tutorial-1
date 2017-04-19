from wagtail.wagtailsnippets.models import register_snippet
from django.db import models
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


@register_snippet
class FooterText(models.Model):

    body = RichTextField()

    panels = [
        FieldPanel('body'),
    ]

    def __str__(self):
        return u"页面最底部文本 - 限单条"

    class Meta:
        verbose_name_plural = u'页面最底部文本'
