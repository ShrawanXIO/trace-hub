# trace-hub
Trace Hub is a Chainlit extension for the Trace Auto-Gen engine. It orchestrates Archivist, Author, and Auditor agents to build high-quality tests via RAG. Features a persistent SQL ledger for story versioning and project-specific KB sync.

# Trace Hub

**Trace Hub** is a Chainlit extension for the Trace Auto-Gen engine. It orchestrates Archivist, Author, and Auditor agents to build high-quality tests via RAG. Features a persistent SQL ledger for story versioning and project-specific KB sync.

---

## Core Capabilities

* **Multi-Agent Orchestration**: Centrally managed workflow coordinating specialized agents to transform requirements into test cases.
* **Intelligent Retrieval (RAG)**: Uses an Archivist agent to query legacy data and functional specs to prevent redundant test creation.
* **Quality Auditing**: An automated Auditor agent verifies drafts against user stories, rejecting logic failures until quality gates are passed.
* **Persistent Memory**: Every user story, agent trace, and generated artifact is stored in a relational database for historical reference and version control.
* **Structured Output**: A Scribe agent converts AI drafts into formatted CSV files ready for manual or automated execution.



---

## System Architecture

Trace Hub acts as the conversational interface for the underlying **Trace Auto-Gen** engine.

### Agent Responsibilities
1.  **Manager**: Orchestrates the start-to-finish workflow and handles input parsing.
2.  **Archivist**: Connects to the Vector Store to retrieve context and reconcile legacy IDs.
3.  **Author**: Drafts the initial test cases based on provided context and task lists.
4.  **Auditor**: Reviews the Author's work against requirements to ensure logic accuracy.
5.  **Scribe**: Formats the final approved content into a structured CSV file.

---

## Repository Structure

```text
trace-hub/
├── app/
│   ├── core/           # Logic connecting Chainlit to the Manager Agent
│   ├── db/             # SQLAlchemy models for story and session persistence
│   ├── settings/       # Knowledge Base path configuration and project binding
│   └── ui/             # Chainlit interface custom components
├── database/           # SQLite/PostgreSQL storage files
├── engine/             # Core Trace Auto-Gen agent logic (Manager, Author, etc.)
├── main.py             # System entry point and conversational flow
├── requirements.txt    # Platform dependencies
└── .env                # API keys and project-specific environment variables
