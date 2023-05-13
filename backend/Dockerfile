FROM python:3.11

WORKDIR /api
RUN pip install pipenv

COPY api/Pipfile* ./
RUN pipenv sync --system

COPY . .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]