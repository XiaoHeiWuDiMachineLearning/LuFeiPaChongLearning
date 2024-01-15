import asyncio
from pyppeteer import launch
from lxml import etree

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.setViewport({'width':1366, 'height':800})
    # 执行js代码

    await page.goto('https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/')
    # await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
    # 规避检测
    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator, { webdriver:{ get: () => false } }) }'''
    )
    page_text = await page.content()
    tree = etree.HTML(page_text)
    await asyncio.sleep(10)

    await browser.close()

if __name__ == '__main__':
    c = main()
    asyncio.get_event_loop().run_until_complete(c)