from doc.tab import *


class Popup(Tab):
    """
    Classe Popup que herda de Tab. E implementa o random_tab, popup_ytb_like
    ira gerenciar os popups das guias
    """

    def __init__(self):
        """
        Construtor da classe Popup
        """
        super().__init__()
        self.data_dir = None
        self.path_to_extension = None
        self.browser = None
        self.context = None
        self.page = None
        self.bot = None

    async def main(self):
        try:
            async with async_playwright() as playwright:
                await self.play(playwright)
                await self.random_tab(playwright)
                await self.close()
        except Exception as ee:
            print(ee)
            return await self.bot.main()
        finally:
            print('\033[1;31m' + 'ACABOU O PROGRAMA' + '\033[0;0m')
            return await self.main()

    async def popup_ytb_like(self, playwright: Playwright) -> None:
        try:
            async with self.page.expect_navigation():
                async with self.page.expect_popup() as self.popup_info:
                    await self.page.locator("#form1 a >> text=Like").click(delay=random.randint(500, 1000))
                    print('\033[1;32m' + 'CLIQUEI NO POPUP YOUTUBE LIKE' + '\033[0;0m')
                    page2 = await self.popup_info.value
                    await page2.locator(
                        "ytd-toggle-button-renderer.style-scope:nth-child(1) > a:nth-child(1) > yt-icon-button:nth-child(1) > button:nth-child(1) > yt-icon:nth-child(1)").click(
                        delay=random.randint(500, 1000))
                    print('\033[1;32m' + 'LIKE REALIZADO COM SUCESSO' + '\033[0;0m')
                    await page2.wait_for_timeout(random.randint(5000, 8000))
                    await page2.close()
                    print('\033[1;32m' + 'FECHOU O POPUP YOUTUBE LIKE' + '\033[0;0m')
                    await self.page.wait_for_timeout(random.randint(9000, 15000))
                    if await self.page.locator("#form1 a >> text=Like").is_visible():
                        if await page2.is_closed():
                            print('\033[1;31m' + 'OPS QUASE ESQUEÇO DE FECHAR!' + '\033[0;0m')
                            await page2.close()
                            return await self.popup_ytb_like(playwright)
                        else:
                            print('\033[1;31m' + 'OPS QUASE ESQUEÇO DE FECHAR!' + '\033[0;0m')
                            await page2.close()
                            return await self.popup_ytb_like(playwright)
                    if not await self.page.locator("#form1 a >> text=Like").is_visible():
                        print('\033[1;32m' + 'LIKE REALIZADO COM SUCESSO' + '\033[0;0m')
                        if await page2.is_closed():
                            return await self.random_tab(playwright)
                        else:
                            await page2.close()
                            return await self.random_tab(playwright)
        except Exception as ee:
            print('\033[1;31m' + 'ACABARAM OS POPUPS !!!' + '\033[0;0m')
            print(ee)
            return await self.random_tab(playwright)

    async def popup_ytb_subscribe(self, playwright: Playwright) -> None:
        try:
            async with self.page.expect_navigation():
                async with self.page.expect_popup() as self.popup_info:
                    await self.page.locator("#form1 a >> text=Subscribe").click(delay=random.randint(500, 1000))
                    print('\033[1;32m' + 'CLIQUEI NO POPUP YOUTUBE SUBSCRIBE' + '\033[0;0m')
                    page2 = await self.popup_info.value
                    await page2.locator(
                        "xpath=/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[2]/div/div[1]/div/div[2]/div[4]/ytd-subscribe-button-renderer").click(
                        delay=random.randint(500, 1000))
                    print('\033[1;32m' + 'SUBSCRIBE REALIZADO COM SUCESSO' + '\033[0;0m')
                    await page2.wait_for_timeout(random.randint(5000, 8000))
                    await page2.close()
                    print('\033[1;32m' + 'FECHOU O POPUP YOUTUBE SUBSCRIBE' + '\033[0;0m')
                    await self.page.wait_for_timeout(random.randint(9000, 15000))
                    if await self.page.locator("#form1 a >> text=Subscribe").is_visible():
                        if await page2.is_closed():
                            return await self.popup_ytb_subscribe(playwright)
                        else:
                            print('\033[1;31m' + 'OPS QUASE ESQUEÇO DE FECHAR!' + '\033[0;0m')
                            await page2.close()
                            return await self.popup_ytb_subscribe(playwright)
                    if not await self.page.locator("#form1 a >> text=Subscribe").is_visible():
                        print('\033[1;32m' + 'SUBSCRIBE REALIZADOS COM SUCESSO' + '\033[0;0m')
                        if await page2.is_closed():
                            await page2.close()
                            return await self.random_tab(playwright)
                        else:
                            await page2.close()
                            return await self.random_tab(playwright)
        except Exception as ee:
            print('\033[1;31m' + 'ACABARAM OS POPUPS !!!' + '\033[0;0m')
            print(ee)
            return await self.random_tab(playwright)


if __name__ == "__main__":
    while True:
        bot = Popup()
        asyncio.run(bot.main())
        asyncio.sleep(random.randint(3, 5))
        print('CONTINUE...')
        continue
