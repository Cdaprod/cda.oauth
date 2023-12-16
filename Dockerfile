FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
# If you have a requirements.txt, uncomment the next line and remove the pip install line.
# RUN pip install --no-cache-dir -r requirements.txt

# For this example, we're directly installing the packages.
RUN pip install --no-cache-dir fastapi uvicorn httpx python-dotenv

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]