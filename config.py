
SUPPORTED_ENVS = ['dev', 'qa']


class Config:
    def __init__(self, env):
        self.base_url = {
            'dev': 'https://www.google.com/search?q=dev',
            'qa': 'https://www.google.com/search?q=qa'
        }[env]
