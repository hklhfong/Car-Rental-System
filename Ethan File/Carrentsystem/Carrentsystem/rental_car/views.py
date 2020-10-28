from django.shortcuts import render, redirect
from .models import Car

def index(request):
    car = Car.objects.all().order_by('-car_id')  # 依據id欄位遞減排序顯示所有資料
    return render(request, 'contents/index.html', locals())

def post1(request):
    if request.method == "POST":#如果是以POST的方式才處理
        brand_name = request.POST['brand_name']
        type = request.POST['type']
        transmission = request.POST['transmission']
        price = request.POST['price']
        luggage_size = request.POST['luggage_size']
        seat_number = request.POST['seat_number']
        release_year = request.POST['release_year']


        car = Car.objects.create(brand_name=brand_name, type=type, transmission=transmission,
                                 price=price, luggage_size=luggage_size, seat_number=seat_number,
                                 release_year=release_year)
        car.save()                      #寫入資料庫
        return redirect('/index/')       #重導到<index.html>網頁
    else:
        message = 'Enter information(Not verified)'
    return render(request, "contents/post1.html", locals())

def delete(request,car_id=None):                  #刪除資料
    if car_id!=None:
        if request.method == "POST":  #如果是以POST的分是才處理
            car = request.POST('cId')  #取得表單輸入的編號
        try:
            car = Car.objects.get(car_id=car_id)  #取得id欄位的資料
            car.delete()                      #刪除資料
            return redirect('/index/')
        except:
            message = "Error!"
    return render(request,"contents/delete.html",locals())


def edit(request,car_id=None,mode=None):
    if mode == "edit": #如果是由<edit.html>按submit
        car = Car.objects.get(car_id=car_id)  #取得要修改的資料紀錄
        car.brand_name = request.GET['brand_name']    #取得表單輸入資料
        car.type = request.GET['type']
        car.transmission = request.GET['transmission']
        car.price = request.GET['price']
        car.luggage_size = request.GET['luggage_size']
        car.seat_number = request.GET['seat_number']
        car.release_year = request.GET['release_year']
        car.save()
        message = "Fixed"
        return redirect('/index/')
    else: #由網址列直接輸入
        try:
            car = Car.objects.get(car_id=car_id)  #取得要修改的資料紀錄
            strdate = str(car.car_id)
            strdate2 = strdate.replace("Y","-")
            strdate2 = strdate.replace("M","-")
            strdate2 = strdate.replace("D","-")
            car.car_id = strdate2
        except:
            message = "This id does not exist!"
    return render(request,"contents/edit.html",locals())
