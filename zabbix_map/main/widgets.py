__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

from zabbix_map import settings
from jinja2 import Template

WIDGETS_TEMPLATE_DIR = "%s/main/templates/widgets/" % settings.BASE_DIR


def render(data, template):
    template = Template(open(template, 'rt').read())
    return template.render(data=data)


def switch(data, template=WIDGETS_TEMPLATE_DIR + 'switch.html'):
    return {
        "caption": data.zabbix_name,
        "text": render(data, template),
    }