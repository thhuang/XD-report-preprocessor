FROM python
WORKDIR '/app'
COPY requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python", "report-preprocess.py"]
