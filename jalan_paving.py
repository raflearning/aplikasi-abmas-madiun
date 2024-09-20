import streamlit as st
import pandas as pd
from io import BytesIO
import numpy as np
import HSPK
# from openpyxl import Workbook
# from openpyxl.utils.dataframe import dataframe_to_rows

def jalan_paving_flow():

    st.subheader("Jalan Paving")

    # Menambahkan 3 kolom untuk gambar di bagian atas
    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/paving 1.jpg", caption="1", use_column_width=True)

    with col2:
        st.image("assets/paving 2.jpg", caption="2", use_column_width=True)

    if st.button("Mulai Input"):
        st.session_state.jalan_paving = {}
        st.session_state.show_galian_input = True
        st.session_state.show_urugan_input = False
        st.session_state.show_paving_input = False
        st.session_state.show_estimasi_input = False

        st.session_state.rab_galian = None
        st.session_state.rab_pemadatan = None
        st.session_state.rab_pemasangan_paving = None
        st.session_state.rab_urugan = None

    # Bagian Galian
    if st.session_state.get('show_galian_input', False):
        st.write("### Pekerjaan Galian")
        jenis_galian = st.selectbox("Jenis Galian", ["Galian Batu", "Galian Tanah", "Galian Lumpur", "Galian Pasir", "Galian Cadas"])
        metode = st.radio("Metode Pekerjaan", ["Manual", "Mekanis", "Semi Mekanis"])
        panjang = st.number_input("Panjang Galian (m)", format="%.2f")
        lebar = st.number_input("Lebar Galian (m)", format="%.2f")
        kedalaman = st.number_input("Kedalaman Galian (m)", format="%.2f")

        if jenis_galian == "Galian Batu" and metode == "Manual":
            if kedalaman <= 1:
                tipe_koefisien = 'galian_1m'
            elif kedalaman >= 1 and kedalaman < 2:
                tipe_koefisien = 'galian_2m'
            elif kedalaman >= 2 and kedalaman < 3:
                tipe_koefisien = 'galian_3m'
            else:
                tipe_koefisien = 'penambahan_1m'

            galian_batu_manual = HSPK.GalianBatuManual(panjang, lebar, kedalaman, tipe_koefisien)
            rab_galian = galian_batu_manual.galian_batu_manual()
            st.session_state.rab_galian = rab_galian

        if jenis_galian == "Galian Tanah" and metode == "Manual":
            if kedalaman <= 1:
                tipe_koefisien = 'galian_1m'
            elif kedalaman >= 1 and kedalaman < 2:
                tipe_koefisien = 'galian_2m'
            elif kedalaman >= 2 and kedalaman < 3:
                tipe_koefisien = 'galian_3m'
            else:
                tipe_koefisien = 'penambahan_1m'

            galian_tanah_manual = HSPK.GalianTanahBiasaManual(panjang, lebar, kedalaman, tipe_koefisien)
            rab_galian = galian_tanah_manual.galian_tanah_biasa_manual()
            st.session_state.rab_galian = rab_galian
            
        if jenis_galian == "Galian Lumpur" and metode == "Manual":
            if kedalaman <= 1:
                tipe_koefisien = 'galian_1m'
            elif kedalaman >= 1 and kedalaman < 2:
                tipe_koefisien = 'galian_2m'
            elif kedalaman >= 2 and kedalaman < 3:
                tipe_koefisien = 'galian_3m'
            else:
                tipe_koefisien = 'penambahan_1m'

            galian_lumpur_manual = HSPK.GalianLumpurManual(panjang, lebar, kedalaman, tipe_koefisien)
            rab_galian = galian_lumpur_manual.galian_lumpur_manual()
            st.session_state.rab_galian = rab_galian

        if jenis_galian == "Galian Pasir" and metode == "Manual":
            if kedalaman <= 1:
                tipe_koefisien = 'galian_1m'
            elif kedalaman >= 1 and kedalaman < 2:
                tipe_koefisien = 'galian_2m'
            elif kedalaman >= 2 and kedalaman < 3:
                tipe_koefisien = 'galian_3m'
            else:
                tipe_koefisien = 'penambahan_1m'

            galian_pasir_manually = HSPK.GalianPasirManual(panjang, lebar, kedalaman, tipe_koefisien)
            rab_galian = galian_pasir_manually.galian_pasir_manual()
            st.session_state.rab_galian = rab_galian
            
        if jenis_galian == "Galian Cadas" and metode == "Manual":
            if kedalaman <= 1:
                tipe_koefisien = 'galian_1m'
            elif kedalaman >= 1 and kedalaman < 2:
                tipe_koefisien = 'galian_2m'
            elif kedalaman >= 2 and kedalaman < 3:
                tipe_koefisien = 'galian_3m'
            else:
                tipe_koefisien = 'penambahan_1m'

            galian_cadas_manual = HSPK.GalianTanahCadasManual(panjang, lebar, kedalaman, tipe_koefisien)
            rab_galian = galian_cadas_manual.galian_tanah_cadas_manual()
            st.session_state.rab_galian = rab_galian         

        if jenis_galian == "Galian Batu" and metode == "Mekanis":
            if kedalaman <= 1:
                volume_galian = 'galian_1m'
            elif kedalaman >= 1 and kedalaman < 2:
                volume_galian = 'galian_2m'
            elif kedalaman >= 2 and kedalaman < 3:
                volume_galian = 'galian_3m'
            else:
                volume_galian = 'penambahan_1m'

            galian_batu_mekanis = HSPK.GalianBatuDenganExcavator(panjang, lebar, kedalaman)
            rab_galian = galian_batu_mekanis.galian_biasa_dengan_excavator()
            st.session_state.rab_galian = rab_galian
            
        if jenis_galian == "Galian Tanah" and metode == "Mekanis":
            if kedalaman <= 1:
                volume_galian = 'galian_1m'
            elif kedalaman >= 1 and kedalaman < 2:
                volume_galian = 'galian_2m'
            elif kedalaman >= 2 and kedalaman < 3:
                volume_galian = 'galian_3m'
            else:
                volume_galian = 'penambahan_1m'

            galian_tanah_mekanis = HSPK.GalianTanahDenganExcavator(panjang, lebar, kedalaman)
            rab_galian = galian_tanah_mekanis.galian_tanah_dengan_excavator()
            st.session_state.rab_galian = rab_galian
            
        if jenis_galian == "Galian Lumpur" and metode == "Mekanis":
            if kedalaman <= 1:
                tipe_koefisien = 'galian_1m'
            elif kedalaman >= 1 and kedalaman < 2:
                tipe_koefisien = 'galian_2m'
            elif kedalaman >= 2 and kedalaman < 3:
                tipe_koefisien = 'galian_3m'
            else:
                tipe_koefisien = 'penambahan_1m'

            galian_lumpur_mekanis = HSPK.GalianLumpurMekanis(panjang, lebar, kedalaman)
            rab_galian = galian_lumpur_mekanis.galian_lumpur_mekanis()
            st.session_state.rab_galian = rab_galian
            
        if jenis_galian == "Galian Pasir" and metode == "Mekanis":
            if kedalaman <= 1:
                tipe_koefisien = 'galian_1m'
            elif kedalaman >= 1 and kedalaman < 2:
                tipe_koefisien = 'galian_2m'
            elif kedalaman >= 2 and kedalaman < 3:
                tipe_koefisien = 'galian_3m'
            else:
                tipe_koefisien = 'penambahan_1m'

            galian_pasir_manually = HSPK.GalianPasirManual(panjang, lebar, kedalaman, tipe_koefisien)
            rab_galian = galian_pasir_manually.galian_pasir_manual()
            st.session_state.rab_galian = rab_galian
            
        if jenis_galian == "Galian Cadas" and metode == "Mekanis":
            if kedalaman <= 1:
                tipe_koefisien = 'galian_1m'
            elif kedalaman >= 1 and kedalaman < 2:
                tipe_koefisien = 'galian_2m'
            elif kedalaman >= 2 and kedalaman < 3:
                tipe_koefisien = 'galian_3m'
            else:
                tipe_koefisien = 'penambahan_1m'

            galian_cadas_manual = HSPK.GalianTanahCadasManual(panjang, lebar, kedalaman, tipe_koefisien)
            rab_galian = galian_cadas_manual.galian_tanah_cadas_manual()
            st.session_state.rab_galian = rab_galian
            
        if jenis_galian == "Galian Batu" and metode == "Semi Mekanis":
            if kedalaman <= 1:
                tipe_koefisien = 'galian_1m'
            elif kedalaman >= 1 and kedalaman < 2:
                tipe_koefisien = 'galian_2m'
            elif kedalaman >= 2 and kedalaman < 3:
                tipe_koefisien = 'galian_3m'
            else:
                tipe_koefisien = 'penambahan_1m'

            galian_batu_semimekanis = HSPK.GalianBatuSemiMekanis(panjang, lebar, kedalaman, tipe_koefisien)
            rab_galian = galian_batu_semimekanis.galian_batu_semi_mekanis()
            st.session_state.rab_galian = rab_galian
            
        if jenis_galian == "Galian Tanah" and metode == "Semi Mekanis":
            if kedalaman <= 1:
                tipe_koefisien = 'galian_1m'
            elif kedalaman >= 1 and kedalaman < 2:
                tipe_koefisien = 'galian_2m'
            elif kedalaman >= 2 and kedalaman < 3:
                tipe_koefisien = 'galian_3m'
            else:
                tipe_koefisien = 'penambahan_1m'

            galian_tanah_semimekanis = HSPK.GalianTanahBiasaSemiMekanis(panjang, lebar, kedalaman, tipe_koefisien)
            rab_galian = galian_tanah_semimekanis.galian_tanah_biasa_semi_mekanis()
            st.session_state.rab_galian = rab_galian      

        if jenis_galian == "Galian Lumpur" and metode == "Semi Mekanis":
            if kedalaman <= 1:
                tipe_koefisien = 'galian_1m'
            elif kedalaman >= 1 and kedalaman < 2:
                tipe_koefisien = 'galian_2m'
            elif kedalaman >= 2 and kedalaman < 3:
                tipe_koefisien = 'galian_3m'
            else:
                tipe_koefisien = 'penambahan_1m'

            galian_lumpur_semimekanis = HSPK.GalianLumpurSemiMekanis(panjang, lebar, kedalaman, tipe_koefisien)
            rab_galian = galian_lumpur_semimekanis.galian_lumpur_semi_mekanis()
            st.session_state.rab_galian = rab_galian
            
        if jenis_galian == "Galian Pasir" and metode == "Semi Mekanis":
            if kedalaman <= 1:
                tipe_koefisien = 'galian_1m'
            elif kedalaman >= 1 and kedalaman < 2:
                tipe_koefisien = 'galian_2m'
            elif kedalaman >= 2 and kedalaman < 3:
                tipe_koefisien = 'galian_3m'
            else:
                tipe_koefisien = 'penambahan_1m'

            galian_pasir_semimekanis = HSPK.GalianPasirSemiMekanis(panjang, lebar, kedalaman, tipe_koefisien)
            rab_galian = galian_pasir_semimekanis.galian_pasir_semi_mekanis()
            st.session_state.rab_galian = rab_galian
            
        if jenis_galian == "Galian Cadas" and metode == "Semi Mekanis":
            if kedalaman <= 1:
                tipe_koefisien = 'galian_1m'
            elif kedalaman >= 1 and kedalaman < 2:
                tipe_koefisien = 'galian_2m'
            elif kedalaman >= 2 and kedalaman < 3:
                tipe_koefisien = 'galian_3m'
            else:
                tipe_koefisien = 'penambahan_1m'

            galian_cadas_semimekanis = HSPK.GalianTanahCadasSemiMekanis(panjang, lebar, kedalaman, tipe_koefisien)
            rab_galian = galian_cadas_semimekanis.galian_tanah_cadas_semi_mekanis()
            st.session_state.rab_galian = rab_galian     

        if st.button("Konfirmasi Galian", key="konfirmasi_galian"):
            if panjang == 0 or lebar == 0:
                st.error("Mohon masukkan panjang, lebar, dan kedalaman yang valid sebelum melanjutkan.")
            else:
                st.session_state.jalan_paving.update({
                    'jenis_galian': jenis_galian,
                    'metode': metode,
                    'panjang': panjang,
                    'lebar': lebar,
                    'kedalaman': kedalaman,
                })
                st.success("Input Galian disimpan! Lanjutkan ke Urugan.")
                st.session_state.show_urugan_input = True
                st.session_state.show_galian_input = False

    # Bagian Urugan
    if st.session_state.get('show_urugan_input', False):
        st.write("### Pekerjaan Urugan")
        panjang_urugan = st.number_input("Panjang Urugan (m)", format="%.2f")
        lebar_urugan = st.number_input("Lebar Urugan (m)", format="%.2f")
        kedalaman_urugan = st.number_input("Kedalaman Urugan (m)", format="%.2f")
        pemadatan_urugan = st.selectbox("Jenis Pemadatan", ["Stamper", "Bulldozer"])

        urugan_sirtu_padat = HSPK.Urugan(panjang_urugan, lebar_urugan, kedalaman_urugan, 'sirtu_padat')
        rab_urugan = urugan_sirtu_padat.urugan()
        st.session_state.rab_urugan = rab_urugan
        
        if pemadatan_urugan == "Stamper":
            pemadatan_stamper = HSPK.PemadatanTanahDenganStamper(panjang_urugan, lebar_urugan, kedalaman_urugan)
            rab_pemadatan = pemadatan_stamper.pemadatan_tanah_dengan_stamper()
            st.session_state.rab_pemadatan = rab_pemadatan
            
        else:
            pemadatan_bulldozer = HSPK.PemadatanTanahDenganBulldozer(panjang_urugan, lebar_urugan, kedalaman_urugan)
            rab_pemadatan = pemadatan_bulldozer.pemadatan_dengan_stamper()
            st.session_state.rab_pemadatan = rab_pemadatan
            
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

        if jenis_paving == "Paving Berwarna" and ketebalan_paving == "6 cm":
            tipe_koefisien = 'paving_berwarna_6cm' 
        elif jenis_paving == "Paving Berwarna" and ketebalan_paving == "8 cm":
            tipe_koefisien = 'paving_berwarna_8cm'
        elif jenis_paving == "Paving Natural" and ketebalan_paving == "6 cm":
            tipe_koefisien = 'paving_natural_6cm'
        elif jenis_paving == "Paving Natural" and ketebalan_paving == "8 cm":
            tipe_koefisien = 'paving_natural_8cm'

        pemasangan_paving = HSPK.PemasanganPaving(panjang_paving, lebar_paving, tipe_koefisien)
        rab_pemasangan_paving = pemasangan_paving.hasil_perhitungan()
        st.session_state.rab_pemasangan_paving = rab_pemasangan_paving

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
            df_galian = pd.DataFrame(st.session_state.rab_galian['data'])
            df_urugan = pd.DataFrame(st.session_state.rab_urugan['data'])
            df_pemadatan = pd.DataFrame(st.session_state.rab_pemadatan['data'])
            df_pemasangan_paving = pd.DataFrame(st.session_state.rab_pemasangan_paving['data'])

            # Menggabungkan semua data frame
            df_combined = pd.concat([df_galian, df_urugan, df_pemadatan, df_pemasangan_paving], ignore_index=True)

            # Membuat workbook dan worksheet baru
            wb = Workbook()
            ws = wb.active
            ws.title = "RAB Jalan Paving"

            # Menambahkan data frame ke worksheet
            for r in dataframe_to_rows(df_combined, index=False, header=True):
                ws.append(r)

            # Menggabungkan sel sesuai kebutuhan
            ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=7)
            ws.merge_cells(start_row=5, start_column=1, end_row=5, end_column=7)
            ws.merge_cells(start_row=8, start_column=1, end_row=8, end_column=7)
            ws.merge_cells(start_row=15, start_column=1, end_row=15, end_column=7)

            # Convert workbook to BytesIO
            output = BytesIO()
            wb.save(output)
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

    #setiap rab bentuk dict dibentuk session state
