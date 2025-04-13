# Rasa Chatbot Server - Semester Project

## Overview

This project is a chatbot built using Rasa, an open-source framework for building conversational AI. The chatbot processes user queries and responds with relevant information based on predefined intents and actions. The bot uses Natural Language Understanding (NLU) and Dialogue Management to handle multi-turn conversations.

## Features

- **Rasa-based NLP Engine**: Built using Rasa, the chatbot can understand user queries and provide appropriate responses.
- **Multi-turn Conversations**: The bot supports dynamic conversations with context.
- **Custom Actions**: Custom actions and logic are defined to make the chatbot more interactive and intelligent.
- **Intents and Entities**: The bot is trained with various intents and entities to understand and respond to user input effectively.

## Project Structure

```
├── rasa-chatbot
│   ├── actions.py          # Custom actions and logic for the bot
│   ├── config.yml          # Rasa configuration file
│   ├── credentials.yml     # Credentials for the bot (e.g., APIs, tokens)
│   ├── domain.yml          # Defines intents, entities, responses, etc.
│   ├── endpoints.yml       # Endpoints configuration for Rasa services
│   ├── nlu.yml             # NLU training data (intents and entities)
│   ├── stories.yml         # Dialogue stories for training the bot
│   └── data/               # Folder containing training data files
│
└── README.md              # Project documentation
```

## Installation

### Prerequisites

- **Python**: Make sure you have Python 3.8+ installed.
- **Rasa**: Install Rasa using pip:
  ```bash
  pip install rasa
  ```

### Steps to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/Maha1503/rasa_chatbot.git
   cd rasa_chatbot
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Train the Rasa model:

   ```bash
   rasa train
   ```

4. Start the Rasa server:

   ```bash
   rasa run --enable-api
   ```

   This will start the Rasa server, and the chatbot will be ready to handle requests via the API.

5. Optionally, if you have custom actions, you can run the action server in a separate terminal window:

   ```bash
   rasa run actions
   ```

## Usage

Once the Rasa server is running, you can interact with the bot via the Rasa API.

1. Use the `/webhooks/rest/webhook` endpoint to send user queries and receive responses from the chatbot.
2. Example of making a request:
   ```bash
   curl -XPOST -H "Content-Type: application/json" -d '{"sender": "user", "message": "Hello"}' http://localhost:5005/webhooks/rest/webhook
   ```
