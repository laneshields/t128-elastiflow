FROM robcowart/elastiflow-logstash-oss:4.0.0-beta

COPY --chown=logstash:root ipfix.yml /etc/logstash/elastiflow/definitions/ipfix.yml
COPY --chown=logstash:root elastiflow.template.json /etc/logstash/elastiflow/templates/elastiflow.template.json
# This will avoid removal of ipfix record data by changing rename actions to copy actions and commenting out remove_field
COPY --chown=logstash:root 20_filter_30_ipfix.logstash.conf /etc/logstash/elastiflow/conf.d/20_filter_30_ipfix.logstash.conf
COPY --chown=logstash:root 20_filter_35_t128_ipfix.logstash.conf /etc/logstash/elastiflow/conf.d/20_filter_35_t128_ipfix.logstash.conf
COPY --chown=logstash:root 20_filter_91_post_process.logstash.conf /etc/logstash/elastiflow/conf.d/20_filter_91_post_process.logstash.conf
COPY --chown=logstash:root sampling_interval.yml /etc/logstash/elastiflow/user_settings/sampling_interval.yml
