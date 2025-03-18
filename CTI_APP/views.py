
from django.shortcuts import render, get_object_or_404, redirect
from .models import CtiLog, BlackListIP, BlackListURL
from .forms import CtiLogForm, CtiLogSearchForm
from django.db.models import Q
from django.core.paginator import Paginator
import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Представление для списка записей с поиском и пагинацией
def cti_list(request):
    form = CtiLogSearchForm(request.GET or None)
    query = request.GET.get('search_query', '')

    if form.is_valid() and query:
        logs = CtiLog.objects.filter(
            Q(cve__icontains=query) | Q(signature__icontains=query)
        ).order_by('-id')
    else:
        logs = CtiLog.objects.all().order_by('-id')

    paginator = Paginator(logs, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'cti/cti_list.html', {
        'form': form,
        'page_obj': page_obj,
        'query': query,
    })


# Представление для поиска с пагинацией
def ctilog_search(request):
    form = CtiLogSearchForm(request.GET or None)
    logs = CtiLog.objects.all()  # Получаем все записи по умолчанию

    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')

        if search_query:
            # Убираем пробелы из строки поиска для более точного совпадения
            search_query = search_query.replace(' ', '').lower()

            # Фильтрация по полям cve и signature с учетом удаления пробелов
            logs = logs.filter(
                Q(cve__icontains=search_query) | Q(signature__icontains=search_query)
            )

    paginator = Paginator(logs, 15)  # Пагинация с 15 записями на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'cti/ctilog_search.html', {
        'form': form,
        'page_obj': page_obj,
        'search_query': search_query  # Передаем поисковый запрос в шаблон
    })


# Представление для детальной страницы записи
def cti_detail(request, log_id):
    log = get_object_or_404(CtiLog, id=log_id)
    return render(request, 'cti/cti_detail.html', {'log': log})


# Представление для создания новой записи
def cti_create(request):
    if request.method == "POST":
        form = CtiLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cti_list')
    else:
        form = CtiLogForm()
    return render(request, 'cti/cti_form.html', {'form': form})


def block_ip(request):
    # Логика для отображения списка IP
    ips = BlackListIP.objects.all()

    # Обработка формы поиска
    search_query = request.GET.get('search_query', '')  # Получаем запрос из формы поиска

    if search_query:
        # Убираем пробелы и делаем строку в нижнем регистре для точности поиска
        search_query = search_query.replace(' ', '').lower()

        # Фильтрация по полям ip_source и country_source
        ips = ips.filter(
            Q(ip_source__icontains=search_query) | Q(country_source__icontains=search_query)
        )

    # Пагинация с 15 записями на странице
    paginator = Paginator(ips, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'cti/block_ip.html', {
        'page_obj': page_obj,
        'search_query': search_query,  # Передаем запрос для сохранения в форме
    })


def url_ip(request):
    # Логика для отображения списка IP
    url = BlackListURL.objects.all()

    # Обработка формы поиска
    search_query = request.GET.get('search_query', '')  # Получаем запрос из формы поиска

    if search_query:
        # Убираем пробелы и делаем строку в нижнем регистре для точности поиска
        search_query = search_query.replace(' ', '').lower()

        # Фильтрация по полям ip_source и country_source
        url = url.filter(
            Q(url_source__icontains=search_query) | Q(attack_date__icontains=search_query)
        )

    # Пагинация с 15 записями на странице
    paginator = Paginator(url, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'cti/block_url.html', {
        'page_obj': page_obj,
        'search_query': search_query,  # Передаем запрос для сохранения в форме
    })


def export_cti_logs_to_csv(request):
    # Создаем HTTP-ответ с указанием кодировки UTF-8
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="cti_logs.csv"'
    
    # Устанавливаем кодировку для CSV
    response.write('\ufeff'.encode('utf-8'))  # Добавляем BOM для поддержки UTF-8 в Excel
    writer = csv.writer(response, delimiter=';', quoting=csv.QUOTE_ALL)

    # Заголовки столбцов
    writer.writerow(["Сигнатура"])

    # Получаем данные из модели
    logs = CtiLog.objects.all()
    for log in logs:
        writer.writerow([log.signature])

    return response



def export_block_ip_csv(request):
    # Создаем HTTP-ответ с указанием кодировки UTF-8
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="black_ip_list.csv"'
    
    # Устанавливаем кодировку для CSV
    response.write('\ufeff'.encode('utf-8'))  # Добавляем BOM для поддержки UTF-8 в Excel
    writer = csv.writer(response, delimiter=';', quoting=csv.QUOTE_ALL)

    # Заголовки столбцов
    writer.writerow(["IP"])

    # Получаем данные из модели
    logs = BlackListIP.objects.all()
    for log in logs:
        writer.writerow([log.ip_source])

    return response


def export_url_csv(request):
    # Создаем HTTP-ответ с указанием кодировки UTF-8
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="black_url_list.csv"'
    
    # Устанавливаем кодировку для CSV
    response.write('\ufeff'.encode('utf-8'))  # Добавляем BOM для поддержки UTF-8 в Excel
    writer = csv.writer(response, delimiter=';', quoting=csv.QUOTE_ALL)

    # Заголовки столбцов
    writer.writerow(["URL"])

    # Получаем данные из модели
    logs = BlackListURL.objects.all()
    for log in logs:
        writer.writerow([log.url_source])

    return response