from django.shortcuts import render


def index(request):
    data = {
        'title': 'Все вакансии',
    }
    return render(request, 'job/index.html', context=data)


def show_job(request, job_id):
    data = {
        'title': 'Одна вакансия',
    }
    return render(request, 'job/job.html', context=data)


def apply(request):
    data = {
        'title': 'Заявка',
    }
    return render(request, 'job/job.html', context=data)
