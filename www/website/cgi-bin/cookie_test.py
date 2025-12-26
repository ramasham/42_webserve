#!/usr/bin/env python3
"""
Cookie Test CGI Script
Demonstrates setting and reading cookies
"""

import os
import datetime

# Get existing cookies
cookies_raw = os.environ.get('HTTP_COOKIE', '')
cookies = {}
if cookies_raw:
    for item in cookies_raw.split(';'):
        if '=' in item:
            key, value = item.strip().split('=', 1)
            cookies[key] = value

# Count visits
visit_count = int(cookies.get('visit_count', 0)) + 1

# Set cookie - increment visit count
print(f"Set-Cookie: visit_count={visit_count}; Path=/; Max-Age=86400")
print(f"Set-Cookie: last_visit={datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}; Path=/")
print("Content-Type: text/html")
print()

print(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie Test | Swiss Journey</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }}
        .card {{
            background: white;
            border-radius: 20px;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
            padding: 3rem;
            max-width: 600px;
            width: 100%;
            text-align: center;
        }}
        .icon {{
            font-size: 4rem;
            margin-bottom: 1rem;
        }}
        h1 {{
            color: #2C5F41;
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }}
        .subtitle {{
            color: #666;
            margin-bottom: 2rem;
        }}
        .visit-count {{
            font-size: 5rem;
            font-weight: bold;
            color: #2C5F41;
            margin: 1rem 0;
        }}
        .info-box {{
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1.5rem 0;
            text-align: left;
        }}
        .info-box h3 {{
            color: #2C5F41;
            margin-bottom: 1rem;
            font-size: 1rem;
        }}
        .cookie-item {{
            display: flex;
            justify-content: space-between;
            padding: 0.5rem 0;
            border-bottom: 1px solid #e0e0e0;
        }}
        .cookie-item:last-child {{
            border-bottom: none;
        }}
        .cookie-name {{
            font-weight: 600;
            color: #333;
        }}
        .cookie-value {{
            color: #7BA05B;
        }}
        .no-cookies {{
            color: #888;
            font-style: italic;
        }}
        .btn {{
            display: inline-block;
            background: #2C5F41;
            color: white;
            padding: 1rem 2rem;
            font-size: 1rem;
            font-weight: 600;
            text-decoration: none;
            border-radius: 10px;
            transition: all 0.3s;
            margin: 0.5rem;
        }}
        .btn:hover {{
            background: #7BA05B;
            transform: translateY(-2px);
        }}
        .btn-refresh {{
            background: #7BA05B;
        }}
    </style>
</head>
<body>
    <div class="card">
        <div class="icon">🍪</div>
        <h1>Cookie Test</h1>
        <p class="subtitle">Testing cookie functionality</p>
        
        <p>You have visited this page</p>
        <div class="visit-count">{visit_count}</div>
        <p>time{"s" if visit_count != 1 else ""}</p>
        
        <div class="info-box">
            <h3>📋 Current Cookies Received:</h3>
            {"".join(f'<div class="cookie-item"><span class="cookie-name">{k}</span><span class="cookie-value">{v}</span></div>' for k, v in cookies.items()) if cookies else '<p class="no-cookies">No cookies yet (first visit!)</p>'}
        </div>
        
        <div class="info-box">
            <h3>📤 Cookies Being Set:</h3>
            <div class="cookie-item">
                <span class="cookie-name">visit_count</span>
                <span class="cookie-value">{visit_count}</span>
            </div>
            <div class="cookie-item">
                <span class="cookie-name">last_visit</span>
                <span class="cookie-value">{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</span>
            </div>
        </div>
        
        <a href="/cgi-bin/cookie_test.py" class="btn btn-refresh">🔄 Refresh to Test</a>
        <a href="/pages/homepage.html" class="btn">← Homepage</a>
    </div>
</body>
</html>
""")
