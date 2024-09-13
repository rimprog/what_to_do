FROM python:3.11-slim

WORKDIR /opt/apps/what_to_do/

# Copy the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application
COPY . .

# Set the default command to run migrations and start the server
CMD uvicorn app.main:app --forwarded-allow-ips '*' --proxy-headers --host 0.0.0.0 --port 5000