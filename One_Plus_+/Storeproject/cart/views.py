
from django.shortcuts import render,redirect
from mainapp.models import Product
from .models import Cart
from django.core.exceptions import ObjectDoesNotExist

def cart_page(req):
    cart = Cart.objects.filter(user=req.session['user'])  # Retrieve cart items\
    # Calculate grand total
    grand_total = sum(item.quantity * item.product.price for item in cart)
    #calulate price 
    # price=item.quantity * item.product.price
    return render(req, 'cart.html', {'cart': cart ,'grand_total': grand_total})



#add items to the cart and add quantity of the product
def addcart(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    print(product)
    print(user)
    try:
        cart=Cart.objects.get(product=product,user=user)
        if cart.quantity<cart.product.stock:
            cart.quantity+=1
            cart.save()
    except Cart.DoesNotExist:
        cart=Cart.objects.create(user=user,product=product,quantity=1)

    return redirect('Cart:cart_page')



#remove the quantity of the product in cart using cart button (-) .
def quantity_remove(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    cart=Cart.objects.get(product=product,user=user)
    if cart.quantity>1:
        cart.quantity-=1
        cart.save()
    
    return redirect('Cart:cart_page')

# remove single product from the cart
def RemoveX(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    cart=Cart.objects.get(product=product,user=user)
    cart.delete()
    return redirect('Cart:cart_page')

def Checkout(req):
    user = req.session['user']
    cart_items = Cart.objects.filter( user=user )
    for i in cart_items:
        products=Product.objects.get(id=i.product.id)
        #stock update after purchasing substrating the quantity
        products.stock-=i.quantity
        products.save()
        #delete the whole products in the cart
        i.delete()
    return redirect('mainapp:Home')

def ClearCart(req):
    user = req.session['user']
    cart_items = Cart.objects.filter( user=user)
    for i in cart_items:
        i.delete()
    return redirect('mainapp:Home')


