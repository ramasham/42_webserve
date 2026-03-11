<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rounded&color=8B5CF6&height=140&section=header&text=webserv&fontSize=42&fontColor=ffffff&animation=fadeIn&desc=A%20Custom%20HTTP%20Server%20in%20C%2B%2B&descAlignY=70&descSize=18" />
</p>

A lightweight HTTP server built from scratch in **C++** as part of the **42 curriculum**.  
This project was designed to explore how web servers work internally by implementing core features such as **socket programming**, **HTTP request parsing**, **epoll-based event handling**, **configuration parsing**, and **CGI execution**.

---

## 📌 About the Project

`webserv` is a custom HTTP server inspired by real-world servers like **Nginx**.

The goal of this project is to understand what happens behind the scenes when a browser sends a request to a server. Instead of using a ready-made framework or server, we built the core logic ourselves using low-level network programming and C++.

This project helped us understand how servers:

- accept and manage client connections
- handle multiple clients at the same time
- parse HTTP requests
- generate HTTP responses
- serve static content
- execute CGI scripts
- manage uploads, errors, and route rules
- use configuration files to control behavior

---

## 🚀 Features

This server includes support for:

- HTTP request parsing
- HTTP response generation
- Static file serving
- Multiple server blocks
- Route-based configuration
- Custom ports and hosts
- Default pages and index handling
- Custom error pages
- Autoindex support
- File upload handling
- CGI execution
- HTTP redirections
- Allowed methods per route
- `GET`, `POST`, and `DELETE` methods
- Non-blocking sockets
- Event-driven client management using **epoll**

---

## 🧠 What This Project Taught Me

`webserv` was one of the most important projects for understanding how backend systems actually work under the hood.

It strengthened my understanding of:

- TCP/IP communication
- sockets and client-server architecture
- non-blocking I/O
- event-driven programming with **epoll**
- HTTP/1.1 request and response flow
- request parsing and response formatting
- CGI execution using processes and pipes
- file handling and uploads
- configuration-based server design
- debugging real system-level behavior
- building modular and maintainable software

---

## 🛠️ Technologies Used

- **C++**
- **HTTP/1.0**
- **Sockets**
- **epoll**
- **CGI**
- **Makefile**
- **Linux**

---

## ⚙️ Build

```bash
Compile the project with:
make

Clean object files with:
make clean

Remove object files and executable with:
make fclean

Rebuild everything with:
make re

▶️ Run

Start the server with:
./webserv config/default.conf

```
---

## ⚙️ Configuration
The server behavior is controlled by a configuration file.
```bash
server {
    listen 8080;
    server_name localhost;
    root ./www;
    index index.html;

    location / {
        allowed_methods GET POST DELETE;
        autoindex on;
    }

    location /uploads {
        root ./www/uploads;
        allowed_methods POST;
    }

    location /cgi-bin {
        cgi_extension .py;
        cgi_path /usr/bin/python3;
    }

    error_page 404 ./www/errors/404.html;
}
```
---

## 🌐 Supported HTTP Methods
### GET
Used to retrieve files and pages from the server.

### POST
Used to send data to the server, including forms and file uploads.

### DELETE
Used to remove resources when the route allows it.
---

## 📄 Static File Serving
The server can serve static content such as:
  - HTML files
  - CSS files
  - JavaScript files
  - images and assets

When a client requests a valid file, the server reads it from disk and returns the correct HTTP response.
This part of the project helped build a deeper understanding of:
  - file handling
  - MIME-type style behavior
  - response headers
  - content delivery flow
    
---
## 📂 Autoindex
When enabled for a route, the server can generate a directory listing if no index file is found.
This feature made it necessary to handle:
  - directory access
  - file listing
  - dynamic HTML response generation
  - route-based behavior control

---

## 📤 File Upload
If enabled in the configuration, the server can accept uploaded files through POST requests.
This required handling:
  - request body parsing
  - content length management
  - file creation and saving
  - upload path validation
  - route restrictions

---

## CGI Support

The server supports **CGI execution** for dynamic content.

Example route:

```conf
location /cgi-bin {
    cgi_extension .py;
    cgi_path /usr/bin/python3;
}
```
Example request:
```
http://localhost:8080/cgi-bin/test.py
```
Implementing CGI required working with:
  - process creation
  - fork()
  - execve()
  - pipes
  - environment variables
  - stdin / stdout redirection

This was one of the most interesting parts of the project because it connected HTTP handling with process management at the system level.

---

## ❌ Error Handling
The server handles common HTTP errors and can return custom error pages.
Examples include:
  - 400 Bad Request
  - 403 Forbidden
  - 404 Not Found
  - 405 Method Not Allowed
  - 500 Internal Server Error

Error handling was important for making the server more reliable and closer to real-world behavior.

---

## ⚡ epoll and Event-Driven Design
One of the core parts of this project was building the server around epoll.
Using epoll made it possible to:
  - monitor multiple file descriptors efficiently
  - handle many client connections without blocking
  - react only when a socket becomes ready for reading or writing
  - build a scalable event-driven server loop
  - Instead of creating one thread or one blocking flow per client, the server waits for events and processes them as they arrive.

This helped deepen my understanding of:
  - event loops
  - readiness-based I/O
  - scalable server architecture
  - efficient client management

---

## 🏗️ Challenges
Some of the main challenges in this project were:
  - designing a clean and modular server architecture
  - correctly parsing HTTP requests
  - handling partial reads and writes
  - managing multiple clients with epoll
  - keeping sockets non-blocking
  - executing CGI without breaking the main server flow
  - handling errors safely
  - respecting configuration rules correctly
  - making the server behavior predictable and maintainable

This project required both low-level precision and high-level system design thinking.

---

## 📖 Key Takeaway
webserv was much more than just building a server.
It was a project that connected systems programming, networking, HTTP, and software architecture into one real application.
It showed how strong fundamentals make complex systems easier to understand, debug, and build.
This project gave me a deeper appreciation for what happens behind every browser request and strengthened my confidence in working close to the system.
