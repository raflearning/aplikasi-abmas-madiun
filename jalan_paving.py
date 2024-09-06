import streamlit as st
import pandas as pd
from io import BytesIO

def jalan_paving_flow():
    st.subheader("Jalan Paving")

    # Menambahkan 3 kolom untuk gambar di bagian atas
    col1, col2 = st.columns(2)

    with col1:
        st.image("paving 1.jpg", caption="1", use_column_width=True)

    with col2:
        st.image("paving 2.jpg", caption="2", use_column_width=True)

    if st.button("Mulai Input"):
        st.session_state.jalan_paving = {}
        st.session_state.show_galian_input = True
        st.session_state.show_urugan_input = False
        st.session_state.show_paving_input = False
        st.session_state.show_estimasi_input = False

    # Bagian Galian
    if st.session_state.get('show_galian_input', False):
        st.write("### Pekerjaan Galian")
        jenis_galian = st.selectbox("Jenis Galian", ["Galian Batu", "Galian Tanah", "Galian Lumpur", "Galian Pasir", "Galian Cadas"])
        metode = st.radio("Metode Pekerjaan", ["Manual", "Mekanis", "Semi Mekanis"])

        panjang = st.number_input("Panjang Galian (m)", format="%.2f", )
        lebar = st.number_input("Lebar Galian (m)", format="%.2f")
        kedalaman = st.number_input("Kedalaman Galian (cm)", format="%d", max_value=100)

        if st.button("Konfirmasi Galian", key="konfirmasi_galian"):
            if panjang == 0 or lebar == 0:
                st.error("Mohon masukkan panjang, lebar, dan kedalaman yang valid sebelum melanjutkan.")
            else:
                st.session_state.jalan_paving.update({
                    'jenis_galian': jenis_galian,
                    'metode': metode,
                    'panjang_galian': panjang,
                    'lebar_galian': lebar,
                    'kedalaman_galian': kedalaman,
                })
                st.success("Input Galian disimpan! Lanjutkan ke Urugan.")
                st.session_state.show_urugan_input = True
                st.session_state.show_galian_input = False

    # Bagian Urugan
    if st.session_state.get('show_urugan_input', False):
        st.write("### Pekerjaan Urugan")
        panjang_urugan = st.number_input("Panjang Urugan (m)", format="%.2f")
        lebar_urugan = st.number_input("Lebar Urugan (m)", format="%.2f")
        kedalaman_urugan = st.number_input("Kedalaman Urugan (cm)", format="%d", max_value=100)
        pemadatan_urugan = st.selectbox("Jenis Pemadatan", ["Stamper", "Bulldozer"])

        if st.button("Konfirmasi Urugan", key="konfirmasi_urugan"):
            if panjang_urugan == 0 or lebar_urugan == 0:
                st.error("Mohon masukkan panjang dan lebar kedalaman yang valid sebelum melanjutkan.")
            else:
                st.session_state.jalan_paving.update({
                    'panjang_urugan': panjang_urugan,
                    'lebar_urugan': lebar_urugan,
                    'kedalaman_urugan': lebar_urugan,
                    'pemadatan_urugan': pemadatan_urugan,
                })
                st.success("Input Urugan disimpan! Lanjutkan ke Pemasangan Paving.")
                st.session_state.show_paving_input = True
                st.session_state.show_urugan_input = False

    # Pemasangan Paving: This step is mandatory after both Galian and Urugan
    if st.session_state.get('show_paving_input', False):
        st.write("### Pemasangan Paving")
        panjang_paving = st.number_input("Panjang Daerah Paving (m)", format="%.2f", )
        lebar_paving = st.number_input("Lebar Daerah Paving (m)", format="%.2f")
        jenis_paving = st.selectbox("Jenis Paving", ["Paving Berwarna", "Paving Natural"])
        ketebalan_paving = st.selectbox("Ketebalan Paving", ["6 cm", "8 cm"])

        if st.button("Konfirmasi Pemasangan Paving", key="Konfirmasi_Pemasangan_Paving"):
            st.session_state.jalan_paving.update({
                'panjang_paving': panjang_paving,
                'lebar_paving': lebar_paving,
                'Jenis_paving': jenis_paving,
                'ketebalan_paving': ketebalan_paving,
            })
            st.success("Input Paving disimpan! Tekan tombol Submit untuk menyimpan semua data.")
            st.session_state.show_estimasi_input = True
            st.session_state.show_paving_input = False

    # Bagian Perhitungan Estimasi RAB
    if st.session_state.get('show_estimasi_input', False):

        st.write("### Perhitungan Estimasi RAB Pembuatan Jalan Paving")

        if st.button("Ekspor ke Excel"):
            data = {
                'Pekerjaan': ['Galian', 'Urugan', 'Pemasangan Paving'],
                'Jenis': [st.session_state.jalan_paving.get('jenis_galian'), '', st.session_state.jalan_paving.get('jenis_paving')],
                'Metode': [st.session_state.jalan_paving.get('metode'), '', ''],
                'Panjang (m)': [st.session_state.jalan_paving.get('panjang_galian'), st.session_state.jalan_paving.get('panjang_urugan'), st.session_state.jalan_paving.get('panjang_paving')],
                'Lebar (m)': [st.session_state.jalan_paving.get('lebar_galian'), st.session_state.jalan_paving.get('lebar_urugan'), st.session_state.jalan_paving.get('lebar_paving')],
                'Kedalaman': [st.session_state.jalan_paving.get('kedalaman_galian'), st.session_state.jalan_paving.get('kedalaman_urugan'), ''],
                'Ketebalan Paving': ['', '', st.session_state.jalan_paving.get('ketebalan_paving')],
                'Pemadatan': ['', st.session_state.jalan_paving.get('pemadatan_urugan'), ''],
            }

            df = pd.DataFrame(data)

            # Convert dataframe to Excel format
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='RAB Jalan Paving')
            output.seek(0)

            # Download the Excel file
            st.download_button(
                label="Download Excel",
                data=output,
                file_name="estimasi_rab_jalan_paving.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        if st.button("Konfirmasi dan Selesai"):
            st.success("RAB telah berhasil direkapitulasi dan selesai.")
            st.balloons()

if __name__ == "__main__":
    st.title("Estimasi RAB")
    jalan_paving_flow()
