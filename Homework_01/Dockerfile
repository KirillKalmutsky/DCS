FROM continuumio/miniconda:latest

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

COPY environment.yml /environment.yml
RUN conda env update -f environment.yml -n base

COPY app.py home/app.py

CMD ["python", "home/app.py" ]