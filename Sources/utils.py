from typing import Any
def generate_docs(obj: Any, isSaved:bool = True,
                  folder_path: str = '/Users/sinazabanfahm/FinAT/Sources/docs') -> str:
    opt = ""
    folder_path = folder_path + "/" if folder_path[-1]!="/" else folder_path
    file_path = folder_path + str(obj) +".txt"
    for attr_name in dir(obj):
        if not attr_name.startswith("__"):
            attr_value = getattr(obj, attr_name)
            try:
                if callable(attr_value):
                    opt+=(f"Documentatin for the callable {attr_name}:\n  {attr_value.__doc__}")
                else:
                    opt+=(f"{attr_name}:\n {attr_value}")
            except Exception as e:
                pass
    if isSaved:
        with open(file_path, 'w') as file:
            file.write(opt)
    return opt
# import yfinance as yf
# obj = yf.Ticker("AAPL")
# generate_docs(obj)