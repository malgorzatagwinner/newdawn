from PyQt6.QtWidgets import QApplication
from qasync import QEventLoop
from login_window import LoginWindow
from chat_client import ChatClient

def main():
    app = QApplication([])
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    def on_login_success(token, username):
        client = ChatClient(token, username)
        client.load_documents()
        loop.create_task(client.connect_to_chat())

    login = LoginWindow(on_login_success)
    login.show()

    with loop:
        loop.run_forever()

if __name__ == "__main__":
    import asyncio
    main()

