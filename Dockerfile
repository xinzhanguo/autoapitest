FROM python:3.9.17
RUN pip install requests && pip install PyYAML && rm -r /root/.cache
WORKDIR /app
COPY *.py /app/
CMD [ "python", "/app/run.py"]