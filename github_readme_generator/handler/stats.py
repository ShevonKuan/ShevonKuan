from urllib.parse import urlencode


class Stats:
    def __init__(self, config):
        config = config["stats"]
        self.streak_stats = Stats.__generate_streak_stats(config["streak-stats"])
        self.widgetbite_views = Stats.__generate_widgetbite_views(
            config["widgetbite-views"]
        )
        self.profile_views = Stats.__generate_profile_views(config["profile-views"])
        self.stats_card = Stats.__generate_stats_card(config["github-readme-stats"])
        self.language_card = Stats.__generate_language_card(
            config["github-readme-stats"]
        )
        self.waka_stats = Stats.__generate_waka_stats(config["github-readme-stats"])
        self.github_profile_trophy = Stats.__generate_github_profile_trophy(
            config["github-profile-trophy"]
        )

    @staticmethod
    def __generate_streak_stats(c):
        # streak-stats
        server_url = c.get("server", "https://streak-stats.demolab.com")
        align = c.get("align", "center")
        streak_stats_url = server_url + "?" + urlencode(c)
        return '<img alt="streak-stats" align="%s" src="%s" width="%s" />' % (
            align,
            (streak_stats_url).lower(),
            c.get("width", "50%"),
        )

    @staticmethod
    def __generate_widgetbite_views(c):
        # widgetbite-views
        server_url = c.get("server", "https://widgetbite.com")
        widgetbite_views_url = server_url + "/stats/" + c["username"]
        align = c.get("align", "center")
        return '<img alt="widgetbite-views" align="%s" src="%s" width="%s" />' % (
            align,
            (widgetbite_views_url).lower(),
            c.get("width", "50%"),
        )

    @staticmethod
    def __generate_profile_views(c):
        # profile-views
        server_url = c.get("server", "https://komarev.com/ghpvc")
        return "![profile-views](%s)" % (
            server_url + "/?username=" + c["username"] + "&style=" + c["style"]
        )

    @staticmethod
    def __generate_stats_card(c):
        # github-readme-stats.stats-card
        base_url = c["server"]
        align = c["stats-card"].get("align", "center")
        options = "?" + urlencode(c["common_options"])
        stats_card_url = base_url + "/api" + options + "&" + urlencode(c["stats-card"])
        return '<img align="%s" src="%s" width="%s" />' % (
            align,
            (stats_card_url).lower(),
            c["stats-card"].get("width", "50%"),
        )

    @staticmethod
    def __generate_language_card(c):
        # github-readme-stats.language-card
        base_url = c["server"]
        align = c["language-card"].get("align", "center")
        options = "?" + urlencode(c["common_options"])
        language_card_url = (
            base_url + "/api/top-langs" + options + "&" + urlencode(c["language-card"])
        )
        return '<img align="%s" src="%s" width="%s" />' % (
            align,
            (language_card_url).lower(),
            c["language-card"].get("width", "50%"),
        )

    @staticmethod
    def __generate_waka_stats(c):
        # github-readme-stats.waka-stats
        base_url = c["server"]
        align = c["waka-stats"].get("align", "center")
        options = "?" + urlencode(c["common_options"])
        waka_stats_url = (
            base_url + "/api/wakatime" + options + "&" + urlencode(c["waka-stats"])
        )
        return '<img align="%s" src="%s" width="%s" />' % (
            align,
            (waka_stats_url).lower(),
            c["waka-stats"].get("width", "50%"),
        )

    @staticmethod
    def __generate_github_profile_trophy(c):
        # github-profile-trophy
        trophy_url = c.get(
            "server", "https://github-profile-trophy.vercel.app/?"
        ) + urlencode(c)
        align = c.get("align", "center")
        return '<img align="%s" src="%s" width="%s" />' % (
            align,
            (trophy_url).lower(),
            c.get("width", "50%"),
        )
