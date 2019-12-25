#!/bin/bash

alerts='[
  {
    "labels": {
       "alertname": "instance_down",
       "instance": "example1"
     },
     "annotations": {
        "info": "The instance example1 is down",
        "summary": "instance example1 is down"
      }
  }
]'

URL="http://192.168.10.48:9093"

curl -XPOST -d"$alerts" $URL/api/v1/alerts
