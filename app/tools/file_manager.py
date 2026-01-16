from pathlib import Path
def save_file(f,c): Path(f).write_text(c); return f
