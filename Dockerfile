# Python base image
FROM python:3.9-slim

# Working directory set karein
WORKDIR /app

# Files copy karein
COPY . .

# Libraries install karein
RUN pip install -r requirements.txt

# Port open karein
EXPOSE 8501

# App chalane ki command
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]