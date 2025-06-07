import requests
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel
from document_viewer import DocumentViewer

class DocumentListWindow(QWidget):
    def __init__(self, token, username):
        super().__init__()
        self.token = token
        self.username = username

        self.setWindowTitle("My Documents")
        self.resize(400, 500)

        self.layout = QVBoxLayout(self)
        self.label = QLabel(f"Welcome, {username}")
        self.list_widget = QListWidget()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.list_widget)

        self.list_widget.itemClicked.connect(self.open_document)

        self.load_documents()

    def load_documents(self):
        headers = {"Authorization": f"Token {self.token}"}
        response = requests.get("http://localhost:8000/api/documents/my-documents/", headers=headers)
        if response.status_code == 200:
            self.documents = response.json()
            for doc in self.documents:
                self.list_widget.addItem(f"{doc['id']} - {doc['title']}")
        else:
            self.list_widget.addItem("Failed to load documents.")

    def open_document(self, item):
        doc_id = item.text().split(" - ")[0]
        self.viewer = DocumentViewer(document_id=doc_id, token=self.token, username=self.username)
        self.viewer.show()
        self.close()

