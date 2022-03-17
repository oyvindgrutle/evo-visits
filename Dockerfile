FROM python:3
ADD main.py /
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD ["python", "./src/main.py"]
