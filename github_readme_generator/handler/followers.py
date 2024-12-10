from ..utils.followers import get_best_followers
class Followers:
    def __init__(self, config):
        self.best_followers = Followers.__generate_best_followers(config)
        self.config = config
    @staticmethod
    def __generate_best_followers(c):
        l = get_best_followers()
        output = ""
        c = c["follower-card"]
        server = c.get("server", "https://github-personal-card.vercel.app")
        margin = c.get("margin","5")
        for i in l:
            output += f'<a href="https://github.com/{i}"><img src="{server}/card?user={i}" alt="{i}" width="{c.get("width","33%")}" align="center"/></a>'
        return output
