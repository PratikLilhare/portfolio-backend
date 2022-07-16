from typing import Generator
from fastapi import HTTPException, Request, status
import aiohttp
from app.config import settings
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_redis(request: Request) -> Generator:
    yield request.app.state.redis


class Github:
    token = settings.GITHUB_TOKEN

    def __init__(self):
        self.headers = {'Authorization': "Token "+self.token}
        self.owner = settings.GITHUB_USER

    async def get_avatar_url(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://api.github.com/users/{self.owner}",
                headers=self.headers
            ) as resp:
                response = await resp.json()

            return response["avatar_url"]

    async def get_projects(self):
        async with aiohttp.ClientSession() as session:
            repositories = []

            async with session.get(
                "https://api.github.com/user/starred",
                headers=self.headers
            ) as resp:
                response = await resp.json()
                for repository in response:
                    try:
                        languages = await self.get_languages_projects(
                            repository["languages_url"]
                        )
                        print(languages)
                        image_url = f"https://raw.githubusercontent.com/{repository['owner']['login']}/{repository['name']}/{repository['default_branch']}/example.png"
                        repositories.append({
                            "name": repository['name'],
                            "link": repository["svn_url"],
                            "languages": languages,
                            "image_url": image_url,
                            "description": repository["description"],
                        })
                    except Exception as e:
                        raise HTTPException(
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=str(e)
                        )

        return repositories

    async def get_languages_projects(self, url):
        async with aiohttp.ClientSession() as session:
            languages = []

            async with session.get(url, headers=self.headers) as resp:
                response = await resp.json()
                languages = [key for key in response.keys()]

            return languages
