# Samuel Adegoke
# sadegoke3@gatech.edu
import streamlit as st
import pandas as pd
import json
import os
from collections import Counter
import plotly.express as px

def clear_inputs():
    st.session_state["title"] = ""
    st.session_state["game_name"] = ""
    st.session_state["scenario_text"] = ""
    st.session_state["confidence"] = 3
    st.session_state["reflection"] = ""
    for skill in ct_skills:
        st.session_state[skill] = False
    global tagging_history
    tagging_history = []
    with open(history_file, "w") as f:
        json.dump(tagging_history, f, indent=2)


st.set_page_config(page_title="CT Tagging Tool", layout="wide")
st.title("Computational Thinking Tagging Tool")
os.makedirs("data", exist_ok=True)
history_file = "data/tagged_data.json"

if os.path.exists(history_file):
    with open(history_file, "r") as f:
        tagging_history = json.load(f)
else:
    tagging_history = []

left_col, right_col = st.columns(2)
with left_col:
    title = st.text_input("Scenario Title", placeholder="e.g., Redstone Elevator Debugging", key="title_input")
    st.header("Upload or Select a Gameplay Scenario")
    upload_type = st.radio("Upload Type", ["Text Description"])
    game_name = st.text_input("Game Title", placeholder="e.g., Minecraft, TFT, Super Smash Bros, etc.", key="game_input")
    scenario_text = ""
    if upload_type == "Text Description":
        scenario_text = st.text_area("Paste gameplay scenario here", placeholder="Describe the gameplay scenario in detail...", key="scenario_input")
    st.subheader("Scenario Preview")

    if scenario_text:
        st.write(scenario_text)
with right_col:
    st.header("Tag Computational Thinking Skills")
    ct_skills = {
        "Pattern Recognition": "Identifying recurring structures, patterns, or behaviors in gameplay.",
        "Abstraction": "Focusing on essential information while ignoring extraneous details.",
        "Decomposition": "Breaking a complex task into smaller, solvable parts.",
        "Algorithmic Thinking": "Designing a series of steps or rules to reach a goal.",
        "Debugging": "Finding and fixing mistakes or inefficiencies.",
        "Evaluation and Refinement": "Assessing and improving a solution or strategy."
    }
    selected_skills = []
    st.markdown("**Select CT Skills (hover to learn more):**")
    for skill, tooltip in ct_skills.items():
        if st.checkbox(skill, help=tooltip, key=f"skill_{skill}"):
            selected_skills.append(skill)
    confidence = st.slider("Confidence in tagging (1 = low, 5 = high)", 1, 5, 3 ,key="confidence_slider")
    reflection = st.text_area("Reflection or notes (optional)", placeholder="Any additional thoughts or context about the tagging...", key="reflection_input")

    if st.button("Submit Tags"):
        if not game_name:
            st.warning("Please enter the game title.")
        elif not scenario_text:
            st.warning("Please provide a gameplay scenario.")
        elif not selected_skills:
            st.warning("Please select at least one CT skill.")
        else:
            submission = {
                "Game": game_name,
                "Title": title,
                "Scenario": scenario_text,
                "Selected Skills": selected_skills,
                "Confidence": confidence,
                "Reflection": reflection
            }
            tagging_history.append(submission)
            with open(history_file, "w") as f:
                json.dump(tagging_history, f, indent=2)
            st.success("Tags submitted successfully!")
            st.json(submission)
st.markdown("---")
st.header("Tagging Summary and Visualizations")
if tagging_history:
    all_skills = []
    for record in tagging_history:
        for skill in record["Selected Skills"]:
            all_skills.append(skill)
    skill_counter = Counter(all_skills)
    bar_chart = pd.DataFrame(skill_counter.items(), columns=["Skill", "Frequency"])
    st.subheader("Skill Frequency (Bar Chart)")
    st.plotly_chart(px.bar(bar_chart, x="Skill", y="Frequency", title="CT Skill Frequency"))
    st.subheader("Skill Distribution (Pie Chart)")
    st.plotly_chart(px.pie(bar_chart, names="Skill", values="Frequency", title="Skill Distribution"))
    skill_confidence = {}
    for skill in ct_skills:
        skill_confidence[skill] = []
    for record in tagging_history:
        for skill in record["Selected Skills"]:
            skill_confidence[skill].append(record["Confidence"])
    avg_confidences = []
    for vals in skill_confidence.values():
        if vals:
            avg_confidences.append(sum(vals) / len(vals))
        else:
            avg_confidences.append(0)
    radar_chart = pd.DataFrame({
        "Skill": list(skill_confidence.keys()),
        "Avg Confidence": avg_confidences
    })
    st.subheader("Average Confidence by Skill (Radar Chart)")
    st.plotly_chart(px.line_polar(radar_chart, r="Avg Confidence", theta="Skill", line_close=True))
    st.markdown("---")
    st.header("Educator Summary")
    most_common = bar_chart.sort_values("Frequency", ascending=False).head(3)
    confidences = []
    for r in tagging_history:
        confidences.append(r["Confidence"])
    avg_conf = round(sum(confidences) / len(confidences), 2)
    st.markdown(f"""
    - **Total Scenarios Tagged**: {len(tagging_history)}
    - **Most Common Skills**: {', '.join(most_common['Skill'].tolist())}
    - **Average Confidence Level**: {avg_conf}/5
    """)

    st.subheader("Export Tagged Data")
    df_export = pd.DataFrame(tagging_history)
    csv_data = df_export.to_csv(index=False)
    st.download_button("Download as CSV", csv_data, "tagged_data.csv", "text/csv")
else:
    st.info("No submissions yet. Submit some tags to see visualizations.")
st.markdown("---")
with st.expander("Reset Tagged Data"):
    st.warning("This will permanently delete all submitted scenarios, reset visualizations, and clear current inputs.")
    if st.button("Reset All Data"):
        clear_inputs()
        st.success("All data and inputs cleared. Please refresh the page.")

