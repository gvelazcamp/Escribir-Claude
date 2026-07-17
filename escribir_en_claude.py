"""
Escribe un mensaje en claude.ai/new usando Playwright.
Requiere sesión ya logueada (usa un profile persistente de Chrome).
"""

import sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Falta instalar playwright. Corré en la terminal:")
    print("  pip install playwright")
    print("  playwright install chromium")
    input("Presioná Enter para salir...")
    sys.exit(1)

MENSAJE = sys.argv[1] if len(sys.argv) > 1 else (
    "Haceme un HTML de automatización para SIVO, mismo formato que los que venimos "
    "realizando, que no sea con voz, no realices preguntas, realizalo según vos veas "
    "que puede sumar para LinkedIn e Instagram, pero que no sea ninguno de los que "
    "ya hemos realizado."
)
USER_DATA_DIR = r"C:\PlaywrightProfiles\claude_profile"  # perfil propio del bot
MODELO = "Opus 4.8"


def seleccionar_modelo(page, modelo: str):
    boton = page.get_by_role("button", name="Sonnet 5").first
    if boton.count() == 0:
        return  # ya está en otro modelo (probablemente el deseado)
    boton.click(timeout=5000)
    page.wait_for_timeout(500)
    opcion = page.get_by_text(modelo, exact=True).first
    if opcion.count() == 0:
        page.get_by_text("Más modelos", exact=True).first.click()
        page.wait_for_timeout(500)
        opcion = page.get_by_text(modelo, exact=True).first
    opcion.click()
    page.wait_for_timeout(500)


def escribir_en_claude(mensaje: str, enviar: bool = True, modelo: str = MODELO):
    p = sync_playwright().start()
    context = p.chromium.launch_persistent_context(
        USER_DATA_DIR,
        headless=False,
        channel="chrome",
    )
    page = context.new_page()
    page.goto("https://claude.ai/new")

    if modelo:
        try:
            seleccionar_modelo(page, modelo)
        except Exception as e:
            print(f"No se pudo cambiar de modelo ({e}), sigo con el default.")

    # Textbox principal (contenteditable, role="textbox")
    cuadro = page.get_by_role("textbox")
    cuadro.wait_for(state="visible", timeout=30000)
    cuadro.click()
    page.wait_for_timeout(300)
    cuadro.press_sequentially(mensaje, delay=15)
    page.wait_for_timeout(500)

    if enviar:
        page.keyboard.press("Enter")
        page.wait_for_timeout(2000)

    return context, page


if __name__ == "__main__":
    try:
        ctx, pg = escribir_en_claude(MENSAJE)
        print("Listo, mensaje enviado.")
        input("El navegador queda abierto. Presioná Enter acá SOLO cuando quieras cerrarlo...")
    except Exception as e:
        import traceback
        traceback.print_exc()
        input("\nOcurrió un error (arriba el detalle). Presioná Enter para salir...")
