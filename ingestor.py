from pathlib import Path
import shutil

landing = Path("landing")
bronze = Path("bronze")
bad_data = Path("bad_data")

bronze.mkdir(parents=True, exist_ok=True)
bad_data.mkdir(parents=True, exist_ok=True)

for item in landing.iterdir():
    if not item.is_file():
        continue
    try:
        target_dir = bronze if item.stat().st_size > 0 else bad_data
        dest = target_dir / item.name
        if dest.exists():
            stem, suffix = item.stem, item.suffix
            i = 1
            while True:
                candidate = target_dir / f"{stem}_{i}{suffix}"
                if not candidate.exists():
                    dest = candidate
                    break
                i += 1
        shutil.move(str(item), str(dest))
        print(f"Procesado: {item.name} -> {'Bronze' if target_dir == bronze else 'Bad Data'}")
    except Exception as e:
        print(f"Error: {item.name} -> {e}")
