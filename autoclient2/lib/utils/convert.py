def convert_mb_to_gb(value,default=0):

    try:
        value = value.strip('MB')
        result = int(value)
    except Exception as e:
        result = default

    return result