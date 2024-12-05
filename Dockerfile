# Select the base image.
FROM python:3.12-slim

# Set the working directory.
WORKDIR /api

# Copy the source code into the container.
COPY . .

# Copy the requirements file into the container.
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && python -m pip install --upgrade pip \
    && python -m pip install -r requirements.txt

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]