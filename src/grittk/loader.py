try:
    from yaml import safe_load as load
except ImportError:
    from json import load
    
