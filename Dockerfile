FROM python:3.8.12-alpine

# Tell docker that we don't want to be bothered with questions
ARG DEBIAN_FRONTEND=noninteractive

RUN apk add --no-cache libffi-dev build-base libxml2-dev libxslt-dev

# set root directory
ENV HOME /root
WORKDIR /root

RUN pip install poetry==1.1.10
# poetry useses virtualenvs by default -> we want global installation
RUN poetry config virtualenvs.create false
ADD pyproject.toml /root/pyproject.toml
ADD poetry.lock /root/poetry.lock
RUN poetry install

COPY recipe_scrapers_rest_api /root

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]
