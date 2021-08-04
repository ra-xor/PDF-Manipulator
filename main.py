//
from pathlib import Path

reports_dir = Path("F:/")

for path in reports_dir.glob("*.pdf"): print(path.name)

expense_reports = list(reports_dir.glob("*.pdf"))
for path in expense_reports: print(path.name)

from PyPDF2 import PdfFileMerger
pdf_merger = PdfFileMerger()
for path in reports_dir: pdf_merger.append(str(path))

with Path("F:/test.pdf").open(mode="wb") as output_file: pdf_merger.write(output_file)
