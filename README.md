

<h1 align="center"> WEB SERVICES AND APPLICATIONS </h1>

![PyhtonAnywhere](https://d226lax1qjow5r.cloudfront.net/blog/blogposts/deploying-pythonanywhere-with-the-messages-api/messages_pythonanywhere_1200x600.png)

## Higher Diploma in Science Data Analytics
## Subject: Web Services and Applications
## Teacher: Andrew Beatty
## Year: 2025/1

# My Project Repository
**by Gabriela Domiciano Avellar**

**I study at [ATU](https://www.atu.ie).**

# 📁 Project Travel Log -  Web Services and Applications


## 💬 Introduction 
This project is a web application that was developed as a final project. Its objective is to demonstrate the use of an API created with Flask to manage a personal travel log.
The system will allow you to create, view, delete, and update travel logs. This data is stored in MySQL and accessed through a modular DAO layer, each responsibility is in a separate file.
The web interface was built with HTML, Bootstrap, which was used to style the system interface, ensuring a better layout, and jQuery, to manipulate the HTML page elements, making the interface interactive and dynamic to communicate with the API in real-time.
The project is also hosted online using the PythonAnywhere service.


### 📁 Project Structure

```plaintext
wsaa_project/
│
├── server.py           # Main Flask app with REST API routes.
├── travelDAO.py        # Data Access Object for MySQL database.
├── dbconfig.py         # MySQL configuration (NOT included on GitHub)
├── tripviewer.html     # Frontend HTML with Bootstrap + jQuery AJAX
├── wsgi.py             # PythonAnywhere deployment entry point
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore file (excludes dbconfig.py)
└── README.md           # Project documentation


```

A `dbconfig.py` has the MySQL connection credentials.  
It was not uploaded to GitHub for security reasons, and it is listed in gitignore.  
The file was manually uploaded to PythonAnywhere for deployment.


### 💻 To run locally 

Clone the repository
- git clone [GitHub](https://github.com/GabrielaDomiciano/WSAA_project).

Create and Activate Virtual Environment
- python -m venv venv

- source venv/bin/activate   # On Windows use venv\Scripts\activate

Install Dependencies

- pip install -r requirements.txt.

Create a table in your MySQL server

Update your MySQL credentials in dbconfig.py.


### 🌐 Access the App

You can access the live version of the project here:

[Travel Log](https://gabidomiciano.pythonanywhere.com)



### 📚 References

The main reference for this project was the content and examples provided by the professor during the semester.

Andrew Beatty Courseware: https://github.com/andrewbeattycourseware/wsaa-courseware.

Andrew Beatty deploytopythonanywhere: https://github.com/andrewbeattycourseware/deploytopythonanywhere .

The lessons from professor Gerard Harrison in the Applied Databases module were also important, especially for database design and SQL structure.

Flask Documentation: https://flask.palletsprojects.com/ - Used to understand route creation, JSON responses, and general API structure.

MySQL Connector: https://pypi.org/project/mysql-connector-python/ - Helped with database connection setup and executing secure SQL queries.

Bootstrap: https://getbootstrap.com/ - Provided styling and layout components such as buttons, tables, forms, and alerts.

jQuery: https://jquery.com/ - Used for DOM manipulation and AJAX calls to interact with the API from the frontend.

W3Schools Tutorial: https://www.w3schools.com/python/python_mysql_getstarted.asp.

Digital Ocean Flask + MySQL Guide: https://www.digitalocean.com/community/tutorials/.how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application.

PythonAnywhere Flask Deployment Guide: https://www.youtube.com/watch?v=z7dYIKm4np8.

Used AI tools, including the one available in VS Code, to help debug issues such as JSON data not being saved or updated correctly in Flask, even when no errors appeared in the browser.
Example prompt: My Flask app on PythonAnywhere is not saving data. The HTML form and JavaScript look fine. What could be wrong? My Update button changes to Save, I send the data with JavaScript, but the database doesn't update. Everything seems correct.


###### You will find comments throughout the project files.

**********************************
END