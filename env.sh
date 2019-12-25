#!/bin/bash

ROOT=$HOME/projects/prometheus-demo
PROMETHEUS_ROOT=$ROOT/prometheus
PROMETHEUS_HOME=$PROMETHEUS_ROOT/prometheus-2.15.0.linux-amd64

ALERTMANAGER_ROOT=$ROOT/alertmanager 
ALERTMANAGER_HOME=$ALERTMANAGER_ROOT/alertmanager-0.20.0.linux-amd64

PUSHGATEWAY_ROOT=$ROOT/pushgateway
PUSHGATEWAY_HOME=$PUSHGATEWAY_ROOT/pushgateway-1.0.1.linux-amd64

GRAFANA_ROOT=$ROOT/grafana
GRAFANA_HOME=$GRAFANA_ROOT/grafana-6.5.2

PATH=$PROMETHEUS_HOME:$ALERTMANAGER_HOME:$GRAFANA_HOME/bin:$PATH
