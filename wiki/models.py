# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, InlinePanel)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from .umodels import RelatedLink


# ------------------------主页-------------------------
class WikiHome(Page):
    logoname = models.CharField(
        max_length=255,
        help_text=u"显示在左上角的网页名称"
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=u"大幅背景图"
    )
    intro = models.TextField(
        blank=True,
        help_text=u"下方简单口号"
    )

    content_panels = Page.content_panels + [
        FieldPanel('logoname'),
        InlinePanel('toplinks', label="顶部右侧链接"),
        ImageChooserPanel('image'),
        FieldPanel('intro', classname="full"),
        InlinePanel('little_intros', label="下方一排推广简述"),
    ]


class WikiHomeTopLink(Orderable, RelatedLink):
    page = ParentalKey('wiki.WikiHome', related_name='toplinks')


class WikiHomeLittleIntros(Orderable):
    page = ParentalKey(WikiHome, related_name='little_intros')
    fa_name = models.CharField(blank=True, max_length=250,
                               help_text=u'''FontAwesome图标类名
                               - 参考fontawesome.io/icons/''')
    title = models.CharField(blank=True, max_length=250,
                             help_text=u"小标题")
    caption = models.CharField(blank=True, max_length=1000,
                               help_text=u"简述")

    panels = [
        FieldPanel('fa_name'),
        FieldPanel('title'),
        FieldPanel('caption'),
    ]
