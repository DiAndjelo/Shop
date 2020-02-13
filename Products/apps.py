from django.apps import AppConfig
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class ProductsConfig(AppConfig):
    name = 'Products'


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
    menu = (
        # ParentItem('Content', children=[
        #     ChildItem(model='demo.country'),
        #     ChildItem(model='demo.continent'),
        #     ChildItem(model='demo.showcase'),
        #     ChildItem('Custom view', url='/admin/custom/'),
        # ], icon='fa fa-leaf'),
        # ParentItem('Integrations', children=[
        #     ChildItem(model='demo.city'),
        # ]),
        ParentItem('Authentication and Authorization', children=[
            ChildItem(model='auth.user'),
            ChildItem('Groups', 'auth.group'),
        ], icon='fa fa-users'),
        ParentItem('Right Side Menu', children=[
            ChildItem('Password change', url='admin:password_change'),
            ChildItem('Open Google', url='http://google.com', target_blank=True),

        ], align_right=True, icon='fa fa-cog'),
    )


