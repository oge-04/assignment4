from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm


# Create your views here.

def homepage(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print("Form submitted")  # Debug print
        if form.is_valid():
            print("Form is valid")  # Debug print
            content = "" 
            if 'file' in request.FILES:
                file = request.FILES['file']
                content = file.read().decode()
                print("File received")  # Debug print
                print("Content received")  # Debug print
            if not content and request.POST.get('manual_input'):
                content = request.POST.get('manual_input', '')
                print("Manual input received")  # Debug print
                print("Content received")  # Debug print
            if not content:
                print("No content")
                return render(request, 'Statistics/homepage.html',{'form':form, 'error':'No Content'})
            
            numbers_list = []
            current_num = ""

            for char in content:
                if char == ",":
                    if current_num:
                        numbers_list += [int(current_num)]
                    current_num = ""
                else:
                    current_num += char
        
            if current_num:
                numbers_list += [int(current_num)]
            
            
            print(f"Numbers list: {numbers_list}")  # Debug print
            request.session['numbers_list'] = numbers_list
            return redirect('results')
        else:
         print(f"Form errors: {form.errors}")  # Debug print
         return render(request, 'Statistics/homepage.html',{'form':form, 'error':'Form Invalid'})
            
    form = UploadFileForm()
    return render(request,'Statistics/homepage.html',{'form':form})


    
def results(request):
    numbers_list = request.session.get('numbers_list', [])
    length = len(numbers_list)

    if length == 0:
        return HttpResponse("No numbers found in file")
    
    #unique count
    unique = []
    for num in numbers_list:
        if num not in unique:
            unique += [num]
    unique_count = len(unique)
    print(unique_count)

    
    #sum
    list_sum = 0
    for num in numbers_list:
        list_sum += num
    print(list_sum)

    #mean
    mean = list_sum/length
    print(mean)

    #median
    sorted_list = numbers_list
    index=0
    while index < len(sorted_list):
        number = index + 1
        while number < len(sorted_list):
            if sorted_list[index] > sorted_list[number]:
                sorted_list[index], sorted_list[number] = sorted_list[number], sorted_list[index]
            number += 1
        index += 1
                
    print (sorted_list)

    median_index = (length-1)//2
    if (length % 2):
        median =  sorted_list[median_index]
    else:
        median = (sorted_list[median_index]+sorted_list[median_index+1])/2
    
    print(median)
        
    #mode
    mode_count = {}
    for num in numbers_list:
        if num in mode_count:
            mode_count[num] += 1
        else:
            mode_count[num] = 1
    max_count = 0
    for key in mode_count:
        if mode_count[key] > max_count:
            max_count = mode_count[key]
    mode = []
    for key in mode_count:
        if mode_count[key] == max_count:
            mode += [key]
    print (mode)
    

    #range
    list_range = sorted_list[len(sorted_list)-1] - sorted_list[0]
    print(list_range)


    #prime numbers
    prime_numbers = []
    for num in sorted_list:
        if num >1:
            i=2
            while i < num:
                if num %i ==0:
                    break
                i += 1
            else:
                prime_numbers += [num]
            

    #armstrong numbers - Numbers equal to the sum of their digits raised to the power of the number of digits.


    return render(request, 'Statistics/results.html', {
        'sum':list_sum,
        'mean':mean,
        'median':median,
        'mode':mode,
        'range':list_range,
        'unique_count':unique_count,
        'prime':prime_numbers

    })


 
