FROM swaggerapi/swagger-ui
MAINTAINER Jason Walsh <jason.walsh@uphs.upenn.edu>
ENV VALIDATOR_URL null
COPY specifications/v2/swagger.json .
ENV SWAGGER_JSON swagger.json
