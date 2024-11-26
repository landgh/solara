FROM python:3.13.0-slim
WORKDIR /app
COPY . .
RUN pip install gunicorn solara flask simple_websocket flask_sock plotly pandas

# Set SOLARA_APP environment variable
ENV SOLARA_APP=dataframe.py

# Expose the port
EXPOSE 8765

CMD ["gunicorn", "--workers", "4", "--threads", "20", "-b", "0.0.0.0:8765", "solara.server.flask:app"]
