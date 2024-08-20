import streamlit as st

def jalan_paving_flow():
    st.subheader("Jalan Paving")

    # Clear previous inputs if navigating to a new section
    if st.button("Reset Inputs"):
        st.session_state.jalan_paving = None

    # Initialize or retrieve inputs from session state
    panjang = st.number_input("Panjang (m)", value=st.session_state.jalan_paving['panjang'] if st.session_state.jalan_paving else 0)
    lebar = st.number_input("Lebar (m)", value=st.session_state.jalan_paving['lebar'] if st.session_state.jalan_paving else 0)
    kedalaman = st.number_input("Kedalaman (cm)", value=st.session_state.jalan_paving['kedalaman'] if st.session_state.jalan_paving else 0)

    pekerjaan = st.selectbox("Pilih Jenis Pekerjaan", ["Galian", "Urugan"])

    # Dynamic content based on the selected pekerjaan
    if pekerjaan == "Galian":
        jenis_galian = st.selectbox("Jenis Galian", ["Galian Batu", "Galian Tanah", "Galian Lumpur", "Galian Pasir", "Galian Cadas"])
        metode = st.radio("Metode Pekerjaan", ["Manual", "Mekanis", "Semi Mekanis"])

        # Save Galian input in session state when confirmed
        if st.button("Konfirmasi Galian"):
            st.session_state.jalan_paving = {
                'panjang': panjang,
                'lebar': lebar,
                'kedalaman': kedalaman,
                'pekerjaan': pekerjaan,
                'jenis_galian': jenis_galian,
                'metode': metode,
            }
            st.success("Input Galian disimpan! Lanjutkan ke Urugan.")
    
    elif pekerjaan == "Urugan":
        jenis_urugan = st.selectbox("Jenis Urugan", ["Urugan Batu Besar", "Urugan Batu Kecil", "Urugan Pasir"])

        # Save Urugan input in session state when confirmed
        if st.button("Konfirmasi Urugan"):
            st.session_state.jalan_paving['pekerjaan_urugan'] = {
                'jenis_urugan': jenis_urugan,
            }
            st.success("Input Urugan disimpan! Lanjutkan ke pemasangan paving.")

    # Pemasangan Paving: This step is mandatory after both Galian and Urugan
    if st.session_state.jalan_paving and 'pekerjaan_urugan' in st.session_state.jalan_paving:
        st.write("### Pemasangan Paving")
        ketebalan_paving = st.selectbox("Ketebalan Paving", ["6 cm", "8 cm"])

        if st.button("Konfirmasi Pemasangan Paving"):
            st.session_state.jalan_paving['pemasangan_paving'] = {
                'ketebalan_paving': ketebalan_paving,
            }
            st.success("Pemasangan Paving selesai! Anda dapat melanjutkan ke opsi lainnya.")

# Example use:
if __name__ == "__main__":
    st.title("Estimasi RAB")
    jalan_paving_flow()
