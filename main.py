import streamlit as st
from generate_mcqs import RAGMCQGenerator
from adaptive_module import AdaptiveEngine

st.set_page_config(page_title="Adaptive MCQ Generator", layout="wide")

# ----------------------------------------------------------
# Initialize session state
# ----------------------------------------------------------
if "engine" not in st.session_state:
    st.session_state.engine = AdaptiveEngine()

if "generator" not in st.session_state:
    st.session_state.generator = RAGMCQGenerator()

if "topics" not in st.session_state:
    st.session_state.topics = st.session_state.generator.load_all_topics_from_blueprint()

if "history" not in st.session_state:
    st.session_state.history = []

if "current_mcq" not in st.session_state:
    st.session_state.current_mcq = None

# ----------------------------------------------------------
# Functions
# ----------------------------------------------------------
def prepare_next_mcq():
    engine = st.session_state.engine
    generator = st.session_state.generator
    topics = st.session_state.topics

    spec = engine.get_next_question_spec(topics)
    topic = spec["topic"]
    difficulty = spec["difficulty"]

    mcq = generator.generate_mcq(topic, difficulty)

    st.session_state.current_mcq = mcq


def submit_answer(user_choice):
    mcq = st.session_state.current_mcq
    engine = st.session_state.engine

    correct_letter = mcq["correct_answer"]
    result = 1 if user_choice == correct_letter else 0

    # update theta
    new_theta = engine.update_theta(mcq["difficulty"], result)

    # save history
    st.session_state.history.append({
        "question": mcq["question"],
        "options": mcq["options"],
        "chosen_answer": user_choice,
        "correct_answer": correct_letter,
        "result": result,
        "topic": mcq["topic"],
        "difficulty": mcq["difficulty"],
        "theta_after": new_theta
    })

    # prepare next question
    prepare_next_mcq()


# ----------------------------------------------------------
# UI
# ----------------------------------------------------------
st.title("🎯 Adaptive MCQ Generator")

# Right panel: stats
with st.sidebar:
    st.header("📊 Adaptive Engine Metrics")

    st.write(f"**θ (ability):** `{round(st.session_state.engine.theta, 3)}`")
    st.write(f"**Questions answered:** {len(st.session_state.history)}")

    if st.session_state.history:
        correct = sum(h["result"] for h in st.session_state.history)
        incorrect = len(st.session_state.history) - correct
        st.write(f"**Correct:** {correct}")
        st.write(f"**Incorrect:** {incorrect}")

    st.markdown("### Last 5 topics used")
    for h in st.session_state.history[-5:]:
        st.write(f"- {h['topic']} ({h['difficulty']})")


# ----------------------------------------------------------
# Start or show MCQ
# ----------------------------------------------------------
if st.session_state.current_mcq is None:
    if st.button("Start Adaptive Session"):
        prepare_next_mcq()
        st.rerun()

else:
    mcq = st.session_state.current_mcq

    st.subheader(f"Topic: **{mcq['topic']}**   |   Difficulty: **{mcq['difficulty']}**")
    st.write(mcq["question"])

    user_choice = st.radio("Choose your answer:", list(mcq["options"].keys()),
                           format_func=lambda x: f"{x}. {mcq['options'][x]}")

    if st.button("Submit Answer"):
        submit_answer(user_choice)
        st.rerun()

# ----------------------------------------------------------
# Reset Button
# ----------------------------------------------------------
st.markdown("---")
if st.button("Reset Session ❌"):
    st.session_state.engine = AdaptiveEngine()
    st.session_state.history = []
    st.session_state.current_mcq = None
    st.rerun()
