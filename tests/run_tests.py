import unittest
import test_META_CO_LIBRARY

# Criando o test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Adicionando testes ao suite
suite.addTests(loader.loadTestsFromModule(TestMetaCOLibrary))


# Executando os testes
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
