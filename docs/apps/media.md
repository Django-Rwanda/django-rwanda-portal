# Media App

## Overview

The **Media app** manages all file and media-related operations in the project.  
It handles **uploads, storage, processing, and access control** for files such as images, documents, and videos.  

By isolating media management in its own app, the system can:
- Centralize **file handling** logic.
- Allow easy integration with **cloud storage providers** (e.g., AWS S3, Google Cloud, DigitalOcean Spaces).
- Support **scalable file delivery** via CDNs.
- Enforce consistent **permissions and access rules** for uploaded media.

---

## Purpose
- Provide a unified interface for **file uploads and downloads**.
- Manage **metadata** for uploaded files (type, owner, size, status).
- Support **media processing tasks** (e.g., resizing images, generating thumbnails).
- Ensure **role-based access control** for files.
- Integrate with other apps (e.g., users’ avatars, post attachments, event images).

---

## Directory Structure

```bash
src/apps/media
├── admin.py # Admin interface for managing media files
├── apps.py # App configuration
├── filters.py # Filtering logic for media queries (e.g., by type, user)
├── forms.py # Django forms for uploading media
├── migrations/ # Database migrations
├── models/ # MediaFile model and related models
├── selectors.py # Query helpers for fetching media objects
├── serializers.py # DRF serializers for API requests/responses
├── services.py # Business logic for handling uploads, processing, deletion
├── signals.py # Hooks for events (e.g., cleanup when user deleted)
├── static/ # Static assets (icons, placeholder images)
├── tasks.py # Background tasks (e.g., async video encoding, image processing)
├── templates/ # Templates for media upload forms and previews
├── tests/ # Unit and integration tests
│ ├── models.py
│ ├── serializers.py
│ ├── tasks.py
│ └── views.py
├── urls.py # view routes for media endpoints
└── views.py # template views views for media upload/download
```


---

## Key Features

### 1. Media Model
- `MediaFile` model stores:
  - File reference (local or cloud).
  - Owner (`ForeignKey` to `User`).
  - Metadata: size, type, upload date, status.
  - Optional fields (e.g., caption, tags, visibility).

### 2. Uploads
- Supports file uploads via API (`multipart/form-data`) or forms.
- Validates file size and type.
- Stores files locally (in dev) or in **cloud storage** (prod).

### 3. Processing
- Background tasks (via **Celery**) for:
  - Image resizing, thumbnails.
  - Video encoding/transcoding.
  - Virus/malware scanning (optional).

### 4. Access Control
- Private vs. public media.
- User-based ownership permissions.
- Role-based restrictions (e.g., only staff can delete media).

### 5. Integration
- **Users app** → profile pictures.
- **Posts app** → images/videos in posts.
- **Events app** → banners, galleries.

---

## Example Usage

### Uploading Media (Service Layer)
```python
from apps.media import services

media = services.upload_media(
    user=request.user,
    file=uploaded_file,
    caption="My profile picture"
)
```

### Fetching Media (Selector Layer)

```bash
from src.apps.media import selectors

images = selectors.list_media_by_user(user_id=1, media_type="image")
```

--- 
 
## Contributor Guidelines

- Follow the project’s `coding standards` (see `CONTRIBUTING.md`).

- Do not duplicate file handling logic — keep it in services.py.

- Use selectors for all queries instead of direct ORM in views.

- Store long-running tasks (e.g., video encoding) in tasks.py.

- Ensure files are cleaned up when related objects (e.g., posts, users) are deleted.

- Ensure new features have tests in `tests/`.

- Add tests for:

    - Uploads.

    - Permission enforcement.

    - Background tasks.

--- 

## Interactions with Other Layers

- Users App: avatars, cover photos.

- Posts App: post attachments.

- Events App: banners and galleries.

- Notifications App: sending media-rich notifications.

- Core App: file validation, custom storage backends.

---

## Next Steps for Development

- Add cloud storage integration (AWS S3, GCP, etc.).

- Implement signed URLs for secure downloads.

- Add support for media streaming (video/audio).

- Provide automatic cleanup of unused media files.