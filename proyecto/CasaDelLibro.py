import gi

from proyecto.CrearFactura import CrearFactura
from proyecto.Inventario import Inventario
from proyecto.NuevoProv import NuevoProv
from proyecto.listaProveedores import listaProveedores

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class CasaDelLibro():
    """Ventana Principal de la Casa del Libro.
       Metodos:
            __init__ --Constructor

            on_btnAñadirProv_clicked -- Acceso a la ventana Añadir Proveedor
            on_btnModProv_clicked -- Acceso a la ventana Modificar Proveedor
            on_btnFactura_clicked  -- Acceso a la ventana Crear Factura
            on_btnInventario_clicked -- Acceso a la ventana Inventario
    """
    def __init__(self):
        """Constructor de la Ventana Principal de la Casa del Libro.
           Ventana que mediante unos botones nos da acceso al resto del programa.

            Parametros:
            -No tiene.

            Excepciones:
            -No teiene.

        """
        builder =  Gtk.Builder()
        builder.add_from_file("CasaDelLibro.glade")

        self.ventana = builder.get_object("Main")

        ##AÑADIMOS LA CABECERA
        cabeceira = Gtk.HeaderBar(title="Ventana Principal")
        cabeceira.set_subtitle("Bienvenido a la Casa del Libro")
        cabeceira.props.show_close_button = True

        self.ventana.set_titlebar(cabeceira)

        señales = {
            "on_btnAñadirProv_clicked": self.on_btnAñadirProv_clicked,
            "on_btnModProv_clicked": self.on_btnModProv_clicked,
            "on_btnFactura_clicked": self.on_btnFactura_clicked,
            "on_btnInventario_clicked": self.on_btnInventario_clicked,
            "on_btnSalir_clicked": Gtk.main_quit,
            "on_Main_destroy": Gtk.main_quit
        }

        builder.connect_signals(señales)

        self.ventana.show_all()

    def on_btnAñadirProv_clicked(self, boton):
        """Abre la ventana Añadir Proveedor
                Este metodo accede a la ventana Añadir Proveedor

            :param boton: acceso al botton
            :return: None
        """
        self.ventana.hide()
        NuevoProv(self.ventana)

    def on_btnModProv_clicked(self, boton):
        """Abre la ventana Modificar Proveedor
                        Este metodo accede a la ventana Modificar Proveedor

                    :param boton: acceso al botton
                    :return: None
                """
        self.ventana.hide()
        listaProveedores(self.ventana)

    def on_btnFactura_clicked(self, boton):
        """Abre la ventana Crear Factura
                Este metodo accede a la ventana Crear Factura

            :param boton: acceso al botton
            :return: None
        """
        self.ventana.hide()
        CrearFactura(self.ventana)

    def on_btnInventario_clicked(self, boton):
        """Abre la ventana ventana Inventario
                Este metodo accede a la ventana Inventario

            :param boton: acceso al botton
            :return: None
        """
        self.ventana.hide()
        Inventario(self.ventana)

def main():
    CasaDelLibro()
    Gtk.main()

if __name__ == "__main__":
    CasaDelLibro()
    Gtk.main()

