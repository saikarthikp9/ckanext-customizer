# Sample docker-compose 

Try out ckanext-customizer extension in a matter of seconds. Uses [docker-compose](https://docs.docker.com/compose/) and [public docker images](https://github.com/saikarthikp9?tab=packages) hosted on Github packages. Not recommended for production deployments.

## Directory Structure

- ckan: contains the source code for the [sample docker image](https://github.com/saikarthikp9/ckanext-customizer/pkgs/container/ckanext-customizer-demo) to try out ckanext-customizer
- .ckan-env: contains the environment variables used by ckanext-customizer (Update these variables before running the docker-compose up command below)

## Commands

- Run a local containerized instance of CKAN with ckanext-customizer and all required dependencies

        docker-compose -f docker-compose.yml up -d

## References

- [CKAN repository](https://github.com/ckan/ckan)
- [Helm Chart for CKAN](https://github.com/keitaroinc/ckan-helm)