import streamlit as st
from streamlit.components.v1 import html

def show_congrats_popup():
    # Custom HTML/CSS for a centered popup
    popup_html = """
    <div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); 
        background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        z-index: 1000; text-align: center; max-width: 400px;'>
        <h2>Congratulations! 🎉</h2>
        <p>You've completed your 30-day audiobook streak!</p>
        <p>Your dedication to daily listening is truly impressive!</p>
    </div>
    <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
        background-color: rgba(0, 0, 0, 0.5); z-index: 999;'>
    </div>
    """
    return popup_html

def success_page():
    # Set page config
    st.set_page_config(page_title="Audiobook Streak - Success", page_icon="🎧")
    
    # Main content
    st.title("30-Day Streak Champion! 🏆")
    st.write("You've reached an incredible milestone in your audiobook journey!")
    
    # Celebration visuals
    st.balloons()
    
    # Streak stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Days Completed", "30")
    with col3:
        st.metric("Achievement", "Tier 1")
    
    
    # Center the generate story button
    st.markdown("<div style='text-align: center; margin-top: 20px;'>", unsafe_allow_html=True)
    if st.button("Generate Story", key="generate_btn"):
        st.session_state.show_popup = False
        st.success("Story generated successfully!")
        audio_file_path = "output.wav"  # or "/kaggle/working/output.wav" if you're on Kaggle
        try:
            with open(audio_file_path, "rb") as audio_file:
                st.audio(audio_file.read(), format="audio/wav")
        except FileNotFoundError:
            st.warning("Audio file not found. Please ensure 'output.wav' exists.")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Additional content
    st.subheader("Your Achievement")
    st.write("Feel free to share your success with friends and keep the streak going!")

if __name__ == "__main__":
    success_page()