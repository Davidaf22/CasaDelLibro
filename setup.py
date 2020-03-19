from setuptools import setup

setup(
    name="proyectoDI",
    version="1.0",
    author="David",
    author_email="dalonsofernandez@danielcastelao.org",
    url="https://www.danielcastelao.org",
    license="GLP",
    platforms="Unix",
    clasifiers=["Development Status :: 3 - Alpha",
                "Environment :: Console",
                "Topic :: Software Development :: Libraries",
                "License :: OSI Aproved :: GNU General Public License",
                "Programming Language :: Python :: 3.4",
                "Operating System :: Linux Ubuntu"
                ],
    description="Proyecto DI con sphinx reportlab y mysqllite",
    keywords="empaquetado instalador paquetes",
    #packages=['proyectoDI'],
    # OTRA FORMA: packages = find_packages(exclude= ['*.test','*.test.*']) podemo excluír lo que queramos

    #data_files=[('datos', ['dat/datos.txt'])],
    entry_points={'console_scripts': ['opemProyect = CasaDelLibro: CasaDelLibro', ], }
)