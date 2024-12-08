from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm


# Create your views here.

def homepage(request):

    return render(request, 'homepage.html')


    
def results(request):
    if request.method == 'POST':
        with open("sample.txt") as file:
            content = file.read()
        
        numbers_list = []
        current_num = ""



        for char in content:
            if char == ",":
                numbers_list += [int(current_num)]
                current_num = ""
            else:
                current_num += char
        
        if current_num:
            numbers_list += [int(current_num)]

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
        sum = 0
        for num in numbers_list:
            sum += num
        print(sum)

        #mean
        mean = sum/length
        print(mean)

        #median
        sorted_list = numbers_list
        for index in range(len(sorted_list)):
            for number in range(index + 1, len(sorted_list)):
                if sorted_list[index] > sorted_list[number]:
                    sorted_list[index], sorted_list[number] = sorted_list[number], sorted_list[index]
        
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
        range = sorted_list[len(sorted_list)-1] - sorted_list[0]
        print(range)


        #prime numbers

 



        #armstrong numbers - Numbers equal to the sum of their digits raised to the power of the number of digits.

    
        return render(request, 'results.html', {
            'sum':sum,
            'mean':mean,
            'median':median,
            'mode':mode,
            'range':range,
            'unique_count':unique_count

        })
    return HttpResponse("Invalid request method.")

 
