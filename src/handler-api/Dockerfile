FROM python:3.9-slim

# Install virtualenv and create a virtual environment
RUN pip install --no-cache-dir virtualenv poetry && virtualenv /env --python=python3.9
ENV PATH /env/bin:$PATH
ENV PYTHONUNBUFFERED TRUE

WORKDIR /app

COPY . .
RUN /env/bin/pip install .

EXPOSE 80
ENTRYPOINT [ "./gunicorn.sh" ]