# Convo Genius

Convo Genius is a Flask-based AI chat application that provides an interactive conversational interface powered by Google Generative AI (Gemini). The application offers a browser-based chat UI, maintains client-side chat history, and returns formatted AI responses as rendered HTML using Markdown conversion.

The project is designed to run locally with minimal setup and focuses on a smooth chat experience with persistent conversation management in the browser.

---

## Overview

The application includes:

* A Flask backend that communicates with Google Generative AI
* A persistent chat session using Gemini’s chat API
* Markdown-to-HTML rendering of AI responses
* A rich browser UI with chat history management stored locally
* JSON-based communication between frontend and backend
* Debug-friendly execution mode

---

## Features

* Interactive AI chat interface
* Uses Gemini 1.5 Flash chat model
* Sends user messages and receives streaming AI responses
* AI replies rendered as HTML using Markdown formatting
* Chat history stored locally in browser storage
* Ability to manage and delete chat history in UI
* Clean and styled conversation layout
* Runs locally in debug mode
* Ready for deployment with Gunicorn support

---

## Tech Stack

**Backend**

* Python
* Flask
* google-generativeai
* markdown

**Frontend**

* HTML
* CSS (inline styling within templates)
* JavaScript (Fetch API + localStorage)

Dependencies are listed in `requirements.txt`.

---

## Project Structure

```
Convo-Genius--main/
│
├── app.py                      # Flask backend + AI integration
├── requirements.txt            # Python dependencies
│
└── templates/
    ├── index.html              # Main chat UI
    ├── login.html              # Additional template included
    └── user-details.html       # Additional template included
```

---

## Installation

1. Ensure Python is installed.
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Set your Google Generative AI API key as an environment variable:

Linux / macOS:

```bash
export API_KEY="YOUR_API_KEY"
```

Windows (PowerShell):

```powershell
setx API_KEY "YOUR_API_KEY"
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

The application runs in debug mode and is typically available at:

```
http://127.0.0.1:5000/
```

---

## Usage

1. Open the web application in your browser.
2. Enter a message in the chat input box.
3. Send the message to receive an AI-generated response.
4. Conversations are saved in local storage and can be managed through the UI.
5. Type `exit` to end the session message (the app will display a session-end notice).

---

## API

### `POST /chat`

Accepts form data:

* `user_input` — text entered by the user

**Behavior**

* Sends input to Gemini chat model
* Converts AI response text to HTML using Markdown
* Returns JSON response

**Example Successful Response**

```json
{
  "user_input": "Hello",
  "bot_response": "<p>Hello there...</p>"
}
```

---

## Notes

* A valid API key is required for the application to work.
* Chat session is maintained server-side using Gemini’s chat handling.
* Chat history persistence is handled on the client using browser storage.
* The application currently runs in debug mode.
* No license file is included in this project.
