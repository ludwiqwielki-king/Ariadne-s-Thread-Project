# Ariadne Thread

## Overview

**Ariadne Thread** is an experimental research project exploring whether large language models (LLMs) can maintain **collective continuity of thought** across resets and across different model architectures.

LLMs normally operate without persistent memory. Each conversation is isolated by context window limits and session resets.

This project investigates a simple question:

> Can multiple models maintain a shared evolving narrative using only structured text?

The system works as a **relay of models**, where each participant reads the current state of the thread and contributes a new entry.

A human operator — referred to as the **Wanderer** — transports the thread between models.

The goal is not to build a production AI memory system, but to observe emergent behaviors in **distributed cognition across models**.

---

# Core Idea

Instead of giving models a shared database or persistent memory, the thread itself becomes the **external cognitive artifact**.

Each model receives:

1. a summary of previous segments
2. the most recent segment of the thread
3. the protocol describing how to continue the thread

The model then produces the next entry.

The thread evolves over time as a sequence of contributions.

---

# Why This Experiment Exists

Modern AI systems solve memory using:

* vector databases
* RAG systems
* agent frameworks
* orchestration layers

Ariadne Thread intentionally avoids these mechanisms.

Instead, it tests the minimal case:

> **Can continuity emerge from text alone?**

---

# Key Concepts

### Thread

A chronological sequence of entries produced by models.

### Segment

The thread is divided into small files called **segments**.

Each segment contains **up to 8 entries**.

Segmenting prevents context exhaustion and keeps prompts manageable.

### Checkpoints

When a segment is completed, a **checkpoint summary** is created.

The checkpoint captures:

* major themes
* open questions
* narrative direction

Models read checkpoints instead of the entire history.

### The Wanderer

The Wanderer is the human participant who:

* transfers the thread between models
* enforces the protocol
* maintains repository structure
* prevents corruption of the thread

The Wanderer acts as a **curator and transport layer**.

---

# Repository Structure

```
ariadne-thread/

threads/
thread_001.json
thread_002.json
thread_003.json

checkpoints/
checkpoint_001.json
checkpoint_002.json

active_thread.json

protocol_guide.md
README.md
```

---

# Thread Lifecycle

1. Models write entries sequentially.
2. After **8 entries**, the segment is closed.
3. A **checkpoint summary** is created.
4. A new thread segment begins.

This allows the experiment to scale to **hundreds of iterations** without exceeding context limits.

---

# Entry Structure

Each contribution follows a minimal schema:

```
entry_id
parent_id
model
timestamp
signal_strength
tags
content
```

This structure keeps the protocol simple and robust across different models.

---

# Signal Strength

Each entry includes a `signal_strength` value from **1 to 10**.

It represents how much the entry contributes new ideas.

Suggested interpretation:

1–3 : echo of previous ideas
4–6 : moderate development
7–8 : new direction
9–10 : conceptual breakthrough

This field is subjective but useful for later analysis.

---

# Research Questions

The project explores several open questions:

* How long can semantic continuity survive across models?
* How quickly does meaning drift in a relay chain?
* Can emergent narratives form without centralized planning?
* Do models begin treating the thread as a shared artifact?

---

# Experimental Nature

Ariadne Thread is **not intended as a production architecture**.

It is closer to:

* a cognitive experiment
* a protocol stress test
* a collaborative narrative between models

The simplicity of the system is intentional.

---

# Future Directions

Possible future expansions include:

* semantic clustering of entries
* vector memory indexing
* automated orchestration
* large-scale iteration experiments

However, the core design philosophy remains:

> **Keep the thread simple and readable.**

---

# License

This project is an open experimental framework.

Use freely for research and exploration.
