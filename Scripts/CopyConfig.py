import json

def copy_data(source_path:str, destination_path:str):
    assert source_path.endswith('.json') and destination_path.endswith('.json')

    with open(source_path, 'r', encoding='utf-8') as f:
        old_config = json.loads(f.read().strip())
    with open(destination_path, 'r', encoding='utf-8') as f:
        new_config = json.loads(f.read().strip())

    for K in new_config.keys():
        if K in old_config.keys():
            new_config[K] = old_config[K]

    with open(destination_path, 'w') as f:
        f.write(json.dumps(new_config))


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print('\nUsage:\npython CopyConfig.py "<path to source>" "<path to target>"')
        raise SystemExit
    elif len(sys.argv) > 3:
        print('\nUse " " to encapsulate your paths')
        raise SystemExit

    copy_data(sys.argv[1], sys.argv[2])
