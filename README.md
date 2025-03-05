# Speech-to-Text Recognition 

This project is a **Speech-to-Text Recognition System** that converts spoken words into written text using **Vosk**. It enables real-time speech transcription and can be used for various applications such as automated note-taking, voice assistants, and accessibility tools.

##  Features
- 🎤 **Real-time speech recognition**
- 🔥 **Offline support** using Vosk models
- 📜 **Supports multiple languages** (depending on model)
- ⚡ **Lightweight and fast**
- 📝 **Saves transcriptions** for later use

## 🛠️ Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/speech-to-text.git
cd speech-to-text
```

### 2️⃣ Set Up a Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Download Vosk Model
Download a Vosk model from [Vosk Models](https://alphacephei.com/vosk/models) and extract it into the `models` directory.

##  Usage
Run the script and start speaking:
```sh
python main.py
```
The recognized text will be displayed on the terminal and saved to a file.

## 📂 Project Structure
```
speech-to-text/
│── models/            # Store downloaded Vosk models here
│── output/            # Transcribed text files
│── main.py            # Main script for speech recognition
│── requirements.txt   # Dependencies list
│── README.md          # Project documentation
```

## 🛠️ Dependencies
- Python 3.x
- Vosk
- Pyaudio or Sounddevice (for audio input)

## 📜 License
This project is open-source and available under the **MIT License**.

---

🚀 **Feel free to contribute!** Fork, star ⭐, and submit a pull request!
