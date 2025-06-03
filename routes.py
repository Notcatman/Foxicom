from flask import render_template, Blueprint, redirect, url_for, session, flash, request
from flask_login import login_required, current_user

routes = Blueprint('routes', __name__)



@routes.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart = session.get('cart', [])
    # ai es aris fasebi da tu gindat secvalet tu me zalian iafad vkidi
    COURSE_COST = {
        'python': 70,
        'javascript': 50,
        'html': 25,
        'css': 25,
        'guitar': 100,
        'piano': 60,
        'bass': 100,
        'electromusic': 75,
        'sketching': 40,
        'stippling': 45,
        'artisticdrawing': 50,
        'technicaldrawing': 55
        
    }
    total = sum(COURSE_COST.get(item, 0) for item in cart)
    if not cart:
        flash("Your cart is empty!")
        return redirect(url_for('routes.home'))
    if request.method == 'POST':
        session['cart'] = []
        return render_template('payment_processing.html')
    
    return render_template('checkout.html', cart=cart, course_cost=COURSE_COST, total=total)

@routes.route('/music courses')
def music_courses():
    COURSE_COST = {
        'python': 70,
        'javascript': 50,
        'html': 25,
        'css': 25,
        'guitar': 100,
        'piano': 60,
        'bass': 100,
        'electromusic': 75,
        'sketching': 40,
        'stippling': 45,
        'artisticdrawing': 50,
        'technicaldrawing': 55
    }
    return render_template('music_courses.html', course_cost=COURSE_COST)

@routes.route('/')
def home():
    COURSE_COST = {
        'python': 70,
        'javascript': 50,
        'html': 25,
        'css': 25,
        'guitar': 100,
        'piano': 60,
        'bass': 100,
        'electromusic': 75,
        'sketching': 40,
        'stippling': 45,
        'artisticdrawing': 50,
        'technicaldrawing': 55
    }
    return render_template('index.html', course_cost=COURSE_COST)

@routes.route('/python')
def python_course():
    return render_template('python.html')

@routes.route('/javascript')
def javascript_course():
    return render_template('javascript.html')

@routes.route('/html')
def html_course():
    return render_template('html.html')

@routes.route('/css')
def css_course():
    return render_template('css.html')

@routes.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@routes.route('/drawing_courses')
def drawing_courses():
    COURSE_COST = {
        'python': 70,
        'javascript': 50,
        'html': 25,
        'css': 25,
        'guitar': 100,
        'piano': 60,
        'bass': 100,
        'electromusic': 75,
        'sketching': 40,
        'stippling': 45,
        'artisticdrawing': 50,
        'technicaldrawing': 55
    }
    return render_template('drawing_courses.html', course_cost=COURSE_COST)

@routes.route('/guitar')
def guitar_course():
    return render_template("guitar.html")

@routes.route('/piano')
def piano_course():
    return render_template("piano.html")

@routes.route('/bass')
def bass_course():
    return render_template("bass.html")

@routes.route('/elecronic')
def electromusic_course():
    return render_template("electromusic.html")

@routes.route('/technicaldrawing')
def technical_drawing():
    return render_template('technical_drawing.html')

@routes.route('/sketching')
def sketching():
    return render_template('sketching.html')

@routes.route('/stippling')
def stippling():
    return render_template('stippling.html')

@routes.route('/artisticdrawing')
def artistic_drawing():
    return render_template('artistic_drawing.html')

@routes.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@routes.app_errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

# es cartia da ak weria rom damatdes nivti cartsi

@routes.route('/add_to_cart/<course>', methods=['POST'])
def add_to_cart(course):
    cart = session.get('cart', [])
    course = course.lower()          
    if course not in cart:
        cart.append(course)
        session['cart'] = cart
        flash(f"{course.title()} course was added to cart!")
    return redirect(request.referrer or url_for('routes.home'))
# es pirikit aris rom cartidan wavsalot nivti
@routes.route('/remove_from_cart/<course>', methods=['POST'])
def remove_from_cart(course):
    cart = session.get('cart', [])
    course = course.lower()
    if course in cart:
        cart.remove(course)
        session['cart'] = cart
        flash(f"{course.title()} course was removed from cart!")
    return redirect(request.referrer or url_for('routes.home'))