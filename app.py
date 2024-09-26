import streamlit as st
from jalan_paving import jalan_paving_flow
from jalan_beton import jalan_beton_flow
from jalan_makadam import jalan_makadam_flow
from saluran_drainase import saluran_drainase_flow

def main():
    st.title("Estimasi RAB Proyek Jalan dan Drainase Desa")

    # Initialize session state for each section if not already done
    if 'jalan_paving' not in st.session_state:
        st.session_state.jalan_paving = None
    if 'jalan_beton' not in st.session_state:
        st.session_state.jalan_beton = None
    if 'jalan_makadam' not in st.session_state:
        st.session_state.jalan_makadam = None
    if 'saluran_drainase' not in st.session_state:
        st.session_state.saluran_drainase = None

    menu = ["Home", "Jalan", "Saluran Drainase"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.write("Selamat datang di aplikasi Estimasi RAB Proyek Jalan dan Drainase Desa.")
        st.write("Pilih kategori proyek untuk memulai.")
    elif choice == "Jalan":
        jalan_options = ["Pilih jenis jalan", "Jalan Paving", "Jalan Beton", "Jalan Makadam"]
        jalan_choice = st.selectbox("Pilih jenis jalan", jalan_options)
        
        if jalan_choice == "Jalan Paving":
            jalan_paving_flow()
        elif jalan_choice == "Jalan Beton":
            jalan_beton_flow()
        elif jalan_choice == "Jalan Makadam":
            jalan_makadam_flow()
    elif choice == "Saluran Drainase":
        saluran_drainase_flow()
    elif choice == "Estimasi RAB":
        show_estimasi_rab()

if __name__ == '__main__':
    main()
