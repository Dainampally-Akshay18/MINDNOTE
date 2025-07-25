# MindNotes 🧠

*Your Mind, Organized - A Professional Note Management System*

 An Enterprise-level note management application that transforms how you capture, organize, and access your thoughts. Built with modern web technologies and featuring a beautiful Ocean-to-Sunset UI theme, MindNotes combines powerful functionality with an intuitive, visually captivating interface.

![Screenshot 1](output/1.png)
![Screenshot 2](output/2.png)
![Screenshot 3](output/3.png)
![Screenshot 4](output/4.png)
![Screenshot 5](output/5.png)
![Screenshot 6](output/6.png)
![Screenshot 7](output/7.png)
![Screenshot 8](output/8.png)
![Screenshot 9](output/9.png)


### ✨ Key Features

- 📝 **Smart Note Management** - Create, edit, and delete notes with ease
- ⭐ **Priority System** - Mark important notes with special visual indicators
- 🔍 **Real-time Search** - Find your notes instantly with live search
- 🎨 **Stunning UI** - Beautiful glassmorphism design with gradient animations
- 📱 **Fully Responsive** - Perfect experience across all devices
- 🚀 **Fast Performance** - Lightning-fast operations with MongoDB
- 🔔 **Toast Notifications** - Real-time feedback for all actions
- 🌊 **Animated Background** - Dynamic, eye-catching visual effects

## 🏗️ Architecture

```
MindNotes/
├── 📁 config/
│   └── db.py              # Database configuration
├── 📁 models/
│   └── note.py            # Note data model
├── 📁 Routes/
│   └── note.py            # API routes and endpoints
├── 📁 schemas/
│   └── note.py            # Data validation schemas
├── 📁 templates/
│   ├── index.html         # Main application page
│   └── about-us.html      # About page
├── index.py               # FastAPI application entry point
└── requirements.txt       # Python dependencies
```

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **Python 3.8+** - Core programming language
- **MongoDB** - NoSQL database for flexible data storage
- **PyMongo** - MongoDB driver for Python
- **Pydantic** - Data validation using Python type annotations

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Advanced styling with glassmorphism effects
- **JavaScript (ES6+)** - Interactive functionality
- **Bootstrap 5.3.7** - Responsive framework
- **Font Awesome 6.5.0** - Beautiful icons
- **Google Fonts** - Inter & Playfair Display typography
- **Animate.css** - Smooth animations

### Design Features
- **Glassmorphism** - Modern frosted glass effects
- **Ocean-to-Sunset Theme** - Stunning gradient color palette
- **Responsive Design** - Mobile-first approach
- **Micro-interactions** - Engaging user feedback

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.8 or higher** - [Download Python](https://python.org/downloads/)
- **MongoDB** - [Install MongoDB](https://docs.mongodb.com/manual/installation/)
- **Git** - [Install Git](https://git-scm.com/downloads)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/mindnotes.git
   cd mindnotes
   ```

2. **Create Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start MongoDB**
   ```bash
   # Windows (if installed as service)
   net start MongoDB

   # macOS (with Homebrew)
   brew services start mongodb-community

   # Linux
   sudo systemctl start mongod
   ```

5. **Run the Application**
   ```bash
   uvicorn index:app --reload
   ```

6. **Open Your Browser**
   Navigate to `http://127.0.0.1:8000` and start organizing your thoughts! 🎉

## 📋 Requirements.txt

Create a `requirements.txt` file in your project root:

```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
pymongo==4.6.0
python-multipart==0.0.6
jinja2==3.1.2
python-dotenv==1.0.0
```

## 🗃️ Database Schema

### Note Document Structure
```javascript
{
  "_id": ObjectId("..."),
  "title": "String - Note title",
  "Description": "String - Note content",
  "important": "Boolean - Priority flag",
  "created_at": "DateTime - Creation timestamp",
  "updated_at": "DateTime - Last update timestamp"
}
```

## 🔧 Configuration

### Database Configuration (`config/db.py`)
```python
from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
conn = client
```

### Environment Variables (Optional)
Create a `.env` file for production settings:
```env
MONGODB_URL=mongodb://localhost:27017/
DATABASE_NAME=MINDNOTE
COLLECTION_NAME=NOTE
```

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Main application page |
| `GET` | `/about-us` | About page |
| `POST` | `/add` | Create new note |
| `POST` | `/delete/{note_id}` | Delete specific note |

### API Response Examples

**Success Response (Add Note):**
```
HTTP 303 Redirect to /?added=true
```

**Success Response (Delete Note):**
```
HTTP 303 Redirect to /?deleted=true
```

**Error Response:**
```
HTTP 303 Redirect to /?error=error_type
```

## 🎨 UI Features

### Visual Elements
- **Glassmorphism Cards** - Beautiful frosted glass effect
- **Gradient Animations** - Dynamic background movements
- **Hover Effects** - Interactive card transformations
- **Toast Notifications** - Real-time user feedback
- **Loading States** - Smooth transition animations

### Color Palette
```css
:root {
  --ocean-gradient: linear-gradient(135deg, #12c2e9 0%, #c471ed 50%, #f64f59 100%);
  --sunset-gradient: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
  --aurora-gradient: linear-gradient(135deg, #a8edea 0%, #fed6e3 50%, #d299c2 100%);
  --important-gradient: linear-gradient(135deg, #ffd54f 0%, #ffb300 100%);
}
```

## 📱 Responsive Design

MindNotes is fully responsive and optimized for:
- 📱 **Mobile Devices** (320px - 768px)
- 📟 **Tablets** (768px - 1024px)
- 💻 **Desktops** (1024px+)
- 🖥️ **Large Screens** (1440px+)

## 🧪 Testing

### Manual Testing Checklist
- [ ] Create new note
- [ ] Mark note as important
- [ ] Search functionality
- [ ] Delete note with confirmation
- [ ] Mobile responsiveness
- [ ] Toast notifications
- [ ] Form validation









