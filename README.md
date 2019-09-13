## Airbnb in Denver: This is Why We Can't Have Nice Things
### Sarah Forward

Background
------
I have been an Airbnb host in Denver for the last year and half. It's been a great source of mostly passive income and about 95% of our guests are pretty easy going. When I first discovered the data, I was interested in finding out:
+ Does the listing description and length increase number of bookings? 
+ What's the ratio of Superhosts to total Airbnb listings in Denver? 
+ Similar to optimizing SEO on websites, do hosts pack in Denver's things-to-do every chance they get?
    * For example, I live in Sloan's Lake and two blocks from Mile High Stadium. That's included in both our listings, but I also let guests know we're a shared-ride away from RiNo, LoHi, Coors Field, 16th Street Mall, the Convention Center, etc. any where I can. 
+ There's a section called "Getting Around" on every listing where hosts can tell guests what kind transporation options are available around the area. What are hosts telling guests? More Uber mentions or Lyft? Are they proponents of the Light Rail? 
+ What's the Airbnb utilization per neighborhood and learning how to map that visually?

But what started out to be a project to see how I could maximize and make more from my Airbnb listings quickly turned into ---something, some kind of detective work---- after finding out where the data came from and digging into the actual data myself. 

Data Description
------
Murray Cox is an Austrailian-native-turned-New-York-transplant who runs [Inside Airbnb](http://insideairbnb.com/about.html) - "an independent, non-commercial set of tools and data that allows you to explore how Airbnb is really being used in cities around the world."

He's been scraping publicly available data on Airbnb from more than 100 cities around the world. You can get listings, calendar dates and availibility, and reviews for cities like Amsterdam, Barcelona, Cape Town, Hong Kong, and, of course, Denver. 

He considers himself a "housing activist" but the media has dubbed him “Airbnb’s global public enemy No. 1" after publishing his first report in 2016 describing in detail how Airbnb and it's hosts were violating New York state law. New York's dwelling law at the time stated that "an apartment with three or more units cannot be rented out for under 30 days unless there's a permanent occupant present." So, if one host is listing multiple apartments - they couldn't possibly be living in *all of them*.  

In December 2015, [Airbnb released a report](https://www.nytimes.com/2015/12/02/technology/airbnb-releases-trove-of-new-york-city-home-sharing-data.html?module=inline) around its presence in New York City in an effort to be more transparent. ---That backfired just two months later. How do I say this better?---

It turns out Cox would regularly update his numbers from as early as 2014. When comparing his data to that of Airbnb's he noticed that there were large chunks of listings missing just before Airbnb released their report. More specifically, it was missing listings that featured Airbnb hosts who were listing multiple apartments and in clear violation of New York's dwelling law. 

Cox and another collaborator, Tom Slee, compiled [a comprehensive report](http://insideairbnb.com/reports/how-airbnbs-data-hid-the-facts-in-new-york-city.pdf) calling out Airbnb for trying to sweep the known violations under the rug. Naturally, Airbnb tried to deny the claims saying that it was "a natural fluctuation — a comedown off of the frenzy of the New York City marathon and Halloween weekend." It was until two weeks later that Airbnb sent a letter to New York state legislators and users admitting that the report was true. 

(New) Capstone 1 Goals
------
+ Getting more comfortable using pandas and sifting through large data.
+ Transition from Jupyter Notebooks into using code editor, Visual Studio Code.
+ Cox stated in [this article from 2016](http://insideairbnb.com/nyc-the-war-against-commercial-listings-continues/) that "Airbnb's business model incentivizes commercial use, regardless of whether it is one host that permanently rents multiple homes, or many hosts that permanently rent one entire home." Is this still true and is it happening in Denver?
+ Finding hosts with multiple listings that could be in possible violation of Denver's short-term rental regulations & licensing.
+ Making my code easily transferrable to the other cities Inside Airbnb features.

Describing the Data
------
Learn more about Denver's Short-Term Rental Regulations & Licensing [here](https://www.denvergov.org/content/denvergov/en/denver-business-licensing-center/business-licenses/short-term-rentals/short-term-rental-faq.html).

The data for Denver and other cities can be found on [Inside Airbnb](http://insideairbnb.com/get-the-data.html). It seems to be updated every month or so. Data from previous months are archived and linked below the city's current shared data sets.

I reviewed the following .CSV fles:
+ Listings
+ Calendar
+ Reviews

Exploration highlighted:
+ **Listings**
    * There are 4,511 total Airbnb listings in Denver across 78 neighbourhoods.
        * 73% - Entire Home/Apt
        * 25% - Private rooms
        * 2%  - Shared rooms
    * There's a designated section where hosts are to enter their license number. This is when I realized I put our license number in the wrong spot and quickly fixed our listings.
    * A "neighbourhood_cleansed" column correctly converts the listing's neighbourhood to be representative of the city's neighbourhood boundaries.
        * **Host entered**: LoDo (Lower Downtown) -> **Becomes**: Union Station
        * **Host entered**: RiNo (River North)    -> **Becomes**: Five Points
    * Property types could be:
        * Guesthouse
        * Loft 
        * House
        * Apartment
        * Bed and breakfast
        * Guest suite
        * Cottage
        * Townhouse
        * Condominium
        * Bungalow
        * Serviced apartment
        * Tiny house
        * Castle
        * Other
        * Hostel
        * Villa
        * Camper/RV
        * Tent
        * Campsite
    * Room type options are:
        * Entire home/apt
        * Private room
        * Shared room

+ **Calendar**
    * Total rows = 1,646,515 
    * The data set featured bookings from June 29, 2019 through June 27, 2020. 
    * A categorical column with True/False values distinguished if the listing was reserved or not.
   
+ **Reviews**
    * Total rows = 221,847
    * Information included:
        * Listing ID
        * Date
        * Reviewer ID
        * Reviewer Name
        * Comments

Data Visualization + Discovery
------
I wanted to see what neighborhood in Denver had the most Airbnb listings to choose from. In Denver, that's Five Points. 
 
![alt text](images/top-10-neighborhoods-in-Denver-with-most-airbnb-listings.jpeg "Top 10 Denver Neighborhoods with the Most Airbnb Listings)

My next question was: "Of these neighborhoods, what are the room types that are listed?"

![alt text](images/most-available-airbnb-listings-in-{city}-by-room-type.jpeg "Most Available Neighbourhoods in Denver & Room Type)

Future Directions
------
Ow now brown cow.

References
------
Carville, Olivia. (2019, March) *Meet Murray Cox, The Man Trying to Take Down Airbnb.* https://www.bloomberg.com/news/articles/2019-05-23/meet-murray-cox-airbnb-s-public-enemy-no-1-in-new-york

Katz, Miranda. (2018, February). *A Lone Data Whiz Is Fighting Airbnb — and Winning.* https://www.wired.com/2017/02/a-lone-data-whiz-is-fighting-airbnb-and-winning/