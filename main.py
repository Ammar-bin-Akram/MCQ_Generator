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

if "mcq_limit" not in st.session_state:
    st.session_state.mcq_limit = None

if "mcq_count" not in st.session_state:
    st.session_state.mcq_count = 0


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

    # Update ability level θ
    new_theta = engine.update_theta(mcq["difficulty"], result)

    # Save history
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

    st.session_state.mcq_count += 1

    # If more questions needed → generate next
    if st.session_state.mcq_count < st.session_state.mcq_limit:
        prepare_next_mcq()
    else:
        st.session_state.current_mcq = None


# ----------------------------------------------------------
# Sidebar Stats Panel
# ----------------------------------------------------------
st.title("🎯 Adaptive MCQ Generator")

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
# MCQ Setup Panel (Input + Start Button Together)
# ----------------------------------------------------------
if st.session_state.mcq_limit is None:
    st.markdown("### 🔢 MCQ Session Setup")

    mcq_limit_input = st.number_input(
        "Enter number of MCQs:",
        min_value=1,
        max_value=100,
        value=None,
        step=1,
        placeholder="Enter number of MCQs..."
    )

    start_clicked = st.button("Start Adaptive Session")

    if start_clicked:
        if mcq_limit_input is None:
            st.warning("⚠️ Please enter how many MCQs you want before starting.")
            st.stop()
        else:
            st.session_state.mcq_limit = int(mcq_limit_input)
            st.session_state.mcq_count = 0
            prepare_next_mcq()
            st.rerun()

    st.stop()


# ----------------------------------------------------------
# If limit is set → Show MCQs
# ----------------------------------------------------------

# Completed all MCQs?
if st.session_state.mcq_count >= st.session_state.mcq_limit:
    st.success(f"You have completed {st.session_state.mcq_limit} MCQs! 🎉")
    if st.button("Restart Session"):
        st.session_state.engine = AdaptiveEngine()
        st.session_state.history = []
        st.session_state.current_mcq = None
        st.session_state.mcq_count = 0
        st.session_state.mcq_limit = None
        st.rerun()

# If no current MCQ generated (should not happen but safe guard)
elif st.session_state.current_mcq is None:
    prepare_next_mcq()
    st.rerun()

# Show MCQ
else:
    mcq = st.session_state.current_mcq

    st.subheader(f"Topic: **{mcq['topic']}**   |   Difficulty: **{mcq['difficulty']}**")
    st.write(mcq["question"])

    user_choice = st.radio(
        "Choose your answer:",
        list(mcq["options"].keys()),
        format_func=lambda x: f"{x}. {mcq['options'][x]}"
    )

    if st.button("Submit Answer"):
        submit_answer(user_choice)
        st.rerun()


# ----------------------------------------------------------
# Reset Button
# ----------------------------------------------------------
st.markdown("---")
if st.button("Reset Session"):
    st.session_state.engine = AdaptiveEngine()
    st.session_state.history = []
    st.session_state.current_mcq = None
    st.session_state.mcq_count = 0
    st.session_state.mcq_limit = None
    st.rerun()
