# # Use the official Python image as a base
# FROM python:3.7

# # Set environment variables
# ENV PYTHONUNBUFFERED 1

# # Set the working directory in the container
# WORKDIR /app

# # Copy the dependencies file to the working directory
# COPY requirements.txt /app/

# # Install any dependencies
# RUN pip config --user set global.progress_bar off
# RUN pip install -r requirements.txt

# # Copy the rest of the application code to the working directory
# COPY . /app/ 
# COPY ./entrypoint.sh /
# ENTRYPOINT ["sh", "/entrypoint.sh"]
# # CMD  ["gunicorn", "src.wsgi:application", "--bind",  "0.0.0.0:8000"]


FROM python:3.7

WORKDIR /app

# Install dependencies
COPY . .
RUN  python -m venv myenv && \
	pip install --upgrade pip && \
	pip install -r requirements.txt 

# Copy the application code
COPY . .

# Expose the port the app will run on
EXPOSE 8000

ENTRYPOINT [ "./entrypoint.sh" ]