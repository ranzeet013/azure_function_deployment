# Use Python 3.12 base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose the port on which the Azure function runs (default is 7071 for Azure Functions Core Tools)
EXPOSE 7071

# Run Azure Functions when the container starts
CMD ["func", "start", "--verbose"]
