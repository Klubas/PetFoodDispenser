import requests

from config.Parameters import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


class TelegramBot:
    def __init__(self, token=TELEGRAM_BOT_TOKEN, chat_id=TELEGRAM_CHAT_ID):
        self.token = token
        self.chat_id = chat_id

        if not self.token:
            raise Exception('Telegram token not set')

        if not self.chat_id:
            raise Exception('Telegram chat_id not set')

        self.api_url = f"https://api.telegram.org/bot{self.token}"

    def send_text(self, message) -> bool:
        if not message:
            raise Exception('Message can not be empty')

        method = "sendMessage"
        params = {"chat_id": self.chat_id, "text": message}
        url = f"{self.api_url}/{method}"

        try:
            request = requests.post(url, params=params)
            request.raise_for_status()
            return True
        except Exception as e:
            print(e)
            return False

    def send_picture(self, picture, caption) -> bool:
        if not picture:
            raise Exception('Picture can not be empty')

        method = "sendPhoto"
        params = {'chat_id': self.chat_id, "caption": caption}
        files = {'photo': picture}
        url = f"{self.api_url}/{method}"

        try:
            request = requests.post(url, params=params, files=files)
            request.raise_for_status()
            return True
        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    bot = TelegramBot()

    if bot.send_text("Test message"):
        print("Message sent")

    if bot.send_picture(picture=open('../static/camera-512px.png', 'rb'),
                        caption="Test picture"):
        print("Picture sent")
