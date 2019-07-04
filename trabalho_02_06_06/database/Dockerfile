FROM postgres:10
RUN localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8
ENV LANG pt_BR.utf8
WORKDIR ./
COPY init.sql /docker-entrypoint-initdb.d/
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=hambotregga
ENV POSTGRES_DB=teste_asa
ENV POSTGRES_HOST=localhost
ENV POSTGRES_PORT=5432