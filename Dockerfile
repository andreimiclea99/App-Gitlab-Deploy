FROM python:slim

WORKDIR /app
COPY src .

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]