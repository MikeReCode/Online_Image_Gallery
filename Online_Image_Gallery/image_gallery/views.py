from django.shortcuts import render
from django.views import View
from image_gallery.models import Image
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView
from image_gallery.forms import ImageForm
from django.shortcuts import redirect, get_object_or_404


class Gallery(LoginRequiredMixin, View):
    def get(self, request):
        images = Image.objects.filter(owner=self.request.user).order_by('date').reverse()
        ctx = {'images': images}
        return render(request, 'image_gallery/gallery.html', ctx)


def django_image_name(filename):
    # Returns image name in the same format Django Store the image
    # Necessary to check if the image is already stored in the database

    return '{0}'.format("_".join(filename.split()))


class AddImages(LoginRequiredMixin, CreateView):
    model = Image
    form_class = ImageForm
    template_name = "image_gallery/form.html"

    def post(self, request, *args, **kwargs):

        # Get a list of all the files you want to upload
        images = request.FILES.getlist('image')
        owner = self.request.user

        # Get all images objects
        al = Image.objects.filter(owner=owner)

        # Create a list with all images names in the database owned by the user
        image_name_list = [i.image.name.split("/")[-1] for i in al]
        print("SAVED IMAGES LIST***", image_name_list, len(image_name_list))

        # Check the images one by one if exist in the database , and if it don't exist add the image to database
        for image in images:
            image_name = django_image_name(image.name)

            # print("CHECK IF IMAGE IS IN DATABASE: ", image_name)
            if image_name not in image_name_list:
                Image.objects.create(image=image, owner=owner)
                print("IMAGE ADDED TO DATABASE:", image_name)

            else:
                print("ALREADY IN THE DATABASE:", image_name)

        return redirect('image_gallery:all')


class DeleteImage(LoginRequiredMixin, DeleteView):
    model = Image
    template_name = "image_gallery/delete.html"

    def get_queryset(self):
        print('delete get_queryset called')
        qs = super(DeleteImage, self).get_queryset()
        return qs.filter(owner=self.request.user)


class DetailImage(LoginRequiredMixin, DetailView):
    model = Image
    template_name = 'image_gallery/detail.html'

    def get(self, request, pk):
        # x = Second.objects.get(id=pk, owner=self.request.user)
        x = get_object_or_404(Image, id=pk, owner=self.request.user)
        context = {'foto': x, }
        return render(request, self.template_name, context)
