from django.shortcuts import render, get_object_or_404 , redirect
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Report
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse,HttpResponse
from Tag.models import Tag
from Group.models import Group,Channel
from user.models import Profile
from Post.models import Post
from .forms import ReportForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def create_report(request,id):
    if (request.method == 'POST'):
        form1 = ReportForm(request.POST)
        if (form1.is_valid()):
            post=Post.objects.get(pk=id)
            form1.instance.Raised_by = request.user
            form1.instance.Post=post
            form1.save()
            return redirect('blog-home')
    else:
        form1 = ReportForm
    context = {
        'form': form1,
        # 'user':request.user
    }
    return render(request, 'Report/report_form.html', context)

def report_list(request):
    profile=Profile.objects.get(user=request.user)

    if profile.moderator is True:
        context={}
        context['reports']=Report.objects.all()
        return render(request,'Report/detail_report.html',context)
    else:
        return HttpResponse('Your are not authorised')
