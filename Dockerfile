FROM python:3.11

WORKDIR /gallery

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt 

COPY ./Image-ExifTool-12.55 ./Image-ExifTool-12.55
WORKDIR /gallery/Image-ExifTool-12.55
RUN perl Makefile.PL && \
    make install

WORKDIR /gallery
COPY ./Online_Image_Gallery ./Online_Image_Gallery

