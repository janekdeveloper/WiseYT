import flet as ft


def AboutView(page):

    content = ft.Column(

        [
            ft.Row(
                [
                    ft.Image(src=f"/logo.png", width=30),
                    ft.Text("About", size=30),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    ft.Text(
                        "Author: JanekDev",
                        selectable=True,
                        size=30)
                ],
            ),
            ft.Row(
                [
                    ft.Text(
                        "GitHub: https://github.com/janekdeveloper",
                        selectable=True,
                        size=30)
                ]
            ),
            ft.Row(
                [
                    ft.Text(
                        "Source Code: https://github.com/janekdeveloper/wiseyt",
                        selectable=True,
                        size=30)
                ]
            )

        ]
    )

    return content
