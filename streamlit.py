from langchain_ollama.llms import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import load_prompt
import os
import streamlit as st
from fpdf import FPDF
from datetime import datetime




model = OllamaLLM(model="llama3.2", base_url="http://localhost:11434")

prompt =load_prompt('workout.json')
parser = StrOutputParser()


def generate_workout(fitness_level, goal, duration, equipment):
    chain = prompt | model | parser
    result = chain.invoke({
        "fitness_level": fitness_level,
        "goal": goal,
        "duration": str(duration),
        "equipment": equipment
    })
    return result

# Function to create a PDF
def create_pdf(workout_plan, fitness_level, goal, duration, equipment):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Personalized Workout Plan", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Fitness Level: {fitness_level}", ln=True)
    pdf.cell(200, 10, txt=f"Goal: {goal}", ln=True)
    pdf.cell(200, 10, txt=f"Duration: {duration} minutes", ln=True)
    pdf.cell(200, 10, txt=f"Equipment: {equipment}", ln=True)
    pdf.ln(10)
    
    pdf.multi_cell(0, 10, workout_plan)
    
 # ✅ Get the Windows Downloads folder path
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    filename = f"Workout_Plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    full_path = os.path.join(downloads_folder, filename)

    pdf.output(full_path)
    return full_path

st.markdown("""
    <style>
    /* Style for all buttons */
    .stButton > button {
        background-color: #4CAF50;  /* Green */
        color: white;
        border: none;
        padding: 0.5em 1em;
        border-radius: 5px;
        font-weight: bold;
        font-size: 16px;
        transition: background-color 0.3s;
    }

    .stButton > button:hover {
        background-color: #45a049; /* Darker green on hover */
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)




st.title("🏋️‍♀️ Personalized Workout Planner")
st.markdown("Generate a custom workout plan tailored to your needs!")

with st.sidebar:
        st.header("Workout Preferences")
        fitness_level = st.selectbox(
            "Fitness Level",
            ["Beginner", "Intermediate", "Advanced"]
        )
        goal = st.selectbox(
            "Fitness Goal",
            ["Weight Loss", "Muscle Gain", "Endurance", "General Fitness"]
        )
        duration = st.number_input(
            "Duration (minutes)",
            min_value=10,
            max_value=120,
            value=30,
            step=5
        )
        equipment = st.selectbox(
            "Equipment Available",
            ["Bodyweight", "Dumbbells", "Gym Equipment", "Resistance Bands"]
        )
        
generate_button = st.button("Generate Workout Plan")

if "workout_history" not in st.session_state:
        st.session_state.workout_history = []

if generate_button:
    with st.spinner("Generating your workout plan..."):
        workout_plan = generate_workout(fitness_level, goal, duration, equipment)
        st.session_state.workout_history.append({
            "plan": workout_plan,
            "fitness_level": fitness_level,
            "goal": goal,
            "duration": duration,
            "equipment": equipment,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        st.success("✅ Workout plan generated successfully!")

    # Display workout plan
    st.subheader("Your Workout Plan")
    st.write(workout_plan)
    pdf_file = create_pdf(workout_plan, fitness_level, goal, duration, equipment)
    with open(pdf_file, "rb") as file:
        st.download_button(
            label="Download as PDF",
            data=file,
            file_name=pdf_file,
            mime="application/pdf"
        )
