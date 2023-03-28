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
        # creating new Issue 
        """
        response = await gh.post(
            '/repos/AleksandraAleksandrova/github-actions/issues',
            data={
                'title': 'API Issue',
                'body': 'This issue was created using GitHUb API in python script!',
            }
        )
        print(f"Issue created at {response['html_url']}")
        """
        # Adding a comment to an issue
        """
        response = await gh.post(
            "/repos/AleksandraAleksandrova/github-actions/issues/8/comments",
            data={"body": "This comment was posted via GitHub API!",},
        )
        print(f"Commented on the issue!")
        """
        # CLosing an issue
        """
        await gh.patch(
            '/repos/AleksandraAleksandrova/github-actions/issues/8',
            data={'state': 'closed'},
        )
        print(f"Closed the issue successfully!")
        """
        # Reacting on an issue (issue should be Open to do this)
        response = await gh.post(
            "/repos/AleksandraAleksandrova/github-actions/issues/7/reactions",
            data={"content": "hooray"},
            accept="application/vnd.github.squirrel-girl-preview+json",
        )
        print(f"Reacted on the issue!")
        

asyncio.run(main())
