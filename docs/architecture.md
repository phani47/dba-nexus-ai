# DBA Nexus AI Architecture

## 1. Overview

DBA Nexus AI is an AI-assisted Database Operations and Root Cause Analysis platform designed to reduce manual effort during database incident investigation.

The platform collects and correlates evidence from multiple sources before generating root cause hypotheses and recommendations.

The initial implementation focuses on Oracle database incidents and will later expand to PostgreSQL and MongoDB.

---

# 2. Architecture Principles

The platform follows these principles:

* Evidence before conclusions
* Read-only investigation by default
* Progressive evidence collection
* Database-engine-specific investigation
* Correlation across multiple data sources
* Explainable RCA
* Human approval for remediation
* No direct LLM access to production databases

---

# 3. High-Level Architecture

```text
                         INCIDENT
                            │
                            ▼
                      INCIDENT API
                            │
                            ▼
                     PLAYBOOK ENGINE
                            │
                            ▼
                      INITIAL TRIAGE
                            │
                            ▼
                     EVIDENCE PLANNER
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
          ORACLE        POSTGRESQL       MONGODB
         COLLECTOR      COLLECTOR       COLLECTOR
             │              │              │
             └──────────────┼──────────────┘
                            │
                            ▼
                       OS COLLECTOR
                            │
                            ▼
                       LOG COLLECTOR
                            │
                            ▼
                       EVIDENCE STORE
                            │
                            ▼
                    CORRELATION ENGINE
                            │
                            ▼
                        RCA ENGINE
                            │
                            ▼
                  RECOMMENDATION ENGINE
                            │
                            ▼
                       DBA APPROVAL
```

---

# 4. Incident API

The Incident API receives an incident from:

* Alert logs
* Monitoring platforms
* Database alerts
* Manual DBA submission
* Future monitoring integrations

Example incident:

```json
{
  "database": "PRODDB",
  "database_type": "oracle",
  "error_code": "ORA-04031",
  "timestamp": "2026-09-12T10:30:00",
  "severity": "HIGH"
}
```

---

# 5. Playbook Engine

The Playbook Engine maps an incident to a database-specific investigation workflow.

Example:

```text
ORA-04031

↓

Oracle Memory Incident

↓

ORA-04031 Investigation Playbook
```

Responsibilities:

* Identify incident type
* Select investigation playbook
* Define initial evidence requirements
* Define investigation phases
* Define possible RCA hypotheses

---

# 6. Initial Triage

Initial Triage collects the minimum evidence required to understand the incident.

For ORA-04031:

* Database status
* Memory configuration
* ORA-04031 error details
* Shared Pool summary
* Operating system memory summary

The system should not immediately collect every possible metric.

---

# 7. Progressive Evidence Collection

The platform uses evidence-driven investigation.

Example:

```text
ORA-04031

↓

Initial Evidence

↓

Shared Pool Usage High

↓

Collect Library Cache Metrics

↓

Parse Activity High

↓

Collect Cursor Metrics

↓

Cursor Growth Detected

↓

Correlate Evidence

↓

Generate RCA Hypothesis
```

This reduces unnecessary data collection and makes the investigation process explainable.

---

# 8. Evidence Planner

The Evidence Planner determines what evidence should be collected next.

Example:

```text
IF Shared Pool Usage > 90%

THEN Collect:

- Library Cache Metrics
- Cursor Metrics
- SQL Parse Metrics
```

Example:

```text
IF OS Memory Pressure Detected

THEN Collect:

- Swap Usage
- Top Memory Processes
- Oracle Process Memory
```

The Evidence Planner should initially be rule-based.

Future versions may use AI-assisted planning.

---

# 9. Database Collectors

Database collectors retrieve database-specific evidence.

## Oracle Collector

Examples:

* Database status
* Memory configuration
* SGA metrics
* Shared Pool metrics
* Library Cache metrics
* Cursor metrics
* Session metrics
* SQL parsing metrics

## PostgreSQL Collector

Future support:

* Database status
* Connections
* Locks
* Long-running queries
* Memory configuration
* WAL metrics
* Autovacuum metrics
* Replication metrics

## MongoDB Collector

Future support:

* Replica Set status
* Connections
* Operations
* Slow queries
* Index usage
* Memory usage
* Replication lag

---

# 10. Operating System Collector

The OS Collector gathers:

* Total memory
* Available memory
* Swap usage
* CPU utilization
* Load average
* Top processes

The collector should use secure, controlled commands.

---

# 11. Log Collector

The Log Collector retrieves relevant events from:

* Oracle alert logs
* Database logs
* Operating system logs

The collector should extract:

* Error code
* Timestamp
* Frequency
* Related errors
* Events occurring before the incident

---

# 12. Evidence Store

All collected evidence should be stored in a structured format.

Example:

```json
{
  "incident_id": "INC-001",
  "source": "oracle",
  "metric": "shared_pool_usage",
  "value": 96,
  "timestamp": "2026-09-12T10:35:00"
}
```

The Evidence Store enables:

* Evidence correlation
* Historical analysis
* Investigation replay
* RCA validation
* Future machine learning

---

# 13. Correlation Engine

The Correlation Engine combines evidence from:

* Database
* Operating system
* Logs
* Workload
* Historical incidents
* Recent changes

Example:

```text
Shared Pool Usage: High

+

Parse Rate: High

+

Cursor Growth: High

+

OS Memory: Healthy

↓

Possible Cause:

Application SQL Behavior
```

---

# 14. RCA Engine

The RCA Engine evaluates evidence and produces root cause hypotheses.

Each hypothesis includes:

* Root cause description
* Supporting evidence
* Contradicting evidence
* Confidence score

Example:

```text
Hypothesis:

Excessive hard parsing is causing Shared Pool pressure.

Confidence:

85%

Supporting Evidence:

- Shared Pool Usage: 96%
- Parse Rate Increased
- Cursor Growth Detected

Contradicting Evidence:

- No OS Memory Pressure
```

The RCA Engine should combine:

* Rules
* Evidence correlation
* DBA knowledge
* AI reasoning

---

# 15. Recommendation Engine

The Recommendation Engine generates recommended actions.

Each recommendation includes:

* Action
* Reason
* Risk level
* Required approval

Example:

```text
Recommendation:

Review application bind variable usage.

Reason:

High hard parsing and cursor growth detected.

Risk:

LOW

Approval:

DBA Review
```

---

# 16. DBA Approval

The platform must not automatically execute high-risk remediation.

Examples requiring DBA approval:

* ALTER SYSTEM
* Database restart
* Instance restart
* Shared Pool flush
* Configuration changes

---

# 17. AI and LLM Role

The LLM is used for:

* Evidence interpretation
* Hypothesis explanation
* Evidence summarization
* Recommendation generation
* Investigation assistance

The LLM should not:

* Directly query production databases
* Execute production commands
* Modify database configuration
* Restart databases
* Make unsupported RCA conclusions

---

# 18. Safety Architecture

The platform should enforce:

```text
READ-ONLY INVESTIGATION

        ↓

STRUCTURED EVIDENCE

        ↓

RULE VALIDATION

        ↓

AI REASONING

        ↓

GUARDRAILS

        ↓

DBA APPROVAL
```

---

# 19. Technology Direction

Initial implementation:

```text
Python

FastAPI

Database Drivers

Structured JSON

Rule Engine

LLM

GitHub
```

Future implementation:

```text
PostgreSQL

MongoDB

Cloud Databases

Historical Evidence

Vector Search

MCP

Advanced Agent Workflow
```

---

# 20. Development Roadmap

## Phase 1

Oracle ORA-04031

* Incident input
* Oracle evidence collection
* Structured evidence
* Rule-based correlation
* RCA hypotheses

## Phase 2

AI-assisted RCA

* LLM reasoning
* Evidence summaries
* Guardrails

## Phase 3

PostgreSQL

* Database incident playbooks
* Evidence collectors

## Phase 4

MongoDB

* Replica Set incidents
* Performance investigation

## Phase 5

Multi-Database Intelligence

* Cross-database patterns
* Historical incidents
* AI-assisted investigation planning

---

# 21. Final Architecture Principle

```text
DO NOT START WITH AI

START WITH EVIDENCE

        ↓

STRUCTURE DBA KNOWLEDGE

        ↓

AUTOMATE EVIDENCE COLLECTION

        ↓

CORRELATE FACTS

        ↓

USE AI FOR REASONING

        ↓

KEEP HUMAN APPROVAL
```

