FROM python:2
MAINTAINER Andrii Dvorzhak <dvorzhak@gmail.com>
WORKDIR /backend
ADD app /backend
RUN cd /backend
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1
RUN chmod 755 flask_run.sh
CMD ["sh", "./flask_run.sh"]