from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

from listings.choices import price_choices , bedroom_choices , county_choices, type_choices

from .models import Listing

# Create your views here
def index(request):
	listings = Listing.objects.all().order_by('-list_date').filter(is_published=True)
	paginator = Paginator(listings, 6)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page)
	return render(request,'listings/listings.html',{'listings' : paged_listings})


def listing(request , listing_id):
	listing = get_object_or_404(Listing , pk=listing_id)
	context = {
	  'listing' : listing
	}
	return render(request,'listings/listing.html',context)


def search(request):
	queryset_list = Listing.objects.order_by('-list_date')
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			queryset_list = queryset_list.filter(description__icontains=keywords)

	if 'town' in request.GET:
		town = request.GET['town']
		if town:
			queryset_list = queryset_list.filter(town__iexact=town)

	if 'county' in request.GET:
		county = request.GET['county']
		if county:
			queryset_list = queryset_list.filter(county__iexact=county)

	if 'bedrooms' in request.GET:
		bedrooms = request.GET['bedrooms']
		if bedrooms:
			queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

	if 'price' in request.GET:
		price = request.GET['price']
		if price:
			queryset_list = queryset_list.filter(price__lte=price)


	return render(request,'listings/search.html',{
		'listings' : queryset_list,
        'county_choices' : county_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices,
        'type_choices' : type_choices,
        'values': request.GET,
		})