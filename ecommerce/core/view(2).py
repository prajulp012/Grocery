class Checkout_Page(View):
    def get(self,request):
        if CheckoutAddress.objects.filter(user=request.user).exists():
            return render(request, "core/checkout_address.html", {"payment_allow": "allow"})
    def post(self,request):
        print("Saving must start")
        form = CheckoutForm(request.POST)
        if form.is_valid():
            street_address = form.cleaned_data.get("street_address")
            apartment_address = form.cleaned_data.get("apartment_address")
            country = form.cleaned_data.get("country")
            zip_code = form.cleaned_data.get("zip")

            checkout_address = CheckoutAddress(user=request.user,street_address=street_address,apartment_address=apartment_address,
                country=country,
                zip_code=zip_code,
            )
            checkout_address.save()
            print("It should render the summary page")
            return render(request, "core/checkout_address.html", {"payment_allow": "allow"})
        else:
            form = CheckoutForm()
            return render(request, "core/checkout_address.html", {"form": form}) 
    
def invoice(request):
    return render(request, "invoice/invoice.html")


