# Speech Dataset Validator

A web application for validating and rating speech samples from the Mozilla Common Voice dataset. This project allows users to edit transcriptions and rank audio quality across multiple dimensions including pronunciation, naturalness, and noise levels.

Built with Django, HTML/CSS, and SQLite.

## Features

- **Voice Rating System**: Rate voices on pronunciation, naturalness, and noise level (1-5 scale)
- **Transcription Editing**: Edit transcriptions directly if they don't match the audio
- **User Authentication**: User account system required before rating voices
- **Random Sample Selection**: Get 5 random voices from the dataset per session
- **Database Management**: SQLite database for storing ratings and transcriptions
- **Multi-language Support**: Built with Thai (TH) dataset, extensible to other languages

## Incoming Features

- Flags or comment system for problematic samples
- Full UX/UI redesign and improvement
- Sentence sense validation checker
- Homophones suggestion system
- Enhanced user authentication and permissions

## Installation

### Prerequisites
- Python 3.8+
- pip or conda

### Setup

1. Clone the repository:
```bash
git clone https://github.com/ItsRatcha/speech-dataset-validator.git
cd speech-dataset-validator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run Django migrations:
```bash
python manage.py migrate
```

4. Create a superuser (admin account):
```bash
python manage.py createsuperuser
```

## Usage

### Starting the Development Server

Run the following command:
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000` by default.

### Accessing the Application

- **Main Interface**: Navigate to the home page to start rating voices
- **Language Selection**: Choose your language before beginning
- **Rating Interface**: Rate 5 random voice samples and edit transcriptions as needed
- **Admin Panel**: Access Django admin at `/admin` with your superuser credentials

## User Authentication

Users are required to have an account before they can rate voices. You can:

- Register new users through the application interface (if registration is enabled)
- Create users via the Django admin panel
- Manage user permissions and accounts in `/admin`

## Database

### Structure

The application uses SQLite (`db.sqlite3`) with the following data models:

#### Language Model
- **id**: Primary key
- **name**: Language name (e.g., "Thai", "English")

#### Audio Model
- **id**: Primary key
- **lang**: Foreign key reference to Language
- **audio**: URL field pointing to the audio file
- **transcript**: Original transcription text

#### Rating Model
- **id**: Primary key
- **uid**: Foreign key reference to User (who gave the rating)
- **pronounciation_score**: Integer rating 1-5
- **naturalness_score**: Integer rating 1-5
- **noise_score**: Integer rating 1-5
- **edit_transcript**: User's edited transcription (optional)
- **timestamp**: DateTime of when the rating was recorded (auto-generated)

### Example Rating

```json
{
  "id": 6,
  "uid": "admin",
  "pronounciation_score": 4,
  "naturalness_score": 4,
  "noise_score": 4,
  "edit_transcript": "เด็กกำลังไม่สบายนะ",
  "timestamp": "2025-04-03 05:46:34"
}
```

## Dataset

This project currently uses data from the **mozilla-foundation/common_voice_17_0** dataset, specifically the Thai (TH) test split.

### Audio Files

Audio files are stored as URLs in the `audio` field of the Audio model. During development, audio files are stored locally in `audio_MVP/TH/` directory. As the project scales, audio files can be relocated to any external storage solution (cloud storage, CDN, etc.) by simply updating the stored URLs. Any service that can host and serve audio URLs is valid for this purpose.

### Adding Audio Data

Audio records are stored in the database with the following structure:
- **Language**: The language the audio belongs to (Thai, English, etc.)
- **Audio URL**: Link to the audio file (local file path or remote URL)
- **Transcript**: Original transcription text

### Modifying Dataset

To use a different dataset or language:
1. Create language entries in the database via Django admin or scripts
2. Add audio records with appropriate URLs and transcriptions
3. Update audio files storage location as needed (local or external)

## Project Structure

```
speech-dataset-validator/
├── manage.py              # Django management script
├── db.sqlite3            # SQLite database
├── requirements.txt      # Python dependencies
├── config/               # Django configuration
│   ├── settings.py      # Project settings
│   ├── urls.py          # URL routing
│   ├── wsgi.py          # WSGI configuration
│   └── asgi.py          # ASGI configuration
├── core/                # Main application
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   ├── forms.py         # Form definitions
│   ├── admin.py         # Admin configuration
│   ├── templates/       # HTML templates
│   │   ├── index.html
│   │   ├── langselect.html
│   │   └── task.html
│   └── migrations/      # Database migrations
├── users/               # User management app
│   ├── models.py        # User models
│   ├── views.py         # User views
│   └── migrations/      # User migrations
└── audio_MVP/           # Audio files storage
    └── TH/              # Thai language audio files
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Made by **Ratchanon Moungwichean**  
Undergraduate Student in Computer Engineering at Thammasat University  
Email: RatchaM.work@gmail.com

## License

This project is licensed under the MIT License - see the LICENSE file for details.
