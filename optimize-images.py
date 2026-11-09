"""Generate local responsive WebP assets; source photographs stay untouched."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / '.tools'))
from PIL import Image

assets = Path(__file__).parent / 'assets'
for name, widths in {'hardware': (640, 1100), 'componentes': (480, 800, 1100), 'pc-gamer': (480, 800)}.items():
    with Image.open(assets / f'{name}.jpg') as source:
        for width in widths:
            output = source.convert('RGB')
            output.thumbnail((width, 10000), Image.Resampling.LANCZOS)
            target = assets / f'{name}-{width}.webp'
            output.save(target, 'WEBP', quality=79, method=6)
            print(f'{target.name}: {output.width}x{output.height}, {target.stat().st_size:,} bytes')

# Tight framing of the original logo eliminates decoding a 2000px square.
with Image.open(assets / 'techdetail-logo.png') as source:
    rgb = source.convert('RGB')
    bounds = rgb.point(lambda value: 255 if value > 35 else 0).getbbox()
    logo = rgb.crop(bounds)
    logo.thumbnail((640, 160), Image.Resampling.LANCZOS)
    logo.save(assets / 'logo.webp', 'WEBP', quality=92, method=6)
    print(f'logo.webp: {logo.width}x{logo.height}, {(assets / "logo.webp").stat().st_size:,} bytes')
