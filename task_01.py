import argparse
from pathlib import Path
import shutil


def copy_files(src: Path, dist: Path):
    try:
        for item in src.iterdir():
            if item.is_dir():
                copy_files(item, dist)  # рекурсивний виклик для папок
            elif item.is_file():
                # беремо розширення без крапки або 'no_extension'
                ext = item.suffix.lstrip(".").lower() or "no_extension"

                target_dir = dist / ext
                target_dir.mkdir(parents=True, exist_ok=True)

                shutil.copy2(item, target_dir / item.name)
    except Exception as e:
        print(f"Помилка при обробці {src}: {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path, nargs="?", default=Path("dist"))
    args = parser.parse_args()

    if not args.source.exists():
        print("Вихідна директорія не існує!")
        return

    copy_files(args.source, args.destination)
    print("Готово!")


if __name__ == "__main__":
    main()

