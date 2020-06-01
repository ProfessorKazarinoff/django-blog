# posts/templatetags/markdown_extras.py

from django import template
from django.template.defaultfilters import stringfilter

import markdown as md

register = template.Library()


@register.filter
@stringfilter
def markdown(value):
    return md.markdown(
        value,
        extensions=[
            "markdown.extensions.fenced_code",
            "markdown.extensions.tables",
            "markdown.extensions.admonition",
            "markdown.extensions.codehilite",
            "markdown.extensions.toc",
        ],
    )
