import streamlit as st

def jalan_makadam_flow():
    st.subheader("Jalan Makadam")

    if st.button("Reset Inputs"):
        st.session_state.jalan_makadam = None

    panjang = st.number_input("Panjang (m)", value=st.session_state.jalan_makadam['panjang'] if st.session_state.jalan_makadam else 0)
    lebar = st.number_input("Lebar (m)", value=st.session_state.jalan_makadam['lebar'] if st.session_state.jalan_makadam else 0)
    kedalaman = st.number_input("Kedalaman (cm)", value=st.session_state.jalan_makadam['kedalaman'] if st.session_state.jalan_makadam else 0)

    pekerjaan = st.selectbox("Pilih Jenis Pekerjaan", ["Galian", "Urugan"])

    if pekerjaan == "Galian":
        jenis_galian = st.selectbox("Jenis Galian", ["Galian Batu", "Galian Tanah", "Galian Lumpur", "Galian Pasir", "Galian Cadas"])
        metode = st.radio("Metode Pekerjaan", ["Manual", "Mekanis"])

        if st.button("Konfirmasi Galian"):
            st.session_state.jalan_makadam = {
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
            st.session_state.jalan_makadam['pekerjaan_urugan'] = {
                'jenis_urugan': jenis_urugan,
            }
            st.success("Input Urugan disimpan! Lanjutkan ke pemasangan makadam.")

    if st.session_state.jalan_makadam and 'pekerjaan_urugan' in st.session_state.jalan_makadam:
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
