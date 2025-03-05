import sys
import vosk
import json
import pyaudio
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton

# Path to Vosk model (Ensure it is correct)
MODEL_PATH = "C:\\Users\\ehond\\OneDrive\\Documents\\Python\\pythonProject\\vosk-model-small-en-us-0.15\\vosk-model-small-en-us-0.15"

class SpeechRecognitionThread(QThread):
    text_received = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.running = False
        self.model = vosk.Model(MODEL_PATH)
        self.recognizer = vosk.KaldiRecognizer(self.model, 16000)

        # PyAudio setup
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        self.stream.start_stream()

    def run(self):
        """ Continuously listens to audio and emits recognized text. """
        self.running = True
        while self.running:
            data = self.stream.read(4000, exception_on_overflow=False)
            if self.recognizer.AcceptWaveform(data):
                result = json.loads(self.recognizer.Result())
                text = result.get("text", "").strip()
                if text:
                    self.text_received.emit(text)  # Send text to GUI

    def stop(self):
        """ Stops the recognition process. """
        self.running = False
        self.quit()
        self.wait()
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()


class SpeechToTextApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Live Speech-to-Text")
        self.setGeometry(200, 200, 500, 400)
        self.initUI()

        # Speech recognition thread
        self.speech_thread = SpeechRecognitionThread()
        self.speech_thread.text_received.connect(self.display_text)

    def initUI(self):
        layout = QVBoxLayout()

        # Text display area
        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        layout.addWidget(self.text_display)

        # Start/Stop button
        self.toggle_button = QPushButton("Start Listening")
        self.toggle_button.clicked.connect(self.toggle_listening)
        layout.addWidget(self.toggle_button)

        self.setLayout(layout)

    def toggle_listening(self):
        """ Starts or stops speech recognition """
        if self.speech_thread.isRunning():
            self.speech_thread.stop()
            self.toggle_button.setText("Start Listening")
        else:
            self.speech_thread.start()
            self.toggle_button.setText("Stop Listening")

    def display_text(self, text):
        """ Displays recognized text in the QTextEdit """
        self.text_display.append(text)

    def closeEvent(self, event):
        """ Cleanup on window close """
        self.speech_thread.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpeechToTextApp()
    window.show()
    sys.exit(app.exec_())
