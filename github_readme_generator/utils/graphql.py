from csv import Error
import requests
import json
from pathlib import Path
import os

class GraphqlQuery:
    def __init__(self, token):
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        self.count = 0
        self.get_rate_limit()
    def get_rate_limit(self):
        print("Github API token remain: ", self.query_use_file("RateLimit"))
    def query_use_file(self, graphqlFile: str):
        # 构建GraphQL查询
        with open(
            Path(__file__).parent.parent / "query" / (graphqlFile + ".graphql"),
            "r",
            encoding="utf8",
        ) as f:
            q = f.read()
        # 发送POST请求到GitHub的GraphQL API端点
        response = requests.post(
            "https://api.github.com/graphql", json={"query": q}, headers=self.headers
        )

        # 检查响应状态码并打印结果
        if response.status_code == 200:
            self.count += 1
            data = response.json()
            return data
        raise Error(
            f"Query failed to run by returning code of {response.status_code}. {response.text}"
        )
    def query_use_string(self, q: str, v=None):
        response = requests.post(
            "https://api.github.com/graphql", json={"query": q,"variables": v}, headers=self.headers
        )

        # 检查响应状态码并打印结果
        if response.status_code == 200:
            self.count += 1
            data = response.json()
            return data
        raise Error(
            f"Query failed to run by returning code of {response.status_code}. {response.text}"
        )

QUERY = GraphqlQuery(os.getenv("GITHUB_TOKEN"))
