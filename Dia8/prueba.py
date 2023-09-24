import unittest
import Cambia_texto
#heredamos métodos para hacer test en esta clase
class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = "Holi Manoli"
        resultado = Cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'Holi Manoli')

if __name__ == '__main__':
    unittest.main()
