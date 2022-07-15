from doc.site_play import *
from doc.browser_play import *


class Tab(Site):
    """
    Classe Tab que herda de Site e implementa o random_tab, play, “login”, close e popup_ytb_like
    ira gerenciar random_tab e provavelmente os Popups
    """
    def __init__(self):
        super().__init__()
        self.data_dir = None
        self.path_to_extension = None
        self.context = None
        self.page = None

    async def random_tab(self, playwright: Playwright) -> None:
        try:
            tabs = {
                "tab_youtube_likes": self.page.locator("body > div.contentnew > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(30)", has_text="YouTube Likes"),
                "tab_youtube_subscribers": self.page.locator("a", has_text="YouTube Subscribe"),
                # "tab_twitter_likes": page.locator("a", has_text="Twitter Likes"),
                # "tab_twitter_retweet": page.locator("a", has_text="Twitter Retweets"),
                # "tab_tiktok_likes": page.locator("a", has_text="TikTok Video Likes"),
                # "tab_reddit_upvotes": page.locator("a", has_text="Reddit Upvotes"),
                # "tab_soundcloud_like": page.locator("a", has_text="SoundCloud Likes"),
                # "tab_facebook_post_share": page.locator("a", has_text="FB Post Share"),
                # "tab_instagram_like": page.locator("a", has_text="Instagram Likes")
                # "point_balance": self.page.locator("points_count", has_text="points"),
            }
            random.choice(list(tabs.keys()))
            await random.choice(list(tabs.values())).click(delay=random.randint(500, 1000))
            print('\033[1;32m' + 'CLIQUEI NA TAB' + '\033[0;0m', await self.page.title())
            await self.page.wait_for_timeout(random.randint(5000, 8000))
            if self.page.url == 'https://addmefast.com/free_points/youtube_likes':
                await self.page.locator('//*[@id="toppointsbalance"]').all_inner_texts()
                print('\033[1;32m' + 'POINTS' + '\033[0;0m', await self.page.locator('//*[@id="toppointsbalance"]').all_inner_texts())
                print('\033[1;32m' + 'SITE:'+'\033[0;0m', await self.page.title())
                return await self.popup_ytb_like(playwright)
            elif self.page.url == 'https://addmefast.com/free_points/youtube_subscribe':
                await self.page.locator('//*[@id="toppointsbalance"]').all_inner_texts()
                print('\033[1;32m' + 'POINTS:'+'\033[0;0m', await self.page.locator('//*[@id="toppointsbalance"]').all_inner_texts())
                print('\033[1;32m' + 'SITE:'+'\033[0;0m', await self.page.title())
                return await self.popup_ytb_subscribe(playwright)
        except Exception as ee:
            print(f'Erro ao random_tab: {ee}')
            if await self.page.locator("text=One more step").is_visible():
                await self.captcha(playwright)
            else:
                await self.random_tab(playwright)

    async def popup_ytb_like(self, playwright: Playwright) -> None:
        pass

    async def popup_ytb_subscribe(self, playwright: Playwright) -> None:
        pass

    async def main(self):
        pass
