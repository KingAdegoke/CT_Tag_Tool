# Computational Thinking Tagging Tool

This project is a lightweight, educator-facing tool for recognizing and annotating **computational thinking (CT)** skills in non-coding games like Minecraft, Teamfight Tactics (TFT), and Super Smash Bros. Built with Streamlit, the tool provides an intuitive tagging interface and real-time visual feedback through interactive charts.

## Features

- Simple tagging UI for educators (no coding required)
- Upload and annotate gameplay scenarios
- Interactive visualizations (bar chart, radar chart, pie chart)
- Support for JSON-based data storage and export
- Accessibility features (keyboard nav, ARIA labels)

---

## Getting Started

### Prerequisites

You’ll need Python 3.7+ installed. Then install the dependencies:

```bash
pip install -r requirements.txt
```
From the root directory of the project, run:

```bash
streamlit run ct_tagger.py
```

## Documentation

- **Educator Guide:** See `educator_guide.md` for classroom usage instructions.
- **User Personas:** Example educators and use case flows are described in `user_personas.md`.

## Example Datasets

You can explore or expand the example gameplay scenarios and annotations in:

- `scenarios.json` – sample inputs
- `tagged_data.json` – outputs from the tool after tagging
