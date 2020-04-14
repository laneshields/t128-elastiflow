FROM robcowart/elastiflow-logstash-oss:4.0.0-beta

COPY --chown=logstash:root ipfix.yml /etc/logstash/elastiflow/definitions/ipfix.yml
COPY --chown=logstash:root 20_filter_29_t128_ipfix.logstash.conf /etc/logstash/elastiflow/conf.d/20_filter_29_t128_ipfix.logstash.conf
COPY --chown=logstash:root sampling_interval.yml /etc/logstash/elastiflow/user_settings/sampling_interval.yml
