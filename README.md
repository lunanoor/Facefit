# FaceFit AI

FaceFit AI is a premium web application that analyzes facial features to provide personalized style recommendations.

## Features
- **Face Shape Analysis**: Detects shape (Oval, Round, Square, etc.) using MediaPipe.
- **Skin Tone Estimation**: Analyzes skin pixels to determine tone and undertone.
- **Style Recommendations**: Suggests hairstyles, hair colors, and clothing palettes based on analysis.
- **Premium UI**: Dark-themed, glassmorphism design.

## Prerequisites
- Python 3.8 or higher
- Pip (Python package manager)

## Installation

1.  Make sure you have the required dependencies installed:
    ```bash
    pip install -r requirements.txt
    ```

    *Dependencies: `flask`, `opencv-python`, `mediapipe`, `numpy`*

## How to Run

1.  Open a terminal/command prompt in this folder.
2.  Run the application:
    ```bash
    python app.py
    ```
3.  Open your browser and navigate to:
    [http://localhost:5000](http://localhost:5000)

## Project Structure
- `app.py`: Main Flask application server.
- `analysis_engine.py`: Core logic for face detection and analysis.
- `recommendations.py`: Rules for style suggestions.
- `static/`: Contains HTML, CSS, and JavaScript files.
