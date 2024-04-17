FROM python:alpine3.7 
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /app
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["python", "app.py"]