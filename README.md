# 🧾 Financial Audit Automation

This project is a simple yet powerful audit automation tool designed for financial data review. It detects common anomalies in general ledger entries using Python and Excel.

---

## 📂 Project Structure

```
financial-audit-automation/
├── data/           # Input files (e.g. sample_general_ledger.xlsx)
├── output/         # Auto-generated anomaly reports (excluded from GitHub)
├── notebooks/      # Jupyter notebooks for EDA and visuals
├── src/            # Python scripts (main logic in audit.py)
├── venv/           # Virtual environment (excluded)
├── README.md       # Project documentation
└── .gitignore      # Git ignore rules
```

---

## ⚙️ Features

- ✅ Detects **duplicate transactions**
- ✅ Flags **large round-number values**
- ✅ Identifies **unusually small entries**
- ✅ Extracts **manual journal entries**
- ✅ Exports flagged data to Excel for audit evidence

---

## 📊 Outputs

After running `src/audit.py`, the following files are created in the `output/` folder:

- `duplicates.xlsx`
- `large_rounds.xlsx`
- `small_values.xlsx`
- `manual_entries.xlsx`

These files are automatically generated and help streamline audit fieldwork and review.

---

## 📒 Jupyter Notebook

Check out the notebook under `notebooks/eda.ipynb` for:

- Summary statistics
- Visual distribution of amounts
- Entry type breakdown
- Visual investigation of anomalies

---

## 🛠️ Setup Instructions

```bash
# Set up the virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the script
python src/audit.py
```

---

## 📌 Python Version
Project uses **Python 3.11.9** (managed with `pyenv`)

---

## 📬 Author

**Souvik Ray**  
BSc in Computer Science & Economics | Former Audit Associate | Aspiring Data Analyst  
🌐 [souvikray.com](https://souvikray.com)
