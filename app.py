import flet as ft

from views.FletRouter import Router
from user_controls.app_bar import NavBar


async def main(page: ft.Page):

    page.theme_mode = "dark"
    page.theme = ft.theme.Theme(color_scheme_seed="yellow")

    page.window_width = 561.0
    page.window_height = 692.0

    page.appbar = await NavBar(page, ft)
    myRouter = Router(page, ft)

    page.on_route_change = myRouter.route_change

    await page.add_async(
        myRouter.body
    )

    page.go('/')


ft.app(target=main, assets_dir="assets")
