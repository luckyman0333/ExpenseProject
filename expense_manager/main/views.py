from django.shortcuts import render
import openpyxl
from django.shortcuts import render, redirect
from .forms import UploadFileForm

import openpyxl
import xlrd
from django.http import HttpResponse
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            
            # Перевіряємо розширення файлу
            if file.name.endswith('.xlsx'):
                try:
                    # Використовуємо openpyxl для .xlsx файлів
                    wb = openpyxl.load_workbook(file)
                    sheet = wb.active

                    print("Завантажені дані з .xlsx файлу:")
                    for row in sheet.iter_rows(min_row=2, values_only=True):
                        print(row)
                    
                    return HttpResponse("Файл успішно завантажено і дані виведено у термінал.")

                except Exception as e:
                    return HttpResponse(f"Помилка під час обробки .xlsx файлу: {str(e)}")

            elif file.name.endswith('.xls'):
                try:
                    # Використовуємо xlrd для .xls файлів
                    wb = xlrd.open_workbook(file_contents=file.read())
                    sheet = wb.sheet_by_index(0)

                    print("Завантажені дані з .xls файлу:")
                    for row_idx in range(1, sheet.nrows):  # Пропускаємо заголовок
                        row = sheet.row_values(row_idx)
                        print(row)

                    return HttpResponse("Файл успішно завантажено і дані виведено у термінал.")

                except Exception as e:
                    return HttpResponse(f"Помилка під час обробки .xls файлу: {str(e)}")
            
            else:
                return HttpResponse("Невірний формат файлу. Завантажте файл у форматі .xls або .xlsx.")
    
    return HttpResponse("Будь ласка, завантажте Excel файл через POST запит.")


def success(request):
    return render(request, 'success.html')
