import json
ss_data = json.loads(open('gui-config.json').read())

back_base_content = open('backup_base_content.txt').read()

password = ""
for item in back_base_content.split('\n'):
    key, *val = item.split("=")
    if key == 'ss_basic_password':
        password = '='.join(val)

setting_conent = ''

for index, ss_item in enumerate(ss_data['configs']):
    setting_conent += 'ssconf_basic_method_{0}={1}\n'.format(index + 1, ss_item['method'])
    setting_conent += 'ssconf_basic_mode_{0}={1}\n'.format(index + 1, 1)
    setting_conent += 'ssconf_basic_name_{0}={1}\n'.format(index + 1, ss_item['remarks'])
    setting_conent += 'ssconf_basic_password_{0}={1}\n'.format(index + 1, password)
    setting_conent += 'ssconf_basic_port_{0}={1}\n'.format(index + 1, ss_item['server_port'])
    setting_conent += 'ssconf_basic_rss_obfs_{0}={1}\n'.format(index + 1, ss_item['obfs'])
    setting_conent += 'ssconf_basic_rss_protocol_{0}={1}\n'.format(index + 1, ss_item['protocol'])
    setting_conent += 'ssconf_basic_server_{0}={1}\n'.format(index + 1, ss_item['server'])
    setting_conent += 'ssconf_basic_use_kcp_{0}={1}\n'.format(index + 1, 0)
    setting_conent += 'ssconf_basic_use_rss_{0}={1}\n'.format(index + 1, 1)
    setting_conent += 'ssconf_basic_rss_obfs_param_{0}={1}\n'.format(index + 1, ss_item['obfsparam'])


backup_file = open('ss_conf_backup.txt', 'w')
backup_file.write(back_base_content + setting_conent)
backup_file.close()
