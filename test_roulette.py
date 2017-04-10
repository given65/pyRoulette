import unittest
import roulette as rlt


class Test_MiseSommeNumero(unittest.TestCase):
    def test_SommeMiseValide (self):
        self.assertEqual(rlt.estSommeMiseValide("toto"),0)
        self.assertEqual(rlt.estSommeMiseValide(-1),0)
        self.assertEqual(rlt.estSommeMiseValide(1.78),0)
        self.assertEqual(rlt.estSommeMiseValide(75),75)
       
    def test_NumeroMiseValide(self):
        self.assertEqual(rlt.estNumeroMiseValide("toto"),-1)
        self.assertEqual(rlt.estNumeroMiseValide(rlt.NUM_MIN-2),-1)
        self.assertEqual(rlt.estNumeroMiseValide(2.5),-1)
        self.assertEqual(rlt.estNumeroMiseValide(rlt.NUM_MAX+1),-1)
        self.assertEqual(rlt.estNumeroMiseValide(45),45)
     
    def test_couleurNumero(self):
        self.assertEqual(rlt.couleurNumero("toto"),"n.c.")
        self.assertEqual(rlt.couleurNumero(0.4),"n.c.")
        self.assertEqual(rlt.couleurNumero(4),"noir")
        self.assertEqual(rlt.couleurNumero(9),"rouge")
       
     
class Test_numeroGagantRoulette(unittest.TestCase):
    def test_numeroRoulette(self):
        self.assertEqual(rlt.numeroRoulette(1),8)
        self.assertEqual(rlt.numeroRoulette(),36)
    
    def test_gainPartie (self) :
        self.assertEqual(rlt.gainPartie(10, 23, 23),30)
        self.assertEqual(rlt.gainPartie(10, 23, 21),5)
        self.assertEqual(rlt.gainPartie(10, 23, 22),0)
        
if __name__ == "__main__":
    unittest.main ()
    
