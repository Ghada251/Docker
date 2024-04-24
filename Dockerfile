FROM python
WORKDIR  /code
COPY . /code

# Install any needed dependencies specified in requirements.txt
RUN pip install numpy nltk

# Download NLTK data
RUN python -m nltk.downloader stopwords punkt

# Define environment variable for NLTK data path
ENV NLTK_DATA=/usr/local/share/nltk_data

# Download NLTK stopwords corpus
RUN python -m nltk.downloader stopwords punkt

# Copy your text file into the container
COPY paragraphs.txt /code/paragraphs.txt
#COPY text_words_Score.py /code/

CMD ["python3","cloud.py"]