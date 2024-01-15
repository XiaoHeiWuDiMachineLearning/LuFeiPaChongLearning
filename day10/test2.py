import asyncio
from pyppeteer import launch
from lxml import etree
async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    # 进入链接
    await page.goto('https://www.baidu.com/')
    # 输入搜索项
    await page.type('#kw', '大黑驴', {'delay':1000})
    # 点击
    await page.click('#su')
    # 等待
    await asyncio.sleep(3)
    # 获取元素
    alists = await page.querySelectorAll('#content_left > div >* a')
    print(alists)
    await alists[3].click()
    # 等待
    await asyncio.sleep(3)
    # 关闭界面
    await page.close()

if __name__ == '__main__':
    c = main()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(c)
