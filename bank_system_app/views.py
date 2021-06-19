from django.shortcuts import render, redirect
from .models import*
from django.contrib import messages

# Create your views here.



def index(request):
    return render(request, 'index.html')


def members(request):
    all_transfer_history = transfer_history.objects.all()

    members = customer.objects.all().order_by('id')
    if request.method == "POST":
        sender_email = request.POST.get('send_email')
        amt =  request.POST.get('amt')
        amt = int(amt)
        receiver_email = request.POST.get('rec_email')


        transfer_money = transfer_history(sender=sender_email, receiver=receiver_email, amount=amt)
        transfer_money.save() 
        
# receiver side
        for i in members:
            if i.email == receiver_email:
                j = i
                id = i.id
                break

# sender side
        for i in members:
            if i.email == sender_email and amt > 0 and amt <= i.balance :
                sender_available_balance = i.balance - amt
                print(sender_available_balance)
                receiver_available_balance = j.balance + amt

                senderdata = customer(id=i.id, name=i.name, email= i.email, balance=sender_available_balance)
                senderdata.save()


                receiverdata = customer(id=j.id, name=j.name, email= j.email, balance=receiver_available_balance)
                receiverdata.save()
                
                messages.info(request,'Money Transfered Successfully!')
                return redirect('/members')

        
    return render(request, 'members.html', {'members': members})



def transactions(request):
    all_transfer_history = transfer_history.objects.all()
    return render(request,'transactions.html',{'transfer_history':all_transfer_history})
