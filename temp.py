import openai
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

# Set OpenAI API key


class ChatbotGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        
        # Set window properties
        self.setWindowTitle("Chatbot")
        self.setGeometry(300, 300, 800, 600)

        # Create text editor for chat window
        self.chat_window = QTextEdit(self)
        self.chat_window.setObjectName("chat_window")

        # Create input text box
        self.input_text = QLineEdit(self)
      
        # Add submit button
        self.submit_btn = QPushButton("Submit", self)
        self.submit_btn.clicked.connect(self.get_response)

        # Set layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.chat_window)
        vbox.addWidget(self.input_text)
        vbox.addWidget(self.submit_btn)

        centralWidget = QWidget(self)
        centralWidget.setLayout(vbox)
        self.setCentralWidget(centralWidget)

    def get_response(self):
        user_input = self.input_text.text()
        self.input_text.clear()

        # Get response from OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        ).choices[0].text

        # Update chat window  
        self.chat_window.append(f"You: {user_input}")
        self.chat_window.append(f"Bot: {response}")
        self.chat_window.setReadOnly(True)

app = QApplication(sys.argv)
gui = ChatbotGUI()
gui.show()
sys.exit(app.exec())