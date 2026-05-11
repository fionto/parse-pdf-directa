from src.portfolio_parser.config import PROJECT_ROOT, PDF_PATH, CACHE_PATH, FIGI_SLEEP_SEC, FIGI_BATCH_SIZE
print(f"Root: {PROJECT_ROOT}")
print(f"PDF Dir: {PDF_PATH}")
print(f"Cache: {CACHE_PATH}")
print(f"Sleep time: {FIGI_SLEEP_SEC}")
print(f"Batch Size: {FIGI_BATCH_SIZE}")
assert FIGI_BATCH_SIZE > 0, "Batch size must be positive"
print("Config validation passed.")