FROM python:3.7
WORKDIR /app
COPY . .
RUN ln -s fresh_tomatoes.html index.html
CMD ["python", "-m", "http.server", "80"]