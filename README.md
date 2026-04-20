# Crear Amoblamientos Website

Official website for **Crear Amoblamientos**, a furniture design and manufacturing business based in Buenos Aires, Argentina.  
The site showcases custom furniture products, company information, and allows visitors to contact the business directly.

---

## Overview

This project is a full-stack web application built with **Django** that presents the products and services of Crear Amoblamientos.  
It includes a product catalog with categories, a responsive interface, and a backend-powered contact form.

The goal of the website is to provide a clean and modern online presence while making it easy for potential clients to explore furniture designs and contact the business.

---

## Features

* Product catalog with categories
* Responsive design using Bootstrap
* Image gallery for products
* Contact form handled via **Django backend (SMTP email sending)**
* WhatsApp contact information
* Company information and history section
* Product filtering by category
* Cloud image storage using Cloudinary
* Production-ready static file handling with WhiteNoise

---

## Technologies Used

### Backend

* Django
* Python

### Frontend

* HTML
* CSS
* Bootstrap
* JavaScript

### Services and Tools

* AWS EC2 (deployment)
* Gunicorn (WSGI server)
* Nginx (reverse proxy)
* PostgreSQL (via `dj_database_url`)
* Cloudinary (media storage)
* SMTP (Gmail) for email handling
* WhiteNoise (static file serving)

---

## Contact Form (SMTP)

The contact form is handled securely on the backend using Django and SMTP.

Instead of using client-side services, form submissions are:
1. Validated using Django Forms
2. Processed in the backend
3. Sent via email using Gmail SMTP

This improves:
* security (no exposed API keys)
* reliability
* control over email handling

---

## Project Structure
