# ✉️ AI Email Writer & Follow-up Tool

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)](https://docs.python.org/3/library/tkinter.html)
[![MySQL](https://img.shields.io/badge/Database-MySQL-lightgrey.svg)](https://www.mysql.com/)
[![SMTP](https://img.shields.io/badge/Protocol-SMTP%2FSSL-green.svg)](https://docs.python.org/3/library/smtplib.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![GitHub forks](https://img.shields.io/github/forks/AkshatSinghRajput/AI-Email-Writer.svg?style=social)](https://github.com/AkshatSinghRajput/AI-Email-Writer/network/forks)
[![GitHub stars](https://img.shields.io/github/stars/AkshatSinghRajput/AI-Email-Writer.svg?style=social)](https://github.com/AkshatSinghRajput/AI-Email-Writer/stargazers)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/AkshatSinghRajput/AI-Email-Writer.svg)](https://github.com/AkshatSinghRajput/AI-Email-Writer/pulls)
[![GitHub contributors](https://img.shields.io/github/contributors/AkshatSinghRajput/AI-Email-Writer.svg)](https://github.com/AkshatSinghRajput/AI-Email-Writer/graphs/contributors)

*An intelligent desktop productivity tool designed to draft professional emails, manage communication history, track follow-ups, and dispatch emails instantly via SMTP.*

</div>

---

## 📑 Table of Contents
- [✨ Key Features](#-key-features)
- [🏆 Project Achievements](#-project-achievements)
- [🏗️ System Architecture](#️-system-architecture)
- [📊 ER & DFD Diagrams](#-er--dfd-diagrams)
- [📁 Folder Structure](#-folder-structure)
- [⚙️ Prerequisites & Setup Guide](#️-prerequisites--setup-guide)
- [🚀 Installation & Running](#-installation--running)
- [💡 How to Use](#-how-to-use)
- [🎯 Use Cases](#-use-cases)
- [⚖️ Pros, Cons & Limitations](#️-pros-cons--limitations)
- [🔮 Future Updates](#-future-updates)
- [🤝 Contribution Guide](#-contribution-guide)
- [🙏 Acknowledgements & Thanks](#-acknowledgements--thanks)

---

## ✨ Key Features
* **AI & Template-Driven Generation**: Instantly build structured emails based on recipient, subject, purpose, and tone (Professional, Casual, Persuasive, Friendly).
* **Live History & Management Table**: Interactive tracking log showing ID, Recipient, Subject, Status (`Draft` / `Sent`), and Timestamp.
* **Real Email Dispatch (SMTP)**: Send emails securely to real inboxes (via TLS/SSL integration with Gmail app passwords).
* **Multi-Record Operations**: Select single or multiple rows in the history table to edit, send, or delete.
* **Live Search & Filter**: Rapidly filter email history by recipient, subject, or status keywords.
* **Dual-Storage Support**: Designed for local in-memory execution with a plug-and-play commented MySQL backend for production persistence.

---

## 🏆 Project Achievements
* Successfully bridged desktop UI automation (`Tkinter`) with network socket protocols (`smtplib`) for live email delivery.
* Implemented real-time treeview selection binding with multi-row deletion and state toggling.
* Created a zero-dependency fallback template mechanism allowing users to run the app instantly without paid API keys.

---

## 🏗️ System Architecture
The application follows a modular client-side architecture separating the Presentation Layer (Tkinter GUI), Application/Business Logic Layer (AI Generator & SMTP Dispatcher), and Storage Layer (Local Dictionary / MySQL).

```text
+-------------------------------------------------------------+
|                     Tkinter GUI Layer                       |
|   (Input Form, Generated Output Preview, History Table)     |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                  Business Logic & Services                  |
|    - Email Generator (AI / Template Engine)                 |
|    - SMTP Client Handler (Secure TLS Transmission)          |
|    - State Management & Filter Controllers                  |
+------------------------------+------------------------------+
                               |
             +-----------------+-----------------+
             |                                   |
             v                                   v
+--------------------------+        +-------------------------+
|    Local State Memory    |        |   MySQL Database (Opt)  |
|   (Runtime Dictionary)   |        | (Persistent SQL Engine) |
+--------------------------+        +-------------------------+
```

---

## 📊 ER & DFD Diagrams

### Entity-Relationship (ER) Model
* **Entity**: `Email`
  * `id` (INT, Primary Key, Auto-Increment)
  * `to_email` (VARCHAR, Not Null)
  * `subject` (VARCHAR, Not Null)
  * `body` (TEXT, Not Null)
  * `status` (VARCHAR, Default: 'Draft')
  * `sent_date` (TIMESTAMP)

### Data Flow Diagram (DFD - Level 1)
1. **Process 1.0 (Input)**: User provides Recipient, Subject, and Purpose $\rightarrow$ passed to **Process 2.0**.
2. **Process 2.0 (AI / Generation)**: Processes text parameters $\rightarrow$ outputs formatted email body to Preview Pane.
3. **Process 3.0 (Storage / Dispatch)**: 
   * Saving stores state into **Data Store (Emails Table)**.
   * Sending invokes **SMTP Relay** to deliver mail to the external recipient.

---

## 📁 Folder Structure
```text
Email-Writer-Tool/
│
├── app.py                # Main application script (GUI + Logic + SMTP)
├── requirements.txt      # Project python dependencies
├── README.md             # Project documentation
└── assets/               # Screenshots, diagrams, and icons
```

---

## ⚙️ Prerequisites & Setup Guide
* **Python**: Version `3.9` or higher installed on your system.
* **Virtual Environment** (Recommended):
  ```bash
  python -m venv venv
  # Activate on Windows:
  venv\Scripts\activate
  # Activate on macOS/Linux:
  source venv/bin/activate
  ```

---

## 🚀 Installation & Running

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/alok-kumar8765/AI-Email-Writer.git
   cd AI-Email-Writer
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Real Email (Optional)**:
   Open `app.py` and update your sender credentials if you plan to send live emails via SMTP:
   ```python
   SENDER_EMAIL = "your_email@gmail.com"
   SENDER_PASSWORD = "your_16_char_app_password"
   ```

4. **Run the Application**:
   ```bash
   py app.py
   ```

---

## 💡 How to Use
1. **Drafting**: Enter the recipient's email address, subject heading, and your core objective/context into the left form panel.
2. **Generating**: Select your preferred tone and click **✨ Generate Email with AI**.
3. **Reviewing & Editing**: Inspect the generated email in the right panel. You can copy it directly to your clipboard or edit the text freely.
4. **Saving**: Click **💾 Save to Local/DB** to commit the draft to your history table at the bottom.
5. **Managing & Sending**: Select any record from the history table. Click **🚀 Send Real Email** to dispatch it to the recipient's live inbox and automatically update its status to `Sent`.

---

## 🎯 Use Cases
* **Job Hunting**: Rapidly generate tailored cold outreach emails and follow-ups to hiring managers and recruiters.
* **Sales & Freelancing**: Send professional project pitches and status check-ins to clients.
* **Customer Support**: Draft standardized, polite response templates quickly.

---

## ⚖️ Pros, Cons & Limitations

### 🟢 Pros
* Clean, intuitive desktop layout with zero browser or web server overhead.
* Fully functional offline fallback mode requires no paid API keys.
* Direct SMTP integration enables true end-to-end email dispatch.

### 🔴 Cons & Limitations
* Desktop-only interface (not accessible via mobile or web browsers).
* Relies on local memory dictionaries unless explicit MySQL configuration is enabled.
* SMTP providers (like Gmail) require App Passwords and enforce daily sending limits.

---

## 🔮 Future Updates
* [ ] Full asynchronous background threading so UI never freezes during SMTP transmission.
* [ ] Plug-and-play GUI settings modal for inputting custom SMTP and OpenAI API keys on the fly.
* [ ] Native attachment support (PDF resumes and documents).
* [ ] Automated follow-up reminder notifications.

---

## 🤝 Contribution Guide
Contributions, bug reports, and feature requests are welcome!
1. **Fork** the repository.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. **Commit** your Changes (`git commit -m 'Add some AmazingFeature'`).
4. **Push** to the Branch (`git push origin feature/AmazingFeature`).
5. Open a **Pull Request**.

---

## 🙏 Acknowledgements & Thanks
* Built with Python and Tkinter.
* Special thanks to open-source contributors and developers exploring automation tools. 

---
<div align="center">
  <sub>Made with ❤️ by Alok Kumar Kaushal</sub>
</div>