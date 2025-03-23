FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy everything, not just app/ (for .env, init.sql, dashboards)
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python3", "app/main.py"]
