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



🔍 Is this the same as MailHog?

Short answer: No, your implementation is not the same as MailHog.

### 🧠 Here's the difference:

#### ✅ My Script:
- Sends real emails via Gmail’s SMTP server (smtp.gmail.com).
- Requires actual credentials (email and password).
- Sends messages to real email addresses on the internet.
- Ideal for production or small automation tasks, but risky without proper credential handling.

#### 🛠️ MailHog:
- MailHog is a local email testing tool.
- It intercepts and captures outgoing emails without actually sending them.
- Provides a web UI and API to view emails sent by your application.
- Safe for testing — no emails ever reach the internet.
- Commonly used during development to test email content, formatting, etc., without spamming real inboxes.

### ✅ Use Case Summary:

Feature | My Script | MailHog
Sends real email | ✔️ Yes | ❌ No
Needs email credentials | ✔️ Yes | ❌ No
Good for testing safely | ⚠️ Risky | ✔️ Yes
Graphical UI to view email | ❌ No | ✔️ Yes
Internet connection needed | ✔️ Yes | ❌ No (runs locally)
