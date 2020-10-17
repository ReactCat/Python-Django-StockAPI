from django.shortcuts import render, redirect
from .models import Stock 
from .forms import StockForm
from django.contrib import messages

def home(request):
    import requests
    import json

    if request.method == "POST":
        stockticker = request.POST['stockticker']
       api_request = requests.get("STOCK_ADD1" 
            + str(ticker_item) + "STOCK_ADD2") 
        try:
            stockapi = json.loads(api_request.content)
        except Exception as e:
            stockapi = "Error..."
        
        return render(request, 'marketdata/home.html', {'stockapi': stockapi})

    else:
        return render(request, 'marketdata/home.html', 
        {'stockticker': "Enter Stock Ticker..."})


def addstock(request):
    import requests
    import json
    if request.method == "POST":
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "Stock has been added to database")
            return redirect('addstock')

        
    else:
        stockticker = Stock.objects.all()

        output = []
        for ticker_item in stockticker:
            api_request = requests.get("STOCK_ADD1" 
            + str(ticker_item) + "STOCK_ADD2") 
           
            try:
                stockapi = json.loads(api_request.content)
                output.append(stockapi)
            except Exception as e:
                stockapi = "Error..."

        return render(request, 'marketdata/addstock.html', 
        {'stockticker': stockticker, 'output': output})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock was deleted"))
    return redirect(deletestock)

   
def deletestock(request):
    stockticker = Stock.objects.all()
    return render(request, 'marketdata/deletestock.html',
    {'stockticker': stockticker})


    







