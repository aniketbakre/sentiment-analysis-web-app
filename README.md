# Sentiment Analysis Web App

## Overview

The Sentiment Analysis Web App allows users to input text and receive a sentiment analysis response. The application is built using Flask for the backend and uses a pre-trained DistilBERT model for sentiment classification. The front-end is designed with HTML, CSS, and JavaScript.

## Features

- User-friendly interface for inputting text.
- Displays the detected sentiment and confidence level.
- Option to refresh the results.

## Directory Structure

```
sentiment-analysis-web-app/
├── app/
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   ├── styles.css
│   │   └── script.js
│   ├── app.py
├── model/ (contains pre-trained DistilBERT model files)
```

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/sentiment-analysis-web-app.git
cd sentiment-analysis-web-app
```

2. **Create a virtual environment:**

```bash
python -m venv venv
```

3. **Activate the virtual environment:**

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS and Linux:

```bash
source venv/bin/activate
```

4. **Install the required packages:**

```bash
pip install -r requirements.txt
```

5. **Place the pre-trained DistilBERT model files in the `model/` directory.**
model_path: [https://drive.google.com/file/d/1o4lwHqudwirRJzVXBk3XxBTzOe4RXBmL/view?usp=sharing](https://drive.google.com/file/d/1o4lwHqudwirRJzVXBk3XxBTzOe4RXBmL/view?usp=drive_link)
## Usage

1. **Run the Flask application:**

```bash
python app.py
```

2. **Open a web browser and navigate to:**

```
http://127.0.0.1:5000/
```

3. **Input your text and click the "Check Emotion" button to see the detected sentiment.**

## Files

- `app.py`: The main Flask application.
- `templates/index.html`: The HTML template for the web app.
- `static/styles.css`: The CSS file for styling the web app.
- `static/script.js`: The JavaScript file for client-side logic.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue or contact [aniketbakre1291@gmail.com](mailto:aniketbakre1291@gmail.com).

---

Feel free to customize the README file according to your specific requirements and repository details.
