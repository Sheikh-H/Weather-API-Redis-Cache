# 🌦️ Cached Weather API Service

<p align="center">
  <b>A lightweight, high-performance weather API wrapper built with Flask, Redis caching, and rate limiting.</b><br>
  Designed for learning backend fundamentals including third-party APIs, caching strategies, and environment variables.
</p>

---

## 📘 Project Overview

**Weather API Redis Cache** is a Flask-based backend service that retrieves real-time weather data from the **Visual Crossing Weather API** and improves performance using **Redis caching** alongside **Flask-Limiter-based rate limiting**.

This project was developed as part of the roadmap.sh backend learning pathway:

* 🔗 Project Brief: https://roadmap.sh/projects/weather-api-wrapper-service
* 🌐 Weather API Provider: https://www.visualcrossing.com/account/

It demonstrates practical experience in:

* Integrating third-party APIs
* Implementing Redis-based caching (cache-aside pattern)
* Managing environment variables securely
* Protecting APIs using rate limiting
* Structuring a scalable Flask backend service

---

## 🙏 Credits & Inspiration

This project was developed with reference to architectural ideas from:

* Reference repository: https://github.com/alinakitieva/weather_api
* Additional guidance from roadmap.sh project documentation

Some debugging support and system improvements were assisted using AI tools to ensure reliability, correctness, and cleaner architecture design.

---

## ⚙️ Features

* 🌍 Live weather data from Visual Crossing API
* ⚡ Redis caching to reduce redundant external API calls
* 🔐 Secure environment variable configuration
* 🚦 Rate limiting (50 requests per hour per IP address)
* 🧠 Cache-aside architecture implementation
* 🧪 Clean and minimal REST API design

---

## 🧰 Requirements

Before running this project, ensure the following are installed:

* Python 3.8 or higher
* Redis server (running locally)
* A free Visual Crossing API key

---

## 🗄️ Redis Setup (Important)

This project requires a running Redis instance before the application starts.

### Install Redis (Linux)

```bash
sudo apt install redis-server
```

Start Redis:

```bash
redis-server
```

Verify Redis is running:

```bash
redis-cli ping
```

Expected output:

```
PONG
```

---

## 🔑 Getting Your API Key

This project uses the free Visual Crossing Weather API.

### Steps:

1. Visit: https://www.visualcrossing.com/account/
2. Sign up or log in
3. Open your **Account Dashboard**
4. Locate the **API Key** section
5. Copy your unique key
6. Paste it into your `.env` file

---

## 📦 Installation Guide

### 1. Clone the repository

```bash
git clone https://github.com/Sheikh-H/Weather-API-Redis-Cache.git
cd Weather-API-Redis-Cache
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask flask-limiter redis python-dotenv requests
```

---

## 🔐 Environment Variables Setup

A sample environment configuration is provided for convenience.

Create a `.env` file in the project root and populate it as follows:

```env
API_KEY=your_api_key_here
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
```

---

## ▶️ Running the Application

Ensure Redis is running before starting the application.

You will need three terminal sessions:

### Terminal 1 — Start Redis

```bash
redis-server
```

### Terminal 2 — Start Flask application

Option 1:

```bash
flask run
```

Option 2:

```bash
python app.py
```

The server will run at:

```
http://localhost:5000
```

### Terminal 3 — Test API requests

```bash
curl "http://localhost:5000/weather?location=Manchester"
```

---

## 🌦️ API Usage

### Base Endpoint

```
GET /weather
```

---

### 📍 Example Requests

#### 1. Basic weather by location

```bash
curl "http://localhost:5000/weather?location=Manchester"
```

---

#### 2. Weather with start date

```bash
curl "http://localhost:5000/weather?location=New York&datefrom=2026-06-01"
```

> The `quote` function is used internally to URL-encode the location parameter, ensuring that spaces and special characters are handled correctly.

---

#### 3. Weather with date range

```bash
curl "http://localhost:5000/weather?location=Manchester&datefrom=2026-06-01&dateto=2026-06-10"
```

---

## 🧠 How It Works (System Design)

### 1. Incoming request

The `/weather` endpoint receives query parameters:

* `location`
* `datefrom`
* `dateto`

---

### 2. Redis cache lookup

The application first checks Redis using the full request URL as the cache key.

* If a cached response exists → it is returned immediately
* If not → the request proceeds to the external API

---

### 3. External API request

The system calls the Visual Crossing API and retrieves weather data in JSON format.

---

### 4. Caching layer

The response is stored in Redis with a TTL of:

```
43200 seconds (12 hours)
```

---

### 5. Response returned

The final JSON response is returned to the client.

---

## 🧩 Function Breakdown

### `get_data(url)`

Main controller function:

* Checks Redis cache first
* Falls back to the API if no cached data exists
* Returns the final response

---

### `get_data_from_redis(url)`

* Retrieves cached data from Redis
* Returns a Python dictionary or `None`

---

### `get_data_from_api(url)`

* Sends a request to the Visual Crossing API
* Parses the JSON response
* Stores the result in the Redis cache
* Returns fresh data

---

### `store_data_in_redis(key, value, expiration)`

* Stores the API response in Redis
* Applies a TTL of 12 hours

---

## 🚦 Rate Limiting

Each client IP address is limited to:

```
50 requests per hour
```

This helps prevent abuse and protects external API usage limits.

---

## 📂 Project Structure

```text
Weather-API-Redis-Cache/
│
├── app.py
├── services/
│   └── cached_data.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚠️ Notes for Beginners

* Ensure Redis is running before starting the application.
* Never expose your API key publicly.
* Caching significantly reduces external API calls and improves performance.
* Rate limiting protects against excessive usage.

---

## 📄 Licence

<p>
  This project is licensed under the <b>MIT Licence</b> — see the <a href="./LICENCE">LICENCE</a> file for details.
</p>

<pre>
MIT Licence

Copyright (c) 2026 Sheikh Hussain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</pre>

---

## Footnote

<div align="center" style="border: 1px solid green; padding: 10px; border-radius: 5px;">
  <p>🗣️ Feel free to follow, connect, and chat!</p>
  <a class="header-badge" target="_blank" href="https://github.com/Sheikh-H"><img src="https://img.shields.io/badge/GitHub-376e00?style=flat&logo=github&logoColor=white" alt="GitHub"></a>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/sheikh-hussain/"><img src="https://img.shields.io/badge/LinkedIn-376e00?style=flat&logo=LinkedIn&logoColor=white" alt="LinkedIn"></a>
  <a class="header-badge" target="_blank" href="mailto:sheikh.hussain1155@gmail.com"><img src="https://img.shields.io/badge/Gmail-376e00?style=flat&logo=gmail&logoColor=white" alt="Gmail"></a>
  <a class="header-badge" target="_blank" href="https://sheikh-hussain.onrender.com/"><img src="https://img.shields.io/badge/Portfolio-376e00?style=flat&logo=github&logoColor=white" alt="Portfolio"></a>
</div>

<div align="center">
  <a href="https://sheikh-hussain.onrender.com/" target="_blank">By Sheikh Hussain 💚</a>
</div>

---

<h2 align="center">⭐ If you like this project, please give it a star on GitHub!</h2>
