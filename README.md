# MAPPA-Multi Asset Portfolio Performance Attribution System
A full-stack performance, attribution, and reporting system inspired by institutional PMA workflows.

## Overview
MAPPA is an end-to-end analytics platform designed to simulate real workflows of a Performance & Attribution Analyst in major asset management firms.
It replicates key responsibilities from PMA teams:
Performance measurement across Equity, Fixed Income, and Multi-Asset portfolios
Holdings-based and returns-based attribution
Residual investigation for unexpected return gaps
Automation & standardization of reporting
Data flow orchestration across multiple internal systems
Client-ready dashboards for consistent global reporting
This project mirrors concepts found in platforms like BlackRock Aladdin, focusing on clean data flows, performance accuracy, attribution explanation, and scalable reporting.

## Project Objectives
Build a robust system that ingests, processes, and analyzes multi-asset portfolio data
Implement Brinson-Fachler attribution for Equity
Implement risk-free/carry/curve/spread FX attribution for Fixed Income
Create a Residual Analyzer to explain unexplained performance gaps
Build automated pipelines using Airflow/Prefect
Deploy a Streamlit dashboard for interactive performance reporting
Maintain institutional-grade documentation, accuracy tracking, and consistency

## Key Features
✔ Multi-Asset Performance Measurement

- Time-weighted returns (TWR)
- Money-weighted returns (MWR)
- Contribution to return

✔ Equity Attribution (Brinson-Fachler)

- Allocation effect
- Selection effect
- Interaction effect

✔ Fixed Income Attribution

- Curve effect
- Spread effect
- Carry & rolldown
- FX contribution

✔ Residual Analyzer

Helps answer questions like:
- “Why does portfolio return mismatch benchmark return?”
Automatically detects:
- Missing holdings
- Incorrect weights
- Price mismatch
- Timing gaps
- Rounding errors
- FX or cash drag residuals

✔ Automated Pipelines

Using Airflow:
- Daily data ingestion
- Returns + attribution
- Residual checks
- Automated PDF + dashboard upload

✔ Professional Streamlit Dashboard

- Performance charts
- Attribution heatmaps
- Top contributors/detractors
- Residual diagnostics
- Export to Excel / PDF


