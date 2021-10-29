import os
import json
from pathlib import Path


SCRIPT_DIR = Path(os.path.dirname(__file__))


def generate_json():
    folder = SCRIPT_DIR.parent / 'zui-icons' / 'src'
    glyph_candidates = {}
    for file in folder.glob('**/*.svg'):
        relative_file = file.relative_to(folder)
        name, ext = os.path.splitext(relative_file.name)

        prefix, suffix = name.rsplit('_', 1)
        if prefix not in glyph_candidates:
            glyph_candidates[prefix] = (int(suffix), relative_file)
            continue

        index, _ = glyph_candidates[prefix]
        if index < int(suffix):
            glyph_candidates[prefix] = (int(suffix), relative_file)
            continue
    glyphs = {k: v[1] for k, v in glyph_candidates.items()}

    config = {
        'props': {
            'ascent': 200,
            'descent': 200,
            'em': 1000,
            'family': 'ZUiIcons'
        },
        'input': str(folder.as_posix()),
        'output': ['ZUiIcons.ttf'],
        'glyphs': {hex(i + 65): str(item.as_posix()) for i, item in enumerate(glyphs.values())}
    }

    with open('config.json', 'w') as json_config:
        json_config.write(json.dumps(config, indent=True))
        print(file=json_config)


if __name__ == '__main__':
    generate_json()

