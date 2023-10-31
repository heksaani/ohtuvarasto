import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

        # varasto object has def __init__(self, tilavuus, alku_saldo = 0):

    def test_konstruktori_luo_tyhjan_varaston(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastoon_lisataan_liikaa(self):
        # lisätään 11 eli kapasiteetti ylittii 12-10 = 2
        self.varasto.lisaa_varastoon(13)
        self.assertAlmostEqual(self.varasto.saldo, 10)  # jos ylittyy asetetaan tilavuus täyteen == 10 


    def test_varastosta_otetaan_liikaa(self):
        # otetaan enemmän kuin mitä siellä on 
        self.varasto.ota_varastosta(20)
        self.assertEqual(self.varasto.saldo, 0)


    def test_tilavuus_alle_nollan(self):
        # test case for this if tilavuus < 0.0:
        storage= Varasto(-1)
        self.assertEqual(storage.tilavuus, 0)

    def test_alkusaldo_alle_nollan(self):
        storage2 = Varasto(10, -1)
        self.assertEqual(storage2.saldo, 0)

    def test_lisattava_maara_alle_nollan(self):
        self.assertEqual(self.varasto.lisaa_varastoon(-1), None)

    def test_otettava_maara_alle_nollan(self):
        self.assertEqual(self.varasto.ota_varastosta(-1), 0)

    def test_tekstin_printtaus(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

