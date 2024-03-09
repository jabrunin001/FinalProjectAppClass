# Architectural Overview

## Introduction

This document provides an overview of the architecture for the Traffic Analytics application.

## Components

- **Flask Web Application**: Serves the REST API for making predictions.
- **Machine Learning Model**: Predicts traffic accident outcomes.
- **AWS Redshift**: Stores traffic data.
- **Prometheus and Grafana**: Monitor the application and visualize metrics.

## Flow

1. Data is loaded into AWS Redshift.
2. The Flask application queries the model for predictions.
3. Prometheus collects metrics from the application.
4. Grafana visualizes the metrics collected by Prometheus.
