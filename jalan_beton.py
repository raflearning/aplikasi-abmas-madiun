import streamlit as st
import pandas as pd
from io import BytesIO

def jalan_beton_flow():
    st.subheader("Jalan Beton")

    if st.button("Mulai Input"):
        st.session_state.jalan_beton = {}
        st.session_state.show_galian_input = True
        st.session_state.show_urugan_input = False
        st.session_state.show_paving_input = False
        st.session_state.show_estimasi_input = False

    # Bagian Galian
    if st.session_state.get('show_galian_input', False):
        st.write("### Pekerjaan Galian")
        jenis_galian = st.selectbox("Jenis Galian", ["Galian Batu", "Galian Tanah", "Galian Lumpur", "Galian Pasir", "Galian Cadas"])
        metode = st.radio("Metode Pekerjaan", ["Manual", "Mekanis", "Semi Mekanis"])

        panjang = st.number_input("Panjang Galian (m)", value=0)
        lebar = st.number_input("Lebar Galian (m)", value=0)
        kedalaman = st.number_input("Kedalaman Makadam", value=0)

        if st.button("Konfirmasi Galian", key="konfirmasi_galian"):
            if panjang == 0 or lebar == 0 or kedalaman == 0:
                st.error("Mohon masukkan panjang, lebar, dan kedalaman yang valid sebelum melanjutkan.")
            else:
                st.session_state.jalan_beton.update({
                    'pekerjaan': "Galian",
                    'jenis_galian': jenis_galian,
                    'metode': metode,
                    'panjang_galian': panjang,
                    'lebar_galian': lebar,
                    'kedalaman_galian': kedalaman,
                })
                st.success("Input Galian disimpan! Lanjutkan ke Urugan.")
                st.session_state.show_urugan_input = True

    # Bagian Urugan
    if st.session_state.get('show_urugan_input', False):
        st.write("### Pekerjaan Urugan")
        panjang_urugan = st.number_input("Panjang Urugan (m)", value=0)
        lebar_urugan = st.number_input("Lebar Urugan (m)", value=0)

        if st.button("Konfirmasi Urugan", key="konfirmasi_urugan"):
            if panjang_urugan == 0 or lebar_urugan == 0:
                st.error("Mohon masukkan panjang dan lebar yang valid sebelum melanjutkan.")
            else:
                st.session_state.jalan_beton.update({
                    'panjang_urugan': panjang_urugan,
                    'lebar_urugan': lebar_urugan,
                })
                st.success("Input Urugan disimpan! Tekan tombol Submit untuk menyimpan semua data.")
                st.session_state.show_paving_input = True

    #bagian pemasangan paving
    if st.session_state.get('show_paving_input', False):
        st.write("### Pemasangan Paving")
        panjang_paving = st.number_input("Panjang Paving (m)", value=0)
        lebar_paving = st.number_input("Lebar Paving (m)", value=0)
        ketebalan_paving = st.radio("Ketebalan Paving", ["8 cm", "6 cm"])

        if st.button("Konfirmasi Pemasangan Paving", key="konfirmasi_paving"):
            if panjang_paving == 0 or lebar_paving == 0:
                st.error("Mohon masukkan panjang, lebar, dan ketebalan yang valid sebelum melanjutkan.")
            else:
                st.session_state.jalan_beton.update({
                    'panjang_paving': panjang_paving,
                    'lebar_paving': lebar_paving,
                    'ketebalan_paving': ketebalan_paving,
                })
                st.success("Input Pemasangan Paving disimpan! Tekan tombol Submit untuk menyimpan semua data.")
                st.session_state.show_estimasi_input = True

    # Bagian Perhitungan Estimasi RAB
    if st.session_state.get('show_estimasi_input', False):
        st.write("### Perhitungan Estimasi RAB Pembuatan Jalan Beton")

        if st.button("Ekspor ke Excel"):
            data = {
                'Pekerjaan': ['Galian', 'Urugan','Pemasangan Paving'],
                'Jenis': [st.session_state.jalan_beton.get('jenis_galian'), 'Urugan', 'Pemasangan Paving'],
                'Metode': [st.session_state.jalan_beton.get('metode'), '', ''],
                'Panjang (m)': [st.session_state.jalan_beton.get('panjang_galian'), st.session_state.jalan_beton.get('panjang_urugan'), st.session_state.jalan_beton.get('jalan_paving')],
                'Lebar (m)': [st.session_state.jalan_beton.get('lebar_galian'), st.session_state.jalan_beton.get('lebar_urugan'), st.session_state.jalan_beton.get('lebar_paving')],
                'Kedalaman': [st.session_state.jalan_beton.get('kedalaman_galian'), '', st.session_state.jalan_beton.get('ketebalan_paving')]
            }

            df = pd.DataFrame(data)

            # Convert dataframe to Excel format
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='RAB Jalan Beton')
            output.seek(0)

            # Download the Excel file
            st.download_button(
                label="Download Excel",
                data=output,
                file_name="estimasi_rab_jalan_beton.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        if st.button("Konfirmasi dan Selesai"):
            st.success("RAB telah berhasil direkapitulasi dan selesai.")
            st.balloons()

if __name__ == "__main__":
    st.title("Estimasi RAB")
    jalan_beton_flow()