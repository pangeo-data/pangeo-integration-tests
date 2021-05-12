FROM python:3.7
ARG COMMIT_SHA

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV COMMIT_SHA=${COMMIT_SHA}
CMD [ "pytest" ]