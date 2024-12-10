import json
import sys
import re
from time import sleep
import requests
from ..utils.graphql import QUERY
from pathlib import Path

with open(
    Path(__file__).parent.parent / "query" / "Followers.graphql",
    "r",
    encoding="utf8",
) as f:
    followers_query_string = f.read()
with open(
    Path(__file__).parent.parent / "query" / "Following.graphql",
    "r",
    encoding="utf8",
) as f:
    following_query_string = f.read()


def get_best_followers():
    followers = []
    following = []
    follower_score = {}

    # 获取followers
    after_cursor = None
    while True:
        result = QUERY.query_use_string(followers_query_string, {"after": after_cursor})
        page_info = result["data"]["viewer"]["followers"]["pageInfo"]
        for node in result["data"]["viewer"]["followers"]["nodes"]:
            followers.append(node["login"])
            follower_score[node["login"]] = (
                node["followers"]["totalCount"] * 0.3
                + node["following"]["totalCount"] * 0.05
                + node["repositoriesContributedTo"]["totalCount"] * 0.35
            )

        if not page_info["hasNextPage"]:
            break
        after_cursor = page_info["endCursor"]

    # 获取following
    after_cursor = None
    while True:
        result = QUERY.query_use_string(following_query_string, {"after": after_cursor})
        page_info = result["data"]["viewer"]["following"]["pageInfo"]

        for node in result["data"]["viewer"]["following"]["nodes"]:
            following.append(node["login"])
            follower_score[node["login"]] = follower_score.get(node["login"], 0)+(
                +sum(
                    [
                        n["stargazers"]["totalCount"]
                        for n in node["repositories"]["nodes"]
                    ]
                )
                * 0.3
            )
        if not page_info["hasNextPage"]:
            break
        after_cursor = page_info["endCursor"]

    print(follower_score)

    mutual_followers = set(followers).intersection(set(following))
    l = list(mutual_followers)
    l.sort(key=lambda x: follower_score[x], reverse=True)
    return l
