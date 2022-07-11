###################
### Extensions ####
###################
FROM ghcr.io/saikarthikp9/ckan:2.9.5 as extbuild

LABEL org.opencontainers.image.source https://github.com/saikarthikp9/ckanext-customizer

# Switch to the root user
USER root

RUN apk add --no-cache \
        git \
        curl \
        python3 \
        python3-dev \
        g++ \
        gcc \
        libffi-dev

ARG CKANEXT_CUSTOMIZER_GIT_TAG=0.1.2

RUN echo "ARG CKANEXT_CUSTOMIZER_GIT_TAG:$CKANEXT_CUSTOMIZER_GIT_TAG"

# Fetch and build the custom CKAN extensions
RUN pip wheel --wheel-dir=/wheels git+https://github.com/saikarthikp9/ckanext-customizer@${CKANEXT_CUSTOMIZER_GIT_TAG}#egg=ckanext-customizer && \
    pip wheel --wheel-dir=/wheels -r https://raw.githubusercontent.com/saikarthikp9/ckanext-customizer/${CKANEXT_CUSTOMIZER_GIT_TAG}/requirements.txt && \
    curl -o /wheels/customizer.txt https://raw.githubusercontent.com/saikarthikp9/ckanext-customizer/${CKANEXT_CUSTOMIZER_GIT_TAG}/requirements.txt

USER ckan

############
### MAIN ###
############
FROM ghcr.io/saikarthikp9/ckan:2.9.5

ENV APP_DIR /srv/app
ENV CKAN__PLUGINS envvars image_view text_view recline_view datastore datapusher customizer

# Switch to the root user
USER root

COPY --from=extbuild /wheels ${APP_DIR}/ext_wheels

# Install and enable the custom extensions
RUN pip install --upgrade virtualenv && \
    pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-customizer && \
    pip install --no-index --find-links=${APP_DIR}/ext_wheels -r ${APP_DIR}/ext_wheels/customizer.txt && \
    ckan config-tool "${APP_DIR}/production.ini" "ckan.plugins = ${CKAN__PLUGINS}" && \
    chown -R ckan:ckan ${APP_DIR}

# Remove wheels
RUN rm -rf ${APP_DIR}/ext_wheels

# Add scripts script
COPY ./docker-entrypoint.d/ ${APP_DIR}/docker-entrypoint.d/
COPY ./docker-afterinit.d/ ${APP_DIR}/docker-afterinit.d/
        
USER ckan
