FROM python
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get -y install tesseract-ocr
RUN apt-get -y install libtesseract-dev
COPY . /myapp
WORKDIR /myapp
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]