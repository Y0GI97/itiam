FROM python

ADD sici.py .

RUN pip install requests beautifulsoup4 python-dotenv

CMD [ "python", "./sici.py"]