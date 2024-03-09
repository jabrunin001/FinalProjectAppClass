# Usage Guide

## Introduction

This guide explains how to use the Traffic Analytics application, including making predictions and interpreting results.

## Making Predictions

1. Send a POST request to `/predict` with the following JSON payload:
   ```json
   {
     "posted_speed_limit": 30,
     "weather_condition": "Clear",
     "lighting_condition": "Daylight",
     "first_crash_type": "Rear End"
   }

The response will contain the prediction result:
{
  "prediction": 2
}

