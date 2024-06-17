import flet as ft


async def NavBar(page, ft=ft):

    NavBar = ft.AppBar(
        leading=ft.Icon(ft.icons.PLAY_CIRCLE),
        leading_width=40,
        title=ft.Text("WiseYT"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.HOME, tooltip='Home',
                          on_click=lambda _: page.go('/')),
            ft.IconButton(ft.icons.SETTINGS_ROUNDED, tooltip='Settings',
                          on_click=lambda _: page.go('/settings')),
            ft.IconButton(ft.icons.PERSON_ROUNDED, tooltip='About',
                          on_click=lambda _: page.go('/about')),
        ]
    )

    return NavBar
