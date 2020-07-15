
FROM cytomine/software-python3-base

ADD demo.py /app/demo.py

ENTRYPOINT ["python", "/app/demo.py"]