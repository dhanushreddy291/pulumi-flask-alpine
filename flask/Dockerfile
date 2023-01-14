FROM python:alpine
WORKDIR /flask
COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]