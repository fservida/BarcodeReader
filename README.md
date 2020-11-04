# BarcodeReader
Simple Python Barcode reader based on opencv and pyzbar.

- Continuosly scan for barcodes.
- Automatically copy detected barcodes to clipboard.
- Automatically open browser window on URL detection.

# Requirements
Python 3.6 environment
pinned numpy==1.19.3 on Windows 2004 due to a Compatibility bug on 1.19.4

# Install
```
git clone https://github.com/fservida/BarcodeReader
cd BarcodeReader
pip install -r requirements.txt
```

# Run
```
python main.py
```