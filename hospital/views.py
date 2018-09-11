from django.shortcuts import get_object_or_404 ,render,redirect
from .models import doctor
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View 
from .forms import UserForm

def index(request):
     
    return render(request,'hospital/home.html')
	

class doctorcreate(CreateView):
      model = doctor
      fields =['name','sex','dob','phone_no','qualifications','address','speciality','user']		

class doctorupdate(UpdateView):
      model = doctor
      fields =['name','sex','dob','phone_no','qualifications','address','speciality']	

class doctordelete(DeleteView):
      model = doctor
      success_url=reverse_lazy('hospital:index')	
      
class UserFormView(View):
      form_class = UserForm
      template_name = 'hospital/registrations_form.html'		
      # display blank form
      def get(self, request):
       form = self.form_class(None)
       return render(request,self.template_name,{'form':form})
      
      #process form data
      def post(self,request):
       form=self.form_class(request.POST)
          
       if form.is_valid():
	 
       	 user = form.save(commit=False)	
	  
         #cleaned(normalised)data
         username=form.cleaned_data['username']
         password=form.cleaned_data['password']
         user.set_password(password)
         user.save()	
         #return user objects if credentials
         user = authenticate(username='username',password='password')
       
         if user is not None:
	   
            if user.is_active:
                login(request,user)
	        #return redirect('hospital:index')  
      
       return render(request,self.template_name,{'form':form})					      	
