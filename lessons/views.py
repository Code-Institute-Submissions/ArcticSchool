""" Views Lessons App """
import random
from django.db.models.aggregates import Count
from django.db.models import Q
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.db.models.functions import Lower
from resorts.models import Resort
from home.models import SocialIcon, LevelCard
from .models import Category, Lesson
from .forms import CategoriesForm, LessonsForm


def lessons(request):
    """ A view to return lessons in selected category """

    lessons = Lesson.objects.all()
    all_lessons = Lesson.objects.all()
    social = SocialIcon.objects.all()
    categories = Category.objects.all()
    levels = LevelCard.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                lessons = lessons.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            lessons = lessons.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            lessons = lessons.filter(category__name__in=categories)
            categories = Category.objects.all()

        if 'q' in request.GET:
            query = request.GET['q']
            if query != "":
                queries = Q(name__icontains=query) | Q(
                    description__icontains=query) | Q(
                    category__name__icontains=query) | Q(
                    level__title__icontains=query)
                lessons = lessons.filter(queries)
            else:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(request.path)

    current_sorting = f'{sort}_{direction}'

    # Get number of lessons in each category
    categories_list = Category.objects.annotate(Count('lesson'))

    context = {
        'socials': social,
        'lessons': lessons,
        'categories': categories,
        'categories_list': categories_list,
        'levels': levels,
        'all_lessons': all_lessons,
        'current_sorting': current_sorting,
        'query_text': query,
    }

    return render(request, 'lessons/lessons.html', context)


def lesson(request, lesson_id):
    """ A view to return lesson detail with resort detail """

    all_lessons = list(Lesson.objects.all())
    resorts = Resort.objects.all()
    social = SocialIcon.objects.all()
    selected_lesson = get_object_or_404(Lesson, pk=lesson_id)
    resort = resorts.get(name=selected_lesson.resort)

    if Lesson.objects.count() < 4:
        context = {
            'socials': social,
            'lesson': selected_lesson,
            'resort': resort,
            'random_lessons' : Lesson.objects.count()
        }
    else:
        random_lessons = random.sample(all_lessons, 4)
        context = {
            'socials': social,
            'lesson': selected_lesson,
            'resort': resort,
            'lessons': random_lessons,
        }

    return render(request, 'lessons/lesson.html', context)


# Categories Management
@staff_member_required
def categories_management(request):
    """ A view to manage lessons categoires """

    categories = Category.objects.all()
    social = SocialIcon.objects.all()

    template = "lessons/mgmt-categories.html"
    context = {
        'categories': categories,
        'socials': social,
    }

    return render(request, template, context)


@staff_member_required
def add_categories_management(request):
    """ Management view to add lesson category """

    if request.method == 'POST':
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect(reverse('categories_management'))
        else:
            messages.error(
                request, 'Adding new category failed. Please ensure the form is valid.')
    else:
        form = CategoriesForm()

    template = "./management/management-forms.html"
    context = {
        'form': form,
    }

    return render(request, template, context)


@staff_member_required
def edit_categories_management(request, category_id):
    """ Management view to edit lessons category """

    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoriesForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Category edited successfully!')
            return redirect(reverse('categories_management'))
        else:
            messages.error(
                request, 'Editing category failed. \
                Please ensure the form is valid.')
    else:
        form = CategoriesForm(instance=category)

    template = "./management/management-forms.html"
    context = {
        'form': form,
        'category': category,
    }

    return render(request, template, context)


@staff_member_required
def remove_categories_management(request, category_id):
    """ Management view to remove lessons category """

    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    messages.success(request, 'Category removed successfully!')

    return redirect(reverse('categories_management'))


# Lessons Management
@staff_member_required
def lessons_management(request):
    """ A view to manage lessons """

    all_lessons = Lesson.objects.all()
    social = SocialIcon.objects.all()

    template = "lessons/mgmt-lessons.html"
    context = {
        'all_lessons': all_lessons,
        'socials': social,
    }

    return render(request, template, context)


@staff_member_required
def add_lessons_management(request):
    """ Management view to add lessons """

    if request.method == 'POST':
        form = LessonsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lesson added successfully!')
            return redirect(reverse('lessons_management'))
        else:
            messages.error(
                request, 'Adding new lesson failed. Please ensure the form is valid.')
    else:
        form = LessonsForm()

    template = "./management/management-forms.html"
    context = {
        'form': form,
    }

    return render(request, template, context)


@staff_member_required
def edit_lessons_management(request, lesson_id):
    """ Management view to edit lessons """

    edit_lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        form = LessonsForm(request.POST, request.FILES, instance=edit_lesson)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Lesson edited successfully!')
            return redirect(reverse('lessons_management'))
        else:
            messages.error(
                request, 'Editing Lesson failed. \
                Please ensure the form is valid.')
    else:
        form = LessonsForm(instance=lesson)

    template = "./management/management-forms.html"
    context = {
        'form': form,
        'lesson': lesson,
    }

    return render(request, template, context)


@staff_member_required
def remove_lessons_management(request, lesson_id):
    """ Management view to remove lessons """

    removed_lesson = get_object_or_404(Lesson, pk=lesson_id)
    if removed_lesson.image:
        removed_lesson.image.delete()
        removed_lesson.delete()
    else:
        removed_lesson.delete()
    messages.success(request, 'Lesson removed successfully!')

    return redirect(reverse('lessons_management'))
