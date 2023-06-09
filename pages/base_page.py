from dataclasses import dataclass

@dataclass
class BasePage:
    browser: object
    url: str

    def open(self):
        self.browser.get(self.url)