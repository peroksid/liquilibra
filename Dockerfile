# TODO: build base image with requirements baked in and rebuild when requirements change
# TODO: use multi-staged build for base image, with pip touching only specific directory 
#       to allow us to copy this over to the build
FROM python:3.8
WORKDIR /liquilibra
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY *.py ./
ENV FLASK_APP librasrv.py
ENV FLASK_RUN_HOST 0.0.0.0
EXPOSE 5000
CMD ["flask", "run"]
