FROM python:3.9-slim

COPY . .

#For linux
# RUN python3 -m venv .venv
# RUN source .venv/bin/activate

#For Windows
RUN python -m venv .venv
RUN .venv\Scripts\activate

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
