# import flet as ft

# views
from views.index_view import IndexView
from views.settings_view import SettingsView
from views.about_view import AboutView


class Router:

    def __init__(self, page, ft):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": IndexView(page),
            "/settings": SettingsView(page),
            "/about": AboutView(page)
        }
        self.body = ft.Container(content=self.routes['/'])

    async def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()
