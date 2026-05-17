# 📜 Nepal-China Bilateral Treaty & Diplomatic Cable NLP Analyzer
> **An Enterprise-Grade NLP Engine & Semantic Mining Pipeline for Auditing Legal Risks, Sovereign Leverage, and Resource Allocation in Low-Resource Diplomatic Text Domains.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![Visualization](https://img.shields.io/badge/Visualization-Plotly%20Express-00C0A8.svg)](https://plotly.com/)
[![NLP-Core](https://img.shields.io/badge/NLP-Regex%20%26%20Semantic%20Mining-6366F1.svg)]()

---

## 🏛️ Geopolitical & Technical Context
In strategic geopolitical hotspots, multi-lateral treaties, MoUs, and confidential diplomatic cables contain dense, highly nuanced legal syntax. Parsing these documents manually to track financial exposures (e.g., debt traps vs. pure grants) or sovereignty trade-offs introduces severe operational bottlenecks. 

This repository implements a **Production-Grade Data Pipeline (Medallion Architecture)** that auto-ingests unstructured diplomatic text payloads, extracts core legal entities via regular expression clusters, and computes a multi-variate **Sovereign Risk Coefficient Index** served through a state-of-the-art visual telemetry console.

---

## 🏗️ End-to-End System Architecture

The analytical workflow processes textual telemetry across a decoupled, multi-tiered pipeline:

```text
[Raw Unstructured Treaty Texts]  ──► Ingested into JSON Format
               │
               ▼
   ┌───────────────────────┐
   │ 🥉 Bronze Data Lake   │  ──► Raw Storage & Continuous Text Stream Auditing
   └──────────┬────────────┘
               │
               ▼
   ┌───────────────────────┐
   │ 🥈 Silver Processing  │  ──► Custom NLP Feature Extraction & Regex Metadata Mining
   └──────────┬────────────┘
               │
               ▼
   ┌───────────────────────┐
   │ 🥇 Gold Risk Core     │  ──► Multi-variate Risk Index Modeling & Threat Allocation
   └──────────┬────────────┘
               │
               ▼
[📊 Premium Telemetry Dashboard] ──► Real-Time Plotly Yield Distribution & Tactical Briefs
