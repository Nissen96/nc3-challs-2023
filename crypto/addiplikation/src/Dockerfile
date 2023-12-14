FROM python:slim-bookworm

# copy src to the image
COPY . /app

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip uninstall pyelftools -y
RUN pip install pyelftools==0.29

# configure the container to run in an executed manner
ENTRYPOINT ["python"]

# expose the app port
EXPOSE 22413

CMD ["server.py"]
