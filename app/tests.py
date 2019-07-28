from django.test import TestCase

from .tradutor import transformar_numero_extenso


class TradutorTest(TestCase):
    def testPositivoUm(self):
        self.assertEqual(transformar_numero_extenso(11), 'onze')

    def testPositivoDois(self):
        self.assertEqual(transformar_numero_extenso(1999), 'um mil e novecentos e noventa e nove')

    def testPositivoTres(self):
        self.assertEqual(transformar_numero_extenso(999999), 'novecentos e noventa e nove mil e novecentos e noventa ' +
                                                             'e nove')

    def testNegativoUm(self):
        self.assertEqual(transformar_numero_extenso(-9), 'menos nove')

    def testNegativoDois(self):
        self.assertEqual(transformar_numero_extenso(-599), 'menos quinhentos e noventa e nove')

    def testNegativoTres(self):
        self.assertEqual(transformar_numero_extenso(-490361), 'menos quatrocentos e noventa mil e trezentos e sessenta e um')
