# Messaging App

## Overview

The **Messaging app** provides **direct communication** between users in the Django Rwanda platform.  
It is designed for **real-time or asynchronous conversations**, supporting both **private (1-to-1)** and **group chats**.  

This app centralizes all message storage, delivery, and read-status tracking, ensuring a **scalable and extensible foundation** for future features (e.g., notifications, integrations with external chat services).

---

## Purpose

- Enable **direct user-to-user** messaging.
- Provide **group conversations** for teams, events, or communities.
- Store **chat history** with timestamps and metadata.
- Track **read receipts** and **delivery status**.
- Integrate with the **Notifications app** for real-time updates.
- Offer **API endpoints** for frontend and mobile clients.

---

## Directory Structure

```bash
src/apps/messaging
├── admin.py # Admin interface for conversations & messages
├── apps.py # App configuration
├── filters.py # Filtering logic (e.g., by sender, date, conversation)
├── forms.py # Forms for message creation
├── migrations/ # Database migrations
├── models/ # Conversation, Message, Participant models
├── selectors.py # Query helpers (e.g., get_messages_for_user)
├── serializers.py # DRF serializers for API exposure
├── services.py # Business logic for sending/reading messages
├── signals.py # Event-driven logic (e.g., trigger notification on new message)
├── static/ # App-specific static assets
├── tasks.py # Celery tasks (e.g., async message delivery, archiving)
├── templates/ # Email templates for message alerts
├── tests/ # Unit & integration tests
│ ├── models.py
│ ├── serializers.py
│ ├── tasks.py
│ └── views.py
├── urls.py # API routes for messaging
└── views.py # DRF views (e.g., send message, list conversations)

```

---

## Key Features

### 1. Conversations
- A **Conversation** can be:
  - **Direct** (between two users).
  - **Group** (multiple participants).
- Supports metadata like:
  - `title`, `created_at`, `updated_at`.

### 2. Messages
- Each message is linked to a **Conversation** and a **Sender**.
- Fields include:
  - `content`, `sent_at`, `read_at`, `status` (sent/delivered/read).
- Supports **attachments** (via `media` app).

### 3. Participants
- Defines which users belong to a conversation.
- Tracks participant-specific metadata:
  - `last_read_at` (for unread count).

### 4. Read Receipts
- Tracks whether a message was **delivered** and **read**.
- Updates `last_read_at` for participants.

### 5. Services Layer
Encapsulates **business logic**:
- `send_message(sender, conversation, content)`
- `mark_as_read(user, message)`
- `create_conversation(users)`

### 6. Selectors Layer
Provides **query helpers**:
- `get_conversations_for_user(user)`
- `get_messages_for_conversation(conversation, limit=50)`

---

## Example Usage

### Sending a Message

```python
from apps.messaging import services

message = services.send_message(
    sender=user,
    conversation=conversation,
    content="Hello, how are you?"
)
```

### Fetching a User’s Conversations

```python
from apps.messaging import selectors

conversations = selectors.get_conversations_for_user(user)
```

---

## Contributor Guidelines

- Keep `views.py` thin: delegate business logic to `services.py`.

- Use selectors.py for queries instead of raw queries in views.

- Integrate notifications in signals.py (e.g., notify participants of a new message).

- Ensure tests exist for all new features (conversations, messages, services).

- Follow privacy and security best practices:

    - Only participants should access a conversation.

    - Use permissions carefully in serializers/views.

---

## Interactions with Other Apps

- Users: Participants in conversations are registered users.

- Media: Messages can include media attachments.

- Notifications: New messages trigger push/email notifications.

- Analytics: Tracks message activity for insights (optional).

---

## Next Steps for Development

- Add `real-time support` (Django Channels / WebSockets).

- Implement `typing indicators` and online status.

- Add `search in messages` (by keyword, sender).

- Support `message reactions` (like emojis).

- Enable `archiving or deleting conversations`.

---

## Documentation

- [API Layer](../api.md)

-  **Apps – includes**:

    - [Users](./users.md)

    - [Posts](./posts.md)

    - [Analytics](./analytics.md)

    - [Comments](./comments.md)

    - [Events](./event.md)

    - [Media](./media.md)

    - [Messaging](./messaging.md)

    - [Notifications](./notification.md)

    - [Tags](./tags.md)

- [Common Layer](../common.md)

- [Config Layer](../config.md)

- [Core Layer](../core.md)

- [Development Guide](../../DEVELOPMENT_GUIDE.md)

---

## License

This project is licensed under the [MIT License](../../LICENSE)

### Copyright (c) 2025 I. Fils