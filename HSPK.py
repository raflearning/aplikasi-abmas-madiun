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
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian

    def tenaga(self):
        self.pekerja = 0.0414 * HSPK_PEKERJA * self.volume_galian
        self.mandor = 0.0041 * HSPK_MANDOR * self.volume_galian

    def peralatan(self):
        self.excavator = 0.0414 * HSPK_EXCAVATOR * self.volume_galian
    
    def ahsp_galian_tanah_dengan_excavator(self):
        self.ahsp_total = self.tenaga() + self.peralatan()
    
    def galian_tanah_dengan_excavator(self):
        self.tenaga()
        self.peralatan()
        self.ahsp_galian_tanah_dengan_excavator()
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
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian

    def tenaga(self):
        self.pekerja = 0.0043 * HSPK_PEKERJA * self.volume_galian
        self.mandor = 0.0011 * HSPK_MANDOR * self.volume_galian

    def peralatan(self):
        self.excavator = 0.0076 * HSPK_EXCAVATOR * self.volume_galian
        self.dump_truck = 0.117 * HSPK_DUMP_TRUCK * self.volume_galian
    
    def ahsp_galian_drainase_dengan_excavator(self):
        self.ahsp_total = self.tenaga() + self.peralatan()

    def galian_drainase_dengan_excavator(self):
        self.tenaga()
        self.peralatan()
        self.ahsp_galian_drainase_dengan_excavator()
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
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian

    def tenaga(self):
        self.pekerja = 0.0073 * HSPK_PEKERJA * self.volume_galian
        self.mandor = 0.0037 * HSPK_MANDOR * self.volume_galian

    def peralatan(self, excavator, dump_truck):
        self.excavator = 0.0256 * HSPK_EXCAVATOR *self. volume_galian
        self.dump_truck = 0.2972 * HSPK_DUMP_TRUCK * self.volume_galian

    def ahsp_galian_biasa_dengan_excavator(self):
        self.ahsp_total = self.tenaga() + self.peralatan()

    def galian_biasa_dengan_excavator(self):
        self.tenaga()
        self.peralatan()
        self.ahsp_galian_biasa_dengan_excavator()
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
        self.ahsp_total = None
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
        self.tenaga()
        self.peralatan()
        self.ahsp_galian_batu_dengan_excavator()
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'excavator' : self.excavator,
            'dump_truck' : self.dump_truck,
            'ahsp_total' : self.ahsp_total
        }

# Galian Tanah Biasa Manual
KOEFISIEN_GALIAN_TANAH_BIASA_MANUAL = {
    'galian_1m' : {
        'pekerja' : 0.563,
        'mandor' : 0.0675,
    },
    'galian_2m' : {
        'pekerja' : 0.675,
        'mandor' : 0.0675,
    },
    'galian_3m' : {
        'pekerja' : 0.76,
        'mandor' : 0.0075,
    },
    'penambahan_1m' : {
        'pekerja' : 0.75,
        'mandor' : 0.0075,
    }
}
class GalianTanahBiasaManual:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian, tipe_koefisien):
        self.pekerja = None
        self.mandor = None
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_TANAH_BIASA_MANUAL[tipe_koefisien]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor'] * HSPK_MANDOR * self.volume_galian

    def ahsp_galian_tanah_biasa_manual(self):
        self.ahsp_total = self.tenaga()
    
    def galian_tanah_biasa_manual(self):
        self.tenaga()
        self.ahsp_galian_tanah_biasa_manual()
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'ahsp_total' : self.ahsp_total
        }

# Galian Tanah Biasa Semi Mekanis
KOEFISIEN_GALIAN_TANAH_BIASA_SEMI_MEKANIS = {
    'galian_1m' : {
        'pekerja' : 0.22,
        'mandor' : 0.022,
        'pertamina_dex' : 0.5,
        'jack_hammer' : 0.05
    },
    'galian_2m' : {
        'pekerja' : 0.26,
        'mandor' : 0.026,
        'pertamina_dex' : 0.5,
        'jack_hammer' : 0.05
    },
    'galian_3m' : {
        'pekerja' : 0.3,
        'mandor' : 0.03,
        'pertamina_dex' : 0.5,
        'jack_hammer' : 0.05
    }
}
class GalianTanahBiasaSemiMekanis:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.pertamina_dex = None
        self.jack_hammer = None
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_TANAH_BIASA_SEMI_MEKANIS[kedalaman_galian]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA *  self.volume_galian
        self.mandor = self.koefisien_galian['mandor'] * HSPK_MANDOR *  self.volume_galian

    def bahan(self):
        self.pertamina_dex = self.koefisien_galian['pertamina_dex'] * HSPK_PERTAMINA_DEX *  self.volume_galian

    def peralatan(self):
        self.jack_hammer = 0.05 * HSPK_JACK_HAMMER *  self.volume_galian
    
    def ahsp_galian_tanah_biasa_semi_mekanis(self):
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan()
    
    def galian_tanah_biasa_semi_mekanis(self):
        self.tenaga()
        self.ahsp_galian_tanah_biasa_semi_mekanis()
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'pertamina_dex' : self.pertamina_dex,
            'jack_hammer' : self.jack_hammer,
            'ahsp_total' : self.ahsp_total
        }

# Galian Tanah Berbatu Manual
KOEFISIEN_GALIAN_TANAH_BERBATU_MANUAL  = {
    'galian_1m' : {
        'pekerja' : 0.22,
        'mandor' : 0.022
    },
    'galian_2m' : {
        'pekerja' : 0.26,
        'mandor' : 0.026
    },
    'galian_3m' : {
        'pekerja' : 0.3,
        'mandor' : 0.03
    }
}
class GalianTanahBerbatuManual:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_TANAH_BERBATU_MANUAL[kedalaman_galian]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor'] * HSPK_MANDOR * self.volume_galian
    
    def ahsp_galian_tanah_berbatu_manual(self):
        self.ahsp_total = self.tenaga()
    
    def galian_tanah_berbatu_manual(self):
        self.tenaga()
        self.ahsp_galian_tanah_berbatu_manual()
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'ahsp_total' : self.ahsp_total
        }

# Galian Tanah Berbatu Semi Mekanis
# Koefisien Galian Tanah Berbatu Semi Mekanis
KOEFISIEN_GALIAN_TANAH_BERBATU_SEMI_MEKANIS  = {
    'galian_1m' : {
        'pekerja' : 0.43,
        'mandor' : 0.043,
        'pertamina_dex' : 1.25,
        'jack_hammer' : 0.125
    },
    'galian_2m' : {
        'pekerja' : 0.5,
        'mandor' : 0.05,
        'pertamina_dex' : 1.25,
        'jack_hammer' : 0.125
    },
    'galian_3m' : {
        'pekerja' : 0.55,
        'mandor' : 0.055,
        'pertamina_dex' : 1.25,
        'jack_hammer' : 0.125
    }
}
class GalianTanahBerbatuSemiMekanis:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.pertamina_dex = None
        self.jack_hammer = None
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_TANAH_BERBATU_SEMI_MEKANIS[kedalaman_galian]
        
    def tenaga(self,):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor'] * HSPK_MANDOR * self.volume_galian

    def bahan(self):
        self.pertamina_dex = self.koefisien_galian['pertamina_dex'] * HSPK_PERTAMINA_DEX * self.volume_galian

    def peralatan(self):
        self.jack_hammer = self.koefisien_galian['koefisien_pjack_hammer'] * HSPK_JACK_HAMMER * self.volume_galian
    
    def ahsp_galian_tanah_berbatu_semi_mekanis(self):
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan()
    
    def galian_tanah_berbatu_semi_mekanis(self):
        self.tenaga()
        self.bahan()
        self.peralatan()
        self.ahsp_galian_tanah_berbatu_semi_mekanis()
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'pertamina_dex' : self.pertamina_dex,
            'jack_hammer' : self.jack_hammer,
            'ahsp_total' : self.ahsp_total
        }
# Galian Batu Manual
KOEFISIEN_GALIAN_BATU_MANUAL  = {
    'galian_1m' : {
        'pekerja' : 3.378,
        'mandor' : 0.3378
    },
    'galian_2m' : {
        'pekerja' : 0.675,
        'mandor' : 0.0675
    },
    'galian_3m' : {
        'pekerja' : 0.76,
        'mandor' : 0.165
    },
    'penambahan_1m' : {
        'pekerja' : 0.075,
        'mandor' : 0.0075
    }
}

class GalianBatuManual:
    def __init__(self, panjang, lebar, kedalaman, tipe_koefisien):
        self.pekerja = None
        self.mandor = None
        self.ahsp_total = None
        self.volume_galian = kedalaman
        self.koefisien_galian = KOEFISIEN_GALIAN_BATU_MANUAL[tipe_koefisien]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor'] * HSPK_MANDOR * self.volume_galian

    def ahsp_galian_batu_manual(self):
        self.tenaga()
        self.ahsp_total = self.pekerja + self.mandor

    def galian_batu_manual(self):
        self.tenaga()
        self.ahsp_galian_batu_manual()
        return {
            'pekerja': self.pekerja,
            'mandor': self.mandor,
            'ahsp_total': self.ahsp_total
        }


# Galian Batu Semi Mekanis
KOEFISIEN_GALIAN_BATU_SEMI_MEKANIS  = {
    'galian_1m' : {
        'pekerja' : 1,
        'mandor' : 0.1,
        'pertamina_dex' : 2.5,
        'jack_hammer' : 0.25
    },
    'galian_2m' : {
        'pekerja' : 1.2,
        'mandor' : 1.12,
        'pertamina_dex' : 2.5,
        'jack_hammer' : 0.25
    },
    'galian_3m' : {
        'pekerja' : 1.32,
        'mandor' : 0.132,
        'pertamina_dex' : 2.5,
        'jack_hammer' : 0.25
    }
}
class GalianBatuSemiMekanis:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.pertamina_dex = None
        self.jack_hammer = None
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_BATU_SEMI_MEKANIS[kedalaman_galian]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['koefisien_pmandor'] * HSPK_MANDOR * self.volume_galian

    def bahan(self):
        self.pertamina_dex = self.koefisien_galian['pertamina_dex'] * HSPK_PERTAMINA_DEX * self.volume_galian

    def peralatan(self):
        self.jack_hammer = self.koefisien_galian['jack_hammer'] * HSPK_JACK_HAMMER * self.volume_galian
        
    def ahsp_galian_batu_semi_mekanis(self):
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan()
    
    def galian_batu_semi_mekanis(self):
        self.tenaga()
        self.bahan()
        self.peralatan()
        self.ahsp_galian_batu_semi_mekanis()
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'pertamina_dex' : self.pertamina_dex,
            'jack_hammer' : self.jack_hammer,
            'ahsp_total' : self.ahsp_total
        }

# Galian Tanah Cadas Manual
KOEFISIEN_GALIAN_TANAH_CADAS_MANUAL  = {
    'galian_1m' : {
        'pekerja' : 1.25,
        'mandor' : 0.125
    },
    'galian_2m' : {
        'pekerja' : 1.392,
        'mandor' : 0.1392
    },
    'galian_3m' : {
        'pekerja' : 1.5,
        'mandor' : 0.15
    },
    'penambahan_1m' : {
        'pekerja' : 0.1,
        'mandor' : 0.01
    }
}
class GalianTanahCadasManual:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_TANAH_CADAS_MANUAL[kedalaman_galian]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor'] * HSPK_MANDOR * self.volume_galian

    def ahsp_galian_tanah_cadas_manual(self):
        self.ahsp_total = self.tenaga()
    
    def galian_tanah_cadas_manual(self):
        self.tenaga()
        self.ahsp_galian_tanah_cadas_manual()
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'ahsp_total' : self.ahsp_total
        }


# Galian Tanah Cadas Semi Mekanis
KOEFISIEN_GALIAN_TANAH_CADAS_SEMI_MEKANIS  = {
    'galian_1m' : {
        'pekerja' : 0.32,
        'mandor' : 0.2,
        'pertamina_dex' : 0.125,
        'jack_hammer' : 0.125
    },
    'galian_2m' : {
        'pekerja' : 0.42,
        'mandor' : 0.042,
        'pertamina_dex' : 0.125,
        'jack_hammer' : 0.125
    },
    'galian_3m' : {
        'pekerja' : 0.4,
        'mandor' : 0.05,
        'pertamina_dex' : 0.125,
        'jack_hammer' : 0.125
    }
}
class GalianTanahCadasSemiMekanis:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.pertamina_dex = None
        self.jack_hammer = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_TANAH_CADAS_SEMI_MEKANIS[kedalaman_galian]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor']* HSPK_MANDOR * self.volume_galian

    def bahan(self):
        self.pertamina_dex = self.koefisien_galian['pertamina_dex'] * HSPK_PERTAMINA_DEX * self.volume_galian

    def peralatan(self):
        self.jack_hammer = self.koefisien_galian['jack_hammer'] * HSPK_JACK_HAMMER * self.volume_galian
    
    def ahsp_galian_tanah_cadas_semi_mekanis(self):
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan()
    
    def galian_tanah_cadas_manual(self):
        self.tenaga()
        self.bahan()
        self.peralatan()
        self.ahsp_galian_tanah_cadas_semi_mekanis()
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'pertamina_dex' : self.pertamina_dex,
            'jack_hammer' : self.jack_hammer,
            'ahsp_total' : self.ahsp_total
        }

# Galian Lumpur Manual
KOEFISIEN_GALIAN_LUMPUR_MANUAL  = {
    'galian_1m' : {
        'pekerja' : 0.83,
        'mandor' : 0.083
    },
    'galian_2m' : {
        'pekerja' : 1,
        'mandor' : 0.1
    },
    'galian_3m' : {
        'pekerja' : 1.15,
        'mandor' : 0.115
    },
    'penambahan_1m' : {
        'pekerja' : 0.15,
        'mandor' : 0.015
    }
}
class GalianLumpurManual:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_LUMPUR_MANUAL[kedalaman_galian]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor'] * HSPK_MANDOR * self.volume_galian
    
    def ahsp_galian_lumpur_manual(self):
        self.ahsp_total = self.tenaga()
    
    def galian_lumpur_manual(self):
        self.tenaga()
        self.ahsp_galian_lumpur_manual()
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'ahsp_total' : self.ahsp_total
        }


# Galian Lumpur Semi Mekanis
KOEFISIEN_GALIAN_LUMPUR_SEMI_MEKANIS  = {
    'galian_1m' : {
        'pekerja' : 0.24,
        'mandor' : 0.024,
        'pertamina_dex' : 0.9,
        'mesin_pompa_lumpur' : 0.0009
    },
    'galian_2m' : {
        'pekerja' : 0.27,
        'mandor' : 0.027,
        'pertamina_dex' : 1.08,
        'mesin_pompa_lumpur' : 0.001
    },
    'galian_3m' : {
        'pekerja' : 0.295,
        'mandor' : 0.0295,
        'pertamina_dex' : 1.32,
        'mesin_pompa_lumpur' : 0.0006
    },
    'penambahan_1m' : {
        'pekerja' : 0.02,
        'mandor' : 0.02,
        'pertamina_dex' : 0.24,
        'mesin_pompa_lumpur' : 0.0002
    }
}
class GalianLumpurSemiMekanis:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.pertamina_dex = None
        self.mesin_pompa_lumpur = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_LUMPUR_SEMI_MEKANIS[kedalaman_galian]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor']* HSPK_MANDOR * self.volume_galian

    def bahan(self):
        self.pertamina_dex = self.koefisien_galian['pertamina_dex'] * HSPK_PERTAMINA_DEX * self.volume_galian

    def peralatan(self):
        self.mesin_pompa_lumpur = self.koefisien_galian['mesin_pompa_lumpur'] * HSPK_MESIN_POMPA_LUMPUR * self.volume_galian
    
    def ahsp_galian_lumpur_semi_mekanis(self):
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan()
    
    def galian_lumpur_semi_mekanis(self):
        self.tenaga()
        self.bahan()
        self.peralatan()
        self.ahsp_galian_lumpur_semi_mekanis()
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'pertamina_dex' : self.pertamina_dex,
            'jack_hammer' : self.mesin_pompa_lumpur,
            'ahsp_total' : self.ahsp_total
        }


# Galian Lumpur Mekanis
class GalianLumpurMekanis:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.dump_truck = None
        self.excavator = None
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian

    def tenaga(self):
        self.pekerja = 0.226 * HSPK_PEKERJA * self.volume_galian
        self.mandor = 0.007 * HSPK_MANDOR * self.volume_galian

    def peralatan(self):
        self.dump_truck = 0.07 * HSPK_DUMP_TRUCK * self.volume_galian
        self.excavator = 0.067 * HSPK_EXCAVATOR * self.volume_galian
    
    def ahsp_galian_lumpur_mekanis(self):
        self.ahsp_total = self.tenaga() + self.peralatan()
    
    def galian_lumpur_mekanis(self):
        self.tenaga()
        self.bahan()
        self.peralatan()
        self.ahsp_galian_lumpur_mekanis()
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'dump_truck' : self.dump_truck,
            'excavator' : self.excavator,
            'ahsp_total' : self.ahsp_total
        }


# Galian Pasir Manual
KOEFISIEN_GALIAN_PASIR_MANUAL  = {
    'galian_1m' : {
        'pekerja' : 0.66,
        'mandor' : 0.066
    },
    'galian_2m' : {
        'pekerja' : 0.8,
        'mandor' : 0.08
    },
    'galian_3m' : {
        'pekerja' : 0.92,
        'mandor' : 0.092
    },
    'penambahan_1m' : {
        'pekerja' : 0.1,
        'mandor' : 0.01
    }
}
class GalianPasirManual:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_PASIR_MANUAL[kedalaman_galian]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor'] * HSPK_MANDOR * self.volume_galian
    
    def ahsp_galian_pasir_manual(self):
        self.ahsp_total = self.tenaga()
    
    def galian_pasir_manual(self):
        self.tenaga()
        self.ahsp_galian_pasir_manual()
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'ahsp_total' : self.ahsp_total
        }


# Galian Pasir Semi Mekanis
KOEFISIEN_GALIAN_PASIR_SEMI_MEKANIS  = {
    'galian_1m' : {
        'pekerja' : 0.1,
        'mandor' : 0.01,
        'pertamina_dex' : 1.1,
        'jack_hammer' : 0.0002
    },
    'galian_2m' : {
        'pekerja' : 0.265,
        'mandor' : 0.0265,
        'pertamina_dex' : 1.5,
        'jack_hammer' : 0.002
    },
    'galian_3m' : {
        'pekerja' : 0.28,
        'mandor' : 0.028,
        'pertamina_dex' : 1.8,
        'jack_hammer' : 0.0003
    },
    'penambahan_1m' : {
        'pekerja' : 0.015,
        'mandor' : 0.002,
        'pertamina_dex' : 0.24,
        'jack_hammer' : 0.00003
    }
}
class GalianPasirSemiMekanis:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian):
        self.pekerja = None
        self.mandor = None
        self.pertamina_dex = None
        self.mesin_pompa_lumpur = None
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_PASIR_SEMI_MEKANIS[kedalaman_galian]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor']* HSPK_MANDOR * self.volume_galian

    def bahan(self):
        self.pertamina_dex = self.koefisien_galian['pertamina_dex'] * HSPK_PERTAMINA_DEX * self.volume_galian

    def peralatan(self):
        self.mesin_pompa_lumpur = self.koefisien_galian['mesin_pompa_lumpur'] * HSPK_MESIN_POMPA_LUMPUR * self.volume_galian
    
    def ahsp_galian_pasir_semi_mekanis(self):
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan()
    
    def galian_pasir_semi_mekanis(self):
        self.tenaga()
        self.bahan()
        self.peralatan()
        self.ahsp_galian_pasir_semi_mekanis()
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'pertamina_dex' : self.pertamina_dex,
            'jack_hammer' : self.mesin_pompa_lumpur,
            'ahsp_total' : self.ahsp_total
        }

# Urugan
KOEFISIEN_URUGAN = {
    'pasir_urug' : {
        'pekerja' : 0.3,
        'mandor' : 0.01,
        'koefisien_urugan' : 1.2,
        'hspk_urugan' : 151650
    },
    'tanah_urug' : {
        'pekerja' : 0.75,
        'mandor' : 0.075,
        'koefisien_urugan' : 1.2,
        'hspk_urugan' : 99650
    },
    'sirtu_padat' : {
        'pekerja' : 0.25,
        'mandor' : 0.025,
        'koefisien_urugan' : 1.2,
        'hspk_urugan' : 175800
    }
}
# Urugan Tanah, Pasir, Sirtu
class Urugan:
    def __init__(self, panjang_urugan, lebar_urugan, jenis_urugan):
        self.pekerja = None
        self.mandor = None
        self.ahsp_total = None
        self.luas_urugan = panjang_urugan * lebar_urugan
        self.urugan = KOEFISIEN_URUGAN[jenis_urugan]

    def tenaga(self):
        self.pekerja = self.urugan['pekerja'] * HSPK_PEKERJA * self.luas_urugan
        self.mandor = self.urugan['mandor'] * HSPK_MANDOR * self.luas_urugan

    def bahan(self):
        self.urug = self.urugan['koefisien_urugan'] * self.urugan['hspk_urugan'] * self.luas_urugan
    
    def ahsp_urugan(self):
        self.ahsp_total = self.tenaga() + self.bahan()
    
    def urugan(self):
        self.tenaga()
        self.bahan()
        self.ahsp_urugan()
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'urugan' : self.urug,
            'ahsp_total' : self.ahsp_total
        }

# Urugan Jalan Sementara (Makadam)
class Urugan:
    def __init__(self, panjang_jalan, lebar_jalan):
        self.pekerja = None
        self.mandor = None
        self.batu_belah = None
        self.batu_pecah = None
        self.pasir_lokal = None
        self.ahsp_total = None
        self.luas_jalan_sementara = panjang_jalan * lebar_jalan

    def tenaga(self):
        self.pekerja = 1 * HSPK_PEKERJA * self.luas_jalan_sementara
        self.mandor = 0.005 * HSPK_MANDOR * self.luas_jalan_sementara

    def bahan(self):
        self.batu_belah = 0.15 * HSPK_BATU_BELAH * self.luas_jalan_sementara
        self.batu_pecah = 0.09 * HSPK_BATU_PECAH * self.luas_jalan_sementara
        self.pasir_lokal = 0.01 * HSPK_PASIR_LOKAL * self.luas_jalan_sementara
    
    def ahsp_jalan_makadam(self):
        self.ahsp_total = self.tenaga() + self.bahan()

    def jalan_makadam(self):
        self.tenaga()
        self.bahan()
        self.ahsp_jalan_makadam()
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'batu_belah' : self.batu_belah,
            'batu_pecah' : self.batu_pecah,
            'pasir_lokal' : self.pasir_lokal,
            'ahsp_total' : self.ahsp_total
        }

# Pemasangan Paving
KOEFISIEN_PEMASANGAN_PAVING = {
    'paving_natural_6cm' : {
        'pekerja' : 0.025,
        'mandor' : 0.0003,
        'tukang_batu' : 0.15,
        'kepala_tukang_batu' : 0.01,
        'koefisien_paving' : 1.01,
        'pasir_urug' : 0.05,
        'hspk_paving' : 87400,
        'hspk_peralatan' : 95856.5
    },
    'paving_natural_8cm' : {
        'pekerja' : 0.025,
        'mandor' : 0.0003,
        'tukang_batu' : 0.15,
        'kepala_tukang_batu' : 0.01,
        'koefisien_paving' : 1.01,
        'pasir_urug' : 0.035,
        'hspk_paving' : 96450,
        'hspk_peralatan' : 102722.25
    },
    'paving_berwarna_6cm' : {
        'pekerja' : 0.25,
        'mandor' : 0.0025,
        'tukang_batu' : 0.25,
        'kepala_tukang_batu' : 0.025,
        'koefisien_paving' : 1.01,
        'pasir_urug' : 0.035,
        'hspk_paving' : 94200,
        'hspk_peralatan' : 100449.75
    },
    'paving_berwarna_8cm' : {
        'pekerja' : 0.025,
        'mandor' : 0.0025,
        'tukang_batu' : 0.25,
        'kepala_tukang_batu' : 0.025,
        'koefisien_paving' : 1.01,
        'pasir_urug' : 0.035,
        'hspk_paving' : 107800,
        'hspk_peralatan' : 114185.75
    }
}

class PemasanganPaving:
    def __init__(self, panjang_jalan_paving, lebar_jalan_paving, jenis_paving):
        self.pekerja = None
        self.tukang_batu = None
        self.kepala_tukang_batu = None
        self.mandor = None
        self.paving = None
        self.pasir_urug = None
        self.alat_pasang = None
        self.ahsp_total = None
        self.luas_pemasangan_paving = panjang_jalan_paving * lebar_jalan_paving
        self.koefisien_pemasangan_paving = KOEFISIEN_PEMASANGAN_PAVING[jenis_paving]

    def tenaga(self):
        self.pekerja = self.koefisien_pemasangan_paving['pekerja'] * HSPK_PEKERJA * self.luas_pemasangan_paving
        self.tukang_batu = self.koefisien_pemasangan_paving['tukang_batu'] * HSPK_TUKANG_BATU * self.luas_pemasangan_paving
        self.kepala_tukang_batu = self.koefisien_pemasangan_paving['kepala_tukang_batu'] * HSPK_KEPALA_TUKANG_BATU * self.luas_pemasangan_paving
        self.mandor = self.koefisien_pemasangan_paving['mandor'] * HSPK_MANDOR * self.luas_pemasangan_paving

    def bahan(self):
        self.paving = self.koefisien_pemasangan_paving['koefisien_paving'] * self.koefisien_pemasangan_paving['hspk_paving'] * self.luas_pemasangan_paving
        self.pasir_urug = self.koefisien_pemasangan_paving['pasir_urug'] * HSPK_PASIR_URUG * self.luas_pemasangan_paving
    
    def peralatan(self):
        self.alat_pasang = self.koefisien_pemasangan_paving['koefisien_paving'] * self.koefisien_pemasangan_paving['hspk_paving'] * self.luas_pemasangan_paving
    
    def ahsp_pemasangan_paving(self):
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan()
    
    def hasil_perhitungan(self):
        self.tenaga()
        self.bahan()
        self.peralatan()
        self.ahsp_pemasangan_paving()
        return {
            'pekerja': self.pekerja,
            'tukang_baku': self.tukang_batu,
            'kepala_tukang_batu' : self.kepala_tukang_batu,
            'mandor' : self.mandor,
            'paving' : self.paving,
            'pasir_urug' :self.pasir_urug,
            'alat_pasang' : self.alat_pasang,
            'ahsp_total' : self.ahsp_total
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
        self.ahsp_total = None
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
    
    def ahsp_beton_readymix(self) :
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan()

    def beton_readymix(self):
        self.tenaga()
        self.bahan()
        self.peralatan()
        self.ahsp_beton_readymix()
        return {
            'pekerja': self.pekerja,
            'tukang': self.tukang,
            'kepala_tukang' : self.kepala_tukang,
            'mandor' : self.mandor,
            'beton' : self.beton,
            'concrete_pump' : self.concrete_pump,
            'ahsp_total' : self.ahsp_total
        }

# Bekisting
# Koefisien Bekisting Lantai
KOEFISIEN_BEKISTING_LANTAI = {
    'multipleks_18mm' : {
        'pekerja' : 0.3,
        'koefisien_tukang' : 0.3,
        'kepala_tukang' : 0.03,
        'mandor' : 0.03,
        'multipleks' : 0.128,
        'kayu_bekisting' : 0.006,
        'paku_biasa' : 0.28,
        'minyak_bekisting' : 0.25
    },
    'multipleks_12mm' : {
        'pekerja' : 0.2,
        'koefisien_tukang' : 0.1,
        'kepala_tukang' : 0.01,
        'mandor' : 0.02,
        'multipleks' : 0.128,
        'kayu_bekisting' : 0.005,
        'paku_biasa' : 0.22,
        'minyak_bekisting' : 0.2
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
        self.ahsp_total = None
        self.luas_bekisting_lantai = panjang_bekisting_lantai * lebar_bekisting_lantai
        self.hspk_multipleks = KOEFISIEN_BEKISTING_LANTAI[tebal_multipleks]

    def tenaga(self):
        self.pekerja = self.hspk_multipleks['pekerja'] * HSPK_PEKERJA * self.luas_bekisting_lantai
        self.tukang = self.hspk_multipleks['koefisien_tukang'] * HSPK_TUKANG * self.luas_bekisting_lantai
        self.kepala_tukang = self.hspk_multipleks['kepala_tukang'] * HSPK_KEPALA_TUKANG * self.luas_bekisting_lantai
        self.mandor = self.hspk_multipleks['mandor'] * HSPK_MANDOR * self.luas_bekisting_lantai

    def bahan(self):
        self.multipleks = self.hspk_multipleks['multipleks'] * HSPK_MULTIPLEKS * self.luas_bekisting_lantai
        self.kayu_bekisting = self.hspk_multipleks['kayu_bekisting'] * HSPK_KAYU_BEKISTING * self.luas_bekisting_lantai
        self.paku_biasa = self.hspk_multipleks['paku_biasa'] * HSPK_PAKU_BIASA * self.luas_bekisting_lantai
        self.minyak_bekisting = self.hspk_multipleks['minyak_bekisting'] * HSPK_MINYAK_BEKISTING * self.luas_bekisting_lantai

    def ahsp_bekisting_lantai(self) :
        self.total = self.tenaga() + self.bahan()   

    def bekisting_lantai(self):
        self.tenaga()
        self.bahan()
        self.ahsp_bekisting_lantai()
        return {
            'pekerja': self.pekerja,
            'tukang': self.tukang,
            'kepala_tukang' : self.kepala_tukang,
            'mandor' : self.mandor,
            'multipleks' : self.multipleks,
            'kayu_bekisting' : self.paku_biasa,
            'paku_biasa' : self.paku_biasa,
            'minyak_bekisting' : self.minyak_bekisting,
            'ahsp_total' : self.ahsp_total
        }
# Bekisting Kolom
KOEFISIEN_BEKISTING_KOLOM = {
    'multipleks_18mm' : {
        'pekerja' : 0.33,
        'koefisien_tukang' : 0.33,
        'kepala_tukang' : 0.033,
        'mandor' : 0.033,
        'multipleks' : 0.128,
        'kayu_bekisting' : 0.007,
        'paku_biasa' : 0.25,
        'minyak_bekisting' : 0.2
    },
    'multipleks_15mm' : {
        'pekerja' : 0.34,
        'koefisien_tukang' :0.17,
        'kepala_tukang' : 0.017,
        'mandor' : 0.034,
        'multipleks' : 0.14,
        'kayu_bekisting' : 0.006,
        'paku_biasa' : 0.3,
        'minyak_bekisting' : 0.2
    },
    'multipleks_12mm' : {
        'pekerja' : 0.22,
        'koefisien_tukang' : 0.11,
        'kepala_tukang' : 0.011,
        'mandor' : 0.022,
        'multipleks' : 0.128,
        'kayu_bekisting' : 0.006,
        'paku_biasa' : 0.25,
        'minyak_bekisting' : 0.2
    }
}
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
        self.ahsp_total = None
        self.luas_bekisting_kolom = panjang_bekisting_kolom * lebar_bekisting_kolom
        self.hspk_multipleks = KOEFISIEN_BEKISTING_KOLOM[tebal_multipleks]

    def tenaga(self):
        self.pekerja = self.hspk_multipleks['pekerja'] * HSPK_PEKERJA * self.luas_bekisting_kolom
        self.tukang = self.hspk_multipleks['koefisien_tukang'] * HSPK_TUKANG * self.luas_bekisting_kolom
        self.kepala_tukang = self.hspk_multipleks['kepala_tukang'] * HSPK_KEPALA_TUKANG * self.luas_bekisting_kolom
        self.mandor = self.hspk_multipleks['mandor'] * HSPK_MANDOR * self.luas_bekisting_kolom

    def bahan(self):
        self.multipleks = self.hspk_multipleks['multipleks'] * HSPK_MULTIPLEKS * self.luas_bekisting_kolom
        self.kayu_bekisting = self.hspk_multipleks['kayu_bekisting'] * HSPK_KAYU_BEKISTING * self.luas_bekisting_kolom
        self.paku_biasa = self.hspk_multipleks['paku_biasa'] * HSPK_PAKU_BIASA * self.luas_bekisting_kolom
        self.minyak_bekisting = self.hspk_multipleks['minyak_bekisting'] * HSPK_MINYAK_BEKISTING * self.luas_bekisting_kolom
    
    def bekisting_kolom(self) :
        self.ahsp_total = self.tenaga() + self.bahan()

    def ahsp_bekisting_kolom(self):
        self.tenaga()
        self.bahan()
        self.bekisting_kolom()
        return {
            'pekerja': self.pekerja,
            'tukang': self.tukang,
            'kepala_tukang' : self.kepala_tukang,
            'mandor' : self.mandor,
            'multipleks' : self.multipleks,
            'kayu_bekisting' : self.paku_biasa,
            'paku_biasa' : self.paku_biasa,
            'minyak_bekisting' : self.minyak_bekisting,
            'ahsp_total' : self.ahsp_total
        }
