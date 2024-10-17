FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install bash curl -y

# Copy the rest of the application
COPY . .