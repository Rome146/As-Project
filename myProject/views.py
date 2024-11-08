from django.shortcuts import render,redirect,get_object_or_404

from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def signupPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Confirm_password=request.POST.get("Confirm_password")
        user_type=request.POST.get("user_type")
        Profile_Pic=request.FILES.get("Profile_Pic")
    
        
        if password==Confirm_password:
            
            
            user=customUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type=user_type,
                Profile_Pic=Profile_Pic,
            )
            if user_type=='seeker':
                seekerProfileModel.objects.create(user=user)
                
            elif user_type=='recruiter':
                recruiterProfileModel.objects.create(user=user)
            
            return redirect("signInPage")
            
    return render(request,"signupPage.html")


def signInPage(request):
    if request.method == 'POST':
        
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")

        try:
            user = authenticate(request, username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('signInPage')

        except customUser.DoesNotExist:
            return redirect('signInPage')

    return render(request, 'signInPage.html')


def homePage(request):
    
    
    return render(request,"base.html")


def logoutPage(request):
    
    logout(request)
    
    return redirect('signInPage')

@login_required
def profilePage(request):
    
    return render(request,"profilePage.html")



def JobFeed(req):
    job = JobModel.objects.all()
    return render(req,'JobFeed.html',{'job':job})


def createdJob(req):
    current_user = req.user
    job = JobModel.objects.filter(user=current_user)
    return render(req,'createdJob.html',{'job':job})

def DeleteJob(req,id):
    job = JobModel.objects.filter(id=id).delete()
    return redirect("createdJob")

def AddJob(req):
    if req.user.user_type=='recruiter':
        if req.method == 'POST':
            current_user = req.user
            JobModel.objects.create(
                Title = req.POST.get('Title'),
                vecancy = req.POST.get('vecancy'),
                Description = req.POST.get('Description'),
                category = req.POST.get('category'),
                Skill = req.POST.get('Skill'),
                Image = req.FILES.get('Image'),
                user = current_user,
            )
            
            return redirect('JobFeed')
    return render(req,'AddJob.html')
def EditJob(req,id):
    job = JobModel.objects.get(id=id)
    if req.method == 'POST':
        current_user = req.user
        job.Title = req.POST.get('Title')
        job.vecancy = req.POST.get('vecancy')
        job.Description = req.POST.get('Description')
        job.category = req.POST.get('category')
        job.Skill = req.POST.get('Skill')
        job.Image = req.FILES.get('Image')
        job.user = current_user
        job.id = id
        job.save()
        return redirect('createdJob')
    return render(req,'EditJob.html',{'job':job})

def ApplyJob(req,id):
    job_data = get_object_or_404(JobModel, id=id)
    if req.method == 'POST':
        jobs = ApplyJobModel(
            user = req.user,
            Job = job_data,
            cover = req.POST.get('cover'),
            Skill = req.POST.get('Skill'),
            resume = req.FILES.get('resume'),
            Apply_pic = req.FILES.get('Apply_pic'),
        )
        jobs.save()
        return redirect('JobFeed')
    return render(req,'ApplyJob.html',{'job':job_data})


def searchPage(req):
    query = req.GET.get('query')
    job = JobModel.objects.filter(Q(Title__icontains=query)|
                                  Q(Skill__icontains=query)|
                                  Q(category__icontains=query))
    
    
    return render(req,'search.html',{'job':job, 'query':query})


def SkillMatchingPage(req):
    current_user = req.user
    MySkill = current_user.seekerProfile.Skill
    job = JobModel.objects.filter(Skill=MySkill)
    return render(req,'SkillMatchingPage.html',{'job':job})


def edit_profile(request):
    user = request.user
    context = {'user': user}

    
    if user.user_type == 'seeker':
        profile = seekerProfileModel.objects.get(user=user)
        context.update({
            'profile': profile,
            'skills': [skill[0] for skill in seekerProfileModel.Skills],
        })

        if request.method == "POST":
            user.contact_no = request.POST.get("contact_no", user.contact_no)
            user.Profile_Pic = request.FILES.get("Profile_Pic", user.Profile_Pic)
            profile.Skill = request.POST.get("Skill", profile.Skill)
            user.save()
            profile.save()
            return redirect("profilePage")
    
    elif user.user_type == 'recruiter':
        profile = recruiterProfileModel.objects.get(user=user)
        context.update({'profile': profile})

        if request.method == "POST":
            user.contact_no = request.POST.get("contact_no", user.contact_no)
            user.Profile_Pic = request.FILES.get("Profile_Pic", user.Profile_Pic)
            profile.company_name = request.POST.get("company_name", profile.company_name)
            user.save()
            profile.save()
            return redirect("profilePage") 

    return render(request, "edit_profile.html", context)
