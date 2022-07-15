from doc.browser_play import *


class Site(BrowserPlay):
    """
    Classe Site(BrowserPlay) é uma classe que herda de BrowserPlay e
    implementa métodos para fazer “login”, abrir uma guia aleatória e
    continua até o fim do programa.
    """

    def __init__(self):
        """
        Construtor da classe Site
        """
        super().__init__()
        self.path = None
        self.data_dir = None
        self.path_to_extension = None
        self.context = None
        self.page = None

    async def play(self, playwright: Playwright) -> None:
        self.path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        self.data_dir = r'C:\Users\mkdob\AppData\Local\Google\Chrome\User Data'
        '''agentes = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.39 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
        ]'''
        # agente = agentes[random.randint(0, len(agentes) - 1)]
        self.context = await playwright.chromium.launch_persistent_context(
            chromium_sandbox=True,
            headless=True,
            executable_path=self.path,
            base_url="https://addmefast.com/",
            bypass_csp=True,
            user_data_dir=self.data_dir,
            ignore_default_args=["--enable-automation", "--disable-extensions"],
            args=[
                # f"--user-agent={agente}",
                # f"--incognito",
                "--disable-infobars",
                "--disable-notifications",
                "--mute-audio",
                # "--disable-background-networking",
            ],
        )
        self.page = await self.context.new_page()
        self.page.set_default_timeout(60000)
        await self.page.goto("https://addmefast.com/")
        await self.page.wait_for_load_state()
        await self.login(playwright)

    async def captcha(self, playwright: Playwright) -> None:
        pass
        """while captcha == 0: ou seja enquanto o captcha for encontrado ele continuar aguardando o captcha ser
        resolvido, como fiz isso ? porque o captcha é um alerta que aparece na tela, eu preciso aguardar
        atribuir o valor de captcha para 0 para que o loop seja interrompido. quando o captcha for resolvido
        o valor de captcha será atribuído para 1, e o loop será interrompido.
        captch4 = 0
            captch4 = await self.page.locator("text=One more step")
            if captch4.is_visible():
                print('\033[1;31m' + 'CAPTCHA ENCONTRADO!:' + '\033[0;0m', await self.page.title())
                await self.page.wait_for_load_state()
            else:
                print('\033[1;32m' + 'SITE:' + '\033[0;0m', await self.page.title())
                await self.login(playwright)
            while captch4 == 0:
                print('Esperando captcha')
                await self.page.wait_for_timeout(3000)
            else:
                print('zero captchas')
                return await self.login(playwright)
        except Exception as e:
            print(e)"""

    async def login(self, playwright: Playwright) -> None:
        print('\033[1;32m' + 'SITE:' + '\033[0;0m', await self.page.title())

        if await self.page.title() == 'AddMeFast.com - Marketing de mídia social GRATUITO e promoção de cripto':
            await self.page.locator("[placeholder=\"Email\"]").click()
            await self.page.wait_for_timeout(1000)
            await self.page.locator("[placeholder=\"Email\"]").fill("mkdobtc98@gmail.com")
            await self.page.wait_for_timeout(1000)
            await self.page.locator("[placeholder=\"Email\"]").press("Tab")
            await self.page.wait_for_timeout(1000)
            await self.page.locator("[placeholder=\"Palavra-passe\"]").fill("Mike@2406379431")
            await self.page.wait_for_timeout(1000)
            await self.page.locator('input[name="login_button"]').click()
            await self.page.wait_for_load_state()
            print('\033[1;32m' + 'SITE:' + '\033[0;0m', await self.page.title())
            await self.random_tab(playwright)
        else:
            print('Login não encontrado')
            print(await self.page.title())
            await self.random_tab(playwright)

    async def random_tab(self, playwright: Playwright) -> None:
        pass

    async def main(self):
        pass
