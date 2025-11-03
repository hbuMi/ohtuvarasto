import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
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

    def test_negatiivinen_tilavuus(self):
        testi = Varasto(-1)
        self.assertAlmostEqual(testi.tilavuus, 0)

    def test_negatiivinen_saldo(self):
        testi = Varasto(1, -1)
        self.assertAlmostEqual(testi.saldo, 0)

    def test_iso_saldo(self):
        testi = Varasto(1, 2)
        self.assertAlmostEqual(testi.saldo, testi.tilavuus)

    def test_lisaa_maara_alle_nolla(self):
        testi = Varasto(1, 0)
        testi.lisaa_varastoon(-3)
        self.assertAlmostEqual(testi.saldo, 0)

    def test_maara_isompi(self):
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_maara_alle_nolla(self):
        self.varasto.lisaa_varastoon(1)
        saatu = self.varasto.ota_varastosta(-8)
        self.assertAlmostEqual(saatu, 0)
        self.assertAlmostEqual(self.varasto.saldo, 1)

    def test_ota_enemman_kuin_saldo(self):
        self.varasto.lisaa_varastoon(8)
        saatu = self.varasto.ota_varastosta(80)
        self.assertAlmostEqual(saatu, 8)
        self.assertEqual(self.varasto.saldo, 0)

    def test_str_metodi_palauttaa_oikean_merkkijonon(self):
        self.varasto.lisaa_varastoon(5)
        odotus = "saldo = 5, vielä tilaa 5"
        self.assertEqual(str(self.varasto), odotus)