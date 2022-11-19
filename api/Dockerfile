FROM python:3.9.13

# Copy files inside Docker images
ADD ./ ./

# Install uvicorn when building the image so that we can run the API
RUN pip install -r requirements.txt

# 
CMD ["./run_api-develop.sh"]