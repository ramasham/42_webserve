#!/usr/bin/env python3
"""
Contact Form Handler CGI Script
Handles POST requests from the contact form
"""

import os
import sys
import urllib.parse
import html

# Get request method
method = os.environ.get('REQUEST_METHOD', 'GET')

print("Content-Type: text/html")
print()

# Common styles
STYLES = """
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }
        .card {
            background: white;
            border-radius: 20px;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
            padding: 3rem;
            max-width: 500px;
            width: 100%;
        }
        h1 {
            color: #2C5F41;
            font-size: 2rem;
            margin-bottom: 0.5rem;
            text-align: center;
        }
        .subtitle {
            color: #666;
            text-align: center;
            margin-bottom: 2rem;
        }
        .form-group {
            margin-bottom: 1.5rem;
        }
        label {
            display: block;
            color: #333;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
        input, textarea {
            width: 100%;
            padding: 0.875rem 1rem;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 1rem;
            transition: border-color 0.3s;
            font-family: inherit;
        }
        input:focus, textarea:focus {
            outline: none;
            border-color: #7BA05B;
        }
        textarea {
            resize: vertical;
            min-height: 120px;
        }
        .btn {
            display: block;
            width: 100%;
            background: #2C5F41;
            color: white;
            padding: 1rem;
            font-size: 1.1rem;
            font-weight: 600;
            text-decoration: none;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s;
            text-align: center;
        }
        .btn:hover {
            background: #7BA05B;
        }
        .btn-secondary {
            background: transparent;
            color: #2C5F41;
            border: 2px solid #2C5F41;
            margin-top: 1rem;
        }
        .btn-secondary:hover {
            background: #2C5F41;
            color: white;
        }
        .icon {
            font-size: 4rem;
            text-align: center;
            margin-bottom: 1rem;
        }
        .message-box {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 10px;
            border-left: 4px solid #7BA05B;
            margin: 1.5rem 0;
        }
        .message-label {
            color: #888;
            font-size: 0.8rem;
            text-transform: uppercase;
            margin-bottom: 0.5rem;
        }
        .message-text {
            color: #333;
            line-height: 1.6;
        }
        .success-text {
            color: #666;
            text-align: center;
            margin-bottom: 1.5rem;
            line-height: 1.6;
        }
    </style>
"""

if method == 'POST':
    # Read POST data from stdin
    content_length = int(os.environ.get('CONTENT_LENGTH', 0))
    post_data = sys.stdin.read(content_length) if content_length > 0 else ''
    
    # Parse the form data
    params = urllib.parse.parse_qs(post_data)
    
    # Escape HTML to prevent XSS
    name = html.escape(params.get('name', [''])[0])
    email = html.escape(params.get('email', [''])[0])
    message = html.escape(params.get('message', [''])[0])
    
    print(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Message Sent | Swiss Journey</title>
    {STYLES}
</head>
<body>
    <div class="card">
        <div class="icon">✅</div>
        <h1>Thank You, {name}!</h1>
        <p class="success-text">Your message has been received.<br>We'll get back to you at <strong>{email}</strong> soon.</p>
        <div class="message-box">
            <div class="message-label">Your message</div>
            <div class="message-text">{message}</div>
        </div>
        <a href="/pages/homepage.html" class="btn">← Back to Homepage</a>
        <a href="/cgi-bin/contact.py" class="btn btn-secondary">Send Another Message</a>
    </div>
</body>
</html>
""")
else:
    print(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us | Swiss Journey</title>
    {STYLES}
</head>
<body>
    <div class="card">
        <h1>Contact Us</h1>
        <p class="subtitle">We'd love to hear from you</p>
        <form action="/cgi-bin/contact.py" method="POST">
            <div class="form-group">
                <label for="name">Your Name</label>
                <input type="text" id="name" name="name" placeholder="John Doe" required>
            </div>
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" placeholder="john@example.com" required>
            </div>
            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message" name="message" placeholder="Tell us about your Swiss journey plans..." required></textarea>
            </div>
            <button type="submit" class="btn">Send Message →</button>
        </form>
        <a href="/pages/homepage.html" class="btn btn-secondary">← Back to Homepage</a>
    </div>
</body>
</html>
""")
