import numpy as np

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
HSPK_BONDEX = 140000
HSPK_KAYU_JAWA = 3499200
HSPK_PLYWOOD = 84600
HSPK_DOLKEN = 20450
HSPK_KAYU_PERANCAH = 3171350
HSPK_PAKU_BIASA = 20450
HSPK_BAMBU = 35000
HSPK_MULTIPLEKS = 180800
HSPK_KAYU_BEKISTING = 3499200
HSPK_MINYAK_BEKISTING = 5650
HSPK_BAJA_TULANGAN_POLOS = 11700
HSPK_JOINT_SEALENT = 42000
HSPK_CAT_ANTI_KARAT = 79100
HSPK_EXPANSION_CAP = 7400
HSPK_POLYTENE_125_MIKRON = 27250
HSPK_CURING_COMPOUND = 51100
HSPK_FORMWORK_PLATE = 45000
HSPK_PAKU = 600
HSPK_ADDITIVE = 44250
HSPK_KAYU_ACUAN = 3171350
HSPK_SEMEN_40KG = 102500
HSPK_TALI_IJUK = 19150
HSPK_PAVING_6CM = 87400
HSPK_PAVING_8CM = 96450
# HPSK_peralatan
HSPK_EXCAVATOR = 819402.32
HSPK_DUMP_TRUCK = 339612.94
HSPK_WHEEL_LOADER = 538209.99
HSPK_JACK_HAMMER = 38465.57
HSPK_COMPRESSOR = 212427.45
HSPK_MESIN_POMPA_LUMPUR = 339211000
HSPK_CONCRETE_PUMP = 611800
HSPK_STAMPER = 26050
HSPK_BULLDOZER = 876843.85
HSPK_WATER_TANKER = 317296.73
HSPK_ROLLER_VIBRATOR = 465580
HSPK_VIBRATOR_ROLLER = 346350
HSPK_TRUK_MIXER = 687737.92
HSPK_CONCRETE_VIBRATOR = 50126.81
HSPK_SLIP_FORM_PAVER = 636817.51
HSPK_BATCHING_PLANT = 884000

# Satuan
# Satuan Tenaga
SATUAN_PEKERJA = 'OH'
SATUAN_MANDOR = 'OH'
SATUAN_TUKANG = 'OH'
SATUAN_TUKANG_BATU = 'OH'
SATUAN_TUKANG_KAYU = 'OH'
SATUAN_KEPALA_TUKANG_BATU = 'OH'
SATUAN_KEPALA_TUKANG = 'OH'
SATUAN_KEPALA_TUKANG_KAYU = 'OH'
# Satuan Bahan
SATUAN_BATU_BELAH = 'm3'
SATUAN_BATU_PECAH = 'm3'
SATUAN_PASIR_LOKAL = 'm3'
SATUAN_PERTAMINA_DEX = 'liter'
SATUAN_PASIR_URUG = 'm3'
SATUAN_BONDEX = 'm2'
SATUAN_KAYU_JAWA = 'm3'
SATUAN_PLYWOOD = 'lembar'
SATUAN_DOLKEN = 'batang'
SATUAN_KAYU_PERANCAH = 'm3'
SATUAN_PAKU_BIASA = 'kg'
SATUAN_BAMBU = 'batang'
SATUAN_MULTIPLEKS = 'lembar'
SATUAN_KAYU_BEKISTING = 'm3'
SATUAN_MINYAK_BEKISTING = 'liter'
SATUAN_BAJA_TULANGAN_POLOS = 'kg'
SATUAN_JOINT_SEALENT = 'kg'
SATUAN_CAT_ANTI_KARAT = 'kg'
SATUAN_EXPANSION_CAP = 'm2'
SATUAN_POLYTENE_125_MIKRON = 'kg'
SATUAN_CURING_COMPOUND = 'liter'
SATUAN_FORMWORK_PLATE = 'm2'
SATUAN_PAKU = 'kg'
SATUAN_ADDITIVE = 'liter'
SATUAN_KAYU_ACUAN = 'kg'
SATUAN_SEMEN_40KG = 'zak'
SATUAN_TALI_IJUK = 'm'
SATUAN_PAVING = 'm2'
SATUAN_BETON = 'm3'
# Satuan Peralatan
SATUAN_EXCAVATOR = 'jam'
SATUAN_DUMP_TRUCK = 'jam'
SATUAN_COMPRESSOR = 'jam'
SATUAN_WHEEL_LOADER = 'jam'
SATUAN_JACK_HAMMER = 'jam'
SATUAN_MESIN_POMPA_LUMPUR = 'sewa/hari'
SATUAN_CONCRETE_PUMP = 'sewa/hari'
SATUAN_STAMPER = 'sewa/hari'
SATUAN_BULLDOZER = 'jam'
SATUAN_WATER_TANKER = 'jam'
SATUAN_ROLLER_VIBRATOR = 'jam'
SATUAN_VIBRATOR_ROLLER = 'jam'
SATUAN_TRUK_MIXER = 'jam'
SATUAN_CONCRETE_VIBRATOR = 'jam'
SATUAN_SLIP_FORM_PAVER = 'jam'
SATUAN_BATCHING_PLANT = 'jam'



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
        return self.pekerja + self.mandor
    def peralatan(self):
        self.excavator = 0.0414 * HSPK_EXCAVATOR * self.volume_galian
        return self.excavator
    def ahsp_galian_tanah_dengan_excavator(self):
        self.ahsp_total = self.tenaga() + self.peralatan()
    
    def galian_tanah_dengan_excavator(self):
        self.tenaga()
        self.peralatan()
        self.ahsp_galian_tanah_dengan_excavator()
        return {
	        'data' : {
                'Uraian': ['Galian', 'Excavator', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan, 0.0414, 0.414, 0.0041],
                'Volume': [np.nan] + [self.volume_galian] * 3,
                'Satuan': [np.nan,
                           SATUAN_EXCAVATOR,
                           SATUAN_PEKERJA,
                           SATUAN_MANDOR],
                'Harga Satuan': [np.nan,
                                 HSPK_EXCAVATOR,
                                 HSPK_PEKERJA,
                                 HSPK_MANDOR],
                'Jumlah': [np.nan,
                           self.excavator,
                           self.pekerja,
                           self.mandor]
                },
	        'subtotal': self.ahsp_total
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
        return self.pekerja + self.mandor
    def peralatan(self):
        self.excavator = 0.0076 * HSPK_EXCAVATOR * self.volume_galian
        self.dump_truck = 0.117 * HSPK_DUMP_TRUCK * self.volume_galian
        return self.excavator + self.dump_truck
    def ahsp_galian_drainase_dengan_excavator(self):
        self.ahsp_total = self.tenaga() + self.peralatan()

    def galian_drainase_dengan_excavator(self):
        self.tenaga()
        self.peralatan()
        self.ahsp_galian_drainase_dengan_excavator()
        return {
	        'data' : {
                'Uraian': ['Galian', 'Excavator', 'Dump Truck', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan, 0.0076, 0.117, 0.0043, 0.0011],
                'Volume': [np.nan] + [self.volume_galian] * 4,
                'Satuan': [np.nan,
                           SATUAN_EXCAVATOR,
                           SATUAN_DUMP_TRUCK,
                           SATUAN_PEKERJA,
                           SATUAN_MANDOR],
                'Harga Satuan': [np.nan,
                                 HSPK_EXCAVATOR,
                                 HSPK_DUMP_TRUCK,
                                 HSPK_PEKERJA,
                                 HSPK_MANDOR],
                'Jumlah': [np.nan,
                           self.excavator,
                           self.dump_truck,
                           self.pekerja,
                           self.mandor]
                },
	        'subtotal': self.ahsp_total
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
        return self.pekerja + self.mandor
    def peralatan(self):
        self.excavator = 0.0256 * HSPK_EXCAVATOR * self.volume_galian
        self.dump_truck = 0.2972 * HSPK_DUMP_TRUCK * self.volume_galian
        return self.excavator + self.dump_truck
    def ahsp_galian_biasa_dengan_excavator(self):
        self.ahsp_total = self.tenaga() + self.peralatan()

    def galian_biasa_dengan_excavator(self):
        self.tenaga()
        self.peralatan()
        self.ahsp_galian_biasa_dengan_excavator()
        return {
            'data' : {
                'Uraian': ['Galian', 'Excavator', 'Dump Truck', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan, 0.0256, 0.2972, 0.0073, 0.0037],
                'Volume': [np.nan] + [self.volume_galian] * 4,
                'Satuan': [np.nan,
                           SATUAN_EXCAVATOR,
                           SATUAN_DUMP_TRUCK,
                           SATUAN_PEKERJA,
                           SATUAN_MANDOR],
                'Harga Satuan': [np.nan,
                                 HSPK_EXCAVATOR,
                                 HSPK_DUMP_TRUCK,
                                 HSPK_PEKERJA,
                                 HSPK_MANDOR],
                'Jumlah': [np.nan,
                           self.excavator,
                           self.dump_truck,
                           self.pekerja, 
                           self.mandor]
                },
            'subtotal': self.ahsp_total
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
        return self.pekerja + self.mandor
    def peralatan(self):
        self.compressor = 0.0738 * HSPK_COMPRESSOR * self.volume_galian
        self.jack_hammer = 0.0738 * HSPK_JACK_HAMMER * self.volume_galian
        self.wheel_loader = 0.0738 * HSPK_WHEEL_LOADER * self.volume_galian
        self.excavator = 0.0738 * HSPK_EXCAVATOR * self.volume_galian
        self.dump_truck = 0.0738 * HSPK_DUMP_TRUCK * self.volume_galian
        return self.compressor + self.jack_hammer + self.wheel_loader + self.excavator + self.dump_truck
    def ahsp_galian_batu_dengan_excavator(self):
        self.ahsp_total = self.tenaga() + self.peralatan()

    def galian_biasa_dengan_excavator(self):
        self.tenaga()
        self.peralatan()
        self.ahsp_galian_batu_dengan_excavator()
        return {
            'data' : {
                'Uraian': ['Galian', 'Compressor', 'Jack Hammer', 'Wheel Loader', 'Excavator', 'Dump Truck', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan, 0.0738, 0.0738, 0.0738, 0.0738, 0.3329, 0.0843, 0.0105],
                'Volume': [np.nan] + [self.volume_galian] * 7,
                'Satuan': [np.nan,
                           SATUAN_COMPRESSOR,
                           SATUAN_JACK_HAMMER,
                           SATUAN_WHEEL_LOADER,
                           SATUAN_EXCAVATOR,
                           SATUAN_DUMP_TRUCK,
                           SATUAN_PEKERJA,
                           SATUAN_MANDOR],
                'Harga Satuan': [np.nan,
                                 HSPK_COMPRESSOR,
                                 HSPK_JACK_HAMMER,
                                 HSPK_WHEEL_LOADER,
                                 HSPK_EXCAVATOR,
                                 HSPK_DUMP_TRUCK,
                                 HSPK_PEKERJA,
                                 HSPK_MANDOR],
                'Jumlah': [np.nan,
                           self.compressor,
                           self.jack_hammer,
                           self.wheel_loader,
                           self.excavator,
                           self.dump_truck,
                           self.pekerja,
                           self.mandor]
                },
            'subtotal': self.ahsp_total
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
        return self.pekerja + self.mandor
    def ahsp_galian_tanah_biasa_manual(self):
        self.ahsp_total = self.tenaga()
    
    def galian_tanah_biasa_manual(self):
        self.tenaga()
        self.ahsp_galian_tanah_biasa_manual()
        return {
            'data' : {
                'Uraian': ['Galian', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan,
                              self.koefisien_galian['pekerja'],
                              self.koefisien_galian['mandor']],
                'Volume': [np.nan] + [self.volume_galian] * 2,
                'Satuan': [np.nan,
                           SATUAN_PEKERJA,
                           SATUAN_MANDOR],
                'Harga Satuan': [np.nan,
                                 HSPK_PEKERJA,
                                 HSPK_MANDOR],
                'Jumlah': [np.nan,
                           self.pekerja,
                           self.mandor]
                },
            'subtotal': self.ahsp_total
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
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian, tipe_koefisien):
        self.pekerja = None
        self.mandor = None
        self.pertamina_dex = None
        self.jack_hammer = None
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_TANAH_BIASA_SEMI_MEKANIS[tipe_koefisien]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA *  self.volume_galian
        self.mandor = self.koefisien_galian['mandor'] * HSPK_MANDOR *  self.volume_galian
        return self.pekerja + self.mandor
    def bahan(self):
        self.pertamina_dex = self.koefisien_galian['pertamina_dex'] * HSPK_PERTAMINA_DEX *  self.volume_galian
        return self.pertamina_dex
    def peralatan(self):
        self.jack_hammer = self.koefisien_galian['jack_hammer'] * HSPK_JACK_HAMMER *  self.volume_galian
        return self.jack_hammer
    def ahsp_galian_tanah_biasa_semi_mekanis(self):
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan()
    
    def galian_tanah_biasa_semi_mekanis(self):
        self.tenaga()
        self.ahsp_galian_tanah_biasa_semi_mekanis()
        return {
            'data' : {
                'Uraian': ['Galian', 'Pertamina Dex', 'Jack Hammer','Pekerja', 'Mandor'],
                'Koefisien': [np.nan,
                              self.koefisien_galian['pertamina_dex'],
                              self.koefisien_galian['jack_hammer'],
                              self.koefisien_galian['pekerja'],
                              self.koefisien_galian['mandor'] ],
                'Volume': [np.nan] + [self.volume_galian] * 4,
                'Satuan': [np.nan,
                           SATUAN_PERTAMINA_DEX,
                           SATUAN_JACK_HAMMER,
                           SATUAN_PEKERJA,
                           SATUAN_MANDOR],
                'Harga Satuan': [np.nan,
                                 HSPK_PERTAMINA_DEX,
                                 HSPK_JACK_HAMMER,
                                 HSPK_PEKERJA,
                                 HSPK_MANDOR],
                'Jumlah': [np.nan,
                            self.pertamina_dex,
                            self.jack_hammer,
                            self.pekerja, 
                            self.mandor ]
                },
            'subtotal': self.ahsp_total
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
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian, tipe_koefisien):
        self.pekerja = None
        self.mandor = None
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_TANAH_BERBATU_MANUAL[tipe_koefisien]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor'] * HSPK_MANDOR * self.volume_galian
        return self.pekerja + self.mandor
    def ahsp_galian_tanah_berbatu_manual(self):
        self.ahsp_total = self.tenaga()
    
    def galian_tanah_berbatu_manual(self):
        self.tenaga()
        self.ahsp_galian_tanah_berbatu_manual()
        return {
	            'data' : {
                'Uraian': ['Galian', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan,
                              self.koefisien_galian['pekerja'],
                              self.koefisien_galian['mandor']  ],
                'Volume': [np.nan] + [self.volume_galian] * 2,
                'Satuan': [np.nan,
                           SATUAN_PEKERJA,
                           SATUAN_MANDOR],
                'Harga Satuan': [np.nan,
                                 HSPK_PERTAMINA_DEX,
                                 HSPK_PEKERJA,],
                'Jumlah': [np.nan,
                           self.pekerja,
                           self.mandor]
                },
	            'subtotal': self.ahsp_total
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
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian, tipe_koefisien):
        self.pekerja = None
        self.mandor = None
        self.pertamina_dex = None
        self.jack_hammer = None
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_TANAH_BERBATU_SEMI_MEKANIS[tipe_koefisien]
        
    def tenaga(self,):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor'] * HSPK_MANDOR * self.volume_galian
        return self.pekerja + self.mandor
    def bahan(self):
        self.pertamina_dex = self.koefisien_galian['pertamina_dex'] * HSPK_PERTAMINA_DEX * self.volume_galian
        return self.pertamina_dex
    def peralatan(self):
        self.jack_hammer = self.koefisien_galian['jack_hammer'] * HSPK_JACK_HAMMER * self.volume_galian
        return self.jack_hammer
    def ahsp_galian_tanah_berbatu_semi_mekanis(self):
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan()
    
    def galian_tanah_berbatu_semi_mekanis(self):
        self.tenaga()
        self.bahan()
        self.peralatan()
        self.ahsp_galian_tanah_berbatu_semi_mekanis()
        return {
	            'data' : {
                'Uraian': ['Galian', 'Pertamina dex', 'Jack Hammer', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan,
                              self.koefisien_galian['pertamina_dex'],
                              self.koefisien_galian['jack_hammer'],
                              self.koefisien_galian['pekerja'],
                              self.koefisien_galian['mandor']  ],
                'Volume': [np.nan] + [self.volume_galian] * 4,
                'Satuan': [np.nan,
                           SATUAN_PERTAMINA_DEX,
                           SATUAN_JACK_HAMMER,
                           SATUAN_PEKERJA,
                           SATUAN_MANDOR],
                'Harga Satuan': [np.nan,
                                HSPK_PERTAMINA_DEX,
                                HSPK_JACK_HAMMER,
                                HSPK_PEKERJA,
                                HSPK_MANDOR],
                'Jumlah': [np.nan,
                            self.pertamina_dex,
                            self.jack_hammer,
                            self.pekerja,
                            self.mandor]
            },
	            'subtotal': self.ahsp_total
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
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian, tipe_koefisien):
        self.pekerja = None
        self.mandor = None
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_BATU_MANUAL[tipe_koefisien]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor'] * HSPK_MANDOR * self.volume_galian
        return self.pekerja + self.mandor
    def ahsp_galian_batu_manual(self):
        self.ahsp_total = self.tenaga()
    
    def galian_batu_manual(self):
        self.tenaga()
        self.ahsp_galian_batu_manual()
        return {
	            'data' : {
                'Uraian': ['Galian', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan,
                            self.koefisien_galian['pekerja'],
                            self.koefisien_galian['mandor']  ],
                'Volume': [np.nan] + [self.volume_galian] * 2,
                'Satuan': [np.nan,
                            SATUAN_PEKERJA,
                            SATUAN_MANDOR],
                'Harga Satuan': [np.nan,
                            HSPK_PEKERJA,
                            HSPK_MANDOR],
                'Jumlah': [np.nan,
                            self.pekerja,
                            self.mandor]
            },
	            'subtotal': self.ahsp_total
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
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian, tipe_koefisien):
        self.pekerja = None
        self.mandor = None
        self.pertamina_dex = None
        self.jack_hammer = None
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_BATU_SEMI_MEKANIS[tipe_koefisien]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor'] * HSPK_MANDOR * self.volume_galian
        return self.pekerja + self.mandor
    def bahan(self):
        self.pertamina_dex = self.koefisien_galian['pertamina_dex'] * HSPK_PERTAMINA_DEX * self.volume_galian
        return self.pertamina_dex
    def peralatan(self):
        self.jack_hammer = self.koefisien_galian['jack_hammer'] * HSPK_JACK_HAMMER * self.volume_galian
        return self.jack_hammer
    def ahsp_galian_batu_semi_mekanis(self):
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan()
    
    def galian_batu_semi_mekanis(self):
        self.tenaga()
        self.bahan()
        self.peralatan()
        self.ahsp_galian_batu_semi_mekanis()
        return {
	            'data' : {
                'Uraian': ['Galian', 'Pertamina dex', 'Jack Hammer', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan,
                            self.koefisien_galian['pertamina_dex'],
                            self.koefisien_galian['jack_hammer'],
                            self.koefisien_galian['pekerja'],
                            self.koefisien_galian['mandor']  ],
                'Volume': [np.nan] + [self.volume_galian] * 4,
                'Satuan': [np.nan,
                            SATUAN_PERTAMINA_DEX,
                            SATUAN_JACK_HAMMER,
                            SATUAN_PEKERJA,
                            SATUAN_MANDOR],
                'Harga Satuan': [np.nan,
                            HSPK_PERTAMINA_DEX,
                            HSPK_JACK_HAMMER,
                            HSPK_PEKERJA,
                            HSPK_MANDOR],
                'Jumlah': [np.nan,
                            self.pertamina_dex,
                            self.jack_hammer,
                            self.pekerja,
                            self.mandor]
            },
	            'subtotal': self.ahsp_total
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
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian, tipe_koefisien):
        self.pekerja = None
        self.mandor = None
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_TANAH_CADAS_MANUAL[tipe_koefisien]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor'] * HSPK_MANDOR * self.volume_galian
        return self.pekerja + self.mandor
    def ahsp_galian_tanah_cadas_manual(self):
        self.ahsp_total = self.tenaga()
    
    def galian_tanah_cadas_manual(self):
        self.tenaga()
        self.ahsp_galian_tanah_cadas_manual()
        return {
	            'data' : {
                'Uraian': ['Galian', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan,
                            self.koefisien_galian['pekerja'],
                            self.koefisien_galian['mandor']  ],
                'Volume': [np.nan] + [self.volume_galian] * 2,
                'Satuan': [np.nan,
                            SATUAN_PEKERJA,
                            SATUAN_MANDOR],
                'Harga Satuan': [np.nan,
                                HSPK_PEKERJA,
                                HSPK_MANDOR],
                'Jumlah': [np.nan,
                            self.pekerja,
                            self.mandor]
            },
	            'subtotal': self.ahsp_total
	    }


# Galian Tanah Cadas Semi Mekanis
KOEFISIEN_GALIAN_TANAH_CADAS_SEMI_MEKANIS  = {
    'galian_1m' : {
        'pekerja' : 0.32,
        'mandor' : 0.02,
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
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian, tipe_koefisien):
        self.pekerja = None
        self.mandor = None
        self.pertamina_dex = None
        self.jack_hammer = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_TANAH_CADAS_SEMI_MEKANIS[tipe_koefisien]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor']* HSPK_MANDOR * self.volume_galian
        return self.pekerja + self.mandor
    def bahan(self):
        self.pertamina_dex = self.koefisien_galian['pertamina_dex'] * HSPK_PERTAMINA_DEX * self.volume_galian
        return self.pertamina_dex
    def peralatan(self):
        self.jack_hammer = self.koefisien_galian['jack_hammer'] * HSPK_JACK_HAMMER * self.volume_galian
        return self.jack_hammer
    def ahsp_galian_tanah_cadas_semi_mekanis(self):
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan()
    
    def galian_tanah_cadas_semi_mekanis(self):
        self.tenaga()
        self.bahan()
        self.peralatan()
        self.ahsp_galian_tanah_cadas_semi_mekanis()
        return {
	            'data' : {
                'Uraian': ['Galian', 'Pertamina dex', 'Jack Hammer', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan,
                                self.koefisien_galian['pertamina_dex'],
                                self.koefisien_galian['jack_hammer'],
                                self.koefisien_galian['pekerja'],
                                self.koefisien_galian['mandor']  ],
                'Volume': [np.nan] + [self.volume_galian] * 4,
                'Satuan': [np.nan,
                            SATUAN_PERTAMINA_DEX,
                            SATUAN_JACK_HAMMER,
                            SATUAN_PEKERJA,
                            SATUAN_MANDOR],
                'Harga Satuan': [np.nan,
                                HSPK_PERTAMINA_DEX,
                                HSPK_JACK_HAMMER,
                                HSPK_PEKERJA,
                                HSPK_MANDOR],
                'Jumlah': [np.nan,
                                self.pertamina_dex,
                                self.jack_hammer,
                                self.pekerja,
                                self.mandor]
            },
	            'subtotal': self.ahsp_total
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
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian, tipe_koefisien):
        self.pekerja = None
        self.mandor = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_LUMPUR_MANUAL[tipe_koefisien]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor'] * HSPK_MANDOR * self.volume_galian
        return self.pekerja + self.mandor
    def ahsp_galian_lumpur_manual(self):
        self.ahsp_total = self.tenaga()
    
    def galian_lumpur_manual(self):
        self.tenaga()
        self.ahsp_galian_lumpur_manual()
        return {
	            'data' : {
                'Uraian': ['Galian', 'Pekerja', 'Mandor'],
                'Koefisien': [np.nan,
                              self.koefisien_galian['pekerja'],
                              self.koefisien_galian['mandor']  ],
                'Volume': [np.nan] + [self.volume_galian] * 2,
                'Satuan': [np.nan,
                            SATUAN_PEKERJA,
                            SATUAN_MANDOR],
                'Harga Satuan': [np.nan,
                            HSPK_PEKERJA,
                            HSPK_MANDOR],
                'Jumlah': [np.nan,
                            self.pekerja,
                            self.mandor]
            },
	            'subtotal': self.ahsp_total
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
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian, tipe_koefisien):
        self.pekerja = None
        self.mandor = None
        self.pertamina_dex = None
        self.mesin_pompa_lumpur = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_LUMPUR_SEMI_MEKANIS[tipe_koefisien]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor']* HSPK_MANDOR * self.volume_galian
        return self.pekerja + self.mandor
    def bahan(self):
        self.pertamina_dex = self.koefisien_galian['pertamina_dex'] * HSPK_PERTAMINA_DEX * self.volume_galian
        return self.pertamina_dex
    def peralatan(self):
        self.mesin_pompa_lumpur = self.koefisien_galian['mesin_pompa_lumpur'] * HSPK_MESIN_POMPA_LUMPUR * self.volume_galian
        return self.mesin_pompa_lumpur
    def ahsp_galian_lumpur_semi_mekanis(self):
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan()
    
    def galian_lumpur_semi_mekanis(self):
        self.tenaga()
        self.bahan()
        self.peralatan()
        self.ahsp_galian_lumpur_semi_mekanis()
        return {
            'data' :{
                'Uraian': ['Galian', 
                           'Pertamina dex', 
                           'Mesin Pompa Lumpur', 
                           'Pekerja', 
                           'Mandor'],
                'Koefisien': [np.nan, 
                              self.koefisien_galian['pertamina_dex'], 
                              self.koefisien_galian['mesin_pompa_lumpur'],
                              self.koefisien_galian['pekerja'],
                              self.koefisien_galian['mandor']],
                'Volume': [np.nan] + [self.volume_galian] * 4,
                'Satuan': [np.nan, 
                           SATUAN_PERTAMINA_DEX,
                           SATUAN_MESIN_POMPA_LUMPUR,
                           SATUAN_PEKERJA , 
                           SATUAN_MANDOR],
                'Harga Satuan': [np.nan, 
                                 HSPK_PERTAMINA_DEX,
                                 HSPK_MESIN_POMPA_LUMPUR,
                                 HSPK_PEKERJA , 
                                 HSPK_MANDOR],
                'Jumlah': [np.nan, 
                           self.pertamina_dex, 
                           self.mesin_pompa_lumpur, 
                           self.pekerja, 
                           self.mandor]
                },
            'subtotal': self.ahsp_total
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
        return self.pekerja + self.mandor
    def peralatan(self):
        self.dump_truck = 0.07 * HSPK_DUMP_TRUCK * self.volume_galian
        self.excavator = 0.067 * HSPK_EXCAVATOR * self.volume_galian
        return self.dump_truck + self.excavator
    def ahsp_galian_lumpur_mekanis(self):
        self.ahsp_total = self.tenaga() + self.peralatan()
    
    def galian_lumpur_mekanis(self):
        self.tenaga()
        self.peralatan()
        self.ahsp_galian_lumpur_mekanis()
        return {
            'data' : {
                        'Uraian': ['Galian', 
                                   'Dump Truck', 
                                   'Excavator', 
                                   'Pekerja', 
                                   'Mandor'],
                        'Koefisien': [np.nan, 
                                      0.07, 
                                      0.067,
                                      0.226,
                                      0.007],
                        'Volume': [np.nan] + [self.volume_galian] * 4,
                        'Satuan': [np.nan, 
                                   SATUAN_DUMP_TRUCK,
                                   SATUAN_EXCAVATOR,
                                   SATUAN_PEKERJA, 
                                   SATUAN_MANDOR],
                        'Harga Satuan': [np.nan, 
                                         HSPK_DUMP_TRUCK,
                                         HSPK_EXCAVATOR, 
                                         HSPK_PEKERJA, 
                                         HSPK_MANDOR],
                        'Jumlah': [np.nan, 
                                   self.dump_truck,
                                   self.excavator, 
                                   self.pekerja, 
                                   self.mandor]
                    },
            'subtotal': self.ahsp_total
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
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian, tipe_koefisien):
        self.pekerja = None
        self.mandor = None
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_PASIR_MANUAL[tipe_koefisien]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor'] * HSPK_MANDOR * self.volume_galian
        return self.pekerja + self.mandor
    def ahsp_galian_pasir_manual(self):
        self.ahsp_total = self.tenaga()
    
    def galian_pasir_manual(self):
        self.tenaga()
        self.ahsp_galian_pasir_manual()
        return {
            'data' : {
                        'Uraian': ['Galian',
                                'Pekerja', 
                                   'Mandor'],
                        'Koefisien': [np.nan, 
                                      self.koefisien_galian['pekerja'], 
                                      self.koefisien_galian['mandor']  ],
                        'Volume': [np.nan] + [self.volume_galian] * 2,
                        'Satuan': [np.nan, 
                                   SATUAN_PEKERJA, 
                                   SATUAN_MANDOR],
                        'Harga Satuan': [np.nan, 
                                         HSPK_PEKERJA, 
                                         HSPK_MANDOR],
                        'Jumlah': [np.nan, 
                                   self.pekerja, 
                                   self.mandor]
                    },
            'subtotal': self.ahsp_total
            }


# Galian Pasir Semi Mekanis
KOEFISIEN_GALIAN_PASIR_SEMI_MEKANIS  = {
    'galian_1m' : {
        'pekerja' : 0.1,
        'mandor' : 0.01,
        'pertamina_dex' : 1.1,
        'mesin_pompa_lumpur' : 0.0002
    },
    'galian_2m' : {
        'pekerja' : 0.265,
        'mandor' : 0.0265,
        'pertamina_dex' : 1.5,
        'mesin_pompa_lumpur' : 0.0002
    },
    'galian_3m' : {
        'pekerja' : 0.28,
        'mandor' : 0.028,
        'pertamina_dex' : 1.8,
        'mesin_pompa_lumpur' : 0.0003
    },
    'penambahan_1m' : {
        'pekerja' : 0.015,
        'mandor' : 0.002,
        'pertamina_dex' : 0.24,
        'mesin_pompa_lumpur': 0.00003
    }
}
class GalianPasirSemiMekanis:
    def __init__(self, panjang_galian, lebar_galian, kedalaman_galian, tipe_koefisien):
        self.pekerja = None
        self.mandor = None
        self.pertamina_dex = None
        self.mesin_pompa_lumpur = None
        self.ahsp_total = None
        self.volume_galian = panjang_galian * lebar_galian * kedalaman_galian
        self.koefisien_galian = KOEFISIEN_GALIAN_PASIR_SEMI_MEKANIS[tipe_koefisien]

    def tenaga(self):
        self.pekerja = self.koefisien_galian['pekerja'] * HSPK_PEKERJA * self.volume_galian
        self.mandor = self.koefisien_galian['mandor'] * HSPK_MANDOR * self.volume_galian
        return self.pekerja + self.mandor
    def bahan(self):
        self.pertamina_dex = self.koefisien_galian['pertamina_dex'] * HSPK_PERTAMINA_DEX * self.volume_galian
        return self.pertamina_dex
    def peralatan(self):
        self.mesin_pompa_lumpur = self.koefisien_galian['mesin_pompa_lumpur'] * HSPK_MESIN_POMPA_LUMPUR * self.volume_galian
        return self.mesin_pompa_lumpur
    def ahsp_galian_pasir_semi_mekanis(self):
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan()
    
    def galian_pasir_semi_mekanis(self):
        self.tenaga()
        self.bahan()
        self.peralatan()
        self.ahsp_galian_pasir_semi_mekanis()
        return {
            'data' : {
                        'Uraian': ['Galian', 
                                   'Pertamina dex', 
                                   'Mesin Pompa Lumpur', 
                                   'Pekerja', 
                                   'Mandor'],
                        'Koefisien': [np.nan, 
                                      self.koefisien_galian['pertamina_dex'],
                                      self.koefisien_galian['mesin_pompa_lumpur'],
                                      self.koefisien_galian['pekerja'], 
                                      self.koefisien_galian['mandor']  ],
                        'Volume': [np.nan] + [self.volume_galian] * 4,
                        'Satuan': [np.nan, 
                                   SATUAN_PERTAMINA_DEX,
                                   SATUAN_MESIN_POMPA_LUMPUR, 
                                   SATUAN_PEKERJA,
                                   SATUAN_MANDOR],
                        'Harga Satuan': [np.nan,
                                         HSPK_PERTAMINA_DEX, 
                                         HSPK_MESIN_POMPA_LUMPUR, 
                                         HSPK_PEKERJA, 
                                         HSPK_MANDOR],
                        'Jumlah': [np.nan, 
                                   self.pertamina_dex,
                                   self.mesin_pompa_lumpur, 
                                   self.pekerja, 
                                   self.mandor]
                    },
            'subtotal': self.ahsp_total
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
    def __init__(self, panjang_urugan, lebar_urugan, kedalaman_urugan, tipe_koefisien):
        self.pekerja = None
        self.mandor = None
        self.ahsp_total = None
        self.volume_urugan = panjang_urugan * lebar_urugan * kedalaman_urugan
        self.jenis_urugan = KOEFISIEN_URUGAN[tipe_koefisien]

    def tenaga(self):
        self.pekerja = self.jenis_urugan['pekerja'] * HSPK_PEKERJA * self.volume_urugan
        self.mandor = self.jenis_urugan['mandor'] * HSPK_MANDOR * self.volume_urugan
        return self.pekerja + self.mandor
    def bahan(self):
        self.urug = self.jenis_urugan['koefisien_urugan'] * self.jenis_urugan['hspk_urugan'] * self.volume_urugan
        return self.urug
    def ahsp_urugan(self):
        self.ahsp_total = self.tenaga() + self.bahan()
    
    def urugan(self):
        self.tenaga()
        self.bahan()
        self.ahsp_urugan()
        return {
            'data' : {
                        'Uraian': ['Urugan',
                                    'Pekerja', 
                                   'Mandor'],
                        'Koefisien': [np.nan, 
                                      self.jenis_urugan['pekerja'], 
                                      self.jenis_urugan['mandor']],
                        'Volume': [np.nan] + [self.volume_urugan] * 2,
                        'Satuan': [np.nan, 
                                   SATUAN_PEKERJA, 
                                   SATUAN_MANDOR],
                        'Harga Satuan': [np.nan, 
                                         HSPK_PEKERJA, 
                                         HSPK_MANDOR],
                        'Jumlah': [np.nan, 
                                   self.pekerja, 
                                   self.mandor]
                    },
            'subtotal': self.ahsp_total
        }

# Urugan Jalan Sementara (Makadam)
class JalanMakadam:
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
        return self.pekerja + self.mandor
    def bahan(self):
        self.batu_belah = 0.15 * HSPK_BATU_BELAH * self.luas_jalan_sementara
        self.batu_pecah = 0.09 * HSPK_BATU_PECAH * self.luas_jalan_sementara
        self.pasir_lokal = 0.01 * HSPK_PASIR_LOKAL * self.luas_jalan_sementara
        return self.batu_belah + self.batu_pecah + self.pasir_lokal
    def ahsp_jalan_makadam(self):
        self.ahsp_total = self.tenaga() + self.bahan()

    def jalan_makadam(self):
        self.tenaga()
        self.bahan()
        self.ahsp_jalan_makadam()
        return {
            'data' : {
                        'Uraian': ['Galian', 
                                   'Batu Belah', 
                                   'Batu Pecah', 
                                   'Pasir Lokal', 
                                   'Pekerja', 
                                   'Mandor'],
                        'Koefisien': [np.nan,
                                      0.15,
                                      0.09,
                                      0.01, 
                                      1, 
                                      0.005],
                        'Volume': [np.nan] + [self.volume_galian] * 5,
                        'Satuan': [np.nan, 
                                   SATUAN_BATU_BELAH, 
                                   SATUAN_BATU_PECAH, 
                                   SATUAN_PASIR_LOKAL, 
                                   SATUAN_PEKERJA, 
                                   SATUAN_MANDOR],
                        'Harga Satuan': [np.nan, 
                                         HSPK_BATU_BELAH, 
                                         HSPK_BATU_PECAH, 
                                         HSPK_PASIR_LOKAL, 
                                         HSPK_PEKERJA, 
                                         HSPK_MANDOR],
                        'Jumlah': [np.nan, 
                                   self.batu_belah, 
                                   self.batu_pecah, 
                                   self.pasir_lokal, 
                                   self.pekerja,
                                   self.mandor]
                    },
            'subtotal': self.ahsp_total
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
    def __init__(self, panjang_jalan_paving, lebar_jalan_paving, tipe_koefisien):
        self.pekerja = None
        self.tukang_batu = None
        self.kepala_tukang_batu = None
        self.mandor = None
        self.paving = None
        self.pasir_urug = None
        self.alat_pasang = None
        self.ahsp_total = None
        self.luas_pemasangan_paving = panjang_jalan_paving * lebar_jalan_paving
        self.koefisien_pemasangan_paving = KOEFISIEN_PEMASANGAN_PAVING[tipe_koefisien]

    def tenaga(self):
        self.pekerja = self.koefisien_pemasangan_paving['pekerja'] * HSPK_PEKERJA * self.luas_pemasangan_paving
        self.tukang_batu = self.koefisien_pemasangan_paving['tukang_batu'] * HSPK_TUKANG_BATU * self.luas_pemasangan_paving
        self.kepala_tukang_batu = self.koefisien_pemasangan_paving['kepala_tukang_batu'] * HSPK_KEPALA_TUKANG_BATU * self.luas_pemasangan_paving
        self.mandor = self.koefisien_pemasangan_paving['mandor'] * HSPK_MANDOR * self.luas_pemasangan_paving
        return self.pekerja + self.tukang_batu + self.kepala_tukang_batu + self.mandor 
    def bahan(self):
        self.paving = self.koefisien_pemasangan_paving['koefisien_paving'] * self.koefisien_pemasangan_paving['hspk_paving'] * self.luas_pemasangan_paving
        self.pasir_urug = self.koefisien_pemasangan_paving['pasir_urug'] * HSPK_PASIR_URUG * self.luas_pemasangan_paving
        return self.paving + self.pasir_urug
    def peralatan(self):
        self.alat_pasang = self.koefisien_pemasangan_paving['koefisien_paving'] * self.koefisien_pemasangan_paving['hspk_paving'] * self.luas_pemasangan_paving
        return self.alat_pasang
    def ahsp_pemasangan_paving(self):
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan()
    
    def hasil_perhitungan(self):
        self.tenaga()
        self.bahan()
        self.peralatan()
        self.ahsp_pemasangan_paving()
        return {
            'data' :{
                'Uraian': ['Pemasangan Paving', 'paving', 'pasir urug', 'pekerja', 'tukang batu', 'kepala tukang batu', 'mandor'],
                'koefisien': [np.nan, 
                            self.koefisien_pemasangan_paving['koefisien_paving'], 
                            self.koefisien_pemasangan_paving['pasir_urug'], 
                            self.koefisien_pemasangan_paving['pekerja'], 
                            self.koefisien_pemasangan_paving['tukang_batu'], 
                            self.koefisien_pemasangan_paving['kepala_tukang_batu'], 
                            self.koefisien_pemasangan_paving['mandor']],

                'Volume': [np.nan] + [self.luas_pemasangan_paving] * 6,
                'Satuan': [np.nan,
                            SATUAN_PAVING,
                            SATUAN_PASIR_URUG, 
                            SATUAN_PEKERJA, 
                            SATUAN_TUKANG_BATU, 
                            SATUAN_KEPALA_TUKANG_BATU, 
                            SATUAN_MANDOR],
                'Harga Satuan': [np.nan,
                                self.koefisien_pemasangan_paving['hspk_paving'],
                                HSPK_PASIR_URUG, 
                                HSPK_PEKERJA, 
                                HSPK_TUKANG_BATU, 
                                HSPK_KEPALA_TUKANG_BATU, 
                                HSPK_MANDOR],
                'Jumlah': [np.nan,
                            self.paving, 
                            self.pasir_urug, 
                            self.pekerja, 
                            self.tukang_batu, 
                            self.kepala_tukang_batu, 
                            self.mandor]
                },
            'subtotal': self.ahsp_total
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
    def __init__(self, panjang_beton, lebar_beton, kedalaman_beton, tipe_koefisien):
        self.pekerja = None
        self.tukang = None
        self.kepala_tukang = None
        self.mandor = None
        self.concrete_pump = None
        self.ahsp_total = None
        self.volume_jalan_beton = panjang_beton * lebar_beton * kedalaman_beton
        self.hspk_beton = KOEFISIEN_HSPK_BETON[tipe_koefisien]

    def tenaga(self):
        self.pekerja = 1 * HSPK_PEKERJA * self.volume_jalan_beton
        self.tukang = 0.25 * HSPK_TUKANG_BATU * self.volume_jalan_beton
        self.kepala_tukang = 0.025 * HSPK_KEPALA_TUKANG * self.volume_jalan_beton
        self.mandor = 0.1 * HSPK_MANDOR * self.volume_jalan_beton
        return self.pekerja + self.tukang + self.kepala_tukang + self.mandor
    def bahan(self):
        self.beton = 1.02 * self.hspk_beton['nilai_hspk_beton'] * self.volume_jalan_beton
        return self.beton
    def peralatan(self):
        self.concrete_pump = 0.12 * HSPK_CONCRETE_PUMP * self.volume_jalan_beton
        return self.concrete_pump
    def ahsp_beton_readymix(self) :
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan()

    def beton_readymix(self):
        self.tenaga()
        self.bahan()
        self.peralatan()
        self.ahsp_beton_readymix()
        return {
            'data' :{
                'Uraian': ['Beton Ready Mix', 'beton', 'concrete_pump', 'pekerja', 'tukang', 'kepala tukang', 'mandor'],
                'koefisien': [np.nan, 
                                1.02, 
                                0.12, 
                                1, 
                                0.25, 
                                0.025, 
                                0.1],

                'Volume': [np.nan] + [self.volume_jalan_beton] * 6,
                'Satuan': [np.nan,
                            SATUAN_BETON,
                            SATUAN_CONCRETE_PUMP, 
                            SATUAN_PEKERJA, 
                            SATUAN_TUKANG, 
                            SATUAN_KEPALA_TUKANG, 
                            SATUAN_MANDOR],

                'Harga Satuan': [np.nan,
                                    self.hspk_beton['nilai_hspk_beton'], 
                                    SATUAN_CONCRETE_PUMP, 
                                    SATUAN_PEKERJA, 
                                    SATUAN_TUKANG, 
                                    SATUAN_KEPALA_TUKANG, 
                                    SATUAN_MANDOR],

                'Jumlah': [np.nan, 
                            self.pekerja, 
                            self.concrete_pump, 
                            self.pekerja, 
                            self.tukang, 
                            self.kepala_tukang, 
                            self.mandor]
            },
            'subtotal': self.ahsp_total
        }

# Bekisting
# Koefisien Bekisting Lantai
KOEFISIEN_BEKISTING_LANTAI = {
    'multipleks_18mm' : {
        'pekerja' : 0.3,
        'tukang' : 0.3,
        'kepala_tukang' : 0.03,
        'mandor' : 0.03,
        'multipleks' : 0.128,
        'kayu_bekisting' : 0.006,
        'paku_biasa' : 0.28,
        'minyak_bekisting' : 0.25
    },
    'multipleks_12mm' : {
        'pekerja' : 0.2,
        'tukang' : 0.1,
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
    def __init__(self, panjang_bekisting_lantai, lebar_bekisting_lantai, tipe_koefisien):
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
        self.hspk_bekisting = KOEFISIEN_BEKISTING_LANTAI[tipe_koefisien]

    def tenaga(self):
        self.pekerja = self.hspk_bekisting['pekerja'] * HSPK_PEKERJA * self.luas_bekisting_lantai
        self.tukang = self.hspk_bekisting['tukang'] * HSPK_TUKANG * self.luas_bekisting_lantai
        self.kepala_tukang = self.hspk_bekisting['kepala_tukang'] * HSPK_KEPALA_TUKANG * self.luas_bekisting_lantai
        self.mandor = self.hspk_bekisting['mandor'] * HSPK_MANDOR * self.luas_bekisting_lantai
        return self.pekerja + self.tukang + self.kepala_tukang + self.mandor
    def bahan(self):
        self.multipleks = self.hspk_bekisting['multipleks'] * HSPK_MULTIPLEKS * self.luas_bekisting_lantai
        self.kayu_bekisting = self.hspk_bekisting['kayu_bekisting'] * HSPK_KAYU_BEKISTING * self.luas_bekisting_lantai
        self.paku_biasa = self.hspk_bekisting['paku_biasa'] * HSPK_PAKU_BIASA * self.luas_bekisting_lantai
        self.minyak_bekisting = self.hspk_bekisting['minyak_bekisting'] * HSPK_MINYAK_BEKISTING * self.luas_bekisting_lantai
        return self.multipleks + self.kayu_bekisting + self.paku_biasa + self.minyak_bekisting
    def ahsp_bekisting_lantai(self) :
        self.total = self.tenaga() + self.bahan()   

    def bekisting_lantai(self):
        self.tenaga()
        self.bahan()
        self.ahsp_bekisting_lantai()
        return {
                'data' : {
                        'Uraian': ['Bekisting', 'Multipleks', 'Kayu Bekisting', 'Paku Biasa', 'Minyak Bekisting', 'Pekerja', 'Tukang', 'Kepala Tukang', 'Mandor'],
                        'Koefisien': [np.nan,
                                    self.hspk_bekisting['multipleks'],
                                    self.hspk_bekisting['kayu_bekisting'],
                                    self.hspk_bekisting['paku_biasa'],
                                    self.hspk_bekisting['minyak_bekisting'],
                                    self.hspk_bekisting['pekerja'],
                                    self.hspk_bekisting['tukang'],
                                    self.hspk_bekisting['kepala_tukang'],
                                    self.hspk_bekisting['mandor']],
                        'Volume': [np.nan] + [self.luas_bekisting_lantai] * 8,
                        'Satuan': [np.nan,
                                    SATUAN_MULTIPLEKS,
                                    SATUAN_KAYU_BEKISTING,
                                    SATUAN_PAKU_BIASA,
                                    SATUAN_MINYAK_BEKISTING,
                                    SATUAN_PEKERJA,
                                    SATUAN_TUKANG,
                                    SATUAN_KEPALA_TUKANG,
                                    SATUAN_MANDOR],
                        'Harga Satuan': [np.nan,
                                        HSPK_MULTIPLEKS,
                                        HSPK_KAYU_BEKISTING,
                                        HSPK_PAKU_BIASA,
                                        HSPK_MINYAK_BEKISTING,
                                        HSPK_PEKERJA,
                                        HSPK_TUKANG,
                                        HSPK_KEPALA_TUKANG,
                                        HSPK_MANDOR],
                        'Jumlah': [np.nan,
                                    self.multipleks,
                                    self.kayu_bekisting,
                                    self.paku_biasa,
                                    self.minyak_bekisting,
                                    self.pekerja,
                                    self.tukang,
                                    self.kepala_tukang,
                                    self.mandor]
                    },
                'subtotal': self.ahsp_total
                }
# Bekisting Kolom
KOEFISIEN_BEKISTING_KOLOM = {
    'multipleks_18mm' : {
        'pekerja' : 0.33,
        'tukang' : 0.33,
        'kepala_tukang' : 0.033,
        'mandor' : 0.033,
        'multipleks' : 0.128,
        'kayu_bekisting' : 0.007,
        'paku_biasa' : 0.25,
        'minyak_bekisting' : 0.2
    },
    'multipleks_15mm' : {
        'pekerja' : 0.34,
        'tukang' :0.17,
        'kepala_tukang' : 0.017,
        'mandor' : 0.034,
        'multipleks' : 0.14,
        'kayu_bekisting' : 0.006,
        'paku_biasa' : 0.3,
        'minyak_bekisting' : 0.2
    },
    'multipleks_12mm' : {
        'pekerja' : 0.22,
        'tukang' : 0.11,
        'kepala_tukang' : 0.011,
        'mandor' : 0.022,
        'multipleks' : 0.128,
        'kayu_bekisting' : 0.006,
        'paku_biasa' : 0.25,
        'minyak_bekisting' : 0.2
    }
}
class BekistingKolom:
    def __init__(self, panjang_bekisting_kolom, lebar_bekisting_kolom, tipe_koefisien):
        self.pekerja = None
        self.tukang = None
        self.kepala_tukang = None
        self.mandor = None
        self.bondex = None
        self.kayu_jawa = None
        self.paku_biasa = None
        self.minyak_bekisting = None
        self.plywood = None
        self.dolken = None
        self.ahsp_total = None
        self.luas_bekisting_kolom = panjang_bekisting_kolom * lebar_bekisting_kolom
        self.hspk_multipleks = KOEFISIEN_BEKISTING_KOLOM[tipe_koefisien]

    def tenaga(self):
        self.pekerja = self.hspk_multipleks['pekerja'] * HSPK_PEKERJA * self.luas_bekisting_kolom
        self.tukang = self.hspk_multipleks['tukang'] * HSPK_TUKANG * self.luas_bekisting_kolom
        self.kepala_tukang = self.hspk_multipleks['kepala_tukang'] * HSPK_KEPALA_TUKANG * self.luas_bekisting_kolom
        self.mandor = self.hspk_multipleks['mandor'] * HSPK_MANDOR * self.luas_bekisting_kolom
        return self.pekerja + self.tukang + self.kepala_tukang + self.mandor
    def bahan(self):
        self.multipleks = self.hspk_multipleks['multipleks'] * HSPK_MULTIPLEKS * self.luas_bekisting_kolom
        self.kayu_bekisting = self.hspk_multipleks['kayu_bekisting'] * HSPK_KAYU_BEKISTING * self.luas_bekisting_kolom
        self.paku_biasa = self.hspk_multipleks['paku_biasa'] * HSPK_PAKU_BIASA * self.luas_bekisting_kolom
        self.minyak_bekisting = self.hspk_multipleks['minyak_bekisting'] * HSPK_MINYAK_BEKISTING * self.luas_bekisting_kolom
        return self.multipleks + self.kayu_bekisting + self.paku_biasa + self.minyak_bekisting
    def bekisting_kolom(self) :
        self.ahsp_total = self.tenaga() + self.bahan()

    def ahsp_bekisting_kolom(self):
        self.tenaga()
        self.bahan()
        self.bekisting_kolom()
        return {
                'data' : {
                        'Uraian': ['Bekisting', 'Multipleks', 'Kayu Bekisting', 'Paku Biasa', 'Minyak Bekisting', 'Pekerja', 'Tukang', 'Kepala Tukang', 'Mandor'],
                        'Koefisien': [np.nan,
                                    self.hspk_multipleks['multipleks'],
                                    self.hspk_multipleks['kayu_bekisting'],
                                    self.hspk_multipleks['paku_biasa'],
                                    self.hspk_multipleks['minyak_bekisting'],
                                    self.hspk_multipleks['pekerja'],
                                    self.hspk_multipleks['tukang'],
                                    self.hspk_multipleks['kepala_tukang'],
                                    self.hspk_multipleks['mandor']],
                        'Volume': [np.nan] + [self.luas_bekisting_kolom] * 8,
                        'Satuan': [np.nan,
                                    SATUAN_MULTIPLEKS,
                                    SATUAN_KAYU_BEKISTING,
                                    SATUAN_PAKU_BIASA,
                                    SATUAN_MINYAK_BEKISTING,
                                    SATUAN_PEKERJA,
                                    SATUAN_TUKANG,
                                    SATUAN_KEPALA_TUKANG,
                                    SATUAN_MANDOR],
                        'Harga Satuan': [np.nan,
                                        HSPK_MULTIPLEKS,
                                        HSPK_KAYU_BEKISTING,
                                        HSPK_PAKU_BIASA,
                                        HSPK_MINYAK_BEKISTING,
                                        HSPK_PEKERJA,
                                        HSPK_TUKANG,
                                        HSPK_KEPALA_TUKANG,
                                        HSPK_MANDOR],
                        'Jumlah': [np.nan,
                                    self.multipleks,
                                    self.kayu_bekisting,
                                    self.paku_biasa,
                                    self.minyak_bekisting,
                                    self.pekerja,
                                    self.tukang,
                                    self.kepala_tukang,
                                    self.mandor]
                    },
                'subtotal': self.ahsp_total
                }

# Pemadatan
# Urugan Tanah Kembali (Drainase)
class UruganTanahKembali:
    def __init__(self, panjang_pemadatan, lebar_pemadatan, kedalaman_pemadatan):
        self.pekerja = None
        self.mandor = None
        self.tukang = None
        self.ahsp_total = None
        self.volume_pemadatan = panjang_pemadatan * lebar_pemadatan * kedalaman_pemadatan

    def tenaga(self):
        self.pekerja = 0.226 * HSPK_PEKERJA * self.volume_pemadatan
        self.mandor = 0.007 * HSPK_MANDOR * self.volume_pemadatan
        self.tukang = 0.0062 * HSPK_TUKANG * self.volume_pemadatan
        return self.pekerja + self.mandor + self.tukang
    def ahsp_urugan_tanah_kembali(self):
        self.ahsp_total = self.tenaga()
    
    def galian_urugan_tanah_kembali(self):
        self.tenaga()
        self.ahsp_urugan_tanah_kembali()
        return {
                'data' :{
                        'Uraian':['Galian', 'Pekerja','Mandor','Tukang'],
                        'Koefisien':[np.nan, 0.226, 0.007,0.0062],
                        'Volume':[np.nan] + [self.volume_pemadatan]*3,
                        'Satuan': [np.nan, 
                                SATUAN_PEKERJA,
                                SATUAN_MANDOR,
                                SATUAN_TUKANG],
                        'Harga Satuan': [np.nan,
                                        HSPK_PEKERJA,
                                        HSPK_MANDOR,
                                        HSPK_TUKANG],
                        'Jumlah': [np.nan,
                                self.pekerja,
                                self.mandor,
                                self.tukang],
                    },
                'subtotal': self.ahsp_total
        }
# Pemadatan Tanah dengan Stamper
class PemadatanTanahDenganStamper:
    def __init__(self, panjang_pemadatan, lebar_pemadatan, kedalaman_pemadatan):
        self.pekerja = None
        self.mandor = None
        self.tukang = None
        self.ahsp_total = None
        self.volume_pemadatan = panjang_pemadatan * lebar_pemadatan * kedalaman_pemadatan

    def tenaga(self):
        self.pekerja = 0.062 * HSPK_PEKERJA * self.volume_pemadatan
        self.mandor = 0.186 * HSPK_MANDOR * self.volume_pemadatan
        self.tukang = 0.0062 * HSPK_TUKANG * self.volume_pemadatan
        return self.pekerja + self.mandor + self.tukang
    def peralatan(self):
        self.stamper = 0.05 * HSPK_STAMPER * self.volume_pemadatan
        return self.stamper
    def ahsp_pemadatan_tanah_dengan_stamper(self):
        self.ahsp_total = self.tenaga() + self.peralatan()
    
    def pemadatan_tanah_dengan_stamper(self):
        self.tenaga()
        self.peralatan()
        self.ahsp_pemadatan_tanah_dengan_stamper()
        return {
                'data' : {
                        'Uraian' : ['Pemadatan', 'Stamper', 'Pekerja', 'Mandor', 'Tukang'],
                        'Koefisien' : [np.nan, 0.05, 0.062, 0.186, 0.0062],
                        'Volume' : [np.nan] + [self.volume_pemadatan]*4,
                        'Satuan' : [np.nan,
                                    SATUAN_STAMPER,
                                    SATUAN_PEKERJA,
                                    SATUAN_MANDOR,
                                    SATUAN_TUKANG],
                        'Harga Satuan' : [np.nan,
                                            HSPK_STAMPER,
                                            HSPK_PEKERJA,
                                            HSPK_MANDOR,
                                            HSPK_TUKANG],
                        'Jumlah' : [np.nan,
                                    self.stamper,
                                    self.pekerja,
                                    self.mandor,
                                    self.tukang]
                    },
                'subtotal': self.ahsp_total
        }
# Pemadatan Tanah dengan Bulldozer
class PemadatanTanahDenganBulldozer:
    def __init__(self, panjang_pemadatan, lebar_pemadatan, kedalaman_pemadatan):
        self.pekerja = None
        self.mandor = None
        self.tukang = None
        self.bulldozer = None
        self.water_tanker = None
        self.roller_vibrator = None
        self.ahsp_total = None
        self.volume_pemadatan = panjang_pemadatan * lebar_pemadatan * kedalaman_pemadatan

    def tenaga(self):
        self.pekerja = 0.062 * HSPK_PEKERJA * self.volume_pemadatan
        self.mandor = 0.186 * HSPK_MANDOR * self.volume_pemadatan
        self.tukang = 0.0062 * HSPK_TUKANG * self.volume_pemadatan
        return self.pekerja + self.mandor + self.tukang
    def peralatan(self):
        self.bulldozer = 0.02 * HSPK_BULLDOZER * self.volume_pemadatan
        self.water_tanker = 0.0078 * HSPK_WATER_TANKER * self.volume_pemadatan
        self.roller_vibrator = 0.0178 * HSPK_ROLLER_VIBRATOR * self.volume_pemadatan
        return self.bulldozer + self.water_tanker + self.roller_vibrator
    def ahsp_pemadatan_tanah_dengan_bulldozer(self):
        self.ahsp_total = self.tenaga() + self.peralatan()
    
    def pemadatan_dengan_stamper(self):
        self.tenaga()
        self.peralatan()
        self.ahsp_pemadatan_tanah_dengan_bulldozer()
        return {
                'data' : {
                        'Uraian' : ['Pemadatan', 'Buldozzer','Water Tanker', 'Roller Fibrator', 'Pekerja','Mandor', 'Tukang'],
                        'Koefisien': [np.nan, 0.02, 0.0078, 0.0178, 0.062, 0.186, 0.0062],
                        'Volume' : [np.nan] + [self.volume_pemadatan]*6,
                        'Satuan': [np.nan,
                                    SATUAN_BULLDOZER,
                                    SATUAN_WATER_TANKER,
                                    SATUAN_ROLLER_VIBRATOR,
                                    SATUAN_PEKERJA,
                                    SATUAN_MANDOR,
                                    SATUAN_TUKANG],
                        'Harga Satuan': [np.nan,
                                        HSPK_BULLDOZER,
                                        HSPK_WATER_TANKER,
                                        HSPK_ROLLER_VIBRATOR,
                                        HSPK_PEKERJA,
                                        HSPK_MANDOR,
                                        HSPK_TUKANG],
                        'Jumlah': [np.nan,
                                    self.bulldozer,
                                    self.water_tanker,
                                    self.roller_vibrator,
                                    self.pekerja,
                                    self.mandor,
                                    self.tukang]
                },
                'subtotal': self.ahsp_total
        }
# Pemadatan Beton dengan Vibrator
class PemadatanBetonDenganVibrator:
    def __init__(self, panjang_pemadatan, lebar_pemadatan, kedalaman_pemadatan):
        self.pekerja = None
        self.mandor = None
        self.vibrator_roller = None
        self.ahsp_total = None
        self.volume_pemadatan = panjang_pemadatan * lebar_pemadatan * kedalaman_pemadatan

    def tenaga(self):
        self.pekerja = 0.25 * HSPK_PEKERJA * self.volume_pemadatan
        self.mandor = 0.025 * HSPK_MANDOR * self.volume_pemadatan
        return self.pekerja + self.mandor
    def peralatan(self):
        self.vibrator_roller = 0.1 * HSPK_VIBRATOR_ROLLER * self.volume_pemadatan
        return self.vibrator_roller
    def ahsp_pemadatan_beton_dengan_vibrator(self):
        self.ahsp_total = self.tenaga() + self.peralatan()
    
    def pemadatan_beton_vibrator(self):
        self.tenaga()
        self.peralatan()
        self.ahsp_pemadatan_beton_dengan_vibrator()
        return {
            'pekerja' : self.pekerja,
            'mandor' : self.mandor,
            'vibrator_roller' : self.vibrator_roller,
            'ahsp_total' : self.ahsp_total
        }
# Pemadatan Beton Manual
class PemadatanBetonManual:
    def __init__(self, panjang_pemadatan, lebar_pemadatan, kedalaman_pemadatan):
        self.pekerja = None
        self.mandor = None
        self.ahsp_total = None
        self.volume_pemadatan = panjang_pemadatan * lebar_pemadatan * kedalaman_pemadatan

    def tenaga(self):
        self.pekerja = 0.25 * HSPK_PEKERJA * self.volume_pemadatan
        self.mandor = 0.025 * HSPK_MANDOR * self.volume_pemadatan
        return self.pekerja + self.mandor
    def ahsp_pemadatan_beton_manual(self):
        self.ahsp_total = self.tenaga()
    
    def pemadatan_beton_manual(self):
        self.tenaga()
        self.ahsp_pemadatan_beton_manual()
        return {
                'data' : {
                    'Uraian': ['Pemadatan', 'Pekerja', 'Mandor'],
                    'Koefisien': [np.nan, 0.25, 0.025],
                    'Volume': [np.nan] + [self.volume_pemadatan]*2,
                    'Satuan': [np.nan,
                            SATUAN_PEKERJA,
                            SATUAN_MANDOR],
                    'Harga Satuan': [np.nan,
                                    HSPK_PEKERJA,
                                    HSPK_MANDOR],
                    'Jumlah': [np.nan,
                            self.pekerja,
                            self.mandor]
                },
                'subtotal': self.ahsp_total
        }
    
# Perkerasan
# Perkerasan Beton Semen
class PerkerasanBetonSemen:
    def __init__(self, panjang_beton, lebar_beton, tebal_beton):
        self.pekerja = None
        self.tukang = None
        self.mandor = None
        self.semen_40kg = None
        self.pasir_urug = None
        self.baja_tulangan_polos = None
        self.joint_sealent = None
        self.cat_anti_karat = None
        self.expansion_cap = None
        self.polytene_125_mikron = None
        self.curing_compound = None
        self.formwork_plate = None
        self.paku = None
        self.additive = None
        self.wheel_loader = None
        self.batching_plant = None
        self.truck_mixer = None
        self.concrete_vibrator = None
        self.water_tanker = None
        self.slip_form_paver = None
        self.ahsp_total = None
        self.volume_beton = panjang_beton * lebar_beton * tebal_beton

    def tenaga(self):
        self.pekerja = 0.2008 * HSPK_PEKERJA * self.volume_beton
        self.tukang = 0.1004 * HSPK_TUKANG* self.volume_beton
        self.mandor = 0.0215 * HSPK_MANDOR * self.volume_beton
        return self.pekerja + self.tukang + self.mandor
    def bahan(self):
        self.semen_40kg = 10.25 * HSPK_SEMEN_40KG * self.volume_beton
        self.pasir_urug = 0.6237 * HSPK_PASIR_URUG * self.volume_beton
        self.baja_tulangan_polos = 45 * HSPK_BAJA_TULANGAN_POLOS * self.volume_beton
        self.joint_sealent = 0.99 * HSPK_JOINT_SEALENT * self.volume_beton
        self.cat_anti_karat = 0.02 * HSPK_CAT_ANTI_KARAT * self.volume_beton
        self.expansion_cap = 0.17 * HSPK_EXPANSION_CAP * self.volume_beton
        self.polytene_125_mikron = 0.3281 * HSPK_POLYTENE_125_MIKRON * self.volume_beton
        self.curing_compound = 0.6525 * HSPK_CURING_COMPOUND * self.volume_beton
        self.formwork_plate = 0.57 * HSPK_FORMWORK_PLATE * self.volume_beton
        self.paku = 0.35 * HSPK_PAKU * self.volume_beton
        self.additive = 0.8568 * HSPK_ADDITIVE * self.volume_beton
        return self.semen_40kg + self.pasir_urug + self.baja_tulangan_polos + self.joint_sealent + self.cat_anti_karat + self.expansion_cap + self.polytene_125_mikron + self. curing_compound + self.formwork_plate + self.paku + self.additive
    def peralatan(self):
        self.wheel_loader = 0.0244 * self.volume_beton
        self.batching_plant = 0.0502 * HSPK_BATCHING_PLANT * self.volume_beton
        self.truck_mixer = 0.4942 * HSPK_TRUK_MIXER * self.volume_beton
        self.concrete_vibrator = 0.0502 * HSPK_CONCRETE_VIBRATOR * self.volume_beton
        self.water_tanker = 0.0422 * HSPK_WATER_TANKER * self.volume_beton
        self.slip_form_paver = 0.0074 * HSPK_SLIP_FORM_PAVER * self.volume_beton
        return self.wheel_loader + self.batching_plant + self.truck_mixer + self.concrete_vibrator + self.water_tanker + self.slip_form_paver
    def ahsp_perkerasan_beton_semen(self) :
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan

    def perkerasan_beton_semen(self):
        self.tenaga()
        self.bahan()
        self.peralatan()
        self.ahsp_perkerasan_beton_semen()
        return {
                'data' : {
                    'Uraian': ['Perkerasan','Semen 40 kg', 'Pasir Urug', 'Baja Tulangan Polos', 'Joint Sealent', 'Cat Anti Karat', 'Expansion Cap', 'Polytene 125 Mikron','Curing Compound','Formwork Plate', 'Paku','Additive','Wheel Loader','Batching Plant', 'Truck Mixer','Concrete Vibrator','Water Tanker','Slip Form Paver', 'Pekerja', 'Tukang', 'Mandor'],
                    'Koefisien': [np.nan, 10.25, 0.6237, 45, 0.99, 0.02, 0.17, 0.3281, 0.6525, 0.57, 0.35, 0.8568, 0.0244, 0.0502, 0.4942, 0.0502, 0.0422, 0.0074, 0.2008, 0.1004, 0.0215],
                    'Volume': [np.nan] + [self.volume_beton]*20,
                    'Satuan': [np.nan,
                                SATUAN_SEMEN_40KG,
                                SATUAN_PASIR_URUG,
                                SATUAN_BAJA_TULANGAN_POLOS,
                                SATUAN_JOINT_SEALENT,
                                SATUAN_CAT_ANTI_KARAT,
                                SATUAN_EXPANSION_CAP,
                                SATUAN_POLYTENE_125_MIKRON,
                                SATUAN_CURING_COMPOUND,
                                SATUAN_FORMWORK_PLATE,
                                SATUAN_PAKU,
                                SATUAN_ADDITIVE,
                                SATUAN_WHEEL_LOADER,
                                SATUAN_BATCHING_PLANT,
                                SATUAN_TRUK_MIXER,
                                SATUAN_CONCRETE_VIBRATOR,
                                SATUAN_WATER_TANKER,
                                SATUAN_SLIP_FORM_PAVER,
                                SATUAN_PEKERJA,
                                SATUAN_TUKANG,
                                SATUAN_MANDOR],
                    'Harga Satuan': [np.nan,
                                    HSPK_SEMEN_40KG,
                                    HSPK_PASIR_URUG,
                                    HSPK_BAJA_TULANGAN_POLOS,
                                    HSPK_JOINT_SEALENT,
                                    HSPK_CAT_ANTI_KARAT,
                                    HSPK_EXPANSION_CAP,
                                    HSPK_POLYTENE_125_MIKRON,
                                    HSPK_CURING_COMPOUND,
                                    HSPK_FORMWORK_PLATE,
                                    HSPK_PAKU,
                                    HSPK_ADDITIVE,
                                    HSPK_WHEEL_LOADER,
                                    HSPK_BATCHING_PLANT,
                                    HSPK_TRUK_MIXER,
                                    HSPK_CONCRETE_VIBRATOR,
                                    HSPK_WATER_TANKER,
                                    HSPK_SLIP_FORM_PAVER,
                                    HSPK_PEKERJA,
                                    HSPK_TUKANG,
                                    HSPK_MANDOR],
                    'Jumlah': [np.nan,
                                self.semen_40kg,
                                self.pasir_urug,
                                self.baja_tulangan_polos,
                                self.joint_sealent,
                                self.cat_anti_karat,
                                self.expansion_cap,
                                self.polytene_125_mikron,
                                self.curing_compound,
                                self.formwork_plate,
                                self.paku,
                                self.additive,
                                self.wheel_loader,
                                self.batching_plant,
                                self.truck_mixer,
                                self.concrete_vibrator,
                                self.water_tanker,
                                self.slip_form_paver,
                                self.pekerja,
                                self.tukang,
                                self.mandor]
                },
                'subtotal': self.ahsp_total
        }
# Perkerasan Jalan Beton
class PerkerasanJalanBeton:
    def __init__(self, panjang_beton, lebar_beton, tebal_beton):
        self.pekerja = None
        self.tukang = None
        self.mandor = None
        self.semen_40kg = None
        self.pasir_urug = None
        self.baja_tulangan_polos = None
        self.joint_sealent = None
        self.cat_anti_karat = None
        self.expansion_cap = None
        self.polytene_125_mikron = None
        self.curing_compound = None
        self.multipleks_12mm = None
        self.kayu_acuan = None
        self.paku = None
        self.additive = None
        self.wheel_loader = None
        self.batching_plant = None
        self.truck_mixer = None
        self.concrete_vibrator = None
        self.water_tanker = None
        self.slip_form_paver = None
        self.ahsp_total = None
        self.volume_beton = panjang_beton * lebar_beton * tebal_beton

    def tenaga(self):
        self.pekerja = 0.2008 * HSPK_PEKERJA * self.volume_beton
        self.tukang = 0.1004 * HSPK_TUKANG* self.volume_beton
        self.mandor = 0.0215 * HSPK_MANDOR * self.volume_beton
        return self.pekerja + self.tukang + self.mandor
    def bahan(self):
        self.semen_40kg = 2.1781 * HSPK_SEMEN_40KG * self.volume_beton
        self.pasir_urug = 0.6237 * HSPK_PASIR_URUG * self.volume_beton
        self.baja_tulangan_polos = 15.875 * HSPK_BAJA_TULANGAN_POLOS * self.volume_beton
        self.joint_sealent = 0.99 * HSPK_JOINT_SEALENT * self.volume_beton
        self.cat_anti_karat = 0.02 * HSPK_CAT_ANTI_KARAT * self.volume_beton
        self.expansion_cap = 0.17 * HSPK_EXPANSION_CAP * self.volume_beton
        self.polytene_125_mikron = 0.4375 * HSPK_POLYTENE_125_MIKRON * self.volume_beton
        self.curing_compound = 0.87 * HSPK_CURING_COMPOUND * self.volume_beton
        self.multipleks_12mm = 0.16 * 262450 * self.volume_beton
        self.kayu_acuan = 0.096 * HSPK_KAYU_ACUAN * self.volume_beton
        self.paku = 1.024 * HSPK_PAKU * self.volume_beton
        self.additive = 0.9139 * HSPK_ADDITIVE * self.volume_beton
        return self.semen_40kg + self.pasir_urug + self.baja_tulangan_polos + self.joint_sealent + self.cat_anti_karat + self.expansion_cap + self.polytene_125_mikron + self.curing_compound + self.multipleks_12mm + self.kayu_acuan + self.paku + self.paku + self.additive
    def peralatan(self):
        self.wheel_loader = 0.0244 * self.volume_beton
        self.batching_plant = 0.0502 * HSPK_BATCHING_PLANT * self.volume_beton
        self.truck_mixer = 0.6709 * HSPK_TRUK_MIXER * self.volume_beton
        self.concrete_vibrator = 0.0502 * HSPK_CONCRETE_VIBRATOR * self.volume_beton
        self.water_tanker = 0.0422 * HSPK_WATER_TANKER * self.volume_beton
        self.slip_form_paver = 0.0074 * HSPK_SLIP_FORM_PAVER * self.volume_beton
        return self.wheel_loader + self.batching_plant + self.truck_mixer + self.concrete_vibrator + self.water_tanker + self.slip_form_paver
    def ahsp_perkerasan_beton_semen(self) :
        self.ahsp_total = self.tenaga() + self.bahan() + self.peralatan

    def perkerasan_beton_semen(self):
        self.tenaga()
        self.bahan()
        self.peralatan()
        self.ahsp_perkerasan_beton_semen()
        return {
                'data' :{
                    'Uraian': ['Perkerasan', 'Semen 40 kg', 'Pasir Urug', 'Baja Tulangan Polos', 'Joint Sealent', 'Cat Anti Karat', 'Expansion Cap', 'Polytene 125 Mikron','Curing Compound','Multipleks 12 mm', 'Kayu Acuan','Paku','Additive','Wheel Loader','Batching Plant', 'Truck Mixer','Concrete Vibrator','Water Tanker','Slip Form Paver', 'Pekerja', 'Tukang', 'Mandor'],
                    'Koefisien': [np.nan, 2.1781, 0.6237, 15.875, 0.99, 0.02, 0.17, 0.4375, 0.87, 0.16, 0.096, 1.024, 0.9139, 0.0244, 0.0502, 0.6709, 0.0502, 0.0422, 0.0074, 0.200, 0.1004, 0.0215],
                    'Volume': [np.nan] + [self.volume_beton]*21,
                    'Satuan': [np.nan,
                            SATUAN_PEKERJA,
                            SATUAN_TUKANG,
                            SATUAN_MANDOR,
                            SATUAN_SEMEN_40KG,
                            SATUAN_PASIR_URUG,
                            SATUAN_BAJA_TULANGAN_POLOS,
                            SATUAN_JOINT_SEALENT,
                            SATUAN_CAT_ANTI_KARAT,
                            SATUAN_EXPANSION_CAP,
                            SATUAN_POLYTENE_125_MIKRON,
                            SATUAN_CURING_COMPOUND,
                            SATUAN_MULTIPLEKS,
                            SATUAN_KAYU_ACUAN,
                            SATUAN_PAKU,
                            SATUAN_ADDITIVE,
                            SATUAN_WHEEL_LOADER,
                            SATUAN_BATCHING_PLANT,
                            SATUAN_TRUK_MIXER,
                            SATUAN_CONCRETE_VIBRATOR,
                            SATUAN_WATER_TANKER,
                            SATUAN_SLIP_FORM_PAVER],
                    'Harga Satuan': [np.nan,
                                    HSPK_SEMEN_40KG,
                                    HSPK_PASIR_URUG,
                                    HSPK_BAJA_TULANGAN_POLOS,
                                    HSPK_JOINT_SEALENT,
                                    HSPK_CAT_ANTI_KARAT,
                                    HSPK_EXPANSION_CAP,
                                    HSPK_POLYTENE_125_MIKRON,
                                    HSPK_CURING_COMPOUND,
                                    262450,
                                    HSPK_KAYU_ACUAN,
                                    HSPK_PAKU,
                                    HSPK_ADDITIVE,
                                    HSPK_WHEEL_LOADER,
                                    HSPK_BATCHING_PLANT,
                                    HSPK_TRUK_MIXER,
                                    HSPK_CONCRETE_VIBRATOR,
                                    HSPK_WATER_TANKER,
                                    HSPK_SLIP_FORM_PAVER,
                                    HSPK_PEKERJA,
                                    HSPK_TUKANG,
                                    HSPK_MANDOR],
                    'Jumlah': [np.nan,
                            self.semen_40kg,
                            self.pasir_urug,
                            self.baja_tulangan_polos,
                            self.joint_sealent,
                            self.cat_anti_karat,
                            self.expansion_cap,
                            self.polytene_125_mikron,
                            self.curing_compound,
                            self.multipleks_12mm,
                            self.kayu_acuan,
                            self.paku,
                            self.additive,
                            self.wheel_loader,
                            self.batching_plant,
                            self.truck_mixer,
                            self.concrete_vibrator,
                            self.water_tanker,
                            self.slip_form_paver,
                            self.pekerja,
                            self.tukang,
                            self.mandor ],
                },
                'subtotal': self.ahsp_total
        }
    
# Perancah Bekisting Lantai
# Perancah Lantai Kayu
class PerancahLantaiKayu:
    def __init__(self, panjang_perancah, lebar_perancah):
        self.pekerja = None
        self.tukang = None
        self.kepala_tukang = None
        self.mandor = None
        self.kayu_perancah = None
        self.paku_biasa = None
        self.ahsp_total = None
        self.luas_perancah = panjang_perancah * lebar_perancah

    def tenaga(self):
        self.pekerja = 0.3 * HSPK_PEKERJA * self.luas_perancah
        self.tukang = 0.15 * HSPK_TUKANG * self.luas_perancah
        self.kepala_tukang = 0.015 * HSPK_KEPALA_TUKANG * self.luas_perancah
        self.mandor = 0.03 * HSPK_MANDOR * self.luas_perancah
        return self.pekerja + self.tukang + self.kepala_tukang + self.mandor
    def bahan(self):
        self.kayu_perancah = 0.02 * HSPK_KAYU_PERANCAH * self.luas_perancah
        self.paku_biasa = 0.25 * HSPK_PAKU_BIASA * self.luas_perancah
        return self.kayu_perancah + self.paku_biasa
    def perancah_lantai(self) :
        self.ahsp_total = self.tenaga() + self.bahan()

    def ahsp_perancah_lantai(self):
        self.tenaga()
        self.bahan()
        self.perancah_lantai()
        return {
                'data' : {
                        'Uraian': ['Bekisting', 'Kayu Perancah', 'Paku Biasa', 'Pekerja', 'Tukang', 'Kepala Tukang', 'Mandor'],
                        'Koefisien': [np.nan, 0.3, 0.15, 0.015, 0.03, 0.02, 0.25],
                        'Volume': [np.nan] + [self.luas_perancah] * 6,
                        'Satuan': [np.nan,
                                SATUAN_KAYU_PERANCAH,
                                SATUAN_PAKU_BIASA,
                                SATUAN_PEKERJA,
                                SATUAN_TUKANG,
                                SATUAN_KEPALA_TUKANG,
                                SATUAN_MANDOR],
                        'Harga Satuan': [np.nan,
                                        HSPK_KAYU_PERANCAH,
                                        HSPK_PAKU_BIASA,
                                        HSPK_PEKERJA,
                                        HSPK_TUKANG,
                                        HSPK_KEPALA_TUKANG,
                                        HSPK_MANDOR],
                        'Jumlah': [np.nan,
                                self.kayu_perancah,
                                self.paku_biasa,
                                self.pekerja,
                                self.tukang,
                                self.kepala_tukang,
                                self.mandor]
                    },
                'subtotal': self.ahsp_total
                }
# Perancah Lantai Dolken
class PerancahLantaiDolken:
    def __init__(self, panjang_perancah, lebar_perancah):
        self.pekerja = None
        self.tukang = None
        self.kepala_tukang = None
        self.mandor = None
        self.dolken = None
        self.paku_biasa = None
        self.ahsp_total = None
        self.luas_perancah = panjang_perancah * lebar_perancah

    def tenaga(self):
        self.pekerja = 0.34 * HSPK_PEKERJA * self.luas_perancah
        self.tukang = 0.17 * HSPK_TUKANG * self.luas_perancah
        self.kepala_tukang = 0.017 * HSPK_KEPALA_TUKANG * self.luas_perancah
        self.mandor = 0.034 * HSPK_MANDOR * self.luas_perancah
        return self.pekerja + self.tukang + self.kepala_tukang + self.mandor
    def bahan(self):
        self.dolken = 1.463 * HSPK_DOLKEN * self.luas_perancah
        self.paku_biasa = 0.3 * HSPK_PAKU_BIASA * self.luas_perancah
        return self.dolken + self.paku_biasa
    def perancah_lantai(self) :
        self.ahsp_total = self.tenaga() + self.bahan()

    def ahsp_perancah_lantai(self):
        self.tenaga()
        self.bahan()
        self.perancah_lantai()
        return {
                'data' : {
                        'Uraian': ['Bekisting', 'Dolken', 'Paku Biasa', 'Pekerja', 'Tukang', 'Kepala Tukang', 'Mandor'],
                        'Koefisien': [np.nan, 0.34, 0.17, 0.017, 0.034, 1.436, 0.3],
                        'Volume': [np.nan] + [self.luas_perancah] * 6,
                        'Satuan': [np.nan,
                                SATUAN_DOLKEN,
                                SATUAN_PAKU_BIASA,
                                SATUAN_PEKERJA,
                                SATUAN_TUKANG,
                                SATUAN_KEPALA_TUKANG,
                                SATUAN_MANDOR],
                        'Harga Satuan': [np.nan,
                                        HSPK_DOLKEN,
                                        HSPK_PAKU_BIASA,
                                        HSPK_PEKERJA,
                                        HSPK_TUKANG,
                                        HSPK_KEPALA_TUKANG,
                                        HSPK_MANDOR],
                        'Jumlah': [np.nan,
                                self.dolken,
                                self.paku_biasa,
                                self.pekerja,
                                self.tukang,
                                self.kepala_tukang,
                                self.mandor]
                    },
                'subtotal': self.ahsp_total
                }
# Perancah Lantai Bambu
class PerancahLantaiBambu:
    def __init__(self, panjang_perancah, lebar_perancah):
        self.pekerja = None
        self.tukang = None
        self.kepala_tukang = None
        self.mandor = None
        self.bambu = None
        self.paku_biasa = None
        self.ahsp_total = None
        self.luas_perancah = panjang_perancah * lebar_perancah

    def tenaga(self):
        self.pekerja = 0.32 * HSPK_PEKERJA * self.luas_perancah
        self.tukang = 0.16 * HSPK_TUKANG * self.luas_perancah
        self.kepala_tukang = 0.016 * HSPK_KEPALA_TUKANG * self.luas_perancah
        self.mandor = 0.032 * HSPK_MANDOR * self.luas_perancah
        return self.pekerja + self.tukang + self.kepala_tukang + self.mandor
    def bahan(self):
        self.bambu = 1.8 * HSPK_BAMBU * self.luas_perancah
        self.paku_biasa = 0.3 * HSPK_PAKU_BIASA * self.luas_perancah
        return self.bambu + self.paku_biasa
    def perancah_lantai(self) :
        self.ahsp_total = self.tenaga() + self.bahan()

    def ahsp_perancah_lantai(self):
        self.tenaga()
        self.bahan()
        self.perancah_lantai()
        return {
                'data' : {
                        'Uraian': ['Bekisting', 'Bambu', 'Paku Biasa', 'Pekerja', 'Tukang', 'Kepala Tukang', 'Mandor'],
                        'Koefisien': [np.nan, 0.32, 0.16, 0.016, 0.032, 1.8, 0.3],
                        'Volume': [np.nan] + [self.luas_perancah] * 6,
                        'Satuan': [np.nan,
                                SATUAN_BAMBU,
                                SATUAN_PAKU_BIASA,
                                SATUAN_PEKERJA,
                                SATUAN_TUKANG,
                                SATUAN_KEPALA_TUKANG,
                                SATUAN_MANDOR],
                        'Harga Satuan': [np.nan,
                                        HSPK_BAMBU,
                                        HSPK_PAKU_BIASA,
                                        HSPK_PEKERJA,
                                        HSPK_TUKANG,
                                        HSPK_KEPALA_TUKANG,
                                        HSPK_MANDOR],
                        'Jumlah': [np.nan,
                                self.bambu,
                                self.paku_biasa,
                                self.pekerja,
                                self.tukang,
                                self.kepala_tukang,
                                self.mandor]
                    },
                'subtotal': self.ahsp_total
                }

# Perancah Bekisting Kolom
# Perancah Kolom Kayu
class PerancahKolomKayu:
    def __init__(self, panjang_perancah, lebar_perancah):
        self.pekerja = None
        self.tukang = None
        self.kepala_tukang = None
        self.mandor = None
        self.kayu_perancah = None
        self.paku_biasa = None
        self.ahsp_total = None
        self.luas_perancah = panjang_perancah * lebar_perancah

    def tenaga(self):
        self.pekerja = 0.34 * HSPK_PEKERJA * self.luas_perancah
        self.tukang = 0.17 * HSPK_TUKANG * self.luas_perancah
        self.kepala_tukang = 0.017 * HSPK_KEPALA_TUKANG * self.luas_perancah
        self.mandor = 0.034 * HSPK_MANDOR * self.luas_perancah
        return self.pekerja + self.tukang + self.kepala_tukang + self.mandor
    def bahan(self):
        self.kayu_perancah = 0.011 * HSPK_KAYU_PERANCAH * self.luas_perancah
        self.paku_biasa = 0.25 * HSPK_PAKU_BIASA * self.luas_perancah
        return self.kayu_perancah + self.paku_biasa
    def perancah_kolom(self) :
        self.ahsp_total = self.tenaga() + self.bahan()

    def ahsp_perancah_kolom(self):
        self.tenaga()
        self.bahan()
        self.perancah_kolom()
        return {
                'data' : {
                        'Uraian': ['Bekisting', 'Kayu Perancah', 'Paku Biasa', 'Pekerja', 'Tukang', 'Kepala Tukang', 'Mandor'],
                        'Koefisien': [np.nan, 0.34, 0.17, 0.017, 0.034, 0.011, 0.25],
                        'Volume': [np.nan] + [self.luas_perancah] * 6,
                        'Satuan': [np.nan,
                                SATUAN_KAYU_PERANCAH,
                                SATUAN_PAKU_BIASA,
                                SATUAN_PEKERJA,
                                SATUAN_TUKANG,
                                SATUAN_KEPALA_TUKANG,
                                SATUAN_MANDOR],
                        'Harga Satuan': [np.nan,
                                        HSPK_KAYU_PERANCAH,
                                        HSPK_PAKU_BIASA,
                                        HSPK_PEKERJA,
                                        HSPK_TUKANG,
                                        HSPK_KEPALA_TUKANG,
                                        HSPK_MANDOR],
                        'Jumlah': [np.nan,
                                self.kayu_perancah,
                                self.paku_biasa,
                                self.pekerja,
                                self.tukang,
                                self.kepala_tukang,
                                self.mandor]
                    },
                'subtotal': self.ahsp_total
                }
# Perancah Kolom Dolken
class PerancahKolomDolken:
    def __init__(self, panjang_perancah, lebar_perancah):
        self.pekerja = None
        self.tukang = None
        self.kepala_tukang = None
        self.mandor = None
        self.dolken = None
        self.paku_biasa = None
        self.ahsp_total = None
        self.luas_perancah = panjang_perancah * lebar_perancah

    def tenaga(self):
        self.pekerja = 0.38 * HSPK_PEKERJA * self.luas_perancah
        self.tukang = 0.19 * HSPK_TUKANG * self.luas_perancah
        self.kepala_tukang = 0.019 * HSPK_KEPALA_TUKANG * self.luas_perancah
        self.mandor = 0.038 * HSPK_MANDOR * self.luas_perancah
        return self.pekerja + self.tukang + self.kepala_tukang + self.mandor
    def bahan(self):
        self.dolken =  0.748 * HSPK_DOLKEN * self.luas_perancah
        self.paku_biasa = 0.24 * HSPK_PAKU_BIASA * self.luas_perancah
        return self.dolken + self.paku_biasa
    def perancah_kolom(self) :
        self.ahsp_total = self.tenaga() + self.bahan()

    def ahsp_perancah_kolom(self):
        self.tenaga()
        self.bahan()
        self.perancah_kolom()
        return {
                'data' : {
                        'Uraian': ['Bekisting', 'Dolken', 'Paku Biasa', 'Pekerja', 'Tukang', 'Kepala Tukang', 'Mandor'],
                        'Koefisien': [np.nan, 0.38, 0.19, 0.019, 0.038, 0.748, 0.24],
                        'Volume': [np.nan] + [self.luas_perancah] * 6,
                        'Satuan': [np.nan,
                                SATUAN_DOLKEN,
                                SATUAN_PAKU_BIASA,
                                SATUAN_PEKERJA,
                                SATUAN_TUKANG,
                                SATUAN_KEPALA_TUKANG,
                                SATUAN_MANDOR],
                        'Harga Satuan': [np.nan,
                                        HSPK_DOLKEN,
                                        HSPK_PAKU_BIASA,
                                        HSPK_PEKERJA,
                                        HSPK_TUKANG,
                                        HSPK_KEPALA_TUKANG,
                                        HSPK_MANDOR],
                        'Jumlah': [np.nan,
                                self.dolken,
                                self.paku_biasa,
                                self.pekerja,
                                self.tukang,
                                self.kepala_tukang,
                                self.mandor]
                    },
                'subtotal': self.ahsp_total
                }
# Perancah Kolom Bambu
class PerancahKolomBambu:
    def __init__(self, panjang_perancah, lebar_perancah):
        self.pekerja = None
        self.tukang = None
        self.kepala_tukang = None
        self.mandor = None
        self.bambu = None
        self.paku_biasa = None
        self.tali_ijuk = None
        self.ahsp_total = None
        self.luas_perancah = panjang_perancah * lebar_perancah

    def tenaga(self):
        self.pekerja = 0.36 * HSPK_PEKERJA * self.luas_perancah
        self.tukang = 0.18 * HSPK_TUKANG * self.luas_perancah
        self.kepala_tukang = 0.018 * HSPK_KEPALA_TUKANG * self.luas_perancah
        self.mandor = 0.036 * HSPK_MANDOR * self.luas_perancah
        return self.pekerja + self.tukang + self.kepala_tukang + self.mandor
    def bahan(self):
        self.bambu = 0.92 * HSPK_BAMBU * self.luas_perancah
        self.paku_biasa = 0.24 * HSPK_PAKU_BIASA * self.luas_perancah
        self.tali_ijuk = 3.5 * HSPK_TALI_IJUK * self.tali_ijuk
        return self.bambu + self.paku_biasa + self.tali_ijuk
    def perancah_kolom(self) :
        self.ahsp_total = self.tenaga() + self.bahan()

    def ahsp_perancah_kolom(self):
        self.tenaga()
        self.bahan()
        self.perancah_kolom()
        return {
                'data' : {
                        'Uraian': ['Bekisting', 'Bambu', 'Paku Biasa', 'Tali Ijuk', 'Pekerja', 'Tukang', 'Kepala Tukang', 'Mandor'],
                        'Koefisien': [np.nan, 0.36, 0.18, 0.018, 0.036, 0.92, 0.24, 3.5],
                        'Volume': [np.nan] + [self.luas_perancah] * 7,
                        'Satuan': [np.nan,
                                SATUAN_BAMBU,
                                SATUAN_PAKU_BIASA,
                                SATUAN_TALI_IJUK,
                                SATUAN_PEKERJA,
                                SATUAN_TUKANG,
                                SATUAN_KEPALA_TUKANG,
                                SATUAN_MANDOR],
                        'Harga Satuan': [np.nan,
                                        HSPK_BAMBU,
                                        HSPK_PAKU_BIASA,
                                        HSPK_TALI_IJUK,
                                        HSPK_PEKERJA,
                                        HSPK_TUKANG,
                                        HSPK_KEPALA_TUKANG,
                                        HSPK_MANDOR],
                        'Jumlah': [np.nan,
                                self.bambu,
                                self.paku_biasa,
                                self.pekerja,
                                self.tukang,
                                self.kepala_tukang,
                                self.mandor]
                    },
                'subtotal': self.ahsp_total
                }
