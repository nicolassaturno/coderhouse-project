from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict

from app_coder.models import Seed, Insurance, Pipes
from app_coder.forms import CourseForm, ProfesorForm, HomeworkForm


def index(request):
    return render(request, "app_coder/home.html")


def seeds(request):
    seeds = Seed.objects.all()

    context_dict = {
        'seeds': seeds
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/profesors.html"
    )


def courses(request):
    courses = Course.objects.all()

    context_dict = {
        'courses': courses
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/courses.html"
    )


def insurance(request):
    insurance = Insurance.objects.all()

    context_dict = {
        'insurance': insurance
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/insurance.html"
    )





def form_hmtl(request):

    if request.method == 'POST':
        course = Course(name=request.POST['name'], code=request.POST['code'])
        course.save()

        courses = Course.objects.all()
        context_dict = {
            'courses': courses
        }

        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/courses.html"
        )

    return render(
        request=request,
        template_name='app_coder/formHTML.html'
    )


def pipes_forms_django(request):
    if request.method == 'POST':
        pipes_form = pipes_form(request.POST)
        if pipes_form.is_valid():
            data = pipes_form.cleaned_data
            pipes = Pipes(
            name=data['name'],
            price=data['price']),
            Pipes.save()

            pipes = Pipes.objects.all()
            context_dict = {
                'pipes': pipes
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/courses.html"
            )

    course_form = CourseForm(request.POST)
    context_dict = {
        'course_form': course_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/course_django_forms.html'
    )


def seeds_form_django(request):
    if request.method == 'POST':
        seeds_form = seeds_form(request.POST)
        if seeds_form.is_valid():
            data = seeds_form.cleaned_data
            seed = Seed(
                name=data['name'],
                code=data['code'],
                specimen=data['specimen'],
                taste=data['taste'],
                price=data['price'],
            )
            seed.save()

            seeds = Seed.objects.all()
            context_dict = {
                'seeds': seeds
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/seeds.html"
            )

    seeds_form = seeds_form(request.POST)
    context_dict = {
        'seeds_form': seeds_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/seeds_django_form.html'
    )

def update_seeds(request, pk: int):
    seed = Seed.objects.get(pk=pk)

    if request.method == 'POST':
        seeds_form = seeds_form(request.POST)
        if seeds_form.is_valid():
            data = seeds_form.cleaned_data
            seed.name = data['name']
            seed.code = data['code']
            seed.specimen = data['specimen']
            seed.taste = data['taste']
            seed.price = data['price']
            seed.save()

            seeds = Seed.objects.all()
            context_dict = {
                'seeds': seeds
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/seeds.html"
            )

    seeds_form = seeds_form(model_to_dict(seeds))
    context_dict = {
        'seed': seeds,
        'seeds_form': seeds_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/seeds_form.html'
    )


def delete_seeds(request, pk: int):
    seed = Seed.objects.get(pk=pk)
    if request.method == 'POST':
        seed.delete()

        seeds = Seed.objects.all()
        context_dict = {
            'seeds': seeds
        }
        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/seeds.html"
        )

    context_dict = {
        'seeds': seeds,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/profesor_confirm_delete.html'
    )



         

def search(request):
    context_dict = dict()
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        courses = Course.objects.filter(name__contains=search_param)
        context_dict = {
            'courses': courses
        }
    elif request.GET['code_search']:
        search_param = request.GET['code_search']
        courses = Course.objects.filter(code__contains=search_param)
        context_dict = {
            'courses': courses
        }
    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        courses = Course.objects.filter(query)
        context_dict = {
            'courses': courses
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/home.html",
    )

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CourseListView(ListView):
    model = Course
    template_name = "app_coder/course_list.html"


class CourseDetailView(DetailView):
    model = Course
    template_name = "app_coder/course_detail.html"


class CourseCreateView(CreateView):
    model = Course
    # template_name = "app_coder/course_form.html"
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('app_coder:course-list')
    fields = ['name', 'code']


class CourseUpdateView(UpdateView):
    model = Course
    # template_name = "app_coder/course_form.html"
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('app_coder:course-list')
    fields = ['name', 'code']


class CourseDeleteView(DeleteView):
    model = Course
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('app_coder:course-list')
