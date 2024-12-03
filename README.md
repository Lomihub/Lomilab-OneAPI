# Lomilab-OneApi
💪 This is a project to design an API based on **Intel's OneAPI**. This project will provide a **user-friendly API system** for extremely fast image classification on **Flask** and popular **AI/ML libraries** on the market. The project will support packaging models into optimized **Docker images** for both **CPU and GPU** and will be deployed on multiple operating systems such as **Windows, Linux, Ubuntu, WSL2, and MacOS**.

## Table of Contents
 - [🎯 Purpose](#purpose)
 - [📂 Structure](#structure)
 - [✨ Features](#features)
 - [📋 Requirements](#requirements)
 - [📖 Usage Guide](#usage-guide)
 - [🤝 Support and Contribution](#support-and-contribution)
 - [📜 License](#license)

#### 🎯 Purpose
- **Simplify the deployment of AI/ML models**
- **Easily package and distribute the system**
- **Support various models and AI/ML libraries**
- **Support multiple operating systems**

#### 📂 Structure
    .
    lomilab-oneapi/
    ├── api/
    │   ├── v1/                              # API version 1
    │   │   ├── __init__.py
    │   │   ├── endpoints/                   # Endpoints for API v1
    │   │   └── models/                      # Models for API v1
    ├── app/                                 # Flask/FastAPI application                            
    ├── tests/                               # Unit tests
    ├── docker/
    │   ├── CPU/                             # Docker image for CPU
    │   ├── gpu/                             # Docker image for GPU                 
    │   └── docker-compose.yml               # Docker Compose configuration to Containerize the API
    ├── docs/                                # Documentation
    ├── scripts/                             # Scripts for deployment
    ├── static/                              # Static files
    ├── .env                                 # Environment variables
    ├── requirements.txt                     # Required libraries if you don't have docker
    ├── README.md                            # Readme file
    └── setup.py                             # Setup file


#### ✨ Features
- 🚀  Support for extremely fast model APIs using Flask or FastAPI
- 📦  Support for packaging models into Docker images for both CPU/GPU
- 🔥  Support for multiple operating systems such as Windows, Linux, Ubuntu, WSL2, and MacOS
- 🌈  Support for popular AI/ML libraries such as TensorFlow, PyTorch, OpenCV, Scikit-learn, etc.
- 🎉  Support for various types of models such as Image Classification, Object Detection, Segmentation, Pose Estimation, OCR, NLP, etc.
- 😍  Easily extendable and customizable according to specific project requirements

#### 📋 Requirements
- Python >= 3.10
- Docker: (https://docs.docker.com/get-docker/)

#### 📖 Usage Guide

#### 🤝 Support and Contribution

#### 📜 License
