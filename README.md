Project Title: Automated Stock Price Alert System

Overview A financial monitoring tool that automates stock tracking. Instead of manual checking, this Python script polls live market data from the NSE (National Stock Exchange) and triggers an instant email notification via SMTP when a specific buying opportunity is detected.

Key Features

Live Monitoring: Fetches real-time data using the Yahoo Finance API.

Conditional Alerting: Only sends notifications when the custom logic (Price < Target) is met.

Secure SMTP: Uses Google App Passwords and TLS encryption to send emails securely without exposing primary credentials.

Tech Stack

Language: Python 3.x

Libraries: requests (Data), smtplib (Notification)

Security: App Password Authentication.
