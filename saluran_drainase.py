import streamlit as st

def saluran_drainase_flow():
    st.subheader("Saluran Drainase")

    if st.button("Reset Inputs"):
        st.session_state.saluran_drainase = None

    panjang = st.number_input("Panjang (m)", value=st.session_state.saluran_drainase['panjang'] if st.session_state.saluran_drainase else 0)
    lebar = st.number_input("Lebar (m)", value=st.session_state.saluran_drainase['lebar'] if st.session_state.saluran_drainase else 0)
    kedalaman = st.number_input("Kedalaman (cm)", value=st.session_state.saluran_drainase['kedalaman'] if st.session_state.saluran_drainase else 0)

    pekerjaan = st.selectbox("Pilih Jenis Pekerjaan", ["Galian", "Urugan"])

    if pekerjaan == "Galian":
        jenis_galian = st.selectbox("Jenis Galian", ["Galian Batu", "Galian Tanah", "Galian Lumpur", "Galian Pasir", "Galian Cadas"])
        metode = st.radio("Metode Pekerjaan", ["Manual", "Mekanis"])

        if st.button("Konfirmasi Galian"):
            st.session_state.saluran_drainase = {
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
            st.session_state.saluran_drainase['pekerjaan_urugan'] = {
                'jenis_urugan': jenis_urugan,
            }
            st.success("Input Urugan disimpan! Lanjutkan ke pemasangan drainase.")

    if st.session_state.saluran_drainase and 'pekerjaan_urugan' in st.session_state.saluran_drainase:
        st.write("### Pemasangan Drainase")
        jenis_saluran = st.selectbox("Jenis Saluran", ["Saluran Terbuka", "Saluran Tertutup"])
        bahan_drainase = st.selectbox("Bahan Drainase", ["Beton", "Bata", "PVC"])

        if st.button("Konfirmasi Pemasangan Drainase"):
            st.session_state.saluran_drainase['pemasangan_drainase'] = {
                'jenis_saluran': jenis_saluran,
                'bahan_drainase': bahan_drainase,
            }
            st.success("Pemasangan Drainase selesai! Anda dapat melanjutkan ke opsi lainnya.")

if __name__ == "__main__":
    st.title("Estimasi RAB")
    saluran_drainase_flow()
