#특정 키워드 제외하기

import re

adapted_code = []
for i in tot:
    if "google.colab" not in cell:  
        cell = re.sub(r'/content/drive/MyDrive/', './', cell)
        adapted_code.append(cell)

adapted_code_joined = '\n\n'.join(adapted_code)

script_path = '/mnt/data/converted_script.py'

with open(script_path, 'w', encoding='utf-8') as script_file:
    script_file.write(adapted_code_joined)

script_path