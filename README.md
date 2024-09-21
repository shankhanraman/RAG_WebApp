# NFL Season Analysis Web App

## Overview
Welcome to the NFL Season Analysis Web App! This project is designed to provide fans with real-time insights into NFL games, player statistics, and team performance. Utilizing a Retrieval-Augmented Generation (RAG) model, the app allows users to ask questions and receive immediate responses based on the latest data.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask
- **Database**: MongoDB
- **APIs**: ESPN API for real-time NFL data

## Features
- Real-time updates on NFL games and stats
- Interactive user queries powered by the RAG model
- User-friendly interface for easy navigation
- Insights on player performance and team standings

## Getting Started

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- MongoDB
- Flask

### Installation
1. Clone the repository:
   ```bash
   git clone [repository_url]
   ```
2. Navigate to the project directory:
   ```bash
   cd Backend
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your MongoDB database and update the connection settings in `config.py`.

5. Run the Flask application:
   ```bash
   python app.py
   ```

6. Open your browser and go to `http://localhost:5000` to access the app.

## Usage
- Type your query related to NFL games or players in the input field and hit enter.
- The app will provide you with real-time responses based on the latest available data.

## Challenges & Solutions
During the development, I faced challenges related to optimizing response times for user queries. I implemented caching mechanisms and improved data processing, resulting in a smoother user experience.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Any improvements or suggestions are welcome!



## Contact
For any questions or feedback, feel free to reach out to me at shankhan.raman@gmail.com.

