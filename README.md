
---

#  Random Dog Generator (Flask Web App)

A simple Flask web application that displays a **random dog image** each time the user presses a button. This project demonstrates basic web development skills such as routing, templates, forms, using a REST API, and serving static files (CSS).

---

##  Features

* Fetches a random dog image from the Dog CEO API
  ➜ [https://dog.ceo/api/breeds/image/random](https://dog.ceo/api/breeds/image/random)
* Clean, minimal interface with custom styling
* Flask template rendering + POST form handling
* Includes static assets (CSS)

---

##  Tech Stack

* **Python 3**
* **Flask**
* **Requests**
* **HTML + Jinja2 templates**
* **CSS (static files)**

---

##  Project Structure

Your folder should look like this:

```
project-folder/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

Your `.gitignore` should include your virtual environment:

```
env/
```

---

##  Setup Instructions

### 1. Clone the repo

```bash
git clone <your-repo-url>
cd <project-folder>
```

### 2. Create and activate the virtual environment

(Make sure it is named **env**, because that’s what your `.gitignore` expects.)

```bash
python3 -m venv env
source env/bin/activate     # macOS / Linux

env\Scripts\activate        # Windows
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

---

##  Running the App

Start the development server:

```bash
python app.py
```

You should see:

```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

Open that link in your browser.

---

##  How It Works

### `app.py`

* Displays the main page
* When the form is submitted (POST):

  * Fetches a random dog image using Requests
  * Passes the URL to `index.html`

### `index.html`

* Shows a button to get a new dog image
* Uses Jinja2 templating to conditionally show the image when available
* Includes your CSS via:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

### `static/style.css`

Your stylesheet that handles the look and layout of the page.

---
