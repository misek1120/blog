from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Record, User
from .form import RecordForm, UserUpdateForm, UserCreateForm, LoginForm
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import Http404
#from django.contrib.auth.models import User

# Create your views here.
class Login(LoginView):
    template_name = 'record/login.html'
    form_class = LoginForm

class Create_account(CreateView):
    success_url = reverse_lazy("index")
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'record/create_account.html', {'form':form})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'record/create_account.html', {'form':form})

class DetailAccount(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = User
    template_name = 'record/account_detail.html'
    success_url = reverse_lazy('account_info')

    def get_object(self):
        object = get_object_or_404(User, username=self.kwargs.get("username"))
        if self.request.user.username == object.username:
            return object
        else:
            print("you are not the owner!!")

class UpdateAccount(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = User
    template_name = "record/account_update_form.html"
    form_class = UserUpdateForm

    #def form_valid(self, form):
    #def post(self, request, *args, **kwargs):
    #    print(UserUpdateForm(data=request.POST))


    """def post(self, request, *args, **kwargs):
        form = UserUpdateForm(data=request.POST)
        print(form)
        if form.is_valid():
            print('aaa')
            form.save()
            username = form.cleaned_data.get('username')
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            #user = authenticate(username=username, password=password)
            #login(request, user)
            return redirect('account_info', {'username': username})
        return render(request, 'record/account_update_form.html', {'form':form})
    """

    def get_object(self):
        object = get_object_or_404(User, username=self.kwargs.get("username"))
        if self.request.user.username == object.username:
            print(object.username)
            return object
        else:
            print("you are not the owner!!")

    def get_success_url(self):
        #return reverse_lazy("account_info", kwargs={"username":self.kwargs["username"]})
        print(self.kwargs)
        return reverse_lazy("account_info", kwargs={'username':self.kwargs['username']})

class RecordListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Record
    context_object_name = "records"
    paginate_by = 10
    def get_queryset(self):
        user_id = self.request.user.uuid
        search_word = [self.request.GET.get('search', None)]
        if search_word[0]:
            return Record.objects.filter(
                Q(user=user_id), Q(title__icontains=search_word[0]) |
                Q(author__icontains=search_word[0]) | Q(summary__icontains=search_word[0]) |
                Q(impressions__icontains=search_word[0]) | Q(learn__icontains=search_word[0]) |
                Q(story__icontains=search_word[0]) | Q(difference__icontains=search_word[0]) |
                Q(importance__icontains=search_word[0]) | Q(agree__icontains=search_word[0]) |
                Q(opposition__icontains=search_word[0]) | Q(unkown__icontains=search_word[0]) |
                Q(example__icontains=search_word[0]) | Q(inspiration__icontains=search_word[0]))
        return Record.objects.filter(user=user_id)

class RecordDetailView(LoginRequiredMixin, DetailView, UserPassesTestMixin):
    login_url = '/login/'
    model = Record
    #raise_exception = True
    #uccess_url = reverse_lazy('detail')
    #template_name = "record/record_detail.html"

    #def test_func(self):
    #    current_user = self.request.user
    #    print(current_user.username)
    #    print(self.kwargs['username'])
    #    return current_user.uuid == get_object_or_404(User, uuid=self.kwargs.get(self.kwargs['username']))

    def get_object(self):
        request_uuid = self.request.user.uuid
        use_object = User.objects.get(username=self.kwargs.get("username"))
        if use_object.uuid != request_uuid:
            print("{0} accessed to {1} records.".format(request_uuid, use_object.uuid))
            raise Http404
            #return render(self.request, '/')
        else:
            return get_object_or_404(Record, pk=self.kwargs.get("pk"))


class RecordCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = RecordForm
    model = Record
    template_name = "record/record_create_form.html"
    success_url = reverse_lazy("index")

    def get_initial(self):
        return {'user': self.request.user.uuid}


class RecordUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = RecordForm
    model = Record
    template_name = "record/record_update_form.html"
    #fields = ["title", "author", "content",]
    def get_success_url(self):
        return reverse_lazy("detail", kwargs={"pk":self.kwargs["pk"]})

class RecordDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Record
    success_url = reverse_lazy("index")
