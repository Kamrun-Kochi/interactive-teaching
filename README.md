# Interactive Teaching

A Django application for creating interactive articles with embedded media content.

## Features

- **Media Items**: Support for multiple media types (text, image, audio, video, YouTube)
- **Interactive Articles**: Articles with clickable terms that link to related media
- **Sections**: Organize articles into ordered sections for better structure
- **Cloudinary Integration**: Media file storage and management via Cloudinary

## Requirements

- Python 3.12+
- Django 4.2
- PostgreSQL (for production)
- Cloudinary account (for media storage)

## Installation

1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - `DATABASE_URL` - PostgreSQL connection string
   - `CLOUDINARY_URL` - Cloudinary API URL
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

```
interactive_teaching/
├── articles/           # Main application
│   ├── models.py      # MediaItem, Article, Section models
│   ├── views.py       # Views for article display
│   ├── urls.py        # Article URL routes
│   └── templates/     # HTML templates
├── config/            # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py          # Django management script
├── requirements.txt   # Python dependencies
└── Procfile           # Deployment configuration
```

## Usage

Create articles with clickable terms using the syntax `[word|media_id]` in the body field. These terms will be automatically linked to their corresponding media items.