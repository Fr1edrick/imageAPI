FROM tiangolo/uvicorn-gunicorn:python3.11

# Maintainer info
LABEL maintainer="Fredy Vaquiro <fvaquiro@unbosque.edu.co>"

# Make working directories
RUN  mkdir -p  /imagePredictorAPI
WORKDIR  /imagePredictorAPI

# Upgrade pip with no cache
RUN pip install --no-cache-dir -U pip

# Copy application requirements file to the created working directory
COPY requirements.txt .

# Install application dependencies from the requirements file
RUN pip install -r requirements.txt

# Upgrade
RUN pip install --upgrade tensorflow keras numpy pillow

# Copy every file in the source folder to the created working directory
COPY  . .

# Run the python application
CMD ["python", "main.py"]