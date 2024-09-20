import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

def show_estimasi_rab():
    st.subheader("Estimasi RAB")

    # Mengakses data dari jalan_makadam, jalan_paving, dan jalan_beton
    jalan_makadam = st.session_state.get('jalan_makadam', {})
    jalan_paving = st.session_state.get('jalan_paving', {})
    jalan_beton = st.session_state.get('jalan_beton', {})
    
    if not jalan_makadam and not jalan_paving and not jalan_beton:
        st.warning("Data tidak ditemukan. Mohon input data pada salah satu branch terlebih dahulu.")
        return

    # Menampilkan data untuk masing-masing jenis jalan jika ada
    if jalan_makadam:
        st.write("### Data Jalan Makadam")
        jenis_galian = jalan_makadam.get('jenis_galian', '')
        metode = jalan_makadam.get('metode', '')
        pemadatan_urugan = jalan_makadam.get('pemadatan_urugan', '')
        
        if 'panjang_galian' in jalan_makadam and 'lebar_galian' in jalan_makadam and 'kedalaman_galian' in jalan_makadam:
            # Menghitung volume galian makadam
            volume_galian = jalan_makadam['panjang_galian'] * jalan_makadam['lebar_galian'] * jalan_makadam['kedalaman_galian']

        if 'panjang_urugan' in jalan_makadam and 'lebar_urugan' in jalan_makadam :
            luas_urugan = jalan_makadam['panjang_urugan'] * jalan_makadam['lebar_urugan']

        if 'panjang_urugan' in jalan_makadam and 'lebar_urugan' in jalan_makadam and 'kedalaman_urugan' in jalan_makadam :
            volume_pemadatan = jalan_makadam['panjang_urugan'] * jalan_makadam['lebar_urugan'] * jalan_makadam['kedalaman_urugan']

    if jalan_paving:
        st.write("### Data Jalan Paving")
        jenis_galian = jalan_paving.get('jenis_galian', '')
        metode = jalan_paving.get('metode', 'Manual')
        
        if 'panjang_galian' in jalan_paving and 'lebar_galian' in jalan_paving and 'kedalaman_galian' in jalan_paving:
            # Menghitung volume galian paving
            volume_galian = jalan_paving['panjang_galian'] * jalan_paving['lebar_galian'] * jalan_paving['kedalaman_galian']
     

        if 'panjang_urugan' in jalan_paving and 'lebar_urugan' in jalan_paving:
            luas_urugan = jalan_paving['panjang_urugan'] * jalan_paving['lebar_urugan']

    if jalan_beton:
        st.write("### Data Jalan Beton")
        jenis_galian = jalan_beton.get('jenis_galian', '')
        metode = jalan_beton.get('metode', 'Manual')
        
        if 'panjang_galian' in jalan_beton and 'lebar_galian' in jalan_beton and 'kedalaman_galian' in jalan_beton:
            # Menghitung volume galian beton
            volume_galian = jalan_beton['panjang_galian'] * jalan_beton['lebar_galian'] * jalan_beton['kedalaman_galian']

        if 'panjang_urugan' in jalan_beton and 'lebar_urugan' in jalan_beton:
            luas_urugan = jalan_beton['panjang_urugan'] * jalan_beton['lebar_urugan']

    # Inisialisasi data
    data = {}

    # Definisi data untuk tabel berdasarkan jenis_galian dan metode
    if jenis_galian == 'Galian Batu':
        if metode == 'Manual':
            data_galian = {
                'Uraian': ['Galian', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan, 3.378, 0.3378],
                'Volume': [np.nan] + [volume_galian] * 2,  # Menggunakan np.nan untuk baris pertama
                'Satuan': [np.nan, 'OH', 'OH'],
                'Harga Satuan': [np.nan, 81500, 98000],
                'Jumlah': [np.nan] * 3
            }
        elif metode == 'Semi Mekanis':
            data_galian = {
                'Uraian': ['Galian', 'Pertamina dex', 'Jack Hammer', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan, 2.5, 0.25, 1, 0.1],
                'Volume': [np.nan] + [volume_galian] * 4,  # Menggunakan np.nan untuk baris pertama
                'Satuan': [np.nan, 'liter', 'sewa-harian', 'OH', 'OH'],
                'Harga Satuan': [np.nan, 13300, 44700, 81500, 98000],
                'Jumlah': [np.nan] * 5
            }
        elif metode == 'Mekanis':
            data_galian = {
                'Uraian': ['Galian', 'Compressor', 'Jack Hammer', 'Wheel Loader', 'Excavator', 'Dump Truck', 'Pekerja (Buruh Tidak Terampil)', 'Mandor'],
                'Koefisien': [np.nan, 0.0738, 0.0738, 0.0738, 0.0738, 0.3329, 0.0843, 0.0105],
                'Volume': [np.nan] + [volume_galian] * 7,  # Menggunakan np.nan untuk baris pertama
                'Satuan': [np.nan, 'jam', 'jam','jam','jam','jam', 'OH', 'OH'],
                'Harga Satuan': [np.nan, 212427.45, 38465.57, 538209.99, 819402.32, 339612.94, 81500, 98000],
                'Jumlah': [np.nan] * 8
            }
    elif jenis_galian == 'Galian Tanah':
        if metode == 'Manual':
            data_galian = {
                'Uraian': ['Galian', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan, 0.563, 0.0675],
                'Volume': [np.nan] + [volume_galian] * 2,  # Menggunakan np.nan untuk baris pertama
                'Satuan': [np.nan, 'OH', 'OH'],
                'Harga Satuan': [np.nan, 81500, 98000],
                'Jumlah': [np.nan] * 3
            }
        elif metode == 'Semi Mekanis':
            data_galian = {
                'Uraian': ['Galian', 'Pertamina dex', 'Jack Hammer', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan, 0.5, 0.05, 0.22, 0.022],
                'Volume': [np.nan] + [volume_galian] * 4,  # Menggunakan np.nan untuk baris pertama
                'Satuan': [np.nan, 'liter', 'sewa-harian', 'OH', 'OH'],
                'Harga Satuan': [np.nan, 13300, 44700, 81500, 98000],
                'Jumlah': [np.nan] * 5
            }
        if metode == 'Mekanis':
            data_galian = {
                'Uraian': ['Galian', 'Excavator','Pekerja', 'Mandor'],
                'Koefisien': [np.nan, 0.0414, 0.83, 0.083],
                'Volume': [np.nan] + [volume_galian] * 3,
                'Satuan': [np.nan, 'jam', 'OH', 'OH'],
                'Harga Satuan': [np.nan, 819402.32, 81500, 98000],
                'Jumlah': [np.nan] * 4
            }
    elif jenis_galian == 'Galian Lumpur':
        if metode == 'Manual':
            data_galian = {
                'Uraian': ['Galian', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan, 0.83, 0.083],
                'Volume': [np.nan] + [volume_galian] * 2,
                'Satuan': [np.nan, 'OH', 'OH'],
                'Harga Satuan': [np.nan, 81500, 98000],
                'Jumlah': [np.nan, np.nan, np.nan]
            }
        elif metode == 'Semi Mekanis':
            data_galian = {
                'Uraian': ['Galian', 'Pertamina dex', 'Mesin Pompa Lumpur', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan, 0.9, 0.0009, 0.24, 0.024],
                'Volume': [np.nan] + [volume_galian] * 4,
                'Satuan': [np.nan, 'liter', 'sewa-harian', 'OH', 'OH'],
                'Harga Satuan': [np.nan, 13300, 339221000, 81500, 98000],
                'Jumlah': [np.nan, np.nan, np.nan, np.nan, np.nan]
            }
        elif metode == 'Mekanis':
            data_galian = {
                'Uraian': ['Galian', 'Dump Truck', 'Excavator', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan, 0.07, 0.067, 0.226, 0.007],
                'Volume': [np.nan] + [volume_galian] * 4,
                'Satuan': [np.nan, 'jam', 'jam', 'OH', 'OH'],
                'Harga Satuan': [np.nan, 339612.94, 819402.32, 81500, 98000],
                'Jumlah': [np.nan, np.nan, np.nan, np.nan, np.nan]
            }
    elif jenis_galian == 'Galian Cadas':
        if metode == 'Manual':
            data_galian = {
                'Uraian': ['Galian', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan, 1.25, 0.125],
                'Volume': [np.nan] + [volume_galian] * 2,
                'Satuan': [np.nan, 'OH', 'OH'],
                'Harga Satuan': [np.nan, 81500, 98000],
                'Jumlah': [np.nan, np.nan, np.nan]
            }
        elif metode == 'Semi Mekanis':
            data_galian = {
                'Uraian': ['Galian', 'Pertamina dex', 'Jack Hammer', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan, 1.25, 0.125, 0.32, 0.032],
                'Volume': [np.nan] + [volume_galian] * 4,
                'Satuan': [np.nan, 'liter', 'sewa-harian', 'OH', 'OH'],
                'Harga Satuan': [np.nan, 13300, 44700, 81500, 98000],
                'Jumlah': [np.nan, np.nan, np.nan, np.nan, np.nan]
            }
    elif jenis_galian == 'Galian Pasir':
        if metode == 'Manual':
            data_galian = {
                'Uraian': ['Galian', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan, 0.66, 0.066],
                'Volume': [np.nan] + [volume_galian] * 2,
                'Satuan': [np.nan, 'OH', 'OH'],
                'Harga Satuan': [np.nan, 81500, 98000],
                'Jumlah': [np.nan, np.nan, np.nan]
            }
        elif metode == 'Semi Mekanis':
            data_galian = {
                 'Uraian': ['Galian', 'Pertamina dex', 'Mesin Pompa Lumpur', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan, 1.1, 0.0002, 0.1, 0.01],
                'Volume': [np.nan] + [volume_galian] * 4,
                'Satuan': [np.nan, 'liter', 'sewa-harian', 'OH', 'OH'],
                'Harga Satuan': [np.nan, 13300, 339221000, 81500, 98000],
                'Jumlah': [np.nan, np.nan, np.nan, np.nan, np.nan]
            }
 
    else:
        st.warning("Jenis galian tidak valid atau belum dipilih.")
        return


   # Definisi data untuk tabel urugan
    data_urugan = {
            'Uraian': ['Urugan', 'Batu Belah', 'Batu Pecah Uk. 1-2 cm (mesin)', 'Pasir Lokal', 'Pekerja', 'Mandor'],
            'Koefisien': [np.nan, 0.15, 0.09, 0.01, 1, 0.005],
            'Volume': [np.nan] + [luas_urugan] * 5,
            'Satuan': [np.nan, 'm3', 'm3', 'm3', 'OH', 'OH'],
            'Harga Satuan': [np.nan, 198350, 325000, 233300, 81500, 98000],
            'Jumlah': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
    }

    data_pemadatan = None

# Definisi data untuk tabel pemadatan
    if pemadatan_urugan == 'Stamper':
        data_pemadatan = {
            'Uraian': ['Pemadatan Tanah', 'Stamper', 'Pekerja', 'Tukang', 'Mandor'],
            'Koefisien': [np.nan, 0.05, 0.062, 0.186, 0.0062],
            'Volume': [np.nan] + [volume_pemadatan] * 4,
            'Satuan': [np.nan, 'sewa-hari', 'OH', 'OH', 'OH'],
            'Harga Satuan': [np.nan, 26050, 81500, 93000, 98000],
            'Jumlah': [np.nan, np.nan, np.nan, np.nan, np.nan]
    }
    elif pemadatan_urugan == 'Bulldozer':
        data_pemadatan = {
            'Uraian': ['Pemadatan Tanah', 'Bulldozer', 'Water Tanker','Roller Vibrator','Pekerja', 'Mandor'],
            'Koefisien': [np.nan, 0.02, 0.0078, 0.0178, 0.1422, 0.0142],
            'Volume': [np.nan] + [volume_pemadatan] * 5,
            'Satuan': [np.nan, 'jam', 'jam', 'jam', 'jam', 'jam'],
            'Harga Satuan': [np.nan, 876843.85, 317296.73, 464580, 81500, 98000],
            'Jumlah': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
    } 
    # data_pemadatanMembuat DataFrame untuk tabel galian dan urugan
    df_galian = pd.DataFrame(data_galian)
    df_urugan = pd.DataFrame(data_urugan)
    df_pemadatan = pd.DataFrame(data_pemadatan)


    # Menggabungkan tabel galian dengan urugan
    df_final = pd.concat([df_galian, df_urugan, df_pemadatan], ignore_index=True)

    # Menghitung kolom 'Jumlah' sebagai hasil perkalian 'Volume', 'Koefisien', dan 'Harga Satuan'
    df_final['Jumlah'] = df_final['Volume'] * df_final['Koefisien'] * df_final['Harga Satuan']

    # Menghitung total jumlah
    total_jumlah_sum = df_final['Jumlah'].sum()

    # Menghitung margin 11%
    margin = total_jumlah_sum * 0.11

    total_jumlah_sum_margin = df_final['Jumlah'].sum() + margin

    # Membuat DataFrame dengan total dan margin
    total_jumlah = pd.DataFrame({
        'Uraian': ['Total', 'Margin', 'Total Setelah Margin'],
        'Koefisien': [np.nan, np.nan, np.nan],
        'Volume': [np.nan, np.nan, np.nan],
        'Satuan': [np.nan, np.nan, np.nan],
        'Harga Satuan': [np.nan, np.nan, np.nan],
        'Jumlah': [total_jumlah_sum, margin, total_jumlah_sum_margin]
    })

    # Menggabungkan `df_final` dengan `total_jumlah` untuk menampilkan hasil akhir
    df_final_with_margin = pd.concat([df_final, total_jumlah], ignore_index=True)

    # Menampilkan DataFrame gabungan di Streamlit
    st.write("### Tabel Estimasi RAB")
    st.dataframe(df_final_with_margin)

    if st.button("Ekspor Data ke Excel"):
        # Menggunakan BytesIO untuk menyimpan file Excel ke dalam memori
        output = BytesIO()

        # Menulis DataFrame ke dalam file Excel
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df_final_with_margin.to_excel(writer, index=False, sheet_name='Estimasi RAB')
        
        # Mengatur ulang pointer output ke posisi awal
        output.seek(0)

        # Menyediakan tombol untuk mengunduh file Excel
        st.download_button(
            label="Download Excel",
            data=output,
            file_name="estimasi_rab.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        if st.button("Konfirmasi dan Selesai"):
            st.success("Estimasi RAB telah berhasil direkapitulasi.")
            st.balloons()

if __name__ == "__main__":
    st.title("Estimasi RAB")
    show_estimasi_rab()
