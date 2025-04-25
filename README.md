# 📧 Email Sender in Python

This repository contains the source code for my **Email Sender** project — a simple Python script that sends emails using SMTP. The application functions like the Gmail app in terms of core functionality but operates entirely via the terminal without a graphical user interface.

## 🔧 Features

- Send emails using your Gmail account (or any SMTP-enabled provider)
- Add a subject and custom message body
- Send to single or multiple recipients
- Secure login using `smtplib` and `ssl`
- Easily customizable and well-documented code

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x
- An email account with SMTP enabled (e.g., Gmail)

> **Note:** If you're using Gmail, make sure to enable "App Passwords" or allow less secure apps (not recommended for production).

### 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/email-sender-python.git
   cd email-sender-python

2. Install required packages (optional, if you use additional libraries):
```bash
pip install -r requirements.txt
```

3. Run the script:
```bash
python email_sender.py
```

### 💻 Usage

Update the script with your credentials and email information:
```bash
sender_email = "your_email@example.com"
password = "your_password"
receiver_email = "recipient@example.com"
subject = "Hello from Python!"
body = "This is a test email sent using a Python script."
```

🔐 Security Warning
Do not hardcode your email credentials in the script, especially if you're pushing to a public repository. Use environment variables or a .env file for better security.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙌 Contributions
Contributions, issues, and suggestions are welcome! Feel free to fork this repo and submit a pull request.

📫 Contact
If you found this project helpful or have questions, feel free to connect with me on LinkedIn https://www.linkedin.com/in/isiaq-ibrahim-468588156/ or drop a message!
