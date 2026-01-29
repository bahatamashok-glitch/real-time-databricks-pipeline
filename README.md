# real-time-databricks-pipeline
Real-time data processing using Azure Databricks, Spark Structured Streaming, and Delta Lake
# Real-Time Databricks Data Pipeline

## Overview
This project demonstrates a real-time data engineering pipeline built using
Azure Databricks, Spark Structured Streaming, and Delta Lake.

## Architecture
Bronze → Silver → Gold (Delta Lake)

## Technologies Used
- Azure Databricks
- PySpark
- Spark Structured Streaming
- Delta Lake

## Project Flow
1. Generate streaming clickstream events
2. Ingest data using Structured Streaming
3. Store raw data in Bronze Delta table
4. Clean and transform data into Silver layer
5. Aggregate metrics in Gold layer

## Key Learnings
- Real-time data ingestion
- Delta Lake architecture
- Streaming ETL pipelines
