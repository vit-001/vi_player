__author__ = 'Nikitin'
from cx_Freeze import setup, Executable

setup(
    name = "VikaPlayer",
    version = "0.1",
    description = "VikaPlayer",
    executables = [Executable("run.pyw")]
)