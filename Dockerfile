FROM python:3.8-slim-bullseye

# Install system packages including build tools and awscli
RUN apt update -y && \
    apt install -y gcc g++ make libffi-dev libzstd-dev awscli && \
    apt clean

WORKDIR /app

COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

CMD ["python3", "app.py"]
