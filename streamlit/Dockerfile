FROM python:3.9.13

# Copy files inside Docker image
ADD ./ ./

# Install all libraries needed
RUN pip install -r requirements.txt

# 
CMD ["./run_api-prod.sh"]