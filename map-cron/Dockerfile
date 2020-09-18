FROM ubuntu:19.10
LABEL maintainer=contact@voxowl.com

RUN apt-get update

# Install docker CLI
RUN apt-get -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
RUN bash -c "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -"
RUN add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
RUN apt-get -y install docker-ce-cli

# Install cron
RUN apt-get -y install cron

# Copy mc-map-cron file to the cron.d directory
COPY mc-map-cron /etc/cron.d/mc-map-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/mc-map-cron

# Apply cron job
RUN crontab /etc/cron.d/mc-map-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log
