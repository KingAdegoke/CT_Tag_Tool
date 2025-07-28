# Educator Guide: Recognizing Computational Thinking in Non-Coding Games

**Author**: Samuel Adegoke  
**Project**: Computational thinking Tagging Tool for non coding video games.   
**Audience**: Educators.

---

##  What Is This Tool?

This tool is a lightweight, web-based platform designed to help educators recognize computational thinking  skills in gameplay scenarios from non-coding games like **Minecraft**, **Teamfight Tactics (TFT)**, and **Super Smash Bros**.

You don’t need a coding background. You don’t need to know the ins and outs of every game. You just need to observe how students approach gameplay. This tool also helps you map that behavior to computational thinking skills.

The goal: make it easy to connect student engagement with games to real skills.

---

##  What Is Computational Thinking?

Computational Thinking refers to a set of cognitive skills foundational to computer science but applicable in many disciplines. The tool uses the **Weintrop et al. (2016)** taxonomy:

- **Pattern Recognition**  
  Identifying trends, sequences, or similarities in events or strategies.

- **Abstraction**  
  Filtering out unimportant details to focus on the core structure of a problem.

- **Decomposition**  
  Breaking down complex tasks into manageable subproblems.

- **Algorithmic Thinking**  
  Creating a sequence of steps or rules to solve a problem.

- **Debugging**  
  Identifying and fixing mistakes through iteration.

- **Evaluation and Refinement**  
  Assessing outcomes and adjusting strategies for better performance.

---

##  How to Use the Tool

### 1. Upload a Gameplay Scenario
- Upload a short description of a gameplay moment.
- This can come from live observation, recordings, or student submissions.

### 2. Tag computational thinking Skills
- Use the checkboxes to identify which computational thinking skills appear in the scenario.
- Hover over the tooltip for a quick definition of each skill.
- Use the confidence slider to indicate how sure you are.
- Optionally, add a reflection note.

### 3. Review Visualizations
- **Bar chart**: Skill frequency across all scenarios.
- **Radar chart**: Skill distribution per scenario.
- **Pie chart**: Overall tag confidence.

These visuals help track trends across time, students, or games.

---

##  Sample Use Cases

###  New Educator Learning computational thinking
Use the tool to become familiar with computational thinking language and thinking patterns in a low-stakes, guided environment.

###  Experienced Teacher
Use the tool to support formative assessment or classroom reflection discussions. It’s a great conversation starter about strategic thinking in games.

---

##  Tips

- There are no right answers. Focus on surfacing thinking, not grading.
- Use radar charts to compare how students or teams engage with different skills.
- Let students tag their own gameplay to promote metacognition.
- Build a computational thinking skill portfolio across time or game formats.

---

## Getting Started
Run locally:  
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
