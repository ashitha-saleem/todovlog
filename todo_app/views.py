from django.shortcuts import  redirect

from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
# from django.http import HttpResponse

# Create your views here.
class TaskListView(ListView):
    model=Task
    template_name='tasks.html'
    context_object_name='obj'
class TaskDetailView(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='i'
class TaskUpdateView(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name='obj2'
    fields=('name','priority','date')
    # success_url=reverse_lazy('cbvtask')
    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model=Task
    template_name='delete.html'
    success_url=reverse_lazy('cbvtask')

def task(request):

    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        obj=Task(name=name,priority=priority,date=date)
        obj.save()
    return redirect('cbvtask')


# def task(request):
#     # return HttpResponse('hello world')
#     obj1 = Task.objects.all()
#
#     if request.method=='POST':
#         name=request.POST.get('name')
#         priority=request.POST.get('priority')
#         date=request.POST.get('date')
#         obj=Task(name=name,priority=priority,date=date)
#         obj.save()
#     # obj1 = Task.objects.all()
#     return render(request,'tasks.html',{'obj':obj1})
# # def task_vw(request):
# #     return render(request,'task_view.html')
# def delete(request,taskid):
#     if request.method=='POST':
#         obj=Task.objects.get(id=taskid)
#         obj.delete()
#         return redirect('/')
#     else:
#         return render(request,'delete.html')
# def update(request,id):
#     obj=Task.objects.get(id=id)
#     form=Todoforms(request.POST or None,instance=obj)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request,'edit.html',{'obj1':obj,'form':form})
