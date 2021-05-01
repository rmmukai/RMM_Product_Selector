from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, 'registration_login.html')


def register(request):
    # See models.py's registration validator for error logic.
    errors = User.objects.registration_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    new_user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    )
    request.session['user'] = new_user.first_name
    request.session['id'] = new_user.id
    return redirect('products')


def login(request):
    # See models.py's login validator for error logic
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    # User will use email to login
    logged_user = User.objects.filter(email=request.POST['login_email'])
    post_password = request.POST['login_password']
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if bcrypt.checkpw(post_password.encode(), logged_user.password.encode()):
            request.session['user'] = logged_user.first_name
            request.session['id'] = logged_user.id
            return redirect('/products')

    return HttpResponse("Not working")


def all_product(request):
    context = {
        'prepreg': Prepreg.objects.all(),
        'carbon_fiber': CarbonFiber.objects.all()
    }
    return render(request, 'all_products.html', context)


def add_prepreg(request):
    return render(request, 'add_prepreg.html')


def create_prepreg(request):
    errors = Prepreg.objects.prepreg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/products/add_prepreg')
    else:
        new_prepreg = Prepreg.objects.create(
            prepreg_name=request.POST['prepreg_name'],
            tg=request.POST['tg'],
            cure_temp=request.POST['cure_temp'],
            prepreg_processing=request.POST['prepreg_processing'],
            omit=request.POST['omit'],
            resin_type=request.POST['resin_type']
        )
        return redirect('/products')


def add_carbon_fiber(request):
    return render(request, 'add_carbon_fiber.html')


def create_carbon_fiber(request):
    errors = CarbonFiber.objects.carbon_fiber_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/products/add_carbon_fiber')
    else:
        new_carbon_fiber = CarbonFiber.objects.create(
            carbon_fiber_name=request.POST['carbon_fiber_name'],
            tensile_modulus=request.POST['tensile_modulus'],
            tensile_strength=request.POST['tensile_strength'],
            resin_matrix=request.POST['resin_matrix'],
            carbon_fiber_processing=request.POST['carbon_fiber_processing']
        )
        return redirect('/products')


def edit_prepreg(request, prepreg_id):
    db_prepreg = Prepreg.objects.get(id=prepreg_id)

    context = {
        'prepreg': db_prepreg,
    }
    return render(request, 'edit_prepreg.html', context)


def update_prepreg(request, prepreg_id):
    db_prepreg = Prepreg.objects.get(id=prepreg_id)
    # This validator is the same one used for the creation of the prepreg. Find under add_prepreg on line 64
    errors = Prepreg.objects.prepreg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/products/{db_prepreg.id}/edit_prepreg')
    else:
        # data from the post into variable
        post_prepreg_name = request.POST.get('prepreg_name')
        post_tg = request.POST.get('tg')
        post_prepreg_processing = request.POST.get('prepreg_processing')
        post_omit = request.POST.get('omit')
        post_resin_type = request.POST.get('resin_type')

        # Update the fields in the database object.
        db_prepreg.prepreg_name = post_prepreg_name
        db_prepreg.tg = post_tg
        db_prepreg.prepreg_processing = post_prepreg_processing
        db_prepreg.omit = post_omit
        db_prepreg.resin_type = post_resin_type

        db_prepreg.save()

        return redirect('/products')


def edit_carbon_fiber(request, carbon_fiber_id):
    db_carbon_fiber = CarbonFiber.objects.get(id=carbon_fiber_id)

    context = {
        'carbon_fiber': db_carbon_fiber
    }
    return render(request, 'edit_carbon_fiber.html', context)


def update_carbon_fiber(request, carbon_fiber_id):
        db_carbon_fiber = CarbonFiber.objects.get(id=carbon_fiber_id)
        # This validator is the same one used for the creation of the carbon fiber. Find under add_carbon_fiber on line 86
        errors = CarbonFiber.objects.carbon_fiber_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/products/{db_carbon_fiber.id}/edit_carbon_fiber')
        else:
            # data from the post into variable
            post_carbon_fiber_name = request.POST.get('carbon_fiber_name')
            post_tensile_modulus = request.POST.get('tensile_modulus')
            post_tensile_strength = request.POST.get('tensile_strength')
            post_resin_matrix = request.POST.get('resin_matrix')
            post_carbon_fiber_processing = request.POST.get('carbon_fiber_processing')

            # Update the fields in the database object.
            db_carbon_fiber.carbon_fiber = post_carbon_fiber_name
            db_carbon_fiber.tensile_modulus = post_tensile_modulus
            db_carbon_fiber.tensile_strength = post_tensile_strength
            db_carbon_fiber.resin_matrix = post_resin_matrix
            db_carbon_fiber.carbon_fiber_processing = post_carbon_fiber_processing

            db_carbon_fiber.save()

            return redirect('/products')


def delete_prepreg(request, prepreg_id):
    prepreg = Prepreg.objects.get(id=prepreg_id)
    prepreg.delete()

    return redirect('/products')

def delete_carbon_fiber(request, carbon_fiber_id):
    carbon_fiber = CarbonFiber.objects.get(id=carbon_fiber_id)
    carbon_fiber.delete()

    return redirect('/products')


def product_selector_old(request):
    # ---------------------------------------
    # This is one way to ot it
    # .values_list() changing the "plan" of the objects. Can give it the field names that you want to give it.
    # This is so I don't call all the data just the data I want. Can query quicker.
    # tensile_modulus is the value we use in the database
    # flat=True means that the tuple list is converted into a string which is easier to use.
    # .distinct() takes a query set and removes duplicate entries.
    # modulus_options = CarbonFiber.objects.all().values_list("tensile_modulus", flat=True).distinct()
    # # print(modulus_options)
    # for tuple in modulus_options:
    #     print(tuple)
    # ---------------------------------------

    all_pp = Prepreg.objects.all()
    all_cf = CarbonFiber.objects.all()

    # set() is a type of unordered list that only grabs seperate keywords. Or grabs words that aren't the same in the list you are. Everything in a set in unique.
    # set() cannot be reordered you have to turn it into a list.
    # Phase1: creating sets
    tensile_modulus_options = set()
    tensile_strength_options = set()
    resin_matrix_options = set()

    # Phase 2: looping through all_cf
    for carbon_fiber in all_cf:
        tensile_modulus_options.add(carbon_fiber.tensile_modulus)
        tensile_strength_options.add(carbon_fiber.tensile_strength)
        resin_matrix_options.add(carbon_fiber.resin_matrix)

    # Phase 3: sorting the data
    # Converting the set() into a list
    tensile_modulus_options=list(tensile_modulus_options)
    # Sorts the list. If its a string it will be alphabetical. Numbers will be in numeric order
    tensile_modulus_options.sort()

    tensile_strength_options=list(tensile_strength_options)
    tensile_strength_options.sort()

    resin_matrix_options=list(resin_matrix_options)
    resin_matrix_options.sort()

    context = {
        'carbon_fiber': all_cf,
        'tensile_modulus_options': tensile_modulus_options,
        'tensile_strength_options': tensile_strength_options,
        'resin_matrix_options': resin_matrix_options,
        'prepreg': all_pp,
    }
    return render(request, 'product_selector.html', context)


def product_selector(request):
    all_pp = Prepreg.objects.all()
    all_cf = CarbonFiber.objects.all()

    context = {
        'carbon_fiber': all_cf,
        'prepreg': all_pp,
            }

    cf_filter_fields = ['tensile_modulus', 'tensile_strength', 'resin_matrix', 'carbon_fiber_processing']

    # Phase1: creating sets
    cf_filter_field_to_unique_set = {}
    for field_name in cf_filter_fields:
        cf_filter_field_to_unique_set[field_name] = set()

    # Phase 2: looping through all_cf
    for carbon_fiber in all_cf:
        for field_name in cf_filter_fields:
            field_value = getattr(carbon_fiber, field_name)
            field_set = cf_filter_field_to_unique_set[field_name]
            field_set.add(field_value)

    # Phase 3: sorting the data
    cf_filter_field_to_ordered_values = {}
    for field_name in cf_filter_fields:
        field_set = cf_filter_field_to_unique_set[field_name]
        values_list = list(field_set)
        values_list.sort()
        cf_filter_field_to_ordered_values[field_name] = values_list

    # Phase 4: add the options to the context
    for field_name in cf_filter_fields:
        context_key = field_name + '_options'
        context[context_key] = cf_filter_field_to_ordered_values[field_name]

# This line seperates filtering for above CF and below prepreg------------------------------------------------

    pp_filter_fields = ['tg', 'cure_temp', 'prepreg_processing', 'omit', 'resin_type']

    pp_filter_field_to_unique_set = {}
    for field_name in pp_filter_fields:
        pp_filter_field_to_unique_set[field_name] = set()

    for prepreg in all_pp:
        for field_name in pp_filter_fields:
            field_value = getattr(prepreg, field_name)
            field_set = pp_filter_field_to_unique_set[field_name]
            field_set.add(field_value)

    pp_filter_field_to_ordered_values = {}
    for field_name in pp_filter_fields:
        field_set = pp_filter_field_to_unique_set[field_name]
        values_list = list(field_set)
        values_list.sort()
        pp_filter_field_to_ordered_values[field_name] = values_list

    for field_name in pp_filter_fields:
        context_key = field_name + '_options'
        context[context_key] = pp_filter_field_to_ordered_values[field_name]

    return render(request, 'product_selector.html', context)