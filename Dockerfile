FROM python:3.9
RUN mkdir /app
WORKDIR /app
COPY /src /app/
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD exec python main.py