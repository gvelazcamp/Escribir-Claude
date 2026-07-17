# Escribir-Claude

Bot que escribe (y opcionalmente envía) un mensaje en [claude.ai/new](https://claude.ai/new) usando Playwright, reutilizando un perfil de Chrome persistente ya logueado.

## Requisitos

- Python 3.9 o superior, instalado y disponible en el `PATH` (verificá con `python --version` en una terminal).
- Google Chrome instalado (el bot lo controla mediante `channel="chrome"`).

## Instalación

1. Cloná o descargá este repositorio.
2. Abrí una terminal en la carpeta del proyecto e instalá las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Instalá el navegador que usa Playwright:

   ```bash
   playwright install chromium
   ```

## Uso

### En Windows

Hacé doble clic en `ejecutar.bat`, o corrélo desde la terminal:

```bat
ejecutar.bat
```

El script usa el `python` del `PATH`, así que asegurate de que el comando `python` funcione en tu terminal antes de ejecutarlo.

### Manualmente (cualquier sistema operativo)

```bash
python escribir_en_claude.py "Tu mensaje acá"
```

Si no pasás ningún argumento, se usa un mensaje de ejemplo definido en `MENSAJE` dentro de `escribir_en_claude.py`.

## Primer uso: iniciar sesión

La primera vez que lo corras, se abrirá una ventana de Chrome con un perfil nuevo y vacío. Vas a tener que iniciar sesión en `claude.ai` manualmente esa vez. Playwright guarda la sesión en un perfil persistente (carpeta configurada en `USER_DATA_DIR` dentro de `escribir_en_claude.py`), así que las próximas ejecuciones ya van a estar logueadas.

## Notas

- El navegador queda abierto al terminar para que puedas revisar el resultado; presioná Enter en la terminal cuando quieras cerrarlo.
- Podés cambiar el modelo usado editando la constante `MODELO` en `escribir_en_claude.py`.
