# syntax=docker/dockerfile:1

FROM python:3.7

WORKDIR /app

# Copy the source code into the container.
COPY /app/text_gen.py .

VOLUME /serverdata

# Run the application.
CMD ["python", "text_gen.py"]
