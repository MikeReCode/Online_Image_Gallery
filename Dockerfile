FROM python:3.11

WORKDIR /gallery

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt 

RUN git clone https://github.com/exiftool/exiftool.git
WORKDIR /gallery/exiftool
RUN perl Makefile.PL && \
    make install


WORKDIR /gallery
COPY ./Online_Image_Gallery ./Online_Image_Gallery

