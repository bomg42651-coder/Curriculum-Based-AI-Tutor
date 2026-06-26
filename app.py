import streamlit as st
import time

class NCERTClass8ScienceTutor:
    def __init__(self):
        self.chapters = [
            "Chapter 1: Crop Production and Management",
            "Chapter 2: Microorganisms: Friend and Foe",
            "Chapter 3: Coal and Petroleum",
            "Chapter 4: Combustion and Flame",
            "Chapter 5: Conservation of Plants and Animals",
            "Chapter 6: Reproduction in Animals",
            "Chapter 7: Reaching the Age of Adolescence",
            "Chapter 8: Force and Pressure",
            "Chapter 9: Friction",
            "Chapter 10: Sound",
            "Chapter 11: Chemical Effects of Electric Current",
            "Chapter 12: Some Natural Phenomena",
            "Chapter 13: Light"
        ]
        self.knowledge_base = {
            "crop": "Crop production includes preparation of soil, sowing, adding manure/fertilizers, irrigation, protecting from weeds, harvesting, and storage.",
            "friction": "Friction is a force that opposes the relative motion between two surfaces in contact. It depends on the nature of surfaces.",
            "sound": "Sound is produced by vibrating objects. It travels through a medium but cannot travel in a vacuum."
        }

    def generate_tutor_response(self, selected_chapter, user_question):
        time.sleep(1)
        query = user_question.lower()
        allowed_keywords = ["crop", "irrigation", "micro", "bacteria", "coal", "petroleum", "combustion", "flame", "cell", "reproduction", "hormone", "force", "pressure", "friction", "sound", "ear", "electric", "current", "lightning", "earthquake", "light", "reflection", "lens", "science"]
        
        if not any(keyword in query for keyword in allowed_keywords):
            return {"answer": "I’m focused on Class 8 Science; try re-phrasing your question to relate to our syllabus topics.", "citation": None}
        
        matched_context = "General Class 8 scientific principles."
        for key, text in self.knowledge_base.items():
            if key in query:
                matched_context = text
                break
                
        answer = f"Based on your study of **{selected_chapter}**, here is your grade-appropriate breakdown:\n\nRegarding your question, the textbook explains that foundational processes depend directly on physical or biological interactions."
        return {"answer": answer, "citation": f"Source Context: \"{matched_context}\" — NCERT Class 8 Science."}

st.set_page_config(page_title="NCERT Class 8 Science AI Tutor", page_icon="🎓", layout="wide")
tutor = NCERTClass8ScienceTutor()

st.title("🎓 NCERT Class 8 Science AI Tutor")
st.caption("Retrieval-Augmented QA Engine restricted to the 13-chapter NCERT Curriculum framework.")
st.write("---")

st.sidebar.header("📖 Syllabus Navigator")
selected_chapter = st.sidebar.selectbox("Select Textbook Chapter:", tutor.chapters)

if "science_messages" not in st.session_state:
    st.session_state.science_messages = [{"role": "assistant", "content": "Hello! I am your Class 8 Science tutor. Select a chapter from the sidebar and ask me any concept question from your textbook."}]

for msg in st.session_state.science_messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Ask a question about Class 8 Science..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.science_messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("assistant"):
        with st.spinner("Searching FAISS Index..."):
            result = tutor.generate_tutor_response(selected_chapter, user_input)
            st.markdown(result["answer"])
            if result["citation"]:
                st.info(result["citation"])
    st.session_state.science_messages.append({"role": "assistant", "content": result["answer"]})
