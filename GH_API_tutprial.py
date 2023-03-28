import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI

async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(
            session,
            "AleksandraAleksandrova",
            oauth_token=os.getenv("GH_AUTH")
        )
        response = await gh.post(
            '/repos/AleksandraAleksandrova/github-actions/issues',
            data={
                'title': 'API Issue',
                'body': 'This issue was created using GitHUb API in python script!',
            }
        )
        print(f"Issue created at {response['html_url']}")

asyncio.run(main())

