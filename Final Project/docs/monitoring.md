# Monitoring Setup and Alerting Guide

## Introduction

This guide covers the setup for monitoring the Traffic Analytics application and configuring alerts.

## Prometheus

Prometheus is configured to scrape metrics from the Flask application. See `monitoring/prometheus.yml` for configuration details.

## Grafana

Grafana is used to visualize the metrics collected by Prometheus. Import `monitoring/grafana-dashboard.json` for a basic dashboard setup.

## Alerts

Configure alerts in Grafana based on thresholds for key metrics like response times and error rates.
