from ..utils.graphql import QUERY
from urllib.parse import quote, urlencode


class Repo():
    def __init__(self, config):
        config = config["stats"]
        # need config.stats to generate repo card
        data = Repo.__query_repos_api()["data"]["viewer"]
        self.latest_update_repo = Repo.__generate_latest_update_repo(
            config["github-readme-stats"], data["latestUpdateRepo"]["nodes"]
        )
        self.starred_repo = Repo.__generate_starred_repo(
            config["github-readme-stats"], data["starredRepositories"]["nodes"]
        )
        self.most_starred_repo = Repo.__generate_most_starred_repo(
            config["github-readme-stats"], data["mostStarRepo"]["nodes"]
        )

    @staticmethod
    def __query_repos_api():
        print(QUERY.headers)
        data = QUERY.query_use_file("Repos")
        return data

    @staticmethod
    def __generate_link(config, owner, repo):
        c = config["common_options"].copy()
        server = config["server"]
        c["username"] = owner
        c["repo"] = repo
        c["description_lines_count"] = config.get("repo-card",{}).get("description_lines_count",3)
        return server + "/api/pin?" + urlencode(c)

    @staticmethod
    def __generate_latest_update_repo(c, d):
        output = []
        for i in d:
            if i["owner"]["login"] == i["name"]: # skip personal profile repo
                continue
            output.append(
                f'<a href="{i["url"]}"><img align="center" src="{Repo.__generate_link(c, i["owner"]["login"], i["name"])+"&show_owner=true"}" alt="{i["name"]}" width="{c.get("repo-card",{}).get("width","50%")}"/></a>'
            )
        return " ".join(output)

    @staticmethod
    def __generate_starred_repo(c, d):
        output = []
        for i in d:
            output.append(
                f'<a href="{i["url"]}"><img align="center" src="{Repo.__generate_link(c, i["owner"]["login"], i["name"])+"&show_owner=true"}" alt="{i["name"]}" width="{c.get("repo-card",{}).get("width","50%")}"/></a>'
            )
        return " ".join(output)

    @staticmethod
    def __generate_most_starred_repo(c, d):
        output = []
        for i in d:
            output.append(
                f'<a href="{i["url"]}"><img align="center" src="{Repo.__generate_link(c, i["owner"]["login"], i["name"])}" alt="{i["name"]}" width="{c.get("repo-card",{}).get("width","50%")}"/></a>'
            )
        return " ".join(output)
