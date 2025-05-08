# frontend/login_window.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
import requests

class LoginWindow(QWidget):
    def __init__(self, on_login_success):
        super().__init__()
        self.on_login_success = on_login_success
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Login")
        layout = QVBoxLayout()

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Username")
        layout.addWidget(self.username)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password)

        self.login_btn = QPushButton("Login", self)
        self.login_btn.clicked.connect(self.login)
        layout.addWidget(self.login_btn)

        self.status = QLabel("")
        layout.addWidget(self.status)

        self.setLayout(layout)

    def login(self):
        response = requests.post("http://localhost:8000/api/login/", data={
            "username": self.username.text(),
            "password": self.password.text()
        })
        if response.status_code == 200:
            data = response.json()
            self.status.setText("Login successful!")
            self.on_login_success(data['token'], data['username'])
            self.close()
        else:
            self.status.setText("Login failed.")

