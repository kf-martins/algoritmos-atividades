import os
import re
import subprocess

# Caminho do arquivo README.md com os diagramas
README_PATH = os.path.join('Fluxograms', 'README.md')
# Pasta de saída para os PNGs
dest_folder = 'Fluxograms'

# Regex para capturar blocos mermaid e o nome da função acima deles
mermaid_block = re.compile(r'###\s*([\w_]+)\s*\([^)]*\)\s*\n+```mermaid\n(.*?)```', re.DOTALL)

def export_mermaid_to_png(mermaid_code, output_path):
    lines = mermaid_code.splitlines()
    filtered = []
    in_yaml = False
    for line in lines:
        if line.strip().startswith('---'):
            in_yaml = not in_yaml
            continue
        if line.strip().startswith('//'):
            continue
        if not in_yaml:
            filtered.append(line)
    clean_code = '\n'.join(filtered).strip()
    temp_file = 'temp.mmd'
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(clean_code)
    try:
        subprocess.run([
            'mmdc.cmd',
            '-i', temp_file,
            '-o', output_path,
            '-t', 'dark',
            '--backgroundColor', 'transparent'
        ], check=True)
    except FileNotFoundError:
        print('Erro: O comando "mmdc" não foi encontrado. Certifique-se de que o Mermaid CLI está instalado e no PATH.')
        os.remove(temp_file)
        return
    os.remove(temp_file)

def main():
    with open(README_PATH, encoding='utf-8') as f:
        content = f.read()
    for match in mermaid_block.finditer(content):
        func_name = match.group(1)
        mermaid_code = match.group(2).strip()
        output_path = os.path.join(dest_folder, f'{func_name}.png')
        print(f'Exportando {func_name}...')
        export_mermaid_to_png(mermaid_code, output_path)
    print('Exportação concluída.')

if __name__ == '__main__':
    main()
