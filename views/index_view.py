import flet as ft
import asyncio
from youtube_dl import YoutubeDL

links = []


def extractYt():

    youtube_dl_opts = {'ignoreerrors': True, 'quiet': True}

    with YoutubeDL(youtube_dl_opts) as ydl:
        print(links)
        link_index = len(links) - 1
        info_video = ydl.extract_info(
            links[link_index],
            download=True)

    return info_video.get("id", None)


def IndexView(page):

    async def button_clicked(e):
        loop = asyncio.get_running_loop()
        link = f"{url_field.value}"
        links.append(link)
        result = await loop.run_in_executor(None, extractYt)

        await page.update_async()

    url_field = ft.TextField(expand=True)
    content = ft.Column(

        [
            ft.Row(
                [
                    ft.Text("Enter link", size=50),
                    url_field,
                    ft.ElevatedButton(text="Download", bgcolor='yellow400', color='yellow900', on_click=button_clicked)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    ft.Image(src=f"/mascot/yuki2.jpg",
                             width=540,
                             border_radius=5,
                             filter_quality=ft.FilterQuality.HIGH,
                             ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
        ],
        expand=True

    )

    return content
