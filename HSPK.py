# Library HSPK
# HSPK Tenaga
HSPK_PEKERJA = 81500
HSPK_MANDOR = 98000
HSPK_TUKANG = 93000
HSPK_TUKANG_BATU = 93000
HSPK_TUKANG_KAYU = 93000
HSPK_KEPALA_TUKANG_BATU = 96000
HSPK_KEPALA_TUKANG = 96000
HSPK_KEPALA_TUKANG_KAYU = 96000

# HSPK_bahan
HSPK_BATU_BELAH = 198350
HSPK_BATU_PECAH = 325000
HSPK_PASIR_LOKAL = 233300
HSPK_PERTAMINA_DEX = 13300
HSPK_PAVING_NATURAL_6CM = 87400
HSPK_PAVING_NATURAL_8CM = 96450
HSPK_PAVING_BERWARNA_6CM = 94200
HSPK_PAVING_BERWARNA_8CM = 107800
HSPK_PASIR_URUG = 151650
HSPK_BONDEK = 140000
HSPK_KAYU_JAWA = 3499200
HSPK_PLYWOOD = 84600
HSPK_DOLKEN = 20450
HSPK_KAYU_PERANCAH = 3171350
HSPK_PAKU_BIASA = 20450
HSPK_BAMBU = 35000
HSPK_MULTIPLEKS = 180800
HSPK_KAYU_BEKISTING = 3499200
HSPK_MINYAK_BEKISTING = 5650

# HPSK_peralatan
HSPK_EXCAVATOR = 819402.32
HSPK_DUMP_TRUCK = 339612.94
HSPK_WHEEL_LOADER = 538209.99
HSPK_JACK_HAMMER = 38465.57
HSPK_COMPRESSOR = 212427.45
HSPK_MESIN_POMPA_LUMPUR = 339211000
HSPK_CONCRET_PUMP = 611800



# Galian dengan Excavator
# Galian Tanah dengan Excavator
class GalianTanahDenganExcavator:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.excavator = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian

    def tenaga(self):
        self.pekerja = 0.0414 * HSPK_PEKERJA * self.volume_galian
        self.mandor = 0.0041 * HSPK_MANDOR * self.volume_galian

    def peralatan(self)
        self.excavator = 0.0414 * HSPK_EXCAVATOR * self.volume_galian
    
    def ahsp_galian_tanah_dengan_excavator(self):
        self.ahsp_total = self.tenaga() + self.peralatan()
    
    def galian_tanah_dengan_excavator(self):
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'excavator' : self.excavator,
            'ahsp_total' : self.ahsp_total
        }
# Galian Drainase dengan Excavator
class GalianDrainaseDenganExcavator:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.excavator = None
        self.dump_truck = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian

    def tenaga(self, pekerja, mandor):
        self.pekerja = 0.0043 * HSPK_PEKERJA * self.volume_galian
        self.mandor = 0.0011 * HSPK_MANDOR * self.volume_galian

    def peralatan(self, excavator, dump_truck):
        self.excavator = 0.0076 * HSPK_EXCAVATOR * self.volume_galian
        self.dump_truck = 0.117 * HSPK_DUMP_TRUCK * self.volume_galian
    
    def ahsp_galian_drainase_dengan_excavator(self):
        self.ahsp_total = self.tenaga() + self.peralatan()

    def galian_drainase_dengan_excavator(self):
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'excavator' : self.excavator,
            'dump_truck' : self.dump_truck,
            'ahsp_total' : self.ahsp_total
        }
# Galian Biasa dengan Excavator
class GalianBiasaDenganExcavator:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.excavator = None
        self.dump_truck = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian

    def tenaga(self):
        self.pekerja = 0.0073 * HSPK_PEKERJA * self.volume_galian
        self.mandor = 0.0037 * HSPK_MANDOR * self.volume_galian

    def peralatan(self, excavator, dump_truck)
        self.excavator = 0.0256 * HSPK_EXCAVATOR *self. volume_galian
        self.dump_truck = 0.2972 * HSPK_DUMP_TRUCK * self.volume_galian

    def ahsp_galian_biasa_dengan_excavator(self):
        self.ahsp_total = self.tenaga() + self.peralatan()

    def galian_biasa_dengan_excavator(self):
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'excavator' : self.excavator,
            'dump_truck' : self.dump_truck,
            'ahsp_total' : self.ahsp_total
        }
# Galian Batu dengan Excavator
class GalianBatuDenganExcavator:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.compressor = None
        self.jack_hammer = None
        self.wheel_loader = None
        self.excavator = None
        self.dump_truck = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian

    def tenaga(self):
        self.pekerja = 0.0843 * HSPK_PEKERJA * self.volume_galian
        self.mandor = 0.0105 * HSPK_MANDOR * self.volume_galian

    def peralatan(self):
        self.compressor = 0.0738 * HSPK_COMPRESSOR * self.volume_galian
        self.jack_hammer = 0.0738 * HSPK_JACK_HAMMER * self.volume_galian
        self.wheel_loader = 0.0738 * HSPK_WHEEL_LOADER * self.volume_galian
        self.excavator = 0.0738 * HSPK_EXCAVATOR * self.volume_galian
        self.dump_truck = 0.0738 * HSPK_DUMP_TRUCK * self.volume_galian
    
    def ahsp_galian_batu_dengan_excavator(self):
        self.ahsp_total = self.tenaga() + self.peralatan()

    def galian_biasa_dengan_excavator(self):
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'excavator' : self.excavator,
            'dump_truck' : self.dump_truck,
            'ahsp_total' : self.ahsp_total
        }

# Galian Tanah Biasa Manual
# Koefisien Galian Tanah Biasa Manual
KOEFISIEN_GALIAN_TANAH_BIASA_MANUAL = {
    'galian_1m' : {
        'koefisien_pekerja' : 0.563,
        'koefisien_mandor' : 0.0675,
    },
    'galian_2m' : {
        'koefisien_pekerja' : 0.675,
        'koefisien_mandor' : 0.0675,
    },
    'galian_3m' : {
        'koefisien_pekerja' : 0.76,
        'koefisien_mandor' : 0.0075,
    },
    'penambahan_1m' : {
        'koefisien_pekerja' : 0.75,
        'koefisien_mandor' : 0.0075,
    }
}
class GalianTanahBiasaManual:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian_tanah = KOEFISIEN_GALIAN_TANAH_BIASA_MANUAL[kedalaman_galian]

    def tenaga(self):
        self.pekerja = self.koefisien_galian_tanah['koefisien_pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian_tanah['koefisien_mandor'] * HSPK_MANDOR * self.volume_galian

    def ashp_galian_tanah_biasa_manual(self):
        self.ahsp_total = self.tenaga()
    
    def galian_tanah_biasa_manual(self):
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'ahsp_total' : self.ahsp_total
        }

# Galian Tanah Biasa Semi Mekanis
# Koefisien Galian Tanah Biasa Semi Mekanis
KOEFISIEN_GALIAN_TANAH_BIASA_SEMI_MEKANIS = {
    'galian_1m' : {
        'koefisien_pekerja' : 0.22,
        'koefisien_mandor' : 0.022,
        'koefisien_pertamina_dex' : 0.5,
        'koefisien_jack_hammer' : 0.05
    },
    'galian_2m' : {
        'koefisien_pekerja' : 0.26,
        'koefisien_mandor' : 0.026,
        'koefisien_pertamina_dex' : 0.5,
        'koefisien_jack_hammer' : 0.05
    },
    'galian_3m' : {
        'koefisien_pekerja' : 0.3,
        'koefisien_mandor' : 0.03,
        'koefisien_pertamina_dex' : 0.5,
        'koefisien_jack_hammer' : 0.05
    }
}
class GalianTanahSemiMekanis:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.pertamina_dex = None
        self.jack_hammer = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.kedalaman_galian_tanah = KOEFISIEN_GALIAN_TANAH_BIASA_SEMI_MEKANIS[kedalaman_galian]

    def tenaga(self):
        self.pekerja = 0.22 * HSPK_PEKERJA *  self.volume_galian
        self.mandor = 0.022 * HSPK_MANDOR *  self.volume_galian

    def bahan(self):
        self.pertamina_dex = 0.5 * HSPK_PERTAMINA_DEX *  self.volume_galian

    def peralatan(self):
        self.jack_hammer = 0.05 * HSPK_JACK_HAMMER *  self.volume_galian
    
    def ashp_galian_tanah_biasa_semi_mekanis(self):
        self.ahsp_total = self.tenaga()
    
    def galian_tanah_biasa(self):
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'pertamina_dex' : self.pertamina_dex,
            'jack_hammer' : self.jack_hammer,
            'ahsp_total' : self.ahsp_total
        }

# Galian Tanah Berbatu Manual
# Koefisien Galian Tanah Berbatu Manual
KOEFISIEN_GALIAN_TANAH_BBERBATu_MANUAL  = {
    'galian_1m' : {
        'koefisien_pekerja' : 0.22,
        'koefisien_mandor' : 0.022
    },
    'galian_2m' : {
        'koefisien_pekerja' : 0.26,
        'koefisien_mandor' : 0.026
    },
    'galian_3m' : {
        'koefisien_pekerja' : 0.3,
        'koefisien_mandor' : 0.03
    }
}
class galian_tanah_berbatu_1m_manual:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian_tanah = KOEFISIEN_GALIAN_TANAH_BIASA_MANUAL[kedalaman_galian]

    def tenaga(self):
        self.pekerja = 1.351 * HSPK_PEKERJA * self.volume_galian
        self.mandor = 0.1351 * HSPK_MANDOR * self.volume_galian

# Galian Tanah Berbatu Semi Mekanis
class galian_tanah_berbatu_1m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.43 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.043 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 1.25 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, jack_hammer):
        self.jack_hammer = 0.125 * HSPK_jack_hammer * luas_galian
class galian_tanah_berbatu_2m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.5 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.05 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 1.25 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, jack_hammer):
        self.jack_hammer = 0.125 * HSPK_jack_hammer * luas_galian
class galian_tanah_berbatu_3m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.55 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.055 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 1.25 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, jack_hammer):
        self.jack_hammer = 0.125 * HSPK_jack_hammer * luas_galian


# Galian Batu Manual
class galian_batu_1m_manual:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 3.378 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.3378 * HSPK_MANDOR * luas_galian
class galian_batu_2m_manual:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.675 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.0675 * HSPK_MANDOR * luas_galian
class galian_batu_3m_manual:
    def Manual(self, pekerja, mandor):
        self.pekerja = 0.76 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.165 * HSPK_MANDOR * luas_galian
class galian_batu_penambahan_1m:
    def Manual(self, pekerja, mandor):
        self.pekerja = 0.075 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.0075 * HSPK_MANDOR * luas_galian
# Galian Batu Semi Mekanis
class galian_batu_1m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 1 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.1 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 2.5 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, jack_hammer):
        self.jack_hammer = 0.25 * HSPK_jack_hammer * luas_galian
class galian_batu_2m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 1.2 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.12 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 2.5 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, jack_hammer):
        self.jack_hammer = 0.25 * HSPK_jack_hammer * luas_galian
class galian_batu_3m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 1.32 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.132 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 2.5 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, jack_hammer):
        self.jack_hammer = 0.25 * HSPK_jack_hammer * luas_galian


# Galian Tanah Cadas Manual
class galian_tanah_cadas_1m_manual:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 1.25 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.125 * HSPK_MANDOR * luas_galian
class galian_tanah_cadas_2m_manual:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 1.392 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.1392 * HSPK_MANDOR * luas_galian
class galian_tanah_cadas_3m_manual:
    def Manual(self, pekerja, mandor):
        self.pekerja = 1.5 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.15 * HSPK_MANDOR * luas_galian
class galian_tanah_cadas_penambahan_1m:
    def Manual(self, pekerja, mandor):
        self.pekerja = 0.1 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.01 * HSPK_MANDOR * luas_galian
# Galian Tanah Cadas Semi Mekanis
class galian_tanah_cadas_1m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.32 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.032 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 1.25 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, jack_hammer):
        self.jack_hammer = 0.125 * HSPK_jack_hammer * luas_galian
class galian_tanah_cadas_2m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.42 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.042 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 1.25 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, jack_hammer):
        self.jack_hammer = 0.125 * HSPK_jack_hammer * luas_galian
class galian_tanah_cadas_3m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.4 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.05 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 1.25 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, jack_hammer):
        self.jack_hammer = 0.125 * HSPK_jack_hammer * luas_galian

# Galian Lumpur Manual
class galian_lumpur_1m_manual:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.83 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.083 * HSPK_MANDOR * luas_galian
class galian_lumpur_2m_manual:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 1 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.01 * HSPK_MANDOR * luas_galian
class galian_lumpur_3m_manual:
    def Manual(self, pekerja, mandor):
        self.pekerja = 1.15 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.115 * HSPK_MANDOR * luas_galian
class galian_lumpur_penambahan_1m:
    def Manual(self, pekerja, mandor):
        self.pekerja = 0.15 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.015 * HSPK_MANDOR * luas_galian
# Galian Lumpur Semi Mekanis
class galian_lumpur_1m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.24 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.024 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 0.9 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, mesin_pompa_lumpur):
        self.mesin_pompa_lumpur = 0.0009 * HSPK_MESIN_POMPA_LUMPUR * luas_galian
class galian_lumpur_2m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.27 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.027 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 1.08 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, mesin_pompa_lumpur):
        self.mesin_pompa_lumpur = 0.001 * HSPK_MESIN_POMPA_LUMPUR * luas_galian
class galian_lumpur_3m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.295 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.0295 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 1.32 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, mesin_pompa_lumpur):
        self.mesin_pompa_lumpur = 0.0006 * HSPK_MESIN_POMPA_LUMPUR * luas_galian
class galian_lumpur_penambahan_1m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.02 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.02 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 0.24 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, mesin_pompa_lumpur):
        self.mesin_pompa_lumpur = 0.0002 * HSPK_MESIN_POMPA_LUMPUR * luas_galian
# Galian Lumpur dengan Alat Berat
class galian_lumpur_penambahan_1m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.02 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.02 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 0.24 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, mesin_pompa_lumpur):
        self.mesin_pompa_lumpur = 0.0002 * HSPK_MESIN_POMPA_LUMPUR * luas_galian


# Galian Pasir Manual
class galian_pasir_1m_manual:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.66 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.066 * HSPK_MANDOR * luas_galian
class galian_pasir_2m_manual:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.8 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.08 * HSPK_MANDOR * luas_galian
class galian_pasir_3m_manual:
    def Manual(self, pekerja, mandor):
        self.pekerja = 0.92 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.092 * HSPK_MANDOR * luas_galian
class galian_pasir_penambahan_1m:
    def Manual(self, pekerja, mandor):
        self.pekerja = 0.1 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.01 * HSPK_MANDOR * luas_galian
# Galian Lumpur Semi Mekanis
class galian_pasir_1m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.1 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.01 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 1.1 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, mesin_pompa_lumpur):
        self.mesin_pompa_lumpur = 0.0002 * HSPK_MESIN_POMPA_LUMPUR * luas_galian
class galian_pasir_2m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.265 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.0265 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 1.5 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, mesin_pompa_lumpur):
        self.mesin_pompa_lumpur = 0.0002 * HSPK_MESIN_POMPA_LUMPUR * luas_galian
class galian_pasir_3m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.28 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.028 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 1.8 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, mesin_pompa_lumpur):
        self.mesin_pompa_lumpur = 0.0003 * HSPK_MESIN_POMPA_LUMPUR * luas_galian
class galian_pasir_penambahan_1m_semi_mekanis:
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 0.015 * HSPK_PEKERJA * luas_galian
        self.mandor = 0.002 * HSPK_MANDOR * luas_galian
    def Bahan(self, pertamina_dex):
        self.pekerja = 0.24 * HSPK_pertamina_dex * luas_galian
    def Peralatan(self, mesin_pompa_lumpur):
        self.mesin_pompa_lumpur = 0.00003 * HSPK_MESIN_POMPA_LUMPUR * luas_galian

# Urugan
# Urugan Jalan Sementara (Makadam)
class JalanSementara:
    def __init__(self, panjang_jalan, lebar_jalan):
        
    def Tenaga(self, pekerja, mandor):
        self.pekerja = 1 * HSPK_PEKERJA * luas_jalan_sementara
        self.mandor = 0.005 * HSPK_MANDOR * luas_jalan_sementara
    def Bahan(self, batu_belah, batu_pecah, pasir_lokal):
        self.batu_belah = 0.15 * HSPK_BATU_BELAH * luas_jalan_sementara
        self.batu_pecah = 0.09 * HSPK_BATU_PECAH * luas_jalan_sementara
        self.pasir_lokal = 0.01 * HSPK_PASIR_LOKAL * luas_jalan_sementara

# Pemasangan
# Paving Block Natural
class paving_natural_6cm:
    def Tenaga(self, pekerja, tukang_batu, kepala_tukang_batu, mandor):
        self.pekerja = 0.025 * HSPK_PEKERJA * luas_pemasangan_paving
        self.tukang_batu = 0.15 * HSPK_TUKANG_BATU * luas_pemasangan_paving
        self.kepala_tukang_batu = 0.01 * HSPK_KEPALA_TUKANG_BATU * luas_pemasangan_paving
        self.mandor = 0.0003 * HSPK_MANDOR * luas_pemasangan_paving
    def Bahan(self, paving_natural_6cm, pasir_urug):
        self.paving_natural_6cm = 1.01 * HSPK_paving_natural_6cm * luas_pemasangan_paving
        self.pasir_urug = 0.05 * HSPK_pasir_urug
class paving_natural_8cm:
    def Tenaga(self, pekerja, tukang_batu, kepala_tukang_batu, mandor):
        self.pekerja = 0.025 * HSPK_PEKERJA * luas_pemasangan_paving
        self.tukang_batu = 0.15 * HSPK_TUKANG_BATU * luas_pemasangan_paving
        self.kepala_tukang_batu = 0.01 * HSPK_KEPALA_TUKANG_BATU * luas_pemasangan_paving
        self.mandor = 0.0003 * HSPK_MANDOR * luas_pemasangan_paving
    def Bahan(self, paving_natural_8cm, pasir_urug):
        self.paving_natural_8cm = 1.01 * HSPK_paving_natural_8cm * luas_pemasangan_paving
        self.pasir_urug = 0.035 * HSPK_pasir_urug
# Paving Block Berwarna
class paving_berwarna_6cm:
    def Tenaga(self, pekerja, tukang_batu, kepala_tukang_batu, mandor):
        self.pekerja = 0.25 * HSPK_PEKERJA * luas_pemasangan_paving
        self.tukang_batu = 0.25 * HSPK_TUKANG_BATU * luas_pemasangan_paving
        self.kepala_tukang_batu = 0.025 * HSPK_KEPALA_TUKANG_BATU * luas_pemasangan_paving
        self.mandor = 0.0025 * HSPK_MANDOR * luas_pemasangan_paving
    def Bahan(self, paving_berwarna_6cm, pasir_urug):
        self.paving_berwarna_6cm = 1.01 * HSPK_paving_berwarna_6cm * luas_pemasangan_paving
        self.pasir_urug = 0.035 * HSPK_pasir_urug
class paving_natural_8cm:
    def __init__(self, panjang_jalan_paving, lebar_jalan_paving):
        self.pekerja = None
        self.tukang_batu = None
        self.kepala_tukang_batu = None
        self.mandor = None
        self.luas_pemasangan_paving = panjang_jalan_paving * lebar_jalan_paving

    def hitung_tenaga(self):
        self.pekerja = 0.025 * HSPK_PEKERJA * self.luas_pemasangan_paving
        self.tukang_batu = 0.25 * HSPK_TUKANG_BATU * self.luas_pemasangan_paving
        self.kepala_tukang_batu = 0.025 * HSPK_KEPALA_TUKANG_BATU * self.luas_pemasangan_paving
        self.mandor = 0.0025 * HSPK_MANDOR * self.luas_pemasangan_paving

    def hitung_bahan(self):
        self.paving_berwarna_8cm = 1.01 * HSPK_paving_berwarna_8cm * self.luas_pemasangan_paving_baru
        self.pasir_urug = 0.035 * HSPK_pasir_urug
    
    def do_ahsp(self):
        self.ahsp_paving_natural_8cm = self.Tenaga() + self.Peralatan() + self.Bahan() + 
    
    def hasil_perhitungan(self):
        return {
            'pekerja': self.pekerja,
            'tukang_baku': self.tukang_batu,
            'kepala_tukang_batu' : self.kepala_tukang_batu,
            'paving_berwarna_8cm' : self.paving_berwarna_8cm,
            'pasir_urug' :self.pasir_urug,
            'ahsp_total' : self.paving_berwarna_8cm
        }
    
# Pengecoran
# Koefisien (nilai) HSPK Beton sesuai Mutu
KOEFISIEN_HSPK_BETON = {
    'beton_k125' : {
        'nilai_hspk_beton' : 794250
    },
    'beton_k150' : {
        'nilai_hspk_beton' : 828250
    },
    'beton_k175' : {
        'nilai_hspk_beton' : 885000
    },
    'beton_k225' : {
        'nilai_hspk_beton' : 1061600
    },
    'beton_k250' : {
        'nilai_hspk_beton' : 1108100
    },
    'beton_k300' : {
        'nilai_hspk_beton' : 1204450
    }
}
# Beton Ready Mix
class BetonReadyMix:
    def __init__(self, panjang_jalan_beton, lebar_jalan_beton, mutu_beton):
        self.pekerja = None
        self.tukang = None
        self.kepala_tukang = None
        self.mandor = None
        self.concrete_pump = None
        self.luas_jalan_beton = panjang_jalan_beton * lebar_jalan_beton
        self.hspk_beton = KOEFISIEN_HSPK_BETON[mutu_beton]

    def tenaga(self):
        self.pekerja = 1 * HSPK_PEKERJA * self.luas_jalan_beton
        self.tukang = 0.25 * HSPK_TUKANG_BATU * self.luas_jalan_beton
        self.kepala_tukang = 0.025 * HSPK_KEPALA_TUKANG * self.luas_jalan_beton
        self.mandor = 0.1 * HSPK_MANDOR * self.luas_jalan_beton
    
    def bahan(self):
        self.beton = 1.02 * self.hspk_beton['nilai_hspk_beton'] * self.luas_jalan_beton

    def peralatan(self):
        self.concrete_pump = 0.12 * HSPK_CONCRET_PUMP * self.luas_jalan_beton
    
    def ahsp_total(self) :
        self.beton_readymix = self.tenaga() + self.bahan() + self.peralatan()

    def ahsp_beton(self):
        return {
            'pekerja': self.pekerja,
            'tukang': self.tukang,
            'kepala_tukang' : self.kepala_tukang,
            'mandor' : self.mandor,
            'beton' : self.beton,
            'concrete_pump' : self.concrete_pump,
            'ahsp_total' : self.beton_readymix
        }

# Bekisting
# Koefisien Bekisting Lantai
KOEFISIEN_BEKISTING_LANTAI = {
    'multipleks_18mm' : {
        'koefisien_pekerja' : 0.3,
        'koefisien_tukang' : 0.3,
        'koefisien_kepala_tukang' : 0.03,
        'koefisien_mandor' : 0.03,
        'koefisien_multipleks' : 0.128,
        'koefisien_kayu_bekisting' : 0.006,
        'koefisien_paku_biasa' : 0.28,
        'koefisien_minyak_bekisting' : 0.25
    },
    'multipleks_12mm' : {
        'koefisien_pekerja' : 0.2,
        'koefisien_tukang' : 0.1,
        'koefisien_kepala_tukang' : 0.01,
        'koefisien_mandor' : 0.02,
        'koefisien_multipleks' : 0.128,
        'koefisien_kayu_bekisting' : 0.005,
        'koefisien_paku_biasa' : 0.22,
        'koefisien_minyak_bekisting' : 0.2
    }
}
# Bekisting Lantai Beton
class BekistingLantai:
    def __init__(self, panjang_bekisting_lantai, lebar_bekisting_lantai, tebal_multipleks):
        self.pekerja = None
        self.tukang = None
        self.kepala_tukang = None
        self.mandor = None
        self.multipleks = None
        self.kayu_bekisting = None
        self.paku_biasa = None
        self.minyak_bekisting = None
        self.luas_bekisting_lantai = panjang_bekisting_lantai * lebar_bekisting_lantai
        self.hspk_multipleks = KOEFISIEN_BEKISTING_LANTAI[tebal_multipleks]

    def tenaga(self):
        self.pekerja = self.hspk_multipleks['koefisien_pekerja'] * HSPK_PEKERJA * self.luas_bekisting_lantai
        self.tukang = self.hspk_multipleks['koefisien_tukang'] * HSPK_TUKANG * self.luas_bekisting_lantai
        self.kepala_tukang = self.hspk_multipleks['koefisien_kepala_tukang'] * HSPK_KEPALA_TUKANG * self.luas_bekisting_lantai
        self.mandor = self.hspk_multipleks['koefisien_mandor'] * HSPK_MANDOR * self.luas_bekisting_lantai

    def bahan(self):
        self.multipleks = self.hspk_multipleks['koefisien_multipleks'] * HSPK_MULTIPLEKS * self.luas_bekisting_lantai
        self.kayu_bekisting = self.hspk_multipleks['koefisien_kayu_bekisting'] * HSPK_KAYU_BEKISTING * self.luas_bekisting_lantai
        self.paku_biasa = self.hspk_multipleks['koefisien_paku_biasa'] * HSPK_PAKU_BIASA * self.luas_bekisting_lantai
        self.minyak_bekisting = self.hspk_multipleks['koefisien_minyak_bekisting'] * HSPK_MINYAK_BEKISTING * self.luas_bekisting_lantai

    def ahsp_total(self) :
        self.bekisting_lantai = self.tenaga() + self.bahan()   

    def ahsp_bekisting_lantai(self):
        return {
            'pekerja': self.pekerja,
            'tukang': self.tukang,
            'kepala_tukang' : self.kepala_tukang,
            'mandor' : self.mandor,
            'multipleks' : self.multipleks,
            'kayu_bekisting' : self.paku_biasa,
            'paku_biasa' : self.paku_biasa,
            'minyak_bekisting' : self.minyak_bekisting,
            'ahsp_total' : self.bekisting_lantai
        }
# Bekisting Kolom
# Koefisien Bekisting Kolom
KOEFISIEN_BEKISTING_KOLOM = {
    'multipleks_18mm' : {
        'koefisien_pekerja' : 0.33,
        'koefisien_tukang' : 0.33,
        'koefisien_kepala_tukang' : 0.033,
        'koefisien_mandor' : 0.033,
        'koefisien_multipleks' : 0.128,
        'koefisien_kayu_bekisting' : 0.007,
        'koefisien_paku_biasa' : 0.25,
        'koefisien_minyak_bekisting' : 0.2
    },
    'multipleks_15mm' : {
        'koefisien_pekerja' : 0.34,
        'koefisien_tukang' :0.17,
        'koefisien_kepala_tukang' : 0.017,
        'koefisien_mandor' : 0.034,
        'koefisien_multipleks' : 0.14,
        'koefisien_kayu_bekisting' : 0.006,
        'koefisien_paku_biasa' : 0.3,
        'koefisien_minyak_bekisting' : 0.2
    },
    'multipleks_12mm' : {
        'koefisien_pekerja' : 0.22,
        'koefisien_tukang' : 0.11,
        'koefisien_kepala_tukang' : 0.011,
        'koefisien_mandor' : 0.022,
        'koefisien_multipleks' : 0.128,
        'koefisien_kayu_bekisting' : 0.006,
        'koefisien_paku_biasa' : 0.25,
        'koefisien_minyak_bekisting' : 0.2
    }
}
# Bekisting Kolom Beton
class BekistingKolom:
    def __init__(self, panjang_bekisting_kolom, lebar_bekisting_kolom, tebal_multipleks):
        self.pekerja = None
        self.tukang = None
        self.kepala_tukang = None
        self.mandor = None
        self.bondek = None
        self.kayu_jawa = None
        self.paku_biasa = None
        self.minyak_bekisting = None
        self.plywood = None
        self.dolken = None
        self.luas_bekisting_kolom = panjang_bekisting_kolom * lebar_bekisting_kolom
        self.hspk_multipleks = KOEFISIEN_BEKISTING_KOLOM[tebal_multipleks]

    def tenaga(self):
        self.pekerja = self.hspk_multipleks['koefisien_pekerja'] * HSPK_PEKERJA * self.luas_bekisting_kolom
        self.tukang = self.hspk_multipleks['koefisien_tukang'] * HSPK_TUKANG * self.luas_bekisting_kolom
        self.kepala_tukang = self.hspk_multipleks['koefisien_kepala_tukang'] * HSPK_KEPALA_TUKANG * self.luas_bekisting_kolom
        self.mandor = self.hspk_multipleks['koefisien_mandor'] * HSPK_MANDOR * self.luas_bekisting_kolom

    def bahan(self):
        self.multipleks = self.hspk_multipleks['koefisien_multipleks'] * HSPK_MULTIPLEKS * self.luas_bekisting_kolom
        self.kayu_bekisting = self.hspk_multipleks['koefisien_kayu_bekisting'] * HSPK_KAYU_BEKISTING * self.luas_bekisting_kolom
        self.paku_biasa = self.hspk_multipleks['koefisien_paku_biasa'] * HSPK_PAKU_BIASA * self.luas_bekisting_kolom
        self.minyak_bekisting = self.hspk_multipleks['koefisien_minyak_bekisting'] * HSPK_MINYAK_BEKISTING * self.luas_bekisting_kolom
    
    def ahsp_total(self) :
        self.bekisting_kolom = self.tenaga() + self.bahan()

    def ahsp_bekisting_kolom(self):
        return {
            'pekerja': self.pekerja,
            'tukang': self.tukang,
            'kepala_tukang' : self.kepala_tukang,
            'mandor' : self.mandor,
            'multipleks' : self.multipleks,
            'kayu_bekisting' : self.paku_biasa,
            'paku_biasa' : self.paku_biasa,
            'minyak_bekisting' : self.minyak_bekisting,
            'ahsp_total' : self.bekisting_kolom
        }