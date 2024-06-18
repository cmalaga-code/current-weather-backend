FROM python:3.12.0-bullseye
WORKDIR /app
SHELL ["/bin/bash", "-c"]
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt upgrade -y
RUN python3 -m venv .venv
RUN source .venv/bin/activate
COPY main.py  .
COPY requirements.txt  .
RUN pip3 install -r requirements.txt
EXPOSE 10000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--workers", "4", "--port", "10000"]