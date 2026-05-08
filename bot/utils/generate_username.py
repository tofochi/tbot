import random as rnd
import string
import httpx
import asyncio


def generate_username(length: int) -> str:
    letters = string.ascii_letters
    return ''.join(rnd.choice(letters) for _ in range(length))


async def check_username(username: str) -> bool:
    url = f"https://t.me/{username}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=10.0, follow_redirects=True)
            html = response.text.lower()

            return "tgme_page" in html and "tgme_page_title" in html
        except:
            return False


async def main():
    while True:
        username = generate_username(5)
        is_taken = await check_username(username)

        if not is_taken:
            print(username)
            return username

asyncio.run(main())