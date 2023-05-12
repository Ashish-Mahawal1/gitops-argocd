FROM python:3.11.3-slim-buster
USER root
COPY . ./src

RUN pip install -r ./src/requirements.txt

CMD [ "python3","./src/app.py" ]
