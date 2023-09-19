def add_to_cart(request, pk):
    # Get that Partiuclar Product of id = pk
    product = Product.objects.get(pk=pk)

    # Create Order item
    order_item, created = OrderItem.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False,
    )

    # Get Query set of Order Object of Particular User
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(product__pk=pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Added Quantity Item")
            return redirect("product_desc", pk=pk)
        else:
            order.items.add(order_item)
            messages.info(request, "Item added to Cart")
            return redirect("product_desc", pk=pk)

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item added to Cart")
        return redirect("index")

def add_item(request, pk):
    # Get that Partiuclar Product of id = pk
    product = Product.objects.get(pk=pk)

    # Create Order item
    order_item, created = OrderItem.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False,
    )

    # Get Query set of Order Object of Particular User
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(product__pk=pk).exists():
            if order_item.quantity < product.product_available_count:
                order_item.quantity += 1
                order_item.save()
                messages.info(request, "Added Quantity Item")
                return redirect("orderlist")
            else:
                messages.info(request, "Sorry! Product is out of Stock")
                return redirect("orderlist")
        else:
            order.items.add(order_item)
            messages.info(request, "Item added to Cart")
            return redirect("product_desc", pk=pk)

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item added to Cart")
        return redirect("product_desc", pk=pk)   

def remove_item(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False,
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(product__pk=pk).exists():
            order_item = OrderItem.objects.filter(
                product=item,
                user=request.user,
                ordered=False,
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.info(request, "Item quantity was updated")
            return redirect("orderlist")
        else:
            messages.info(request, "This item is not in your cart")
            return redirect("orderlist")
    else:
        messages.info(request, "You Do not have any Order")
        return redirect("orderlist")   

class Remove_Item(View):
    def get(self,request,pk):
        item = get_object_or_404(Product, pk=pk)
        order_qs = Order.objects.filter(user=request.user,ordered=False,)
        if order_qs.exists():
            order = order_qs[0]
            if order.items.filter(product__pk=pk).exists():
                order_item = OrderItem.objects.filter(product=item,user=request.user,ordered=False,)[0]
                if order_item.quantity > 1:
                    order_item.quantity -= 1
                    order_item.save()
                else:
                    order_item.delete()
                    messages.info(request, "Item quantity was updated")
                    return redirect("orderlist")
            else:
                messages.info(request, "This item is not in your cart")
                return redirect("orderlist")
        else:
            messages.info(request, "You Do not have any Order")
            return redirect("orderlist")

def product_desc(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "core/product_desc2.html", {"product": product})

def index(request):
    products = Product.objects.all()
    return render(request,'core/indexx.html',{'products':products}) 

def orderlist(request):
    if Order.objects.filter(user=request.user, ordered=False).exists():
        order = Order.objects.get(user=request.user, ordered=False)
        return render(request, "core/orderlist(2).html", {"order": order})
    return render(request, "core/orderlist(2).html", {"message": "Your Cart is Empty"})

def checkout_page(request):
    if CheckoutAddress.objects.filter(user=request.user).exists():
        return render(request, "core/checkout_address.html", {"payment_allow": "allow"})
    if request.method == "POST":
        print("Saving must start")
        form = CheckoutForm(request.POST)
        if form.is_valid():
            street_address = form.cleaned_data.get("street_address")
            apartment_address = form.cleaned_data.get("apartment_address")
            country = form.cleaned_data.get("country")
            zip_code = form.cleaned_data.get("zip")

            checkout_address = CheckoutAddress(
                user=request.user,
                street_address=street_address,
                apartment_address=apartment_address,
                country=country,
                zip_code=zip_code,
            )
            checkout_address.save()
            print("It should render the summary page")
            return render(
                request, "core/checkout_address.html", {"payment_allow": "allow"}
            )

    else:
        form = CheckoutForm()
        return render(request, "core/checkout_address.html", {"form": form})
        
        

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            print("True")
            form.save()
            print("Data Saved Successfully")
            messages.success(request, "Product Added Successfully")
            return redirect("/")
        else:
            print("Not Working")
            messages.info("Product is not Added, Try Again")
    else:
        form = ProductForm()
    return render(request, "core/add_product.html", {"form": form})