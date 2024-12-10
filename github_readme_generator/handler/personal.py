class Personal:
    def __init__(self, config):
        self.config = config["personal"]
        self.telegram = f'<a href="{self.config["telegram"]}" target="_blank"><img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt=telegram align="center" /></a>'
        self.linkedin = f'<a href="{self.config["linkedin"]}" target="_blank"><img src="https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" alt=linkedin align="center" /></a>'
        self.twitter = f'<a href="{self.config["twitter"]}" target="_blank"><img src="https://img.shields.io/badge/twitter-%2300acee.svg?&style=for-the-badge&logo=twitter&logoColor=white" alt=twitter align="center" /></a>'
        self.kaggle = f'<a href="{self.config["kaggle"]}" target="_blank"><img src="https://img.shields.io/badge/kaggle-%2344BAE8.svg?&style=for-the-badge&logo=kaggle&logoColor=white" alt=kaggle align="center" /></a>'
        self.wechat = f'<a href="{self.config["wechat"]}" target="_blank"><img src="https://img.shields.io/badge/WeChat-07C160?style=for-the-badge&logo=wechat&logoColor=white" alt=wechat align="center" /></a>'
        self.gmail = f'<a href="mailto:{self.config["gmail"]}" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" align="center" /></a>'
        self.github = f'<a href="{self.config["github"]}" target="_blank"><img src="https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white" alt=github align="center" /></a>'
        self.stackoverflow = f'<a href="{self.config["stackoverflow"]}" target="_blank"><img src="https://img.shields.io/badge/stackoverflow-%23F28032.svg?&style=for-the-badge&logo=stackoverflow&logoColor=white" alt=stackoverflow align="center" /></a>'
        self.patreon = f'<a href="{self.config["patreon"]}" target="_blank"><img src="https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white" alt=patreon align="center" /></a>'
