# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Show logs immediately in Jenkins
ENV PYTHONUNBUFFERED=1

# Copy dependency file first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run the calculator
CMD ["python", "-m", "calculator.calculator"]