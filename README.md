# Dependency Impact Explorer

Trace direct dependencies and discover downstream consumers in breadth-first order. Each affected component has a cited edge from a shortest impact path.

## Quick start

From this directory, run these commands with Python 3.12 or 3.13. The example corpus is fictional and runs offline with the standard library.

```sh
python3 core.py ask 'Impact of tax'
python3 core.py build data/source.json snapshot.json
python3 core.py ask 'Direct users of pricing' --snapshot snapshot.json
python3 -m unittest discover -v
python3 evaluate.py
```

## Asking questions

Ask “Impact of tax”, “Direct users of pricing” or “Dependencies of checkout”. A leaf with no recorded matches returns insufficient evidence.

## Using your own sources

Use the records in `data/source.json` as a schema example. Supply unique citation IDs and usable source locators. Build a new snapshot after additions, edits, or deletions. A successful build atomically replaces the previous snapshot. Results contain the answer, retrieval method and source locators. Unsupported queries return `insufficient_evidence`.

The graph describes declared component dependencies. Runtime imports, version resolution and observed outage impact require additional data.

See [QA.md](QA.md) for measured results, review status and release limits.
