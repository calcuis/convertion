import os, win32com.client

def convert_word_to_pdf(doc_path, pdf_path):
    word = win32com.client.Dispatch("Word.Application")
    doc = word.Documents.Open(doc_path)
    doc.SaveAs(pdf_path, FileFormat=17)  # 17 is the format ID for PDFs
    doc.Close()
    word.Quit()
    print(f"Converted {doc_path} to {pdf_path}")

def convert_excel_to_pdf(excel_path, pdf_path):
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False
    workbook = excel.Workbooks.Open(excel_path)
    workbook.ExportAsFixedFormat(0, pdf_path)  # 0 is the format ID for PDFs
    workbook.Close(False)
    excel.Quit()
    print(f"Converted {excel_path} to {pdf_path}")

def convert_ppt_to_pdf(ppt_path, pdf_path):
    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    powerpoint.Visible = True
    presentation = powerpoint.Presentations.Open(ppt_path, WithWindow=False)
    presentation.SaveAs(pdf_path, 32)  # 32 is the format ID for PDFs
    presentation.Close()
    powerpoint.Quit()
    print(f"Converted {ppt_path} to {pdf_path}")

def convert_all_to_pdf(file_type):
    current_directory = os.getcwd()

    for file_name in os.listdir(current_directory):
        file_path = os.path.join(current_directory, file_name)
        pdf_path = os.path.splitext(file_path)[0] + '.pdf'
        
        if file_type=="2":
            if file_name.endswith(".doc") or file_name.endswith(".docx"):
                convert_word_to_pdf(file_path, pdf_path)
        elif file_type=="3":
            if file_name.endswith(".xls") or file_name.endswith(".xlsx"):
                convert_excel_to_pdf(file_path, pdf_path)
        elif file_type=="4":
            if file_name.endswith(".ppt") or file_name.endswith(".pptx"):
                convert_ppt_to_pdf(file_path, pdf_path)

if __name__ == "__main__":
    print("Please select a conversion:\n1. ALL to pdf\n2. word to pdf\n3. excel to pdf\n4. powerpoint to pdf")
    choice = input("Enter your choice (1 to 4): ")

    if choice=="1":
        convert_all_to_pdf("2")
        convert_all_to_pdf("3")
        convert_all_to_pdf("4")
    elif choice=="2":
        convert_all_to_pdf(choice)
    elif choice=="3":
        convert_all_to_pdf(choice)
    elif choice=="4":
        convert_all_to_pdf(choice)
    else:
        print("Not a valid number.")
