import streamlit as st

def jalan_beton_flow():
    st.subheader("Jalan Beton")

    if st.button("Reset Inputs"):
        st.session_state.jalan_beton = None

    # Initialize or retrieve inputs from session state
    panjang = st.number_input("Panjang (m)", value=st.session_state.jalan_beton['panjang'] if st.session_state.jalan_beton else 0)
    lebar = st.number_input("Lebar (m)", value=st.session_state.jalan_beton['lebar'] if st.session_state.jalan_beton else 0)
    kedalaman = st.number_input("Kedalaman (cm)", value=st.session_state.jalan_beton['kedalaman'] if st.session_state.jalan_beton else 0)

    pekerjaan = st.selectbox("Pilih Jenis Pekerjaan", ["Galian", "Urugan"])

    if pekerjaan == "Galian":
        jenis_galian = st.selectbox("Jenis Galian", ["Galian Batu", "Galian Tanah", "Galian Lumpur", "Galian Pasir", "Galian Cadas"])
        metode = st.radio("Metode Pekerjaan", ["Manual", "Mekanis"])

        if st.button("Konfirmasi Galian"):
            st.session_state.jalan_beton = {
                'panjang': panjang,
                'lebar': lebar,
                'kedalaman': kedalaman,
                'pekerjaan': pekerjaan,
                'jenis_galian': jenis_galian,
                'metode': metode,
            }
            st.success("Input Galian disimpan! Lanjutkan ke Urugan.")

    elif pekerjaan == "Urugan":
        jenis_urugan = st.selectbox("Jenis Urugan", ["Urugan Batu Besar", "Urugan Kecil", "Urugan Pasir"])

        if st.button("Konfirmasi Urugan"):
            st.session_state.jalan_beton['pekerjaan_urugan'] = {
                'jenis_urugan': jenis_urugan,
            }
            st.success("Input Urugan disimpan! Lanjutkan ke pemasangan beton.")

    if st.session_state.jalan_beton and 'pekerjaan_urugan' in st.session_state.jalan_beton:
        st.write("### Pemasangan Beton")
        ketebalan_beton = st.selectbox("Ketebalan Beton", ["10 cm", "15 cm", "20 cm"])

        if st.button("Konfirmasi Pemasangan Beton"):
            st.session_state.jalan_beton['pemasangan_beton'] = {
                'ketebalan_beton': ketebalan_beton,
            }
            st.success("Pemasangan Beton selesai! Anda dapat melanjutkan ke opsi lainnya.")

if __name__ == "__main__":
    st.title("Estimasi RAB")
    jalan_beton_flow()
