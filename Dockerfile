FROM python:3
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/altcap
ENV PYTHONPATH "${PYTHONPATH}:/app/altcap"