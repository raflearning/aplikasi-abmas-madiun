import streamlit as st
import pandas as pd
from io import BytesIO
from estimasi_rab import show_estimasi_rab

def jalan_makadam_flow():
    st.subheader("Jalan Makadam")

    # Menambahkan 2 kolom untuk gambar di bagian atas
    col1, col2 = st.columns(2)

    with col1:
        st.image("jalan makadam 1.jpg", caption="1", use_column_width=True)

    with col2:
        st.image("jalan makadam 2.jpg", caption="2", use_column_width=True)

    # Tombol untuk memulai input
    if st.button("Mulai Input"):
        st.session_state.jalan_makadam = {}
        st.session_state.show_galian_input = True
        st.session_state.show_urugan_input = False
        st.session_state.show_estimasi_input = False

    # Bagian Galian
    if st.session_state.get('show_galian_input', False):
        st.write("### Pekerjaan Galian")
        jenis_galian = st.selectbox("Jenis Galian", ["Galian Batu", "Galian Tanah", "Galian Lumpur", "Galian Pasir", "Galian Cadas"])
        metode = st.radio("Metode Pekerjaan", ["Manual", "Mekanis", "Semi Mekanis"])

        panjang = st.number_input("Panjang Galian (m)", format="%.2f", min_value=0.0)
        lebar = st.number_input("Lebar Galian (m)", format="%.2f", min_value=0.0)
        kedalaman = st.number_input("Kedalaman Makadam (m)", format="%.2f", min_value=0.0)

        if st.button("Konfirmasi Galian", key="konfirmasi_galian"):
            if panjang == 0 or lebar == 0 or kedalaman == 0:
                st.error("Mohon masukkan panjang, lebar, dan kedalaman yang valid sebelum melanjutkan.")
            else:
                st.session_state.jalan_makadam.update({
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
        st.write("### Pekerjaan Pemasangan Jalan Makadam")
        panjang_urugan = st.number_input("Panjang Urugan (m)", format="%.2f", min_value=0.0)
        lebar_urugan = st.number_input("Lebar Urugan (m)", format="%.2f", min_value=0.0)
        pemadatan_urugan = st.selectbox("Jenis Pemadatan", ["Stamper", "Bulldozer"])

        if st.button("Konfirmasi Urugan", key="konfirmasi_urugan"):
            if panjang_urugan == 0 or lebar_urugan == 0:
                st.error("Mohon masukkan panjang dan lebar yang valid sebelum melanjutkan.")
            else:
                st.session_state.jalan_makadam.update({
                    'panjang_urugan': panjang_urugan,
                    'lebar_urugan': lebar_urugan,
                    'pemadatan_urugan': pemadatan_urugan,
                })
                st.success("Input Urugan disimpan! Tekan tombol Submit untuk menyimpan semua data.")
                st.session_state.show_estimasi_input = True

    # Bagian Perhitungan Estimasi RAB
    if st.session_state.get('show_estimasi_input', False):
        st.write("### Perhitungan Estimasi RAB Pembuatan Jalan Makadam")

        if st.button("Lihat Estimasi RAB"):
            show_estimasi_rab()

        if st.button("Konfirmasi dan Selesai"):
            st.success("RAB telah berhasil direkapitulasi dan selesai.")
            st.balloons()

            # Simpan dataframe untuk estimasi RAB di session state
            data = {
                'Pekerjaan': ['Galian', 'Urugan'],
                'Jenis': [
                    st.session_state.jalan_makadam.get('jenis_galian', ''),
                    st.session_state.jalan_makadam.get('pemadatan_urugan', '')
                ],
                'Metode': [
                    st.session_state.jalan_makadam.get('metode', ''),
                    st.session_state.jalan_makadam.get('pemadatan_urugan', '')
                ],
                'Panjang (m)': [
                    st.session_state.jalan_makadam.get('panjang_galian', 0),
                    st.session_state.jalan_makadam.get('panjang_urugan', 0)
                ],
                'Lebar (m)': [
                    st.session_state.jalan_makadam.get('lebar_galian', 0),
                    st.session_state.jalan_makadam.get('lebar_urugan', 0)
                ],
                'Kedalaman (m)': [
                    st.session_state.jalan_makadam.get('kedalaman_galian', 0),
                    0  # Kedalaman Urugan tidak diinput
                ]
            }
            df_final_with_margin = pd.DataFrame(data)
            st.session_state.df_final_with_margin = df_final_with_margin

    # Menampilkan dan Menyediakan Tombol Unduh Excel jika Dataframe Tersedia
    if 'df_final_with_margin' in st.session_state:
        st.write("### Download Estimasi RAB")
        df = st.session_state.df_final_with_margin

        # Konversi DataFrame ke format Excel
        def to_excel(df):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Estimasi RAB')
            processed_data = output.getvalue()
            return processed_data

        excel_data = to_excel(df)

        # Tombol untuk mendownload file Excel
        st.download_button(
            label="Download Excel",
            data=excel_data,
            file_name="estimasi_rab.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

if __name__ == "__main__":
    st.title("Estimasi RAB")
    
    # Inisialisasi session_state jika belum ada
    if 'show_galian_input' not in st.session_state:
        st.session_state.show_galian_input = False
    if 'show_urugan_input' not in st.session_state:
        st.session_state.show_urugan_input = False
    if 'show_estimasi_input' not in st.session_state:
        st.session_state.show_estimasi_input = False
    if 'jalan_makadam' not in st.session_state:
        st.session_state.jalan_makadam = {}
    if 'df_final_with_margin' not in st.session_state:
        st.session_state.df_final_with_margin = None

    jalan_makadam_flow()