FROM python:3.9.13

# Copy files inside Docker images
ADD ./ ./

# Install all required packages
RUN pip install -r requirements.txt

# 
CMD ["./run_streamlit-prod.sh"]