FROM python:3.7.8-slim

# remember to expose the port your app'll be exposed on.
EXPOSE 8080

RUN pip install -U pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy into a directory of its own (so it isn't in the toplevel dir)
COPY . /workdirectory
RUN ls workdirectory
RUN ls workdirectory/source
WORKDIR /workdirectory/source

# run it!
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]
