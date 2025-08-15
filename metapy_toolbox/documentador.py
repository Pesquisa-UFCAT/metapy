import re
import os


def read_file_path(directory):
    """
    Esta função lê todos os arquivos .py dentro da pasta fornecida e retorna seus caminhos.

    Args:
        directory (str): Caminho da pasta a ser lida.

    Returns:
        list: Lista de caminhos dos arquivos .py encontrados.
    """
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_paths.append(os.path.join(root, file))
    return file_paths


def read_python_file(file_path):
    functions_dict = {}

    with open(file_path, 'r') as file:
        file_content = file.read()
        function_pattern = re.compile(r'def\s+(\w+)\((.*?)\):(?:\s*"""\s*(.*?)\s*""")?', re.DOTALL)
        functions = function_pattern.findall(file_content)

        for func_name, func_args, func_description in functions:
            if func_description:
                description = func_description.strip().split('\n')[0]

                args_list = [arg.strip() for arg in func_args.split(',')]
                
                # Capturando a seção Args e Returns separadamente
                args_section = re.search(r'Args:\s*(.*?)\s*(?:Returns:|$)', func_description, re.DOTALL)
                returns_section = re.search(r'Returns:\s*(.*)', func_description, re.DOTALL)

                extracted_args = {}
                if args_section:
                    args_content = args_section.group(1)
                    description_args = re.findall(r'\s*([a-zA-Z0-9_]+)\s*\((.*?)\):\s*(.*)', args_content)
                    for arg_name, arg_type, arg_description in description_args:
                        extracted_args[arg_name] = {
                            'type': arg_type.strip(),
                            'description': arg_description.strip()
                        }

                extracted_returns = {}
                if returns_section:
                    returns_content = returns_section.group(1)
                    description_returns = re.findall(r'\s*([a-zA-Z0-9_]+)\s*\((.*?)\):\s*(.*)', returns_content)
                    for ret_name, ret_type, ret_description in description_returns:
                        extracted_returns[ret_name] = {
                            'type': ret_type.strip(),
                            'description': ret_description.strip()
                        }

                functions_dict[func_name] = {
                    'description': description,
                    'args': args_list,
                    'extracted_args': extracted_args,
                    'return': extracted_returns
                }

    return functions_dict


def generate_md_files(functions_info, output_folder):
    # Verificar e criar subpastas se não existirem
    os.makedirs(output_folder, exist_ok=True)
    
    nav_counter = 1
    for func_name, func_info in functions_info.items():
        md_filename = f'{output_folder}/{func_name}.md'
        with open(md_filename, 'w') as md_file:
            md_file.write('---\n')
            md_file.write('layout: default\n')
            md_file.write(f'title: {func_name}\n')
            md_file.write('grand_parent: Framework\n')
            md_file.write('parent: Common Library functions\n')
            md_file.write(f'nav_order: {nav_counter}\n')
            md_file.write('has_toc: false\n')
            md_file.write('---\n\n')

            md_file.write(f'<h3>{func_name}</h3>\n\n')

            md_file.write(f'<br>\n\n')

            md_file.write(f'<p align = "justify">\n')
            md_file.write(f'    {func_info["description"]}\n')
            md_file.write(f'</p>\n\n')

            md_file.write('```python\n')
            md_file.write(f'{func_name}(')
            md_file.write(', '.join(func_info['args']))
            md_file.write(')\n')
            md_file.write('```\n\n')

            md_file.write('Input variables\n')
            md_file.write('{: .label .label-yellow }\n\n')

            md_file.write('<table style = "width:100%">\n')
            md_file.write('    <thead>\n')
            md_file.write('      <tr>\n')
            md_file.write('        <th>Name</th>\n')
            md_file.write('        <th>Description</th>\n')
            md_file.write('        <th>Type</th>\n')
            md_file.write('      </tr>\n')
            md_file.write('    </thead>\n')
            if func_info['args']:
                if func_info['extracted_args']:
                    for arg_name, arg_info in func_info['extracted_args'].items():
                        md_file.write('    <tr>\n')
                        md_file.write(f'        <td><code>{arg_name}</code></td>\n')
                        md_file.write(f'        <td>{arg_info["description"]}</td>\n')
                        if arg_info["type"] == 'dict':
                            md_file.write(f'        <td>dictionary</td>\n')
                        elif arg_info["type"] == 'str':
                            md_file.write(f'        <td>string</td>\n')
                        elif arg_info["type"] == 'int':
                            md_file.write(f'        <td>integer</td>\n')
                        elif arg_info["type"] == 'bool':
                            md_file.write(f'        <td>boolean</td>\n')
                        else:
                            md_file.write(f'        <td>{arg_info["type"]}</td>\n')
                        md_file.write('    </tr>\n')
                else:
                    for arg_name in func_info['args']:
                        md_file.write('    <tr>\n')
                        md_file.write(f'        <td><code>{arg_name}</code></td>\n')
                        md_file.write(f'        <td>Description not available.</td>\n')
                        md_file.write(f'        <td>None</td>\n')
                        md_file.write('    </tr>\n')
            else:
                md_file.write('    <tr>\n')
                md_file.write(f'        <td><code>None</code></td>\n')
                md_file.write(f'        <td>This function does not receive any input.</td>\n')
                md_file.write(f'        <td>None</td>\n')
                md_file.write('    </tr>\n')

            md_file.write('</table>\n\n')

            md_file.write('Output variables\n')
            md_file.write('{: .label .label-yellow }\n\n')

            md_file.write('<table style = "width:100%">\n')
            md_file.write('    <thead>\n')
            md_file.write('      <tr>\n')
            md_file.write('        <th>Name</th>\n')
            md_file.write('        <th>Description</th>\n')
            md_file.write('        <th>Type</th>\n')
            md_file.write('      </tr>\n')
            md_file.write('    </thead>\n')

            if func_info['return']:
                for ret_name, ret_info in func_info['return'].items():
                    md_file.write('    <tr>\n')
                    md_file.write(f'        <td><code>{ret_name}</code></td>\n')
                    md_file.write(f'        <td>{ret_info["description"]}</td>\n')
                    if ret_info["type"] == 'dict':
                        md_file.write(f'        <td>dictionary</td>\n')
                    elif ret_info["type"] == 'str':
                        md_file.write(f'        <td>string</td>\n')
                    elif ret_info["type"] == 'int':
                        md_file.write(f'        <td>integer</td>\n')
                    elif ret_info["type"] == 'bool':
                        md_file.write(f'        <td>boolean</td>\n')
                    else:
                        md_file.write(f'        <td>{ret_info["type"]}</td>\n')
                    md_file.write('    </tr>\n')
            else:
                md_file.write('    <tr>\n')
                md_file.write(f'        <td><code>None</code></td>\n')
                md_file.write(f'        <td>The function displays the plot on the screen and saves it to the local folder of the <code>.ipynb</td>\n')
                md_file.write(f'        <td>None</td>\n')
                md_file.write('    </tr>\n')

            md_file.write('</table>\n\n')

            md_file.write(f'Example 1\n')
            md_file.write('{: .label .label-blue }\n\n')

            md_file.write(f'<p align = "justify">\n')
            md_file.write(f'    <i>\n')
            md_file.write(f'        Use the <code>{func_name}</code> function to perform a task.\n')
            md_file.write(f'    </i>\n')
            md_file.write(f'</p>\n\n')

            md_file.write('```python\n')
            md_file.write('# Example code goes here\n')
            md_file.write('```\n\n')

            md_file.write('```bash\n')
            md_file.write('# Example output goes here\n')
            md_file.write('```\n\n')
        nav_counter += 1


if __name__ == '__main__':
    directory = "metapy_toolbox/"
    file_paths = read_file_path(directory)
    for file_path in file_paths:
        print(f'Arquivo Python encontrado: {file_path}')
        functions_info = read_python_file(file_path)
        output_folder = f'docs/{os.path.basename(file_path).replace(".py", "")}'
        generate_md_files(functions_info, output_folder)
        print(f'Arquivo Markdown gerado com sucesso: {output_folder}')
