import coverage
import unittest
import io
import contextlib

def executar_testes(retornar=False):
    cov = coverage.Coverage()
    cov.start()

    suite = unittest.defaultTestLoader.discover('tests')
    buffer = io.StringIO()

    with contextlib.redirect_stdout(buffer):
        unittest.TextTestRunner(verbosity=2).run(suite)

    cov.stop()
    cov.save()
    with contextlib.redirect_stdout(buffer):
        cov.report()

    resultado = buffer.getvalue()
    if retornar:
        return resultado
    else:
        print(resultado)
