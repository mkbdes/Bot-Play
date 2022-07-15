"""
Esse script é um exemplo de como criar uma classe BrowserPlay
que é uma classe que herdará de PlaywrightAsync e passará a herança
para a futura (classe) Site que será criada posteriormente.

BrowserPlay terá apenas um método play que será chamado pelo
método play async da classe PlaywrightAsync.
"""


try:
    import os
    import sys
    import random
    import inspect
    import asyncio
    from playwright.async_api import async_playwright, Playwright
    print(sys.version.upper())
    print("\n")
except ImportError as e:
    print(f'Erro ao importar: {e}')
    sys.exit(1)

CURRENT_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


class BrowserPlay(object):
    """
    Um simples navegador que ira receber o
    é o método que será chamado pelo método play async da classe PlaywrightAsync.
    """
    def __init__(self):
        """
        Construtor da classe BrowserPlay
        """
        self.context = None
        self.page = None

    async def __aenter__(self):
        return self

    async def close(self):
        await self.page.close()
        await self.context.close()

    async def play(self, playwright: Playwright) -> None:
        pass

    async def login(self, playwright: Playwright) -> None:
        pass

    async def main(self):
        pass

    async def captcha(self, playwright: Playwright):
        pass


'''if __name__ == "__main__":
    bot = BrowserPlay()
    asyncio.run(bot.main())
    print("Done")
    sys.exit(0)'''

'''
await page.click("button") # click triggers navigation.
await page.wait_for_load_state() # the promise resolves after "load" event.
async with page.expect_popup() as page_info:
    await page.click("button") # click triggers a popup.
popup = await page_info.value
 # Following resolves after "domcontentloaded" event.
await popup.wait_for_load_state("domcontentloaded")
print(await popup.title()) # popup is ready to use.
Shortcut for main frame's frame.wait_for_load_state().

'''

'''async def main():
    async with async_playwright() as playwright: 
        browser = await playwright.chromium.launch(
            headless=False,  # Show the browser
            args=['--no-sandbox', '--disable-setuid-sandbox'],  # Disable sandbox
        )   
        page = await browser.new_page()
        await page.goto('https://books.toscrape.com/')
        # Data Extraction Code Here
        await page.wait_for_load_state('load')  # Wait for 1 second
        await browser.close()
        
if __name__ == '__main__':
    asyncio.run(main())

async def run(playwright):
    webkit = playwright.webkit
    browser = await webkit.launch(headless=False)
    page = await browser.new_page()
    await page.goto('https://books.toscrape.com/')
    await page.evaluate("window.x = 0; setTimeout(() => { window.x = 100 }, 1000);")
    await page.wait_for_function("() => window.x > 0")
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())'''
