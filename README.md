

<h1 align="center"> WEB SERVICES AND APPLICATIONS </h1>

![PyhtonAnywhere](https://d226lax1qjow5r.cloudfront.net/blog/blogposts/deploying-pythonanywhere-with-the-messages-api/messages_pythonanywhere_1200x600.png)

## Higher Diploma in Science Data Analytics
## Subject: Web Services and Applications
## Teacher: Andrew Beatty
## Year: 2025/1

# My Project Repository
**by Gabriela Domiciano Avellar**

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
