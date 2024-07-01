file_path = '/mnt/data/php.ini'
with open(file_path, 'r') as file:
    php_ini_content = file.readlines()

# 修改 php.ini 文件内容
modified_php_ini_content = []
for line in php_ini_content:
    # 启用需要的函数
    if line.strip().startswith('disable_functions'):
        modified_php_ini_content.append('disable_functions =\n')
    else:
        modified_php_ini_content.append(line)
    
    # 启用 opcache 扩展
    if 'zend_extension' in line and 'opcache' in line:
        modified_php_ini_content.append('zend_extension=opcache.so\n')

# 添加 opcache 扩展配置
modified_php_ini_content.append('\n')
modified_php_ini_content.append('[opcache]\n')
modified_php_ini_content.append('opcache.enable=1\n')
modified_php_ini_content.append('opcache.enable_cli=1\n')
modified_php_ini_content.append('opcache.memory_consumption=128\n')
modified_php_ini_content.append('opcache.interned_strings_buffer=8\n')
modified_php_ini_content.append('opcache.max_accelerated_files=10000\n')
modified_php_ini_content.append('opcache.revalidate_freq=2\n')
modified_php_ini_content.append('opcache.fast_shutdown=1\n')

# 写回修改后的内容到 php.ini 文件
with open(file_path, 'w') as file:
    file.writelines(modified_php_ini_content)
