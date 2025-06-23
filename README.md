# Late Show API
**Phase 4  Code Challenge**

## **Description**
This is a Flask-based RESTful API for managing TV show episodes, guests, and their appearances on the show. The project allows users to retrieve episode and guest data, as well as add new guest appearances with a rating.


## Features

- Models:
  - `Episode`
  - `Guest`
  - `Appearance`
- Relationships:
  - An episode has many guests through appearances
  - A guest has many episodes through appearances
- Routes:
  - `GET /episodes`
  - `GET /episodes/:id`
  - `GET /guests`
  - `POST /appearances`
- Validation:
  - `Appearance.rating` must be between 1 and 5
- Cascading deletes on `Appearance`
- Serialization with controlled recursion depth






## Setup Instructions 

### **Requirements**
- Before setting up the project, ensure you have the following installed:
- Python 3
- Flask
- Flask SQLAlchemy
- SQLite 
- Postman for endpoint testing
    

### Getting Started 
1. **Clone the repository**   
Open your terminal and run the following command:
    ```sh
    $git clone https://github.com/awuorochelle75/lateshow.git



2. **Navigate to the project folder**
    ```sh
        $cd lateshow

3. **Install dependencies**
    ```sh
        $pipenv install flask flask_sqlalchemy flask_migrate


4. **Create virtual environment**
    ```sh
        $pipenv shell


5. **Set up your environment and database**

    ```sh
        $flask db init
        flask db migrate -m "Initial migration"
        flask db upgrade
        python -m app.seed  


6. **Run the server**

    ```sh
        $flask run
        

7.you can check http://localhost:5000/episodes to test


## API Testing
- Use Postman to test the provided endpoints.


## Contact Information
 Email: awuorochelle@gmail.com

## License
 MIT License @2025 Rochelle Awuor


