# ARGUS — Argumentative Graph & Understanding System

> Cut through any Reddit thread in seconds. No endless scrolling.

ARGUS is a graph-based argument mapping engine for online conversations. 
Paste a Reddit thread URL → ARGUS builds a semantic argument graph underneath 
→ surfaces structured intelligence on top.

---

## What it does

Most Reddit summarizers feed comments into an LLM and get a paragraph back.  
ARGUS builds the argument structure first — mathematically — then uses an LLM 
only to articulate what the graph already found.

**The graph is the brain. The LLM is just the voice.**

---

## Planned Output (per thread)

- **Thread Verdict** — overall consensus or lack of it, influence-weighted
- **Argument Clusters** — distinct positions, each represented by the most original comment
- **Claim Map** — visual graph of which arguments support or contradict each other
- **The Outlier** — most semantically unique take in the entire thread
- **Query Box** — ask questions, get answers from the thread's own content

---

## Tech Stack (in progress)

- `Python` — core language
- `requests` — Reddit JSON fetching (no API key needed)
- `sentence-transformers` — comment embeddings
- `scikit-learn` — KMeans clustering
- `Neo4j` — graph database for argument nodes and edges
- `Google Gemini API` — LLM summarization
- `FastAPI` — backend
- `Streamlit` — frontend

---

## Current Progress

- [x] Fetch Reddit thread via `.json` trick (no PRAW needed)
- [x] Parse top-level comments with author, score, body
- [x] Extract first-level replies per comment
- [x] Filter deleted comments and AutoModerator noise
- [ ] Recursive deep reply traversal
- [ ] Sentence-transformer embeddings
- [ ] KMeans clustering
- [ ] Neo4j graph construction
- [ ] Gemini summarization
- [ ] FastAPI backend
- [ ] Streamlit frontend

---

## Setup

```bash
git clone https://github.com/GK-171107/Argus.git
cd Argus
pip install requests
python base.py
```

---

## Status

Active development. First year CSE undergrad building this as a research + portfolio project.

---

*Built by Ganeshkumar V*
