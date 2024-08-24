import streamlit as st

def jalan_makadam_flow():
    st.subheader("Jalan Makadam")

    if "jalan_makadam" not in st.session_state:
        st.session_state.jalan_makadam = {}

    if st.button("Reset Inputs"):
        st.session_state.jalan_makadam = {}

    pekerjaan = st.selectbox("Pilih Jenis Pekerjaan", ["Galian", "Urugan"])

    if pekerjaan == "Galian":
        jenis_galian = st.selectbox("Jenis Galian", ["Galian Batu", "Galian Tanah", "Galian Lumpur", "Galian Pasir", "Galian Cadas"])
        metode = st.radio("Metode Pekerjaan", ["Manual", "Mekanis"])

        if st.button("Lanjutkan ke Input Dimensi Galian"):
            st.session_state.jalan_makadam.update({
                'pekerjaan': pekerjaan,
                'jenis_galian': jenis_galian,
                'metode': metode,
            })
            st.session_state.show_galian_input = True

    if st.session_state.get('show_galian_input', False) and pekerjaan == "Galian":
        st.write("### Input Dimensi Galian")
        panjang = st.number_input("Panjang Galian (m)", value=0)
        lebar = st.number_input("Lebar Galian (m)", value=0)
        kedalaman = st.number_input("Kedalaman Galian (cm)", value=0)

        if st.button("Konfirmasi Galian"):
            st.session_state.jalan_makadam.update({
                'panjang': panjang,
                'lebar': lebar,
                'kedalaman': kedalaman,
            })
            st.success("Input Galian disimpan! Lanjutkan ke Urugan.")
            st.session_state.show_galian_input = False

    elif pekerjaan == "Urugan":
        jenis_urugan = st.selectbox("Jenis Urugan", ["Urugan Batu Besar", "Urugan Kecil", "Urugan Pasir"])

        if st.button("Lanjutkan ke Input Dimensi Urugan"):
            st.session_state.jalan_makadam.update({
                'pekerjaan': pekerjaan,
                'jenis_urugan': jenis_urugan,
            })
            st.session_state.show_urugan_input = True

    if st.session_state.get('show_urugan_input', False) and pekerjaan == "Urugan":
        st.write("### Input Dimensi Urugan")
        panjang = st.number_input("Panjang Urugan (m)", value=0)
        lebar = st.number_input("Lebar Urugan (m)", value=0)
        kedalaman = st.number_input("Kedalaman Urugan (cm)", value=0)

        if st.button("Konfirmasi Urugan"):
            st.session_state.jalan_makadam.update({
                'panjang': panjang,
                'lebar': lebar,
                'kedalaman': kedalaman,
            })
            st.success("Input Urugan disimpan! Lanjutkan ke pemasangan makadam.")
            st.session_state.show_urugan_input = False

    if 'jenis_urugan' in st.session_state.jalan_makadam:
        st.write("### Pemasangan Makadam")
        ketebalan_makadam = st.selectbox("Ketebalan Makadam", ["10 cm", "15 cm", "20 cm"])

        if st.button("Konfirmasi Pemasangan Makadam"):
            st.session_state.jalan_makadam['pemasangan_makadam'] = {
                'ketebalan_makadam': ketebalan_makadam,
            }
            st.success("Pemasangan Makadam selesai! Anda dapat melanjutkan ke opsi lainnya.")

if __name__ == "__main__":
    st.title("Estimasi RAB")
    jalan_makadam_flow()