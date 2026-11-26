packages = ['deep_translator', 'googletrans', 'transformers', 'translate', 'requests', 'urllib.request']

for pkg in packages:
    try:
        __import__(pkg)
        print(f"Package '{pkg}': AVAILABLE")
    except ImportError:
        print(f"Package '{pkg}': NOT available")
