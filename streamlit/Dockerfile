FROM python:3.9
EXPOSE 8501
WORKDIR /project
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV PORT=8501
CMD streamlit run  --server.enableXsrfProtection false --server.enableCORS false --server.port ${PORT}  main.py