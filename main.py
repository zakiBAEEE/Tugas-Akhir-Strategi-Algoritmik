from pathlib import Path
import streamlit.web.bootstrap as bootstrap

# Path ke app.py
GUI_PATH = Path(__file__).parent / "gui" / "app.py"

def main():
    bootstrap.run(
        str(GUI_PATH),         # Path ke script Streamlit
        is_hello=False,        # False artinya bukan contoh Hello World
        args=[],               # Argumen CLI tambahan (kosongkan jika tidak ada)
        flag_options={}        # Opsi konfigurasi streamlit
    )

if __name__ == "__main__":
    main()
