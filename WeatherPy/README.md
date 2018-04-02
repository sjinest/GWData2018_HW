

```python
#Import Dependencies
import random
import json
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn 
from citipy import citipy 
```


```python
#Defining API variables
api_key = "0266a6d48b3d8982f57959da0c50bce7"
base_url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "APPID": api_key
}

#This is an example of the weather API which takes three params: api key, city name and country code
#api.openweathermap.org/data/2.5/weather?q=London,uk
```


```python
# We're getting random cities so we set min and max latitudes and longitudes
lat_min = -90
lat_max = 90
lon_min = -180
lon_max = 180

#We're going to loop through random cities by writing a for loop and creating variables to get the min/max
#latitudes and longitudes

city_list =[]
country_list = []
temp_list = []
humidity_list = []
cloudiness_list = []
wind_speed_list = []
latitude_list = []
longitude_list = []
date_list = []

x=0
while x < 500:
    rand_lat = random.uniform(lat_min, lat_max)
    rand_lon = random.uniform(lon_min, lon_max)
    city = citipy.nearest_city(rand_lat, rand_lon)
#     print(city.city_name)  
#     city.country_code
    params['q'] = city.city_name + ',' + city.country_code
#We're then print the random city and country code of that city
#     print(city.city_name, city.country_code)

#Next we're going to call the API request
    response_data = requests.get(base_url, params=params).json()
#     print(json.dumps(response_data, indent=4, sort_keys=True))
    if(response_data['cod'] == 200):
      
        city_list.append(city.city_name)
        print(city.city_name)
        
        country_list.append(city.country_code)
        print(city.country_code)
        
        temp = response_data["main"]["temp_max"]
        temp_list.append(temp)
        print(f"The temperature for {city.city_name} is: {temp}")  
        
        humidity = response_data["main"]["humidity"]
        humidity_list.append(humidity)
        print(f"The humidity for {city.city_name} is: {humidity}")  

        cloudiness = response_data["clouds"]["all"]
        cloudiness_list.append(cloudiness)
        print(f"The cloudiness for {city.city_name} is: {cloudiness}")  

        wind_speed = response_data["wind"]["speed"]
        wind_speed_list.append(wind_speed)
        print(f"The wind speed for {city.city_name} is: {wind_speed}") 
        
        latitude_list.append(rand_lat)
        print(f"The latitude for {city.city_name} is: {rand_lat}")
        
        longitude_list.append(rand_lon)
        
        date = response_data["dt"]
        date_list.append(date)
        x=x+1
        
```

    vanimo
    pg
    The temperature for vanimo is: 299.227
    The humidity for vanimo is: 100
    The cloudiness for vanimo is: 80
    The wind speed for vanimo is: 4.1
    The latitude for vanimo is: -2.337525881945794
    san cristobal
    ec
    The temperature for san cristobal is: 288.852
    The humidity for san cristobal is: 100
    The cloudiness for san cristobal is: 92
    The wind speed for san cristobal is: 1.05
    The latitude for san cristobal is: -12.735963002125473
    hailar
    cn
    The temperature for hailar is: 272.602
    The humidity for hailar is: 39
    The cloudiness for hailar is: 0
    The wind speed for hailar is: 8.9
    The latitude for hailar is: 47.51081833907716
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -63.23474155948145
    ribeira grande
    pt
    The temperature for ribeira grande is: 290.077
    The humidity for ribeira grande is: 98
    The cloudiness for ribeira grande is: 92
    The wind speed for ribeira grande is: 7.4
    The latitude for ribeira grande is: 40.23591310707573
    ribeira grande
    pt
    The temperature for ribeira grande is: 290.077
    The humidity for ribeira grande is: 98
    The cloudiness for ribeira grande is: 92
    The wind speed for ribeira grande is: 7.4
    The latitude for ribeira grande is: 47.14653006002749
    ugoofaaru
    mv
    The temperature for ugoofaaru is: 301.652
    The humidity for ugoofaaru is: 100
    The cloudiness for ugoofaaru is: 88
    The wind speed for ugoofaaru is: 2.55
    The latitude for ugoofaaru is: 5.4055487387095695
    nikolskoye
    ru
    The temperature for nikolskoye is: 273.15
    The humidity for nikolskoye is: 90
    The cloudiness for nikolskoye is: 90
    The wind speed for nikolskoye is: 7
    The latitude for nikolskoye is: 47.834034252822306
    kaitong
    cn
    The temperature for kaitong is: 284.352
    The humidity for kaitong is: 41
    The cloudiness for kaitong is: 92
    The wind speed for kaitong is: 6.7
    The latitude for kaitong is: 44.85876314250555
    otradnoye
    ru
    The temperature for otradnoye is: 273.15
    The humidity for otradnoye is: 90
    The cloudiness for otradnoye is: 90
    The wind speed for otradnoye is: 8
    The latitude for otradnoye is: 45.50798046661086
    atuona
    pf
    The temperature for atuona is: 300.827
    The humidity for atuona is: 100
    The cloudiness for atuona is: 32
    The wind speed for atuona is: 6.05
    The latitude for atuona is: 1.9986109458367594
    cape town
    za
    The temperature for cape town is: 292.15
    The humidity for cape town is: 77
    The cloudiness for cape town is: 0
    The wind speed for cape town is: 4.1
    The latitude for cape town is: -78.84414804180055
    constitucion
    mx
    The temperature for constitucion is: 295.15
    The humidity for constitucion is: 12
    The cloudiness for constitucion is: 40
    The wind speed for constitucion is: 7.7
    The latitude for constitucion is: 20.890230175189032
    kapaa
    us
    The temperature for kapaa is: 299.15
    The humidity for kapaa is: 83
    The cloudiness for kapaa is: 40
    The wind speed for kapaa is: 3.6
    The latitude for kapaa is: 29.773273595458747
    busselton
    au
    The temperature for busselton is: 294.027
    The humidity for busselton is: 95
    The cloudiness for busselton is: 0
    The wind speed for busselton is: 6.5
    The latitude for busselton is: -54.91940788370978
    busselton
    au
    The temperature for busselton is: 294.027
    The humidity for busselton is: 95
    The cloudiness for busselton is: 0
    The wind speed for busselton is: 6.5
    The latitude for busselton is: -89.60457269691074
    port moresby
    pg
    The temperature for port moresby is: 305.15
    The humidity for port moresby is: 62
    The cloudiness for port moresby is: 20
    The wind speed for port moresby is: 4.6
    The latitude for port moresby is: -10.85060912218647
    saldanha
    za
    The temperature for saldanha is: 290.15
    The humidity for saldanha is: 88
    The cloudiness for saldanha is: 88
    The wind speed for saldanha is: 3.1
    The latitude for saldanha is: -35.816847511391074
    husavik
    is
    The temperature for husavik is: 271.15
    The humidity for husavik is: 92
    The cloudiness for husavik is: 90
    The wind speed for husavik is: 2.6
    The latitude for husavik is: 66.48488531075213
    coahuayana
    mx
    The temperature for coahuayana is: 294.727
    The humidity for coahuayana is: 57
    The cloudiness for coahuayana is: 12
    The wind speed for coahuayana is: 0.9
    The latitude for coahuayana is: 5.811276787538489
    port alfred
    za
    The temperature for port alfred is: 295.327
    The humidity for port alfred is: 89
    The cloudiness for port alfred is: 44
    The wind speed for port alfred is: 6.4
    The latitude for port alfred is: -66.32665882661225
    ushuaia
    ar
    The temperature for ushuaia is: 280.15
    The humidity for ushuaia is: 87
    The cloudiness for ushuaia is: 75
    The wind speed for ushuaia is: 5.7
    The latitude for ushuaia is: -83.54033002636197
    norman wells
    ca
    The temperature for norman wells is: 268.15
    The humidity for norman wells is: 85
    The cloudiness for norman wells is: 90
    The wind speed for norman wells is: 8.7
    The latitude for norman wells is: 83.80819674262932
    ushuaia
    ar
    The temperature for ushuaia is: 280.15
    The humidity for ushuaia is: 87
    The cloudiness for ushuaia is: 75
    The wind speed for ushuaia is: 5.7
    The latitude for ushuaia is: -81.74931266803549
    palmer
    us
    The temperature for palmer is: 281.15
    The humidity for palmer is: 48
    The cloudiness for palmer is: 1
    The wind speed for palmer is: 2.1
    The latitude for palmer is: 62.20581336231248
    bredasdorp
    za
    The temperature for bredasdorp is: 289.15
    The humidity for bredasdorp is: 87
    The cloudiness for bredasdorp is: 68
    The wind speed for bredasdorp is: 1.5
    The latitude for bredasdorp is: -78.55668540111282
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -46.99884412232354
    cherskiy
    ru
    The temperature for cherskiy is: 272.527
    The humidity for cherskiy is: 74
    The cloudiness for cherskiy is: 0
    The wind speed for cherskiy is: 3.55
    The latitude for cherskiy is: 76.03100408076236
    ushuaia
    ar
    The temperature for ushuaia is: 280.15
    The humidity for ushuaia is: 87
    The cloudiness for ushuaia is: 75
    The wind speed for ushuaia is: 5.7
    The latitude for ushuaia is: -88.033477824515
    mar del plata
    ar
    The temperature for mar del plata is: 285.652
    The humidity for mar del plata is: 72
    The cloudiness for mar del plata is: 0
    The wind speed for mar del plata is: 3
    The latitude for mar del plata is: -64.3412949416014
    cap malheureux
    mu
    The temperature for cap malheureux is: 300.15
    The humidity for cap malheureux is: 83
    The cloudiness for cap malheureux is: 75
    The wind speed for cap malheureux is: 5.1
    The latitude for cap malheureux is: -18.077584517045352
    ushuaia
    ar
    The temperature for ushuaia is: 280.15
    The humidity for ushuaia is: 87
    The cloudiness for ushuaia is: 75
    The wind speed for ushuaia is: 5.7
    The latitude for ushuaia is: -60.911288315538265
    bambous virieux
    mu
    The temperature for bambous virieux is: 300.15
    The humidity for bambous virieux is: 83
    The cloudiness for bambous virieux is: 40
    The wind speed for bambous virieux is: 3.1
    The latitude for bambous virieux is: -29.802113544642346
    livingston
    us
    The temperature for livingston is: 277.15
    The humidity for livingston is: 100
    The cloudiness for livingston is: 90
    The wind speed for livingston is: 2.1
    The latitude for livingston is: 45.11719169295404
    antigonish
    ca
    The temperature for antigonish is: 278.15
    The humidity for antigonish is: 86
    The cloudiness for antigonish is: 20
    The wind speed for antigonish is: 5.7
    The latitude for antigonish is: 45.38352913648265
    hilo
    us
    The temperature for hilo is: 300.15
    The humidity for hilo is: 65
    The cloudiness for hilo is: 75
    The wind speed for hilo is: 6.7
    The latitude for hilo is: 14.754299976317924
    saint-augustin
    ca
    The temperature for saint-augustin is: 273.15
    The humidity for saint-augustin is: 46
    The cloudiness for saint-augustin is: 40
    The wind speed for saint-augustin is: 1.5
    The latitude for saint-augustin is: 57.080876782786845
    vaini
    to
    The temperature for vaini is: 299.15
    The humidity for vaini is: 94
    The cloudiness for vaini is: 90
    The wind speed for vaini is: 2.6
    The latitude for vaini is: -85.28500941906104
    tasiilaq
    gl
    The temperature for tasiilaq is: 268.15
    The humidity for tasiilaq is: 62
    The cloudiness for tasiilaq is: 76
    The wind speed for tasiilaq is: 7.2
    The latitude for tasiilaq is: 57.45538053442806
    chitral
    pk
    The temperature for chitral is: 271.077
    The humidity for chitral is: 93
    The cloudiness for chitral is: 88
    The wind speed for chitral is: 0.4
    The latitude for chitral is: 36.20059018515883
    albany
    au
    The temperature for albany is: 293.477
    The humidity for albany is: 74
    The cloudiness for albany is: 0
    The wind speed for albany is: 5.05
    The latitude for albany is: -89.96728071084553
    vaini
    to
    The temperature for vaini is: 299.15
    The humidity for vaini is: 94
    The cloudiness for vaini is: 90
    The wind speed for vaini is: 2.6
    The latitude for vaini is: -25.172936147802616
    mosquera
    co
    The temperature for mosquera is: 287.15
    The humidity for mosquera is: 87
    The cloudiness for mosquera is: 75
    The wind speed for mosquera is: 2.1
    The latitude for mosquera is: 3.581766494273893
    lebu
    cl
    The temperature for lebu is: 287.727
    The humidity for lebu is: 93
    The cloudiness for lebu is: 0
    The wind speed for lebu is: 7.45
    The latitude for lebu is: -33.067722267799134
    carnarvon
    au
    The temperature for carnarvon is: 302.152
    The humidity for carnarvon is: 78
    The cloudiness for carnarvon is: 0
    The wind speed for carnarvon is: 2.75
    The latitude for carnarvon is: -22.1493438216946
    grand gaube
    mu
    The temperature for grand gaube is: 300.15
    The humidity for grand gaube is: 83
    The cloudiness for grand gaube is: 75
    The wind speed for grand gaube is: 5.1
    The latitude for grand gaube is: -11.938612674403046
    punta arenas
    cl
    The temperature for punta arenas is: 283.15
    The humidity for punta arenas is: 87
    The cloudiness for punta arenas is: 90
    The wind speed for punta arenas is: 3.1
    The latitude for punta arenas is: -70.3148461412346
    arraial do cabo
    br
    The temperature for arraial do cabo is: 298.652
    The humidity for arraial do cabo is: 84
    The cloudiness for arraial do cabo is: 48
    The wind speed for arraial do cabo is: 8.95
    The latitude for arraial do cabo is: -55.903363284401166
    buraydah
    sa
    The temperature for buraydah is: 290.15
    The humidity for buraydah is: 100
    The cloudiness for buraydah is: 75
    The wind speed for buraydah is: 3.6
    The latitude for buraydah is: 26.1903286161738
    punta arenas
    cl
    The temperature for punta arenas is: 283.15
    The humidity for punta arenas is: 87
    The cloudiness for punta arenas is: 90
    The wind speed for punta arenas is: 3.1
    The latitude for punta arenas is: -69.06223164315256
    ushuaia
    ar
    The temperature for ushuaia is: 280.15
    The humidity for ushuaia is: 87
    The cloudiness for ushuaia is: 75
    The wind speed for ushuaia is: 5.7
    The latitude for ushuaia is: -56.235750451328244
    tuktoyaktuk
    ca
    The temperature for tuktoyaktuk is: 261.15
    The humidity for tuktoyaktuk is: 78
    The cloudiness for tuktoyaktuk is: 90
    The wind speed for tuktoyaktuk is: 8.2
    The latitude for tuktoyaktuk is: 85.87302881941721
    hithadhoo
    mv
    The temperature for hithadhoo is: 303.027
    The humidity for hithadhoo is: 98
    The cloudiness for hithadhoo is: 88
    The wind speed for hithadhoo is: 3.6
    The latitude for hithadhoo is: -16.114769198989435
    ulladulla
    au
    The temperature for ulladulla is: 296.15
    The humidity for ulladulla is: 69
    The cloudiness for ulladulla is: 0
    The wind speed for ulladulla is: 3.6
    The latitude for ulladulla is: -39.2645690217681
    coquimbo
    cl
    The temperature for coquimbo is: 287.15
    The humidity for coquimbo is: 82
    The cloudiness for coquimbo is: 90
    The wind speed for coquimbo is: 1
    The latitude for coquimbo is: -29.66631845841558
    albany
    au
    The temperature for albany is: 293.477
    The humidity for albany is: 74
    The cloudiness for albany is: 0
    The wind speed for albany is: 5.05
    The latitude for albany is: -81.69533327097925
    puerto ayora
    ec
    The temperature for puerto ayora is: 298.327
    The humidity for puerto ayora is: 97
    The cloudiness for puerto ayora is: 36
    The wind speed for puerto ayora is: 3.4
    The latitude for puerto ayora is: -1.042143276600953
    ushuaia
    ar
    The temperature for ushuaia is: 280.15
    The humidity for ushuaia is: 87
    The cloudiness for ushuaia is: 75
    The wind speed for ushuaia is: 5.7
    The latitude for ushuaia is: -89.71589526398871
    chapais
    ca
    The temperature for chapais is: 258.15
    The humidity for chapais is: 84
    The cloudiness for chapais is: 90
    The wind speed for chapais is: 1
    The latitude for chapais is: 50.87430189974609
    arraial do cabo
    br
    The temperature for arraial do cabo is: 298.652
    The humidity for arraial do cabo is: 84
    The cloudiness for arraial do cabo is: 48
    The wind speed for arraial do cabo is: 8.95
    The latitude for arraial do cabo is: -41.30531537267341
    kropotkin
    ru
    The temperature for kropotkin is: 279.027
    The humidity for kropotkin is: 93
    The cloudiness for kropotkin is: 24
    The wind speed for kropotkin is: 4.3
    The latitude for kropotkin is: 57.787220074401716
    avarua
    ck
    The temperature for avarua is: 301.15
    The humidity for avarua is: 78
    The cloudiness for avarua is: 75
    The wind speed for avarua is: 3.6
    The latitude for avarua is: -40.711177625829706
    tessalit
    ml
    The temperature for tessalit is: 293.552
    The humidity for tessalit is: 28
    The cloudiness for tessalit is: 20
    The wind speed for tessalit is: 2.1
    The latitude for tessalit is: 23.252705256858277
    nyaunglebin
    mm
    The temperature for nyaunglebin is: 301.327
    The humidity for nyaunglebin is: 73
    The cloudiness for nyaunglebin is: 8
    The wind speed for nyaunglebin is: 1.75
    The latitude for nyaunglebin is: 18.309368037591568
    muros
    es
    The temperature for muros is: 282.15
    The humidity for muros is: 100
    The cloudiness for muros is: 75
    The wind speed for muros is: 4.6
    The latitude for muros is: 44.55413787902327
    bilibino
    ru
    The temperature for bilibino is: 275.402
    The humidity for bilibino is: 71
    The cloudiness for bilibino is: 8
    The wind speed for bilibino is: 2.5
    The latitude for bilibino is: 65.96854484540268
    baffa
    pk
    The temperature for baffa is: 287.577
    The humidity for baffa is: 96
    The cloudiness for baffa is: 80
    The wind speed for baffa is: 1
    The latitude for baffa is: 34.2555205438771
    tabuk
    sa
    The temperature for tabuk is: 290.15
    The humidity for tabuk is: 59
    The cloudiness for tabuk is: 0
    The wind speed for tabuk is: 2.1
    The latitude for tabuk is: 29.51855903872395
    peleduy
    ru
    The temperature for peleduy is: 267.227
    The humidity for peleduy is: 60
    The cloudiness for peleduy is: 68
    The wind speed for peleduy is: 3.3
    The latitude for peleduy is: 60.832023349616776
    ojinaga
    mx
    The temperature for ojinaga is: 293.677
    The humidity for ojinaga is: 16
    The cloudiness for ojinaga is: 92
    The wind speed for ojinaga is: 1.2
    The latitude for ojinaga is: 30.202878796161144
    bronnoysund
    no
    The temperature for bronnoysund is: 272.15
    The humidity for bronnoysund is: 100
    The cloudiness for bronnoysund is: 40
    The wind speed for bronnoysund is: 2.6
    The latitude for bronnoysund is: 65.55960979584373
    hilo
    us
    The temperature for hilo is: 300.15
    The humidity for hilo is: 65
    The cloudiness for hilo is: 75
    The wind speed for hilo is: 6.7
    The latitude for hilo is: 11.553370189549554
    cabo san lucas
    mx
    The temperature for cabo san lucas is: 302.15
    The humidity for cabo san lucas is: 21
    The cloudiness for cabo san lucas is: 20
    The wind speed for cabo san lucas is: 4.6
    The latitude for cabo san lucas is: 15.95150123281232
    bredasdorp
    za
    The temperature for bredasdorp is: 289.15
    The humidity for bredasdorp is: 87
    The cloudiness for bredasdorp is: 68
    The wind speed for bredasdorp is: 1.5
    The latitude for bredasdorp is: -85.64047250987208
    kodiak
    us
    The temperature for kodiak is: 267.15
    The humidity for kodiak is: 92
    The cloudiness for kodiak is: 1
    The wind speed for kodiak is: 2.6
    The latitude for kodiak is: 50.000847290724465
    den helder
    nl
    The temperature for den helder is: 278.15
    The humidity for den helder is: 100
    The cloudiness for den helder is: 90
    The wind speed for den helder is: 2.1
    The latitude for den helder is: 53.24327774718557
    san carlos de bariloche
    ar
    The temperature for san carlos de bariloche is: 284.15
    The humidity for san carlos de bariloche is: 50
    The cloudiness for san carlos de bariloche is: 0
    The wind speed for san carlos de bariloche is: 2.6
    The latitude for san carlos de bariloche is: -40.741401470171105
    castro
    cl
    The temperature for castro is: 280.852
    The humidity for castro is: 97
    The cloudiness for castro is: 0
    The wind speed for castro is: 1.75
    The latitude for castro is: -42.392060075060904
    koslan
    ru
    The temperature for koslan is: 260.777
    The humidity for koslan is: 69
    The cloudiness for koslan is: 0
    The wind speed for koslan is: 1.15
    The latitude for koslan is: 64.26972674156045
    norrtalje
    se
    The temperature for norrtalje is: 272.15
    The humidity for norrtalje is: 74
    The cloudiness for norrtalje is: 0
    The wind speed for norrtalje is: 4.6
    The latitude for norrtalje is: 61.108913725081266
    bredasdorp
    za
    The temperature for bredasdorp is: 289.15
    The humidity for bredasdorp is: 87
    The cloudiness for bredasdorp is: 68
    The wind speed for bredasdorp is: 1.5
    The latitude for bredasdorp is: -38.99545674663962
    new norfolk
    au
    The temperature for new norfolk is: 292.15
    The humidity for new norfolk is: 34
    The cloudiness for new norfolk is: 0
    The wind speed for new norfolk is: 6.2
    The latitude for new norfolk is: -60.50617844017019
    norman wells
    ca
    The temperature for norman wells is: 268.15
    The humidity for norman wells is: 85
    The cloudiness for norman wells is: 90
    The wind speed for norman wells is: 8.7
    The latitude for norman wells is: 79.55761479807632
    ribeira grande
    pt
    The temperature for ribeira grande is: 290.077
    The humidity for ribeira grande is: 98
    The cloudiness for ribeira grande is: 92
    The wind speed for ribeira grande is: 7.4
    The latitude for ribeira grande is: 27.49754534691897
    bilma
    ne
    The temperature for bilma is: 287.177
    The humidity for bilma is: 40
    The cloudiness for bilma is: 0
    The wind speed for bilma is: 1.25
    The latitude for bilma is: 19.157452040956287
    cabo san lucas
    mx
    The temperature for cabo san lucas is: 302.15
    The humidity for cabo san lucas is: 21
    The cloudiness for cabo san lucas is: 20
    The wind speed for cabo san lucas is: 4.6
    The latitude for cabo san lucas is: 11.037141109687681
    avarua
    ck
    The temperature for avarua is: 301.15
    The humidity for avarua is: 78
    The cloudiness for avarua is: 75
    The wind speed for avarua is: 3.6
    The latitude for avarua is: -23.418398684025377
    thompson
    ca
    The temperature for thompson is: 251.15
    The humidity for thompson is: 48
    The cloudiness for thompson is: 20
    The wind speed for thompson is: 2.1
    The latitude for thompson is: 61.39541342244945
    vanimo
    pg
    The temperature for vanimo is: 299.227
    The humidity for vanimo is: 100
    The cloudiness for vanimo is: 80
    The wind speed for vanimo is: 4.1
    The latitude for vanimo is: -3.7675325471870735
    cherskiy
    ru
    The temperature for cherskiy is: 272.527
    The humidity for cherskiy is: 74
    The cloudiness for cherskiy is: 0
    The wind speed for cherskiy is: 3.55
    The latitude for cherskiy is: 71.33598809684656
    busselton
    au
    The temperature for busselton is: 294.027
    The humidity for busselton is: 95
    The cloudiness for busselton is: 0
    The wind speed for busselton is: 6.5
    The latitude for busselton is: -86.05160459906816
    busselton
    au
    The temperature for busselton is: 294.027
    The humidity for busselton is: 95
    The cloudiness for busselton is: 0
    The wind speed for busselton is: 6.5
    The latitude for busselton is: -55.34610740397087
    esperance
    au
    The temperature for esperance is: 294.677
    The humidity for esperance is: 69
    The cloudiness for esperance is: 0
    The wind speed for esperance is: 3.1
    The latitude for esperance is: -39.70484832330512
    punta arenas
    cl
    The temperature for punta arenas is: 283.15
    The humidity for punta arenas is: 87
    The cloudiness for punta arenas is: 90
    The wind speed for punta arenas is: 3.1
    The latitude for punta arenas is: -86.98782323296341
    bredasdorp
    za
    The temperature for bredasdorp is: 289.15
    The humidity for bredasdorp is: 87
    The cloudiness for bredasdorp is: 68
    The wind speed for bredasdorp is: 1.5
    The latitude for bredasdorp is: -85.83509147306283
    lamu
    ke
    The temperature for lamu is: 300.727
    The humidity for lamu is: 90
    The cloudiness for lamu is: 92
    The wind speed for lamu is: 3.55
    The latitude for lamu is: -2.7363745908233454
    puerto ayora
    ec
    The temperature for puerto ayora is: 298.327
    The humidity for puerto ayora is: 97
    The cloudiness for puerto ayora is: 36
    The wind speed for puerto ayora is: 3.4
    The latitude for puerto ayora is: 3.5105877039339077
    busselton
    au
    The temperature for busselton is: 294.027
    The humidity for busselton is: 95
    The cloudiness for busselton is: 0
    The wind speed for busselton is: 6.5
    The latitude for busselton is: -38.95314792599776
    noumea
    nc
    The temperature for noumea is: 302.15
    The humidity for noumea is: 70
    The cloudiness for noumea is: 0
    The wind speed for noumea is: 7.7
    The latitude for noumea is: -28.787066207572202
    cabo san lucas
    mx
    The temperature for cabo san lucas is: 302.15
    The humidity for cabo san lucas is: 21
    The cloudiness for cabo san lucas is: 20
    The wind speed for cabo san lucas is: 4.6
    The latitude for cabo san lucas is: 8.207017496815084
    kavaratti
    in
    The temperature for kavaratti is: 301.927
    The humidity for kavaratti is: 100
    The cloudiness for kavaratti is: 36
    The wind speed for kavaratti is: 0.75
    The latitude for kavaratti is: 10.831987610452785
    nikolskoye
    ru
    The temperature for nikolskoye is: 273.15
    The humidity for nikolskoye is: 90
    The cloudiness for nikolskoye is: 90
    The wind speed for nikolskoye is: 7
    The latitude for nikolskoye is: 48.13124638306351
    berlevag
    no
    The temperature for berlevag is: 263.702
    The humidity for berlevag is: 100
    The cloudiness for berlevag is: 12
    The wind speed for berlevag is: 1.5
    The latitude for berlevag is: 88.41337529400906
    albany
    au
    The temperature for albany is: 293.477
    The humidity for albany is: 74
    The cloudiness for albany is: 0
    The wind speed for albany is: 5.05
    The latitude for albany is: -34.27026238259832
    ried
    at
    The temperature for ried is: 277.15
    The humidity for ried is: 80
    The cloudiness for ried is: 75
    The wind speed for ried is: 2.1
    The latitude for ried is: 48.32455735901266
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -21.859626761671763
    victoria
    sc
    The temperature for victoria is: 301.15
    The humidity for victoria is: 78
    The cloudiness for victoria is: 80
    The wind speed for victoria is: 1.5
    The latitude for victoria is: -0.4925624059920892
    bethel
    us
    The temperature for bethel is: 275.15
    The humidity for bethel is: 64
    The cloudiness for bethel is: 1
    The wind speed for bethel is: 9.3
    The latitude for bethel is: 42.96480790771159
    karratha
    au
    The temperature for karratha is: 309.552
    The humidity for karratha is: 32
    The cloudiness for karratha is: 24
    The wind speed for karratha is: 2.1
    The latitude for karratha is: -19.342583099609456
    georgetown
    sh
    The temperature for georgetown is: 299.677
    The humidity for georgetown is: 100
    The cloudiness for georgetown is: 12
    The wind speed for georgetown is: 5.25
    The latitude for georgetown is: -0.8173873893076262
    hermanus
    za
    The temperature for hermanus is: 285.052
    The humidity for hermanus is: 91
    The cloudiness for hermanus is: 0
    The wind speed for hermanus is: 0.8
    The latitude for hermanus is: -70.97960526996039
    atuona
    pf
    The temperature for atuona is: 300.827
    The humidity for atuona is: 100
    The cloudiness for atuona is: 32
    The wind speed for atuona is: 6.05
    The latitude for atuona is: -10.138956567919578
    victoria
    sc
    The temperature for victoria is: 301.15
    The humidity for victoria is: 78
    The cloudiness for victoria is: 80
    The wind speed for victoria is: 1.5
    The latitude for victoria is: -8.063173838557077
    tanout
    ne
    The temperature for tanout is: 290.227
    The humidity for tanout is: 25
    The cloudiness for tanout is: 0
    The wind speed for tanout is: 2.35
    The latitude for tanout is: 14.496512726935904
    chaman
    pk
    The temperature for chaman is: 289.277
    The humidity for chaman is: 39
    The cloudiness for chaman is: 64
    The wind speed for chaman is: 2.05
    The latitude for chaman is: 31.66752461454726
    puerto ayora
    ec
    The temperature for puerto ayora is: 298.327
    The humidity for puerto ayora is: 97
    The cloudiness for puerto ayora is: 36
    The wind speed for puerto ayora is: 3.4
    The latitude for puerto ayora is: -10.125820033933309
    axim
    gh
    The temperature for axim is: 300.527
    The humidity for axim is: 100
    The cloudiness for axim is: 20
    The wind speed for axim is: 4.95
    The latitude for axim is: 1.7443203809774275
    ambilobe
    mg
    The temperature for ambilobe is: 293.952
    The humidity for ambilobe is: 98
    The cloudiness for ambilobe is: 64
    The wind speed for ambilobe is: 0.85
    The latitude for ambilobe is: -8.853793546439618
    mvuma
    zw
    The temperature for mvuma is: 286.352
    The humidity for mvuma is: 95
    The cloudiness for mvuma is: 0
    The wind speed for mvuma is: 3.75
    The latitude for mvuma is: -18.700335797657047
    cheney
    us
    The temperature for cheney is: 280.15
    The humidity for cheney is: 70
    The cloudiness for cheney is: 75
    The wind speed for cheney is: 5.7
    The latitude for cheney is: 47.280590972925296
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -31.934515821101826
    rognan
    no
    The temperature for rognan is: 270.15
    The humidity for rognan is: 92
    The cloudiness for rognan is: 40
    The wind speed for rognan is: 5.7
    The latitude for rognan is: 65.3088911112865
    port elizabeth
    za
    The temperature for port elizabeth is: 293.15
    The humidity for port elizabeth is: 100
    The cloudiness for port elizabeth is: 75
    The wind speed for port elizabeth is: 2.6
    The latitude for port elizabeth is: -72.76805237342386
    havoysund
    no
    The temperature for havoysund is: 269.15
    The humidity for havoysund is: 73
    The cloudiness for havoysund is: 0
    The wind speed for havoysund is: 3.6
    The latitude for havoysund is: 72.58456787200831
    impfondo
    cg
    The temperature for impfondo is: 294.477
    The humidity for impfondo is: 100
    The cloudiness for impfondo is: 56
    The wind speed for impfondo is: 1.85
    The latitude for impfondo is: 2.327322486505139
    sawtell
    au
    The temperature for sawtell is: 302.15
    The humidity for sawtell is: 54
    The cloudiness for sawtell is: 0
    The wind speed for sawtell is: 6.7
    The latitude for sawtell is: -31.47676831680699
    sinnamary
    gf
    The temperature for sinnamary is: 298.827
    The humidity for sinnamary is: 100
    The cloudiness for sinnamary is: 92
    The wind speed for sinnamary is: 3.45
    The latitude for sinnamary is: 19.799349915829822
    tuktoyaktuk
    ca
    The temperature for tuktoyaktuk is: 261.15
    The humidity for tuktoyaktuk is: 78
    The cloudiness for tuktoyaktuk is: 90
    The wind speed for tuktoyaktuk is: 8.2
    The latitude for tuktoyaktuk is: 87.98271621475305
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -45.69188811710091
    khatanga
    ru
    The temperature for khatanga is: 251.402
    The humidity for khatanga is: 76
    The cloudiness for khatanga is: 56
    The wind speed for khatanga is: 5.25
    The latitude for khatanga is: 86.52911890057274
    bethel
    us
    The temperature for bethel is: 275.15
    The humidity for bethel is: 64
    The cloudiness for bethel is: 1
    The wind speed for bethel is: 9.3
    The latitude for bethel is: 46.58714549485927
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -48.76135461581437
    busselton
    au
    The temperature for busselton is: 294.027
    The humidity for busselton is: 95
    The cloudiness for busselton is: 0
    The wind speed for busselton is: 6.5
    The latitude for busselton is: -76.66564809428269
    port alfred
    za
    The temperature for port alfred is: 295.327
    The humidity for port alfred is: 89
    The cloudiness for port alfred is: 44
    The wind speed for port alfred is: 6.4
    The latitude for port alfred is: -85.94680828544264
    kapaa
    us
    The temperature for kapaa is: 299.15
    The humidity for kapaa is: 83
    The cloudiness for kapaa is: 40
    The wind speed for kapaa is: 3.6
    The latitude for kapaa is: 36.571927365111605
    albany
    au
    The temperature for albany is: 293.477
    The humidity for albany is: 74
    The cloudiness for albany is: 0
    The wind speed for albany is: 5.05
    The latitude for albany is: -60.3734509546682
    atuona
    pf
    The temperature for atuona is: 300.827
    The humidity for atuona is: 100
    The cloudiness for atuona is: 32
    The wind speed for atuona is: 6.05
    The latitude for atuona is: -1.764823754602162
    hobart
    au
    The temperature for hobart is: 292.15
    The humidity for hobart is: 34
    The cloudiness for hobart is: 0
    The wind speed for hobart is: 6.2
    The latitude for hobart is: -71.94355159212141
    sitka
    us
    The temperature for sitka is: 276.527
    The humidity for sitka is: 55
    The cloudiness for sitka is: 24
    The wind speed for sitka is: 4.35
    The latitude for sitka is: 54.37148068994239
    ahuimanu
    us
    The temperature for ahuimanu is: 300.15
    The humidity for ahuimanu is: 74
    The cloudiness for ahuimanu is: 1
    The wind speed for ahuimanu is: 2.6
    The latitude for ahuimanu is: 31.683231020061214
    atuona
    pf
    The temperature for atuona is: 300.827
    The humidity for atuona is: 100
    The cloudiness for atuona is: 32
    The wind speed for atuona is: 6.05
    The latitude for atuona is: -6.4976768347164295
    hirara
    jp
    The temperature for hirara is: 298.15
    The humidity for hirara is: 64
    The cloudiness for hirara is: 20
    The wind speed for hirara is: 2.1
    The latitude for hirara is: 20.72248913414282
    ushuaia
    ar
    The temperature for ushuaia is: 280.15
    The humidity for ushuaia is: 87
    The cloudiness for ushuaia is: 75
    The wind speed for ushuaia is: 5.7
    The latitude for ushuaia is: -69.12920866648201
    son la
    vn
    The temperature for son la is: 295.852
    The humidity for son la is: 83
    The cloudiness for son la is: 56
    The wind speed for son la is: 1.05
    The latitude for son la is: 21.574895404455646
    ushuaia
    ar
    The temperature for ushuaia is: 280.15
    The humidity for ushuaia is: 87
    The cloudiness for ushuaia is: 75
    The wind speed for ushuaia is: 5.7
    The latitude for ushuaia is: -56.722549149366614
    santiago
    pe
    The temperature for santiago is: 288.302
    The humidity for santiago is: 94
    The cloudiness for santiago is: 0
    The wind speed for santiago is: 1.15
    The latitude for santiago is: -14.903518744297813
    punta arenas
    cl
    The temperature for punta arenas is: 283.15
    The humidity for punta arenas is: 87
    The cloudiness for punta arenas is: 90
    The wind speed for punta arenas is: 3.1
    The latitude for punta arenas is: -86.74805999525323
    cidreira
    br
    The temperature for cidreira is: 293.827
    The humidity for cidreira is: 97
    The cloudiness for cidreira is: 92
    The wind speed for cidreira is: 3.55
    The latitude for cidreira is: -53.15104731623347
    avarua
    ck
    The temperature for avarua is: 301.15
    The humidity for avarua is: 78
    The cloudiness for avarua is: 75
    The wind speed for avarua is: 3.6
    The latitude for avarua is: -14.825454504945085
    vaini
    to
    The temperature for vaini is: 299.15
    The humidity for vaini is: 94
    The cloudiness for vaini is: 90
    The wind speed for vaini is: 2.6
    The latitude for vaini is: -80.00353928268692
    rovaniemi
    fi
    The temperature for rovaniemi is: 262.15
    The humidity for rovaniemi is: 78
    The cloudiness for rovaniemi is: 0
    The wind speed for rovaniemi is: 3.6
    The latitude for rovaniemi is: 67.7956356100722
    altus
    us
    The temperature for altus is: 279.15
    The humidity for altus is: 60
    The cloudiness for altus is: 1
    The wind speed for altus is: 5.9
    The latitude for altus is: 34.936490256193636
    nikolskoye
    ru
    The temperature for nikolskoye is: 273.15
    The humidity for nikolskoye is: 90
    The cloudiness for nikolskoye is: 90
    The wind speed for nikolskoye is: 7
    The latitude for nikolskoye is: 43.02098887795481
    vila velha
    br
    The temperature for vila velha is: 301.15
    The humidity for vila velha is: 83
    The cloudiness for vila velha is: 75
    The wind speed for vila velha is: 2.6
    The latitude for vila velha is: -24.764972237551973
    georgetown
    sh
    The temperature for georgetown is: 299.677
    The humidity for georgetown is: 100
    The cloudiness for georgetown is: 12
    The wind speed for georgetown is: 5.25
    The latitude for georgetown is: -5.903679436913009
    shingu
    jp
    The temperature for shingu is: 294.15
    The humidity for shingu is: 64
    The cloudiness for shingu is: 20
    The wind speed for shingu is: 3.1
    The latitude for shingu is: 27.716869010181853
    geraldton
    au
    The temperature for geraldton is: 303.15
    The humidity for geraldton is: 40
    The cloudiness for geraldton is: 20
    The wind speed for geraldton is: 4.1
    The latitude for geraldton is: -34.187404920883466
    albany
    au
    The temperature for albany is: 293.477
    The humidity for albany is: 74
    The cloudiness for albany is: 0
    The wind speed for albany is: 5.05
    The latitude for albany is: -66.74124745029957
    provideniya
    ru
    The temperature for provideniya is: 274.15
    The humidity for provideniya is: 80
    The cloudiness for provideniya is: 75
    The wind speed for provideniya is: 4
    The latitude for provideniya is: 40.75724178512482
    tessalit
    ml
    The temperature for tessalit is: 293.552
    The humidity for tessalit is: 28
    The cloudiness for tessalit is: 20
    The wind speed for tessalit is: 2.1
    The latitude for tessalit is: 21.201641952433818
    ushuaia
    ar
    The temperature for ushuaia is: 280.15
    The humidity for ushuaia is: 87
    The cloudiness for ushuaia is: 75
    The wind speed for ushuaia is: 5.7
    The latitude for ushuaia is: -85.88659216897584
    houma
    cn
    The temperature for houma is: 297.952
    The humidity for houma is: 38
    The cloudiness for houma is: 0
    The wind speed for houma is: 1.45
    The latitude for houma is: 35.39641062605621
    ushuaia
    ar
    The temperature for ushuaia is: 280.15
    The humidity for ushuaia is: 87
    The cloudiness for ushuaia is: 75
    The wind speed for ushuaia is: 5.7
    The latitude for ushuaia is: -87.66505020099989
    longyearbyen
    sj
    The temperature for longyearbyen is: 262.15
    The humidity for longyearbyen is: 36
    The cloudiness for longyearbyen is: 8
    The wind speed for longyearbyen is: 5.7
    The latitude for longyearbyen is: 77.73252605781784
    east london
    za
    The temperature for east london is: 297.352
    The humidity for east london is: 99
    The cloudiness for east london is: 24
    The wind speed for east london is: 10.6
    The latitude for east london is: -36.546793189525815
    ushuaia
    ar
    The temperature for ushuaia is: 280.15
    The humidity for ushuaia is: 87
    The cloudiness for ushuaia is: 75
    The wind speed for ushuaia is: 5.7
    The latitude for ushuaia is: -85.83085578531487
    vaini
    to
    The temperature for vaini is: 299.15
    The humidity for vaini is: 94
    The cloudiness for vaini is: 90
    The wind speed for vaini is: 2.6
    The latitude for vaini is: -45.79448034921837
    salalah
    om
    The temperature for salalah is: 299.15
    The humidity for salalah is: 83
    The cloudiness for salalah is: 40
    The wind speed for salalah is: 2.1
    The latitude for salalah is: 15.870791567338912
    saint-philippe
    re
    The temperature for saint-philippe is: 298.15
    The humidity for saint-philippe is: 65
    The cloudiness for saint-philippe is: 0
    The wind speed for saint-philippe is: 3.1
    The latitude for saint-philippe is: -53.84203790562453
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -22.364292938828427
    punta arenas
    cl
    The temperature for punta arenas is: 283.15
    The humidity for punta arenas is: 87
    The cloudiness for punta arenas is: 90
    The wind speed for punta arenas is: 3.1
    The latitude for punta arenas is: -56.84096628003417
    vaini
    to
    The temperature for vaini is: 299.15
    The humidity for vaini is: 94
    The cloudiness for vaini is: 90
    The wind speed for vaini is: 2.6
    The latitude for vaini is: -34.390384723123155
    kruisfontein
    za
    The temperature for kruisfontein is: 291.227
    The humidity for kruisfontein is: 91
    The cloudiness for kruisfontein is: 12
    The wind speed for kruisfontein is: 2.2
    The latitude for kruisfontein is: -81.70183899103543
    bluff
    nz
    The temperature for bluff is: 290.602
    The humidity for bluff is: 83
    The cloudiness for bluff is: 48
    The wind speed for bluff is: 7.05
    The latitude for bluff is: -84.53743586908166
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -21.27829223629601
    saint george
    bm
    The temperature for saint george is: 293.15
    The humidity for saint george is: 88
    The cloudiness for saint george is: 75
    The wind speed for saint george is: 1
    The latitude for saint george is: 30.948795865652883
    cape town
    za
    The temperature for cape town is: 292.15
    The humidity for cape town is: 77
    The cloudiness for cape town is: 0
    The wind speed for cape town is: 4.1
    The latitude for cape town is: -71.86560359335655
    dubti
    et
    The temperature for dubti is: 290.727
    The humidity for dubti is: 41
    The cloudiness for dubti is: 0
    The wind speed for dubti is: 1.3
    The latitude for dubti is: 12.7484601959371
    vaini
    to
    The temperature for vaini is: 299.15
    The humidity for vaini is: 94
    The cloudiness for vaini is: 90
    The wind speed for vaini is: 2.6
    The latitude for vaini is: -79.34021225430766
    barrow
    us
    The temperature for barrow is: 271.15
    The humidity for barrow is: 92
    The cloudiness for barrow is: 90
    The wind speed for barrow is: 2.1
    The latitude for barrow is: 71.61339721135414
    port alfred
    za
    The temperature for port alfred is: 295.327
    The humidity for port alfred is: 89
    The cloudiness for port alfred is: 44
    The wind speed for port alfred is: 6.4
    The latitude for port alfred is: -72.71482493240072
    hermanus
    za
    The temperature for hermanus is: 285.052
    The humidity for hermanus is: 91
    The cloudiness for hermanus is: 0
    The wind speed for hermanus is: 0.8
    The latitude for hermanus is: -57.91022597617825
    saldanha
    za
    The temperature for saldanha is: 290.15
    The humidity for saldanha is: 88
    The cloudiness for saldanha is: 88
    The wind speed for saldanha is: 3.1
    The latitude for saldanha is: -39.68103188119813
    severo-kurilsk
    ru
    The temperature for severo-kurilsk is: 271.577
    The humidity for severo-kurilsk is: 100
    The cloudiness for severo-kurilsk is: 64
    The wind speed for severo-kurilsk is: 2.5
    The latitude for severo-kurilsk is: 33.778408231536716
    pacific grove
    us
    The temperature for pacific grove is: 290.15
    The humidity for pacific grove is: 58
    The cloudiness for pacific grove is: 1
    The wind speed for pacific grove is: 3.1
    The latitude for pacific grove is: 32.51806045907085
    ribeira grande
    pt
    The temperature for ribeira grande is: 290.077
    The humidity for ribeira grande is: 98
    The cloudiness for ribeira grande is: 92
    The wind speed for ribeira grande is: 7.4
    The latitude for ribeira grande is: 34.99264574814352
    ilulissat
    gl
    The temperature for ilulissat is: 272.15
    The humidity for ilulissat is: 50
    The cloudiness for ilulissat is: 0
    The wind speed for ilulissat is: 8.2
    The latitude for ilulissat is: 88.3897141585802
    albany
    au
    The temperature for albany is: 293.477
    The humidity for albany is: 74
    The cloudiness for albany is: 0
    The wind speed for albany is: 5.05
    The latitude for albany is: -64.3937687674244
    challans
    fr
    The temperature for challans is: 284.15
    The humidity for challans is: 66
    The cloudiness for challans is: 0
    The wind speed for challans is: 5.7
    The latitude for challans is: 46.25948568382998
    victoria
    sc
    The temperature for victoria is: 301.15
    The humidity for victoria is: 78
    The cloudiness for victoria is: 80
    The wind speed for victoria is: 1.5
    The latitude for victoria is: -2.0792632498206984
    vaini
    to
    The temperature for vaini is: 299.15
    The humidity for vaini is: 94
    The cloudiness for vaini is: 90
    The wind speed for vaini is: 2.6
    The latitude for vaini is: -79.53099140312263
    hobart
    au
    The temperature for hobart is: 292.15
    The humidity for hobart is: 34
    The cloudiness for hobart is: 0
    The wind speed for hobart is: 6.2
    The latitude for hobart is: -64.44113816621388
    ilulissat
    gl
    The temperature for ilulissat is: 272.15
    The humidity for ilulissat is: 50
    The cloudiness for ilulissat is: 0
    The wind speed for ilulissat is: 8.2
    The latitude for ilulissat is: 72.62012972443787
    kapaa
    us
    The temperature for kapaa is: 299.15
    The humidity for kapaa is: 83
    The cloudiness for kapaa is: 40
    The wind speed for kapaa is: 3.6
    The latitude for kapaa is: 22.7621880539115
    clyde river
    ca
    The temperature for clyde river is: 259.15
    The humidity for clyde river is: 84
    The cloudiness for clyde river is: 90
    The wind speed for clyde river is: 6.2
    The latitude for clyde river is: 70.92241425481294
    kapaa
    us
    The temperature for kapaa is: 299.15
    The humidity for kapaa is: 83
    The cloudiness for kapaa is: 40
    The wind speed for kapaa is: 3.6
    The latitude for kapaa is: 37.34825535519093
    sterling
    us
    The temperature for sterling is: 286.15
    The humidity for sterling is: 54
    The cloudiness for sterling is: 90
    The wind speed for sterling is: 3.1
    The latitude for sterling is: 57.209828966020325
    severo-kurilsk
    ru
    The temperature for severo-kurilsk is: 271.577
    The humidity for severo-kurilsk is: 100
    The cloudiness for severo-kurilsk is: 64
    The wind speed for severo-kurilsk is: 2.5
    The latitude for severo-kurilsk is: 42.639986955287526
    sisimiut
    gl
    The temperature for sisimiut is: 262.352
    The humidity for sisimiut is: 65
    The cloudiness for sisimiut is: 8
    The wind speed for sisimiut is: 1.05
    The latitude for sisimiut is: 65.40528840181679
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -27.940368954722203
    luderitz
    na
    The temperature for luderitz is: 288.15
    The humidity for luderitz is: 93
    The cloudiness for luderitz is: 44
    The wind speed for luderitz is: 3.1
    The latitude for luderitz is: -37.4414066985454
    jamestown
    sh
    The temperature for jamestown is: 296.802
    The humidity for jamestown is: 100
    The cloudiness for jamestown is: 36
    The wind speed for jamestown is: 7
    The latitude for jamestown is: -23.18717471683412
    davila
    ph
    The temperature for davila is: 300.15
    The humidity for davila is: 61
    The cloudiness for davila is: 20
    The wind speed for davila is: 1
    The latitude for davila is: 19.681279498716066
    busselton
    au
    The temperature for busselton is: 294.027
    The humidity for busselton is: 95
    The cloudiness for busselton is: 0
    The wind speed for busselton is: 6.5
    The latitude for busselton is: -61.141694511699995
    nikolskoye
    ru
    The temperature for nikolskoye is: 273.15
    The humidity for nikolskoye is: 90
    The cloudiness for nikolskoye is: 90
    The wind speed for nikolskoye is: 7
    The latitude for nikolskoye is: 45.188375143651825
    hermanus
    za
    The temperature for hermanus is: 285.052
    The humidity for hermanus is: 91
    The cloudiness for hermanus is: 0
    The wind speed for hermanus is: 0.8
    The latitude for hermanus is: -60.57827483693053
    beringovskiy
    ru
    The temperature for beringovskiy is: 273.302
    The humidity for beringovskiy is: 95
    The cloudiness for beringovskiy is: 0
    The wind speed for beringovskiy is: 4.2
    The latitude for beringovskiy is: 62.01499042919389
    san juan
    ar
    The temperature for san juan is: 287.327
    The humidity for san juan is: 97
    The cloudiness for san juan is: 92
    The wind speed for san juan is: 2.4
    The latitude for san juan is: -31.50501079130637
    mount gambier
    au
    The temperature for mount gambier is: 291.227
    The humidity for mount gambier is: 74
    The cloudiness for mount gambier is: 92
    The wind speed for mount gambier is: 3.35
    The latitude for mount gambier is: -40.69014198226347
    jamestown
    sh
    The temperature for jamestown is: 296.802
    The humidity for jamestown is: 100
    The cloudiness for jamestown is: 36
    The wind speed for jamestown is: 7
    The latitude for jamestown is: -36.04671955582961
    jamestown
    sh
    The temperature for jamestown is: 296.802
    The humidity for jamestown is: 100
    The cloudiness for jamestown is: 36
    The wind speed for jamestown is: 7
    The latitude for jamestown is: -15.13637134375476
    hamilton
    bm
    The temperature for hamilton is: 293.15
    The humidity for hamilton is: 82
    The cloudiness for hamilton is: 90
    The wind speed for hamilton is: 0.5
    The latitude for hamilton is: 32.39753214893025
    evensk
    ru
    The temperature for evensk is: 274.077
    The humidity for evensk is: 88
    The cloudiness for evensk is: 92
    The wind speed for evensk is: 7.15
    The latitude for evensk is: 61.19953549161005
    sola
    vu
    The temperature for sola is: 300.477
    The humidity for sola is: 100
    The cloudiness for sola is: 88
    The wind speed for sola is: 4.1
    The latitude for sola is: -13.449011368031577
    taltal
    cl
    The temperature for taltal is: 285.527
    The humidity for taltal is: 96
    The cloudiness for taltal is: 0
    The wind speed for taltal is: 0.75
    The latitude for taltal is: -26.362439700360426
    ilorin
    ng
    The temperature for ilorin is: 297.427
    The humidity for ilorin is: 76
    The cloudiness for ilorin is: 0
    The wind speed for ilorin is: 5.3
    The latitude for ilorin is: 8.566929647994954
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -22.469015326946405
    orzhytsya
    ua
    The temperature for orzhytsya is: 280.277
    The humidity for orzhytsya is: 96
    The cloudiness for orzhytsya is: 76
    The wind speed for orzhytsya is: 5.4
    The latitude for orzhytsya is: 49.68418139516203
    luena
    ao
    The temperature for luena is: 290.827
    The humidity for luena is: 97
    The cloudiness for luena is: 92
    The wind speed for luena is: 1.2
    The latitude for luena is: -13.717631586012487
    kaseda
    jp
    The temperature for kaseda is: 293.15
    The humidity for kaseda is: 52
    The cloudiness for kaseda is: 20
    The wind speed for kaseda is: 1.5
    The latitude for kaseda is: 30.262504776457064
    kununurra
    au
    The temperature for kununurra is: 309.15
    The humidity for kununurra is: 39
    The cloudiness for kununurra is: 0
    The wind speed for kununurra is: 2.1
    The latitude for kununurra is: -19.131458411892822
    rassvet
    ru
    The temperature for rassvet is: 271.927
    The humidity for rassvet is: 91
    The cloudiness for rassvet is: 0
    The wind speed for rassvet is: 6
    The latitude for rassvet is: 56.95449225520079
    qaanaaq
    gl
    The temperature for qaanaaq is: 260.177
    The humidity for qaanaaq is: 85
    The cloudiness for qaanaaq is: 76
    The wind speed for qaanaaq is: 0.75
    The latitude for qaanaaq is: 81.95786675014347
    kodiak
    us
    The temperature for kodiak is: 267.15
    The humidity for kodiak is: 92
    The cloudiness for kodiak is: 1
    The wind speed for kodiak is: 2.6
    The latitude for kodiak is: 43.81189986550558
    brainerd
    us
    The temperature for brainerd is: 266.15
    The humidity for brainerd is: 61
    The cloudiness for brainerd is: 1
    The wind speed for brainerd is: 2.1
    The latitude for brainerd is: 46.825555363649215
    busselton
    au
    The temperature for busselton is: 294.027
    The humidity for busselton is: 95
    The cloudiness for busselton is: 0
    The wind speed for busselton is: 6.5
    The latitude for busselton is: -73.07306143892603
    beloha
    mg
    The temperature for beloha is: 296.152
    The humidity for beloha is: 87
    The cloudiness for beloha is: 12
    The wind speed for beloha is: 5.1
    The latitude for beloha is: -33.183853254343525
    korla
    cn
    The temperature for korla is: 279.802
    The humidity for korla is: 89
    The cloudiness for korla is: 92
    The wind speed for korla is: 3.35
    The latitude for korla is: 38.17342990250654
    grand-lahou
    ci
    The temperature for grand-lahou is: 298.602
    The humidity for grand-lahou is: 92
    The cloudiness for grand-lahou is: 44
    The wind speed for grand-lahou is: 2.45
    The latitude for grand-lahou is: 2.533255801533869
    la ronge
    ca
    The temperature for la ronge is: 259.15
    The humidity for la ronge is: 50
    The cloudiness for la ronge is: 20
    The wind speed for la ronge is: 2.1
    The latitude for la ronge is: 62.94129406124705
    albany
    au
    The temperature for albany is: 293.477
    The humidity for albany is: 74
    The cloudiness for albany is: 0
    The wind speed for albany is: 5.05
    The latitude for albany is: -61.638914999744955
    santa rosa
    ar
    The temperature for santa rosa is: 288.15
    The humidity for santa rosa is: 93
    The cloudiness for santa rosa is: 0
    The wind speed for santa rosa is: 2.1
    The latitude for santa rosa is: -36.81419531753407
    tete
    mz
    The temperature for tete is: 296.677
    The humidity for tete is: 77
    The cloudiness for tete is: 68
    The wind speed for tete is: 3.65
    The latitude for tete is: -15.161517777771039
    oistins
    bb
    The temperature for oistins is: 298.15
    The humidity for oistins is: 78
    The cloudiness for oistins is: 20
    The wind speed for oistins is: 5.1
    The latitude for oistins is: 11.55503882571152
    tondano
    id
    The temperature for tondano is: 303.15
    The humidity for tondano is: 66
    The cloudiness for tondano is: 20
    The wind speed for tondano is: 2.1
    The latitude for tondano is: 0.2928751956928721
    blagoyevo
    ru
    The temperature for blagoyevo is: 260.677
    The humidity for blagoyevo is: 63
    The cloudiness for blagoyevo is: 0
    The wind speed for blagoyevo is: 1.15
    The latitude for blagoyevo is: 65.49125226518382
    port macquarie
    au
    The temperature for port macquarie is: 301.15
    The humidity for port macquarie is: 54
    The cloudiness for port macquarie is: 0
    The wind speed for port macquarie is: 1.5
    The latitude for port macquarie is: -32.392155970837145
    mahebourg
    mu
    The temperature for mahebourg is: 300.15
    The humidity for mahebourg is: 83
    The cloudiness for mahebourg is: 40
    The wind speed for mahebourg is: 3.1
    The latitude for mahebourg is: -31.408851515460725
    scarborough
    gb
    The temperature for scarborough is: 277.15
    The humidity for scarborough is: 93
    The cloudiness for scarborough is: 92
    The wind speed for scarborough is: 4.1
    The latitude for scarborough is: 55.195487313496585
    redlands
    us
    The temperature for redlands is: 294.15
    The humidity for redlands is: 42
    The cloudiness for redlands is: 90
    The wind speed for redlands is: 5.1
    The latitude for redlands is: 39.55610073542542
    flic en flac
    mu
    The temperature for flic en flac is: 300.15
    The humidity for flic en flac is: 83
    The cloudiness for flic en flac is: 75
    The wind speed for flic en flac is: 5.1
    The latitude for flic en flac is: -20.072752735925334
    tuktoyaktuk
    ca
    The temperature for tuktoyaktuk is: 261.15
    The humidity for tuktoyaktuk is: 78
    The cloudiness for tuktoyaktuk is: 90
    The wind speed for tuktoyaktuk is: 8.2
    The latitude for tuktoyaktuk is: 81.76322743810385
    cape town
    za
    The temperature for cape town is: 292.15
    The humidity for cape town is: 77
    The cloudiness for cape town is: 0
    The wind speed for cape town is: 4.1
    The latitude for cape town is: -70.45459832373007
    lopandino
    ru
    The temperature for lopandino is: 275.927
    The humidity for lopandino is: 91
    The cloudiness for lopandino is: 80
    The wind speed for lopandino is: 7.65
    The latitude for lopandino is: 52.30203846681269
    ucluelet
    ca
    The temperature for ucluelet is: 279.15
    The humidity for ucluelet is: 70
    The cloudiness for ucluelet is: 20
    The wind speed for ucluelet is: 10.3
    The latitude for ucluelet is: 47.56170013227819
    sawakin
    sd
    The temperature for sawakin is: 293.827
    The humidity for sawakin is: 100
    The cloudiness for sawakin is: 0
    The wind speed for sawakin is: 2.3
    The latitude for sawakin is: 20.220619392282757
    upernavik
    gl
    The temperature for upernavik is: 266.477
    The humidity for upernavik is: 80
    The cloudiness for upernavik is: 68
    The wind speed for upernavik is: 4.4
    The latitude for upernavik is: 88.95569225506262
    kalengwa
    zm
    The temperature for kalengwa is: 291.202
    The humidity for kalengwa is: 90
    The cloudiness for kalengwa is: 12
    The wind speed for kalengwa is: 3.85
    The latitude for kalengwa is: -12.799903865709112
    lebu
    cl
    The temperature for lebu is: 287.727
    The humidity for lebu is: 93
    The cloudiness for lebu is: 0
    The wind speed for lebu is: 7.45
    The latitude for lebu is: -39.24801010541645
    cape town
    za
    The temperature for cape town is: 292.15
    The humidity for cape town is: 77
    The cloudiness for cape town is: 0
    The wind speed for cape town is: 4.1
    The latitude for cape town is: -56.50423405194305
    butaritari
    ki
    The temperature for butaritari is: 301.927
    The humidity for butaritari is: 98
    The cloudiness for butaritari is: 8
    The wind speed for butaritari is: 5.45
    The latitude for butaritari is: 18.34834505114179
    kingston
    us
    The temperature for kingston is: 280.15
    The humidity for kingston is: 30
    The cloudiness for kingston is: 1
    The wind speed for kingston is: 2.1
    The latitude for kingston is: 42.046091307347524
    copiapo
    cl
    The temperature for copiapo is: 287.15
    The humidity for copiapo is: 82
    The cloudiness for copiapo is: 0
    The wind speed for copiapo is: 0.85
    The latitude for copiapo is: -27.00372728162465
    riyadh
    sa
    The temperature for riyadh is: 293.15
    The humidity for riyadh is: 32
    The cloudiness for riyadh is: 75
    The wind speed for riyadh is: 1.5
    The latitude for riyadh is: 21.80784054683008
    new norfolk
    au
    The temperature for new norfolk is: 292.15
    The humidity for new norfolk is: 34
    The cloudiness for new norfolk is: 0
    The wind speed for new norfolk is: 6.2
    The latitude for new norfolk is: -70.60961801061754
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -64.53436850067035
    atuona
    pf
    The temperature for atuona is: 300.827
    The humidity for atuona is: 100
    The cloudiness for atuona is: 32
    The wind speed for atuona is: 6.05
    The latitude for atuona is: -4.122853300746343
    nueva loja
    ec
    The temperature for nueva loja is: 295.827
    The humidity for nueva loja is: 95
    The cloudiness for nueva loja is: 20
    The wind speed for nueva loja is: 0.85
    The latitude for nueva loja is: 0.19090422482068448
    dhari
    in
    The temperature for dhari is: 296.852
    The humidity for dhari is: 64
    The cloudiness for dhari is: 0
    The wind speed for dhari is: 2.6
    The latitude for dhari is: 21.14998889497491
    nikolskoye
    ru
    The temperature for nikolskoye is: 273.15
    The humidity for nikolskoye is: 90
    The cloudiness for nikolskoye is: 90
    The wind speed for nikolskoye is: 7
    The latitude for nikolskoye is: 41.54004954202327
    mar del plata
    ar
    The temperature for mar del plata is: 285.652
    The humidity for mar del plata is: 72
    The cloudiness for mar del plata is: 0
    The wind speed for mar del plata is: 3
    The latitude for mar del plata is: -57.311551506813494
    jamestown
    sh
    The temperature for jamestown is: 296.802
    The humidity for jamestown is: 100
    The cloudiness for jamestown is: 36
    The wind speed for jamestown is: 7
    The latitude for jamestown is: -25.559009590002987
    esperance
    au
    The temperature for esperance is: 294.677
    The humidity for esperance is: 69
    The cloudiness for esperance is: 0
    The wind speed for esperance is: 3.1
    The latitude for esperance is: -28.41548723377091
    flinders
    au
    The temperature for flinders is: 296.15
    The humidity for flinders is: 69
    The cloudiness for flinders is: 44
    The wind speed for flinders is: 3.6
    The latitude for flinders is: -32.5381375994417
    punta arenas
    cl
    The temperature for punta arenas is: 283.15
    The humidity for punta arenas is: 87
    The cloudiness for punta arenas is: 90
    The wind speed for punta arenas is: 3.1
    The latitude for punta arenas is: -63.60563760398879
    hermanus
    za
    The temperature for hermanus is: 285.052
    The humidity for hermanus is: 91
    The cloudiness for hermanus is: 0
    The wind speed for hermanus is: 0.8
    The latitude for hermanus is: -73.90479056243676
    hasaki
    jp
    The temperature for hasaki is: 294.15
    The humidity for hasaki is: 60
    The cloudiness for hasaki is: 0
    The wind speed for hasaki is: 2.6
    The latitude for hasaki is: 27.059281167177787
    makinsk
    kz
    The temperature for makinsk is: 266.552
    The humidity for makinsk is: 90
    The cloudiness for makinsk is: 76
    The wind speed for makinsk is: 5.9
    The latitude for makinsk is: 51.71803381893267
    yulara
    au
    The temperature for yulara is: 307.15
    The humidity for yulara is: 14
    The cloudiness for yulara is: 0
    The wind speed for yulara is: 7.2
    The latitude for yulara is: -29.045564345678883
    port blair
    in
    The temperature for port blair is: 301.352
    The humidity for port blair is: 100
    The cloudiness for port blair is: 20
    The wind speed for port blair is: 4.45
    The latitude for port blair is: 9.920103569630527
    harper
    lr
    The temperature for harper is: 300.652
    The humidity for harper is: 100
    The cloudiness for harper is: 92
    The wind speed for harper is: 4.55
    The latitude for harper is: -2.0019957774663055
    fairbanks
    us
    The temperature for fairbanks is: 274.15
    The humidity for fairbanks is: 40
    The cloudiness for fairbanks is: 75
    The wind speed for fairbanks is: 3.6
    The latitude for fairbanks is: 66.8665183810009
    bluff
    nz
    The temperature for bluff is: 290.602
    The humidity for bluff is: 83
    The cloudiness for bluff is: 48
    The wind speed for bluff is: 7.05
    The latitude for bluff is: -81.59481909453842
    busselton
    au
    The temperature for busselton is: 294.027
    The humidity for busselton is: 95
    The cloudiness for busselton is: 0
    The wind speed for busselton is: 6.5
    The latitude for busselton is: -85.52870566550222
    nkayi
    cg
    The temperature for nkayi is: 297.477
    The humidity for nkayi is: 96
    The cloudiness for nkayi is: 92
    The wind speed for nkayi is: 1.05
    The latitude for nkayi is: -4.247659514276123
    cascavel
    br
    The temperature for cascavel is: 293.15
    The humidity for cascavel is: 94
    The cloudiness for cascavel is: 40
    The wind speed for cascavel is: 1.15
    The latitude for cascavel is: -25.307660455110167
    cape town
    za
    The temperature for cape town is: 292.15
    The humidity for cape town is: 77
    The cloudiness for cape town is: 0
    The wind speed for cape town is: 4.1
    The latitude for cape town is: -54.45322186603101
    atuona
    pf
    The temperature for atuona is: 300.827
    The humidity for atuona is: 100
    The cloudiness for atuona is: 32
    The wind speed for atuona is: 6.05
    The latitude for atuona is: -13.853434721268286
    komsomolskiy
    ru
    The temperature for komsomolskiy is: 248.602
    The humidity for komsomolskiy is: 39
    The cloudiness for komsomolskiy is: 24
    The wind speed for komsomolskiy is: 1.4
    The latitude for komsomolskiy is: 75.2190778133594
    tagusao
    ph
    The temperature for tagusao is: 302.977
    The humidity for tagusao is: 69
    The cloudiness for tagusao is: 8
    The wind speed for tagusao is: 0.7
    The latitude for tagusao is: 12.582532195923477
    makakilo city
    us
    The temperature for makakilo city is: 300.15
    The humidity for makakilo city is: 65
    The cloudiness for makakilo city is: 20
    The wind speed for makakilo city is: 3.1
    The latitude for makakilo city is: 13.82861538966327
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -28.175958263478755
    podgornoye
    ru
    The temperature for podgornoye is: 265.027
    The humidity for podgornoye is: 75
    The cloudiness for podgornoye is: 36
    The wind speed for podgornoye is: 3.1
    The latitude for podgornoye is: 58.03775284941176
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -86.8891219457745
    torbay
    ca
    The temperature for torbay is: 274.15
    The humidity for torbay is: 64
    The cloudiness for torbay is: 90
    The wind speed for torbay is: 8.2
    The latitude for torbay is: 38.04690683126114
    kapaa
    us
    The temperature for kapaa is: 299.15
    The humidity for kapaa is: 83
    The cloudiness for kapaa is: 40
    The wind speed for kapaa is: 3.6
    The latitude for kapaa is: 13.143042402212913
    winfield
    us
    The temperature for winfield is: 274.15
    The humidity for winfield is: 86
    The cloudiness for winfield is: 90
    The wind speed for winfield is: 4.1
    The latitude for winfield is: 37.389721304938234
    luderitz
    na
    The temperature for luderitz is: 288.15
    The humidity for luderitz is: 93
    The cloudiness for luderitz is: 44
    The wind speed for luderitz is: 3.1
    The latitude for luderitz is: -29.949126406976745
    saskylakh
    ru
    The temperature for saskylakh is: 260.552
    The humidity for saskylakh is: 83
    The cloudiness for saskylakh is: 80
    The wind speed for saskylakh is: 3
    The latitude for saskylakh is: 83.3965920872852
    georgetown
    sh
    The temperature for georgetown is: 299.677
    The humidity for georgetown is: 100
    The cloudiness for georgetown is: 12
    The wind speed for georgetown is: 5.25
    The latitude for georgetown is: -10.386923074933009
    hermanus
    za
    The temperature for hermanus is: 285.052
    The humidity for hermanus is: 91
    The cloudiness for hermanus is: 0
    The wind speed for hermanus is: 0.8
    The latitude for hermanus is: -78.42978066273338
    kodiak
    us
    The temperature for kodiak is: 267.15
    The humidity for kodiak is: 92
    The cloudiness for kodiak is: 1
    The wind speed for kodiak is: 2.6
    The latitude for kodiak is: 57.177223158079954
    lompoc
    us
    The temperature for lompoc is: 287.15
    The humidity for lompoc is: 87
    The cloudiness for lompoc is: 20
    The wind speed for lompoc is: 4.6
    The latitude for lompoc is: 30.238899183517944
    cabo san lucas
    mx
    The temperature for cabo san lucas is: 302.15
    The humidity for cabo san lucas is: 21
    The cloudiness for cabo san lucas is: 20
    The wind speed for cabo san lucas is: 4.6
    The latitude for cabo san lucas is: 21.93169947270694
    katsuura
    jp
    The temperature for katsuura is: 292.15
    The humidity for katsuura is: 63
    The cloudiness for katsuura is: 20
    The wind speed for katsuura is: 1.5
    The latitude for katsuura is: 21.578269321902653
    atuona
    pf
    The temperature for atuona is: 300.827
    The humidity for atuona is: 100
    The cloudiness for atuona is: 32
    The wind speed for atuona is: 6.05
    The latitude for atuona is: -11.803654168311539
    kilgore
    us
    The temperature for kilgore is: 295.15
    The humidity for kilgore is: 82
    The cloudiness for kilgore is: 20
    The wind speed for kilgore is: 2.1
    The latitude for kilgore is: 32.48066478208793
    ilebo
    cd
    The temperature for ilebo is: 296.827
    The humidity for ilebo is: 98
    The cloudiness for ilebo is: 36
    The wind speed for ilebo is: 0.9
    The latitude for ilebo is: -4.8901020358455725
    livingstonia
    mw
    The temperature for livingstonia is: 293.077
    The humidity for livingstonia is: 100
    The cloudiness for livingstonia is: 88
    The wind speed for livingstonia is: 0.95
    The latitude for livingstonia is: -10.704759122969946
    atuona
    pf
    The temperature for atuona is: 300.827
    The humidity for atuona is: 100
    The cloudiness for atuona is: 32
    The wind speed for atuona is: 6.05
    The latitude for atuona is: -1.279434615880234
    cherskiy
    ru
    The temperature for cherskiy is: 272.527
    The humidity for cherskiy is: 74
    The cloudiness for cherskiy is: 0
    The wind speed for cherskiy is: 3.55
    The latitude for cherskiy is: 75.19997872624577
    bluff
    nz
    The temperature for bluff is: 290.602
    The humidity for bluff is: 83
    The cloudiness for bluff is: 48
    The wind speed for bluff is: 7.05
    The latitude for bluff is: -68.26574564048803
    tuktoyaktuk
    ca
    The temperature for tuktoyaktuk is: 261.15
    The humidity for tuktoyaktuk is: 78
    The cloudiness for tuktoyaktuk is: 90
    The wind speed for tuktoyaktuk is: 8.2
    The latitude for tuktoyaktuk is: 88.11171793155495
    saldanha
    za
    The temperature for saldanha is: 290.15
    The humidity for saldanha is: 88
    The cloudiness for saldanha is: 88
    The wind speed for saldanha is: 3.1
    The latitude for saldanha is: -33.966242172418795
    avarua
    ck
    The temperature for avarua is: 301.15
    The humidity for avarua is: 78
    The cloudiness for avarua is: 75
    The wind speed for avarua is: 3.6
    The latitude for avarua is: -74.4643565575268
    half moon bay
    us
    The temperature for half moon bay is: 294.15
    The humidity for half moon bay is: 76
    The cloudiness for half moon bay is: 1
    The wind speed for half moon bay is: 5.7
    The latitude for half moon bay is: 33.28508919953319
    katsuura
    jp
    The temperature for katsuura is: 292.15
    The humidity for katsuura is: 63
    The cloudiness for katsuura is: 20
    The wind speed for katsuura is: 1.5
    The latitude for katsuura is: 22.248626324897188
    sao filipe
    cv
    The temperature for sao filipe is: 294.402
    The humidity for sao filipe is: 97
    The cloudiness for sao filipe is: 0
    The wind speed for sao filipe is: 7.15
    The latitude for sao filipe is: 8.07693410006317
    algiers
    dz
    The temperature for algiers is: 289.15
    The humidity for algiers is: 36
    The cloudiness for algiers is: 40
    The wind speed for algiers is: 2.6
    The latitude for algiers is: 37.17204600529065
    tiksi
    ru
    The temperature for tiksi is: 263.402
    The humidity for tiksi is: 83
    The cloudiness for tiksi is: 64
    The wind speed for tiksi is: 1.8
    The latitude for tiksi is: 80.74659110774007
    impfondo
    cg
    The temperature for impfondo is: 294.477
    The humidity for impfondo is: 100
    The cloudiness for impfondo is: 56
    The wind speed for impfondo is: 1.85
    The latitude for impfondo is: 1.093941370631896
    georgetown
    sh
    The temperature for georgetown is: 299.677
    The humidity for georgetown is: 100
    The cloudiness for georgetown is: 12
    The wind speed for georgetown is: 5.25
    The latitude for georgetown is: -7.883069829240597
    banjarmasin
    id
    The temperature for banjarmasin is: 304.402
    The humidity for banjarmasin is: 73
    The cloudiness for banjarmasin is: 24
    The wind speed for banjarmasin is: 4.15
    The latitude for banjarmasin is: -3.4367233932853622
    hirara
    jp
    The temperature for hirara is: 298.15
    The humidity for hirara is: 64
    The cloudiness for hirara is: 20
    The wind speed for hirara is: 2.1
    The latitude for hirara is: 24.357983112845787
    punta arenas
    cl
    The temperature for punta arenas is: 283.15
    The humidity for punta arenas is: 87
    The cloudiness for punta arenas is: 90
    The wind speed for punta arenas is: 3.1
    The latitude for punta arenas is: -88.3599972056126
    aklavik
    ca
    The temperature for aklavik is: 262.15
    The humidity for aklavik is: 72
    The cloudiness for aklavik is: 90
    The wind speed for aklavik is: 5.1
    The latitude for aklavik is: 70.67789572371683
    lourdes
    co
    The temperature for lourdes is: 296.15
    The humidity for lourdes is: 100
    The cloudiness for lourdes is: 75
    The wind speed for lourdes is: 1
    The latitude for lourdes is: 7.994867806429909
    san patricio
    mx
    The temperature for san patricio is: 298.15
    The humidity for san patricio is: 83
    The cloudiness for san patricio is: 5
    The wind speed for san patricio is: 5.1
    The latitude for san patricio is: 15.540357094888947
    acapulco
    mx
    The temperature for acapulco is: 299.15
    The humidity for acapulco is: 88
    The cloudiness for acapulco is: 5
    The wind speed for acapulco is: 4.6
    The latitude for acapulco is: 3.6777329355231387
    hermanus
    za
    The temperature for hermanus is: 285.052
    The humidity for hermanus is: 91
    The cloudiness for hermanus is: 0
    The wind speed for hermanus is: 0.8
    The latitude for hermanus is: -72.55027444855202
    san patricio
    mx
    The temperature for san patricio is: 298.15
    The humidity for san patricio is: 83
    The cloudiness for san patricio is: 5
    The wind speed for san patricio is: 5.1
    The latitude for san patricio is: 6.27282419411911
    bathsheba
    bb
    The temperature for bathsheba is: 298.15
    The humidity for bathsheba is: 78
    The cloudiness for bathsheba is: 20
    The wind speed for bathsheba is: 5.1
    The latitude for bathsheba is: 19.68845534798247
    nantucket
    us
    The temperature for nantucket is: 280.15
    The humidity for nantucket is: 65
    The cloudiness for nantucket is: 1
    The wind speed for nantucket is: 4.1
    The latitude for nantucket is: 41.20444570220786
    bluff
    nz
    The temperature for bluff is: 290.602
    The humidity for bluff is: 83
    The cloudiness for bluff is: 48
    The wind speed for bluff is: 7.05
    The latitude for bluff is: -86.77526200257404
    marystown
    ca
    The temperature for marystown is: 276.677
    The humidity for marystown is: 93
    The cloudiness for marystown is: 92
    The wind speed for marystown is: 11.85
    The latitude for marystown is: 44.96692083114215
    hukuntsi
    bw
    The temperature for hukuntsi is: 289.477
    The humidity for hukuntsi is: 90
    The cloudiness for hukuntsi is: 12
    The wind speed for hukuntsi is: 4.65
    The latitude for hukuntsi is: -24.245274468711244
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -33.314825145289376
    kurilsk
    ru
    The temperature for kurilsk is: 274.702
    The humidity for kurilsk is: 89
    The cloudiness for kurilsk is: 0
    The wind speed for kurilsk is: 3.8
    The latitude for kurilsk is: 44.19454943627437
    castro
    cl
    The temperature for castro is: 280.852
    The humidity for castro is: 97
    The cloudiness for castro is: 0
    The wind speed for castro is: 1.75
    The latitude for castro is: -43.69453392935055
    tiksi
    ru
    The temperature for tiksi is: 263.402
    The humidity for tiksi is: 83
    The cloudiness for tiksi is: 64
    The wind speed for tiksi is: 1.8
    The latitude for tiksi is: 77.18065906521971
    hilo
    us
    The temperature for hilo is: 300.15
    The humidity for hilo is: 65
    The cloudiness for hilo is: 75
    The wind speed for hilo is: 6.7
    The latitude for hilo is: 24.289809768798264
    east london
    za
    The temperature for east london is: 297.352
    The humidity for east london is: 99
    The cloudiness for east london is: 24
    The wind speed for east london is: 10.6
    The latitude for east london is: -51.048707956434946
    luoyang
    cn
    The temperature for luoyang is: 298.277
    The humidity for luoyang is: 54
    The cloudiness for luoyang is: 0
    The wind speed for luoyang is: 1.85
    The latitude for luoyang is: 34.45520440094883
    tiksi
    ru
    The temperature for tiksi is: 263.402
    The humidity for tiksi is: 83
    The cloudiness for tiksi is: 64
    The wind speed for tiksi is: 1.8
    The latitude for tiksi is: 86.68693906714623
    cape town
    za
    The temperature for cape town is: 292.15
    The humidity for cape town is: 77
    The cloudiness for cape town is: 0
    The wind speed for cape town is: 4.1
    The latitude for cape town is: -82.78579518621333
    ushuaia
    ar
    The temperature for ushuaia is: 280.15
    The humidity for ushuaia is: 87
    The cloudiness for ushuaia is: 75
    The wind speed for ushuaia is: 5.7
    The latitude for ushuaia is: -62.0735148175707
    shalinskoye
    ru
    The temperature for shalinskoye is: 267.777
    The humidity for shalinskoye is: 70
    The cloudiness for shalinskoye is: 56
    The wind speed for shalinskoye is: 4.7
    The latitude for shalinskoye is: 55.54733123273866
    ponta do sol
    cv
    The temperature for ponta do sol is: 293.552
    The humidity for ponta do sol is: 100
    The cloudiness for ponta do sol is: 0
    The wind speed for ponta do sol is: 5.85
    The latitude for ponta do sol is: 16.412124275603432
    butaritari
    ki
    The temperature for butaritari is: 301.927
    The humidity for butaritari is: 98
    The cloudiness for butaritari is: 8
    The wind speed for butaritari is: 5.45
    The latitude for butaritari is: 28.966574021278447
    bluff
    nz
    The temperature for bluff is: 290.602
    The humidity for bluff is: 83
    The cloudiness for bluff is: 48
    The wind speed for bluff is: 7.05
    The latitude for bluff is: -69.05948009924481
    kawalu
    id
    The temperature for kawalu is: 298.902
    The humidity for kawalu is: 79
    The cloudiness for kawalu is: 24
    The wind speed for kawalu is: 1.05
    The latitude for kawalu is: -16.97165616245414
    santa fe
    cu
    The temperature for santa fe is: 296.15
    The humidity for santa fe is: 78
    The cloudiness for santa fe is: 40
    The wind speed for santa fe is: 3.1
    The latitude for santa fe is: 21.46527379821137
    leningradskiy
    ru
    The temperature for leningradskiy is: 269.677
    The humidity for leningradskiy is: 92
    The cloudiness for leningradskiy is: 0
    The wind speed for leningradskiy is: 3.1
    The latitude for leningradskiy is: 79.57341491831926
    esperance
    au
    The temperature for esperance is: 294.677
    The humidity for esperance is: 69
    The cloudiness for esperance is: 0
    The wind speed for esperance is: 3.1
    The latitude for esperance is: -40.15363126958131
    suba
    ph
    The temperature for suba is: 302.15
    The humidity for suba is: 74
    The cloudiness for suba is: 20
    The wind speed for suba is: 3.1
    The latitude for suba is: 9.43959714190433
    vanimo
    pg
    The temperature for vanimo is: 299.227
    The humidity for vanimo is: 100
    The cloudiness for vanimo is: 80
    The wind speed for vanimo is: 4.1
    The latitude for vanimo is: -4.277165647247827
    hasaki
    jp
    The temperature for hasaki is: 294.15
    The humidity for hasaki is: 60
    The cloudiness for hasaki is: 0
    The wind speed for hasaki is: 2.6
    The latitude for hasaki is: 31.683924553238796
    hilo
    us
    The temperature for hilo is: 300.15
    The humidity for hilo is: 65
    The cloudiness for hilo is: 75
    The wind speed for hilo is: 6.7
    The latitude for hilo is: 20.520254546000757
    cape town
    za
    The temperature for cape town is: 292.15
    The humidity for cape town is: 77
    The cloudiness for cape town is: 0
    The wind speed for cape town is: 4.1
    The latitude for cape town is: -75.7307729921178
    kapaa
    us
    The temperature for kapaa is: 299.15
    The humidity for kapaa is: 83
    The cloudiness for kapaa is: 40
    The wind speed for kapaa is: 3.6
    The latitude for kapaa is: 35.58016201432751
    saint-philippe
    re
    The temperature for saint-philippe is: 298.15
    The humidity for saint-philippe is: 65
    The cloudiness for saint-philippe is: 0
    The wind speed for saint-philippe is: 3.1
    The latitude for saint-philippe is: -41.02002122103106
    lima
    pe
    The temperature for lima is: 286.852
    The humidity for lima is: 88
    The cloudiness for lima is: 0
    The wind speed for lima is: 0.75
    The latitude for lima is: -18.999320524058675
    hilo
    us
    The temperature for hilo is: 300.15
    The humidity for hilo is: 65
    The cloudiness for hilo is: 75
    The wind speed for hilo is: 6.7
    The latitude for hilo is: 8.02803744580919
    neuquen
    ar
    The temperature for neuquen is: 288.15
    The humidity for neuquen is: 82
    The cloudiness for neuquen is: 0
    The wind speed for neuquen is: 1.25
    The latitude for neuquen is: -41.60165606524143
    qaanaaq
    gl
    The temperature for qaanaaq is: 260.177
    The humidity for qaanaaq is: 85
    The cloudiness for qaanaaq is: 76
    The wind speed for qaanaaq is: 0.75
    The latitude for qaanaaq is: 86.22806797751548
    punta arenas
    cl
    The temperature for punta arenas is: 283.15
    The humidity for punta arenas is: 87
    The cloudiness for punta arenas is: 90
    The wind speed for punta arenas is: 3.1
    The latitude for punta arenas is: -88.2650582221137
    port lincoln
    au
    The temperature for port lincoln is: 291.902
    The humidity for port lincoln is: 86
    The cloudiness for port lincoln is: 56
    The wind speed for port lincoln is: 4.25
    The latitude for port lincoln is: -47.33368389581821
    fortuna
    us
    The temperature for fortuna is: 285.15
    The humidity for fortuna is: 81
    The cloudiness for fortuna is: 1
    The wind speed for fortuna is: 5.1
    The latitude for fortuna is: 37.03937707344278
    husavik
    is
    The temperature for husavik is: 271.15
    The humidity for husavik is: 92
    The cloudiness for husavik is: 90
    The wind speed for husavik is: 2.6
    The latitude for husavik is: 67.78175183397039
    hilo
    us
    The temperature for hilo is: 300.15
    The humidity for hilo is: 65
    The cloudiness for hilo is: 75
    The wind speed for hilo is: 6.7
    The latitude for hilo is: 13.539388272906237
    vaini
    to
    The temperature for vaini is: 299.15
    The humidity for vaini is: 94
    The cloudiness for vaini is: 90
    The wind speed for vaini is: 2.6
    The latitude for vaini is: -37.43287092858975
    hermanus
    za
    The temperature for hermanus is: 285.052
    The humidity for hermanus is: 91
    The cloudiness for hermanus is: 0
    The wind speed for hermanus is: 0.8
    The latitude for hermanus is: -83.82857657279652
    aykhal
    ru
    The temperature for aykhal is: 255.802
    The humidity for aykhal is: 59
    The cloudiness for aykhal is: 32
    The wind speed for aykhal is: 4.7
    The latitude for aykhal is: 64.76850915759724
    tiksi
    ru
    The temperature for tiksi is: 263.402
    The humidity for tiksi is: 83
    The cloudiness for tiksi is: 64
    The wind speed for tiksi is: 1.8
    The latitude for tiksi is: 76.38863604514086
    ushuaia
    ar
    The temperature for ushuaia is: 280.15
    The humidity for ushuaia is: 87
    The cloudiness for ushuaia is: 75
    The wind speed for ushuaia is: 5.7
    The latitude for ushuaia is: -82.50040140131428
    homagama
    lk
    The temperature for homagama is: 301.927
    The humidity for homagama is: 95
    The cloudiness for homagama is: 56
    The wind speed for homagama is: 0.15
    The latitude for homagama is: 6.903080904865391
    bluff
    nz
    The temperature for bluff is: 290.602
    The humidity for bluff is: 83
    The cloudiness for bluff is: 48
    The wind speed for bluff is: 7.05
    The latitude for bluff is: -63.6901165075551
    kamakwie
    sl
    The temperature for kamakwie is: 294.527
    The humidity for kamakwie is: 95
    The cloudiness for kamakwie is: 0
    The wind speed for kamakwie is: 0.75
    The latitude for kamakwie is: 9.383620897686498
    saint george
    bm
    The temperature for saint george is: 293.15
    The humidity for saint george is: 88
    The cloudiness for saint george is: 75
    The wind speed for saint george is: 1
    The latitude for saint george is: 31.681076426476807
    puerto ayora
    ec
    The temperature for puerto ayora is: 298.327
    The humidity for puerto ayora is: 97
    The cloudiness for puerto ayora is: 36
    The wind speed for puerto ayora is: 3.4
    The latitude for puerto ayora is: 1.2994702396075724
    puerto ayora
    ec
    The temperature for puerto ayora is: 298.327
    The humidity for puerto ayora is: 97
    The cloudiness for puerto ayora is: 36
    The wind speed for puerto ayora is: 3.4
    The latitude for puerto ayora is: -17.231407961282216
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -40.000880216823106
    busselton
    au
    The temperature for busselton is: 294.027
    The humidity for busselton is: 95
    The cloudiness for busselton is: 0
    The wind speed for busselton is: 6.5
    The latitude for busselton is: -81.38521952745907
    ushuaia
    ar
    The temperature for ushuaia is: 280.15
    The humidity for ushuaia is: 87
    The cloudiness for ushuaia is: 75
    The wind speed for ushuaia is: 5.7
    The latitude for ushuaia is: -80.79186816236911
    torbay
    ca
    The temperature for torbay is: 274.15
    The humidity for torbay is: 64
    The cloudiness for torbay is: 90
    The wind speed for torbay is: 8.2
    The latitude for torbay is: 47.895147448757854
    lebu
    cl
    The temperature for lebu is: 287.727
    The humidity for lebu is: 93
    The cloudiness for lebu is: 0
    The wind speed for lebu is: 7.45
    The latitude for lebu is: -37.30415432351601
    manggar
    id
    The temperature for manggar is: 303.077
    The humidity for manggar is: 91
    The cloudiness for manggar is: 32
    The wind speed for manggar is: 3.15
    The latitude for manggar is: -3.054349865791437
    cape town
    za
    The temperature for cape town is: 292.15
    The humidity for cape town is: 77
    The cloudiness for cape town is: 0
    The wind speed for cape town is: 4.1
    The latitude for cape town is: -73.33292934062158
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -24.247390703984564
    ponta do sol
    cv
    The temperature for ponta do sol is: 293.552
    The humidity for ponta do sol is: 100
    The cloudiness for ponta do sol is: 0
    The wind speed for ponta do sol is: 5.85
    The latitude for ponta do sol is: 19.965249313501857
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -37.98357988729925
    hobart
    au
    The temperature for hobart is: 292.15
    The humidity for hobart is: 34
    The cloudiness for hobart is: 0
    The wind speed for hobart is: 6.2
    The latitude for hobart is: -46.2845588335867
    sovetskiy
    ru
    The temperature for sovetskiy is: 268.027
    The humidity for sovetskiy is: 86
    The cloudiness for sovetskiy is: 64
    The wind speed for sovetskiy is: 3.75
    The latitude for sovetskiy is: 73.3033956620703
    thunder bay
    ca
    The temperature for thunder bay is: 271.15
    The humidity for thunder bay is: 46
    The cloudiness for thunder bay is: 90
    The wind speed for thunder bay is: 5.7
    The latitude for thunder bay is: 48.138182182823385
    kutum
    sd
    The temperature for kutum is: 287.452
    The humidity for kutum is: 18
    The cloudiness for kutum is: 0
    The wind speed for kutum is: 4.35
    The latitude for kutum is: 14.161656336860148
    tuktoyaktuk
    ca
    The temperature for tuktoyaktuk is: 261.15
    The humidity for tuktoyaktuk is: 78
    The cloudiness for tuktoyaktuk is: 90
    The wind speed for tuktoyaktuk is: 8.2
    The latitude for tuktoyaktuk is: 82.09960764735803
    busselton
    au
    The temperature for busselton is: 294.027
    The humidity for busselton is: 95
    The cloudiness for busselton is: 0
    The wind speed for busselton is: 6.5
    The latitude for busselton is: -60.76343035030694
    jauja
    pe
    The temperature for jauja is: 276.827
    The humidity for jauja is: 100
    The cloudiness for jauja is: 92
    The wind speed for jauja is: 1.25
    The latitude for jauja is: -12.106391358948727
    hobart
    au
    The temperature for hobart is: 292.15
    The humidity for hobart is: 34
    The cloudiness for hobart is: 0
    The wind speed for hobart is: 6.2
    The latitude for hobart is: -53.162409436843205
    mar del plata
    ar
    The temperature for mar del plata is: 285.652
    The humidity for mar del plata is: 72
    The cloudiness for mar del plata is: 0
    The wind speed for mar del plata is: 3
    The latitude for mar del plata is: -60.78425057657294
    bluff
    nz
    The temperature for bluff is: 290.602
    The humidity for bluff is: 83
    The cloudiness for bluff is: 48
    The wind speed for bluff is: 7.05
    The latitude for bluff is: -80.64984184033833
    georgetown
    sh
    The temperature for georgetown is: 299.677
    The humidity for georgetown is: 100
    The cloudiness for georgetown is: 12
    The wind speed for georgetown is: 5.25
    The latitude for georgetown is: -9.310821507864972
    san carlos de bariloche
    ar
    The temperature for san carlos de bariloche is: 284.15
    The humidity for san carlos de bariloche is: 50
    The cloudiness for san carlos de bariloche is: 0
    The wind speed for san carlos de bariloche is: 2.6
    The latitude for san carlos de bariloche is: -39.76310005681336
    aconibe
    gq
    The temperature for aconibe is: 293.702
    The humidity for aconibe is: 99
    The cloudiness for aconibe is: 80
    The wind speed for aconibe is: 0.9
    The latitude for aconibe is: 1.1975740032615363
    hermanus
    za
    The temperature for hermanus is: 285.052
    The humidity for hermanus is: 91
    The cloudiness for hermanus is: 0
    The wind speed for hermanus is: 0.8
    The latitude for hermanus is: -81.80366931464293
    lerwick
    gb
    The temperature for lerwick is: 272.15
    The humidity for lerwick is: 86
    The cloudiness for lerwick is: 0
    The wind speed for lerwick is: 2.6
    The latitude for lerwick is: 61.00896179751507
    north bend
    us
    The temperature for north bend is: 282.15
    The humidity for north bend is: 93
    The cloudiness for north bend is: 90
    The wind speed for north bend is: 3.1
    The latitude for north bend is: 44.149529924411866
    new norfolk
    au
    The temperature for new norfolk is: 292.15
    The humidity for new norfolk is: 34
    The cloudiness for new norfolk is: 0
    The wind speed for new norfolk is: 6.2
    The latitude for new norfolk is: -63.53135027613152
    naryan-mar
    ru
    The temperature for naryan-mar is: 254.052
    The humidity for naryan-mar is: 61
    The cloudiness for naryan-mar is: 24
    The wind speed for naryan-mar is: 1.55
    The latitude for naryan-mar is: 68.07299432681441
    severo-kurilsk
    ru
    The temperature for severo-kurilsk is: 271.577
    The humidity for severo-kurilsk is: 100
    The cloudiness for severo-kurilsk is: 64
    The wind speed for severo-kurilsk is: 2.5
    The latitude for severo-kurilsk is: 48.969216810617695
    ushuaia
    ar
    The temperature for ushuaia is: 280.15
    The humidity for ushuaia is: 87
    The cloudiness for ushuaia is: 75
    The wind speed for ushuaia is: 5.7
    The latitude for ushuaia is: -60.671295633704624
    vao
    nc
    The temperature for vao is: 299.277
    The humidity for vao is: 98
    The cloudiness for vao is: 92
    The wind speed for vao is: 8.2
    The latitude for vao is: -28.01071873098104
    yellowknife
    ca
    The temperature for yellowknife is: 260.15
    The humidity for yellowknife is: 50
    The cloudiness for yellowknife is: 20
    The wind speed for yellowknife is: 3.1
    The latitude for yellowknife is: 65.98682773978135
    bredasdorp
    za
    The temperature for bredasdorp is: 289.15
    The humidity for bredasdorp is: 87
    The cloudiness for bredasdorp is: 68
    The wind speed for bredasdorp is: 1.5
    The latitude for bredasdorp is: -65.28006708229603
    punta arenas
    cl
    The temperature for punta arenas is: 283.15
    The humidity for punta arenas is: 87
    The cloudiness for punta arenas is: 90
    The wind speed for punta arenas is: 3.1
    The latitude for punta arenas is: -82.23975609886703
    hachinohe
    jp
    The temperature for hachinohe is: 282.527
    The humidity for hachinohe is: 89
    The cloudiness for hachinohe is: 32
    The wind speed for hachinohe is: 1.6
    The latitude for hachinohe is: 40.43832505373675
    kieta
    pg
    The temperature for kieta is: 302.202
    The humidity for kieta is: 91
    The cloudiness for kieta is: 44
    The wind speed for kieta is: 4.75
    The latitude for kieta is: -0.34751241171348113
    amuntai
    id
    The temperature for amuntai is: 301.577
    The humidity for amuntai is: 90
    The cloudiness for amuntai is: 68
    The wind speed for amuntai is: 1.15
    The latitude for amuntai is: -1.8914688859874218
    cayenne
    gf
    The temperature for cayenne is: 297.15
    The humidity for cayenne is: 100
    The cloudiness for cayenne is: 100
    The wind speed for cayenne is: 2.65
    The latitude for cayenne is: 13.246295078423884
    kapaa
    us
    The temperature for kapaa is: 299.15
    The humidity for kapaa is: 83
    The cloudiness for kapaa is: 40
    The wind speed for kapaa is: 3.6
    The latitude for kapaa is: 34.135648252152535
    severo-kurilsk
    ru
    The temperature for severo-kurilsk is: 271.577
    The humidity for severo-kurilsk is: 100
    The cloudiness for severo-kurilsk is: 64
    The wind speed for severo-kurilsk is: 2.5
    The latitude for severo-kurilsk is: 47.382039622326175
    hobart
    au
    The temperature for hobart is: 292.15
    The humidity for hobart is: 34
    The cloudiness for hobart is: 0
    The wind speed for hobart is: 6.2
    The latitude for hobart is: -81.27483970734512
    san luis
    ar
    The temperature for san luis is: 291.477
    The humidity for san luis is: 81
    The cloudiness for san luis is: 68
    The wind speed for san luis is: 4.55
    The latitude for san luis is: -32.95606598551521
    nemuro
    jp
    The temperature for nemuro is: 277.15
    The humidity for nemuro is: 80
    The cloudiness for nemuro is: 75
    The wind speed for nemuro is: 4.6
    The latitude for nemuro is: 37.864709363283566
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -18.039495569076763
    pointe michel
    dm
    The temperature for pointe michel is: 298.902
    The humidity for pointe michel is: 97
    The cloudiness for pointe michel is: 100
    The wind speed for pointe michel is: 6.6
    The latitude for pointe michel is: 14.765566994411643
    ko samui
    th
    The temperature for ko samui is: 302.15
    The humidity for ko samui is: 79
    The cloudiness for ko samui is: 20
    The wind speed for ko samui is: 2.1
    The latitude for ko samui is: 9.92593649275571
    beringovskiy
    ru
    The temperature for beringovskiy is: 273.302
    The humidity for beringovskiy is: 95
    The cloudiness for beringovskiy is: 0
    The wind speed for beringovskiy is: 4.2
    The latitude for beringovskiy is: 49.65214898825616
    miyako
    jp
    The temperature for miyako is: 296.15
    The humidity for miyako is: 77
    The cloudiness for miyako is: 20
    The wind speed for miyako is: 2.1
    The latitude for miyako is: 40.09234227556365
    ribeira grande
    pt
    The temperature for ribeira grande is: 290.077
    The humidity for ribeira grande is: 98
    The cloudiness for ribeira grande is: 92
    The wind speed for ribeira grande is: 7.4
    The latitude for ribeira grande is: 31.60438482930759
    ribas do rio pardo
    br
    The temperature for ribas do rio pardo is: 293.052
    The humidity for ribas do rio pardo is: 95
    The cloudiness for ribas do rio pardo is: 76
    The wind speed for ribas do rio pardo is: 0.95
    The latitude for ribas do rio pardo is: -21.063213515905076
    butaritari
    ki
    The temperature for butaritari is: 301.927
    The humidity for butaritari is: 98
    The cloudiness for butaritari is: 8
    The wind speed for butaritari is: 5.45
    The latitude for butaritari is: 15.702116125646512
    albany
    au
    The temperature for albany is: 293.477
    The humidity for albany is: 74
    The cloudiness for albany is: 0
    The wind speed for albany is: 5.05
    The latitude for albany is: -54.28162945795874
    mar del plata
    ar
    The temperature for mar del plata is: 285.652
    The humidity for mar del plata is: 72
    The cloudiness for mar del plata is: 0
    The wind speed for mar del plata is: 3
    The latitude for mar del plata is: -70.7955681170937
    bredasdorp
    za
    The temperature for bredasdorp is: 289.15
    The humidity for bredasdorp is: 87
    The cloudiness for bredasdorp is: 68
    The wind speed for bredasdorp is: 1.5
    The latitude for bredasdorp is: -86.8416207841493
    oktyabrskiy
    ru
    The temperature for oktyabrskiy is: 275.15
    The humidity for oktyabrskiy is: 93
    The cloudiness for oktyabrskiy is: 90
    The wind speed for oktyabrskiy is: 7
    The latitude for oktyabrskiy is: 60.90989400528886
    rikitea
    pf
    The temperature for rikitea is: 299.477
    The humidity for rikitea is: 100
    The cloudiness for rikitea is: 0
    The wind speed for rikitea is: 3
    The latitude for rikitea is: -57.44528434439828
    verkhoyansk
    ru
    The temperature for verkhoyansk is: 268.477
    The humidity for verkhoyansk is: 73
    The cloudiness for verkhoyansk is: 8
    The wind speed for verkhoyansk is: 2.1
    The latitude for verkhoyansk is: 66.60868542832702
    kodiak
    us
    The temperature for kodiak is: 267.15
    The humidity for kodiak is: 92
    The cloudiness for kodiak is: 1
    The wind speed for kodiak is: 2.6
    The latitude for kodiak is: 51.50761091228449
    wadi maliz
    tn
    The temperature for wadi maliz is: 280.15
    The humidity for wadi maliz is: 93
    The cloudiness for wadi maliz is: 12
    The wind speed for wadi maliz is: 1.05
    The latitude for wadi maliz is: 36.46953611553661
    new norfolk
    au
    The temperature for new norfolk is: 292.15
    The humidity for new norfolk is: 34
    The cloudiness for new norfolk is: 0
    The wind speed for new norfolk is: 6.2
    The latitude for new norfolk is: -82.10344582458745
    atuona
    pf
    The temperature for atuona is: 300.827
    The humidity for atuona is: 100
    The cloudiness for atuona is: 32
    The wind speed for atuona is: 6.05
    The latitude for atuona is: -9.182039203136796
    busselton
    au
    The temperature for busselton is: 294.027
    The humidity for busselton is: 95
    The cloudiness for busselton is: 0
    The wind speed for busselton is: 6.5
    The latitude for busselton is: -71.31032852588248
    puerto ayora
    ec
    The temperature for puerto ayora is: 298.327
    The humidity for puerto ayora is: 97
    The cloudiness for puerto ayora is: 36
    The wind speed for puerto ayora is: 3.4
    The latitude for puerto ayora is: -12.851505519832088
    punta arenas
    cl
    The temperature for punta arenas is: 283.15
    The humidity for punta arenas is: 87
    The cloudiness for punta arenas is: 90
    The wind speed for punta arenas is: 3.1
    The latitude for punta arenas is: -89.92155226345764
    kruisfontein
    za
    The temperature for kruisfontein is: 291.227
    The humidity for kruisfontein is: 91
    The cloudiness for kruisfontein is: 12
    The wind speed for kruisfontein is: 2.2
    The latitude for kruisfontein is: -55.47208081944513
    ushuaia
    ar
    The temperature for ushuaia is: 280.15
    The humidity for ushuaia is: 87
    The cloudiness for ushuaia is: 75
    The wind speed for ushuaia is: 5.7
    The latitude for ushuaia is: -77.46172438304981
    bluff
    nz
    The temperature for bluff is: 290.602
    The humidity for bluff is: 83
    The cloudiness for bluff is: 48
    The wind speed for bluff is: 7.05
    The latitude for bluff is: -80.7339789604586
    vaini
    to
    The temperature for vaini is: 299.15
    The humidity for vaini is: 94
    The cloudiness for vaini is: 90
    The wind speed for vaini is: 2.6
    The latitude for vaini is: -78.46311523160816
    hermanus
    za
    The temperature for hermanus is: 285.052
    The humidity for hermanus is: 91
    The cloudiness for hermanus is: 0
    The wind speed for hermanus is: 0.8
    The latitude for hermanus is: -50.175244282943424
    port alfred
    za
    The temperature for port alfred is: 295.327
    The humidity for port alfred is: 89
    The cloudiness for port alfred is: 44
    The wind speed for port alfred is: 6.4
    The latitude for port alfred is: -69.16891019235106
    bluff
    nz
    The temperature for bluff is: 290.602
    The humidity for bluff is: 83
    The cloudiness for bluff is: 48
    The wind speed for bluff is: 7.05
    The latitude for bluff is: -80.01370678377978
    nikolskoye
    ru
    The temperature for nikolskoye is: 273.15
    The humidity for nikolskoye is: 90
    The cloudiness for nikolskoye is: 90
    The wind speed for nikolskoye is: 7
    The latitude for nikolskoye is: 42.801630264341355
    arraial do cabo
    br
    The temperature for arraial do cabo is: 298.652
    The humidity for arraial do cabo is: 84
    The cloudiness for arraial do cabo is: 48
    The wind speed for arraial do cabo is: 8.95
    The latitude for arraial do cabo is: -31.142925990416742
    dikson
    ru
    The temperature for dikson is: 258.677
    The humidity for dikson is: 82
    The cloudiness for dikson is: 48
    The wind speed for dikson is: 5.2
    The latitude for dikson is: 83.76341865829275
    orbetello
    it
    The temperature for orbetello is: 277.15
    The humidity for orbetello is: 86
    The cloudiness for orbetello is: 0
    The wind speed for orbetello is: 1.5
    The latitude for orbetello is: 41.759765292860834
    vanderhoof
    ca
    The temperature for vanderhoof is: 268.402
    The humidity for vanderhoof is: 45
    The cloudiness for vanderhoof is: 36
    The wind speed for vanderhoof is: 2.8
    The latitude for vanderhoof is: 53.034505169975176
    aklavik
    ca
    The temperature for aklavik is: 262.15
    The humidity for aklavik is: 72
    The cloudiness for aklavik is: 90
    The wind speed for aklavik is: 5.1
    The latitude for aklavik is: 75.66255922131822
    presidencia roque saenz pena
    ar
    The temperature for presidencia roque saenz pena is: 293.302
    The humidity for presidencia roque saenz pena is: 92
    The cloudiness for presidencia roque saenz pena is: 8
    The wind speed for presidencia roque saenz pena is: 2.05
    The latitude for presidencia roque saenz pena is: -25.24695739639806
    lubbock
    us
    The temperature for lubbock is: 280.15
    The humidity for lubbock is: 56
    The cloudiness for lubbock is: 75
    The wind speed for lubbock is: 7.7
    The latitude for lubbock is: 33.72278240115293
    kijang
    id
    The temperature for kijang is: 303.202
    The humidity for kijang is: 79
    The cloudiness for kijang is: 0
    The wind speed for kijang is: 5.15
    The latitude for kijang is: -0.34992521631154716
    new norfolk
    au
    The temperature for new norfolk is: 292.15
    The humidity for new norfolk is: 34
    The cloudiness for new norfolk is: 0
    The wind speed for new norfolk is: 6.2
    The latitude for new norfolk is: -60.509987742061504
    gubkinskiy
    ru
    The temperature for gubkinskiy is: 261.527
    The humidity for gubkinskiy is: 85
    The cloudiness for gubkinskiy is: 68
    The wind speed for gubkinskiy is: 3.3
    The latitude for gubkinskiy is: 63.59689726481244
    port alfred
    za
    The temperature for port alfred is: 295.327
    The humidity for port alfred is: 89
    The cloudiness for port alfred is: 44
    The wind speed for port alfred is: 6.4
    The latitude for port alfred is: -83.47995376931169
    atuona
    pf
    The temperature for atuona is: 300.827
    The humidity for atuona is: 100
    The cloudiness for atuona is: 32
    The wind speed for atuona is: 6.05
    The latitude for atuona is: -5.50328865944897
    liverpool
    ca
    The temperature for liverpool is: 278.302
    The humidity for liverpool is: 83
    The cloudiness for liverpool is: 36
    The wind speed for liverpool is: 6.1
    The latitude for liverpool is: 39.428663935277655
    bindura
    zw
    The temperature for bindura is: 283.277
    The humidity for bindura is: 88
    The cloudiness for bindura is: 0
    The wind speed for bindura is: 1
    The latitude for bindura is: -17.599304269190313
    avarua
    ck
    The temperature for avarua is: 301.15
    The humidity for avarua is: 78
    The cloudiness for avarua is: 75
    The wind speed for avarua is: 3.6
    The latitude for avarua is: -58.50003422998678
    tasiilaq
    gl
    The temperature for tasiilaq is: 268.15
    The humidity for tasiilaq is: 62
    The cloudiness for tasiilaq is: 76
    The wind speed for tasiilaq is: 7.2
    The latitude for tasiilaq is: 61.1134017919579
    manzanillo
    mx
    The temperature for manzanillo is: 298.15
    The humidity for manzanillo is: 83
    The cloudiness for manzanillo is: 5
    The wind speed for manzanillo is: 5.1
    The latitude for manzanillo is: 15.023637989479738
    skjervoy
    no
    The temperature for skjervoy is: 270.477
    The humidity for skjervoy is: 100
    The cloudiness for skjervoy is: 32
    The wind speed for skjervoy is: 5.45
    The latitude for skjervoy is: 70.9138073256949
    longkou
    cn
    The temperature for longkou is: 290.977
    The humidity for longkou is: 52
    The cloudiness for longkou is: 0
    The wind speed for longkou is: 6.15
    The latitude for longkou is: 38.230870559101646
    simao
    cn
    The temperature for simao is: 297.952
    The humidity for simao is: 57
    The cloudiness for simao is: 0
    The wind speed for simao is: 1.25
    The latitude for simao is: 23.430896241546748
    ilulissat
    gl
    The temperature for ilulissat is: 272.15
    The humidity for ilulissat is: 50
    The cloudiness for ilulissat is: 0
    The wind speed for ilulissat is: 8.2
    The latitude for ilulissat is: 85.69381207075105
    cape town
    za
    The temperature for cape town is: 292.15
    The humidity for cape town is: 77
    The cloudiness for cape town is: 0
    The wind speed for cape town is: 4.1
    The latitude for cape town is: -71.65786636606902
    biloxi
    us
    The temperature for biloxi is: 292.15
    The humidity for biloxi is: 93
    The cloudiness for biloxi is: 1
    The wind speed for biloxi is: 2.2
    The latitude for biloxi is: 29.338217936670063
    arraial do cabo
    br
    The temperature for arraial do cabo is: 298.652
    The humidity for arraial do cabo is: 84
    The cloudiness for arraial do cabo is: 48
    The wind speed for arraial do cabo is: 8.95
    The latitude for arraial do cabo is: -39.86551964426511
    busselton
    au
    The temperature for busselton is: 294.027
    The humidity for busselton is: 95
    The cloudiness for busselton is: 0
    The wind speed for busselton is: 6.5
    The latitude for busselton is: -55.53894804580867
    hermanus
    za
    The temperature for hermanus is: 285.052
    The humidity for hermanus is: 91
    The cloudiness for hermanus is: 0
    The wind speed for hermanus is: 0.8
    The latitude for hermanus is: -41.29413732094162
    tuktoyaktuk
    ca
    The temperature for tuktoyaktuk is: 261.15
    The humidity for tuktoyaktuk is: 78
    The cloudiness for tuktoyaktuk is: 90
    The wind speed for tuktoyaktuk is: 8.2
    The latitude for tuktoyaktuk is: 80.35891461001424
    orlik
    ru
    The temperature for orlik is: 256.477
    The humidity for orlik is: 47
    The cloudiness for orlik is: 36
    The wind speed for orlik is: 1.4
    The latitude for orlik is: 51.408741807728745
    bilibino
    ru
    The temperature for bilibino is: 275.402
    The humidity for bilibino is: 71
    The cloudiness for bilibino is: 8
    The wind speed for bilibino is: 2.5
    The latitude for bilibino is: 72.0217493814637
    san andres
    co
    The temperature for san andres is: 297.777
    The humidity for san andres is: 100
    The cloudiness for san andres is: 92
    The wind speed for san andres is: 4
    The latitude for san andres is: 13.66197467863877
    acapulco
    mx
    The temperature for acapulco is: 299.15
    The humidity for acapulco is: 88
    The cloudiness for acapulco is: 5
    The wind speed for acapulco is: 4.6
    The latitude for acapulco is: 6.442252527483959
    puerto ayora
    ec
    The temperature for puerto ayora is: 298.327
    The humidity for puerto ayora is: 97
    The cloudiness for puerto ayora is: 36
    The wind speed for puerto ayora is: 3.4
    The latitude for puerto ayora is: -12.486049319291709
    albany
    au
    The temperature for albany is: 293.477
    The humidity for albany is: 74
    The cloudiness for albany is: 0
    The wind speed for albany is: 5.05
    The latitude for albany is: -87.64879950819567
    hobart
    au
    The temperature for hobart is: 292.15
    The humidity for hobart is: 34
    The cloudiness for hobart is: 0
    The wind speed for hobart is: 6.2
    The latitude for hobart is: -60.539977434390224
    kapaa
    us
    The temperature for kapaa is: 299.15
    The humidity for kapaa is: 83
    The cloudiness for kapaa is: 40
    The wind speed for kapaa is: 3.6
    The latitude for kapaa is: 40.00076552592225
    dikson
    ru
    The temperature for dikson is: 258.677
    The humidity for dikson is: 82
    The cloudiness for dikson is: 48
    The wind speed for dikson is: 5.2
    The latitude for dikson is: 71.81607637980937
    torbay
    ca
    The temperature for torbay is: 274.15
    The humidity for torbay is: 64
    The cloudiness for torbay is: 90
    The wind speed for torbay is: 8.2
    The latitude for torbay is: 41.36539364911019
    hermanus
    za
    The temperature for hermanus is: 285.052
    The humidity for hermanus is: 91
    The cloudiness for hermanus is: 0
    The wind speed for hermanus is: 0.8
    The latitude for hermanus is: -84.78300904375492
    aboyne
    gb
    The temperature for aboyne is: 273.15
    The humidity for aboyne is: 76
    The cloudiness for aboyne is: 40
    The wind speed for aboyne is: 1
    The latitude for aboyne is: 57.11631311629296
    new norfolk
    au
    The temperature for new norfolk is: 292.15
    The humidity for new norfolk is: 34
    The cloudiness for new norfolk is: 0
    The wind speed for new norfolk is: 6.2
    The latitude for new norfolk is: -65.27466589147978
    talnakh
    ru
    The temperature for talnakh is: 250.502
    The humidity for talnakh is: 80
    The cloudiness for talnakh is: 48
    The wind speed for talnakh is: 6.7
    The latitude for talnakh is: 75.92583128120484
    yar-sale
    ru
    The temperature for yar-sale is: 248.927
    The humidity for yar-sale is: 76
    The cloudiness for yar-sale is: 0
    The wind speed for yar-sale is: 4.35
    The latitude for yar-sale is: 69.16702938610547
    kodiak
    us
    The temperature for kodiak is: 267.15
    The humidity for kodiak is: 92
    The cloudiness for kodiak is: 1
    The wind speed for kodiak is: 2.6
    The latitude for kodiak is: 43.39284795741642
    ahipara
    nz
    The temperature for ahipara is: 295.202
    The humidity for ahipara is: 68
    The cloudiness for ahipara is: 0
    The wind speed for ahipara is: 3.3
    The latitude for ahipara is: -35.806127009015725
    channarayapatna
    in
    The temperature for channarayapatna is: 296.15
    The humidity for channarayapatna is: 100
    The cloudiness for channarayapatna is: 20
    The wind speed for channarayapatna is: 2.6
    The latitude for channarayapatna is: 12.939671640516224
    la reforma
    mx
    The temperature for la reforma is: 298.15
    The humidity for la reforma is: 38
    The cloudiness for la reforma is: 75
    The wind speed for la reforma is: 1.1
    The latitude for la reforma is: 24.104880501870426
    mayor pablo lagerenza
    py
    The temperature for mayor pablo lagerenza is: 296.527
    The humidity for mayor pablo lagerenza is: 90
    The cloudiness for mayor pablo lagerenza is: 64
    The wind speed for mayor pablo lagerenza is: 1.15
    The latitude for mayor pablo lagerenza is: -19.092284663483525
    singaraja
    id
    The temperature for singaraja is: 300.902
    The humidity for singaraja is: 83
    The cloudiness for singaraja is: 56
    The wind speed for singaraja is: 0.95
    The latitude for singaraja is: -7.575938783284371
    nikolskoye
    ru
    The temperature for nikolskoye is: 273.15
    The humidity for nikolskoye is: 90
    The cloudiness for nikolskoye is: 90
    The wind speed for nikolskoye is: 7
    The latitude for nikolskoye is: 34.985471378037204
    vung tau
    vn
    The temperature for vung tau is: 301.15
    The humidity for vung tau is: 74
    The cloudiness for vung tau is: 40
    The wind speed for vung tau is: 2.6
    The latitude for vung tau is: 9.16487949629601
    kodiak
    us
    The temperature for kodiak is: 267.15
    The humidity for kodiak is: 92
    The cloudiness for kodiak is: 1
    The wind speed for kodiak is: 2.6
    The latitude for kodiak is: 54.339779509957566
    cayenne
    gf
    The temperature for cayenne is: 297.15
    The humidity for cayenne is: 100
    The cloudiness for cayenne is: 100
    The wind speed for cayenne is: 2.65
    The latitude for cayenne is: 13.668642466985432
    vaini
    to
    The temperature for vaini is: 299.15
    The humidity for vaini is: 94
    The cloudiness for vaini is: 90
    The wind speed for vaini is: 2.6
    The latitude for vaini is: -29.8677128400672
    busselton
    au
    The temperature for busselton is: 294.027
    The humidity for busselton is: 95
    The cloudiness for busselton is: 0
    The wind speed for busselton is: 6.5
    The latitude for busselton is: -79.94346775111562
    santa helena de goias
    br
    The temperature for santa helena de goias is: 294.852
    The humidity for santa helena de goias is: 88
    The cloudiness for santa helena de goias is: 68
    The wind speed for santa helena de goias is: 3.5
    The latitude for santa helena de goias is: -18.08545257618171
    korla
    cn
    The temperature for korla is: 279.802
    The humidity for korla is: 89
    The cloudiness for korla is: 92
    The wind speed for korla is: 3.35
    The latitude for korla is: 40.30070622125831
    manoel urbano
    br
    The temperature for manoel urbano is: 296.577
    The humidity for manoel urbano is: 97
    The cloudiness for manoel urbano is: 20
    The wind speed for manoel urbano is: 0.95
    The latitude for manoel urbano is: -8.792031308761082
    


```python
dictionary = {
    "City": city_list,
    "Country": country_list,
    "Max Temperature": temp_list,
    "Humidity": humidity_list,
    "Cloudiness": cloudiness_list,
    "Wind Speed": wind_speed_list,
    "Latitude": latitude_list,
    "Longitude": longitude_list,
    "Date": date_list
}
dictionary_df = pd.DataFrame(data=dictionary)
dictionary_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Cloudiness</th>
      <th>Country</th>
      <th>Date</th>
      <th>Humidity</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Max Temperature</th>
      <th>Wind Speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>vanimo</td>
      <td>80</td>
      <td>pg</td>
      <td>1522636296</td>
      <td>100</td>
      <td>-2.337526</td>
      <td>140.954631</td>
      <td>299.227</td>
      <td>4.10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>san cristobal</td>
      <td>92</td>
      <td>ec</td>
      <td>1522636296</td>
      <td>100</td>
      <td>-12.735963</td>
      <td>-92.462291</td>
      <td>288.852</td>
      <td>1.05</td>
    </tr>
    <tr>
      <th>2</th>
      <td>hailar</td>
      <td>0</td>
      <td>cn</td>
      <td>1522636305</td>
      <td>39</td>
      <td>47.510818</td>
      <td>120.209729</td>
      <td>272.602</td>
      <td>8.90</td>
    </tr>
    <tr>
      <th>3</th>
      <td>rikitea</td>
      <td>0</td>
      <td>pf</td>
      <td>1522635430</td>
      <td>100</td>
      <td>-63.234742</td>
      <td>-125.602406</td>
      <td>299.477</td>
      <td>3.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ribeira grande</td>
      <td>92</td>
      <td>pt</td>
      <td>1522635427</td>
      <td>98</td>
      <td>40.235913</td>
      <td>-40.561389</td>
      <td>290.077</td>
      <td>7.40</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.scatter(temp_list, latitude_list, facecolors="blue", edgecolors="black", linewidth=1, marker='o', alpha=0.8)
plt.title('City Latitude vs. Max Temperature')
plt.xlabel("Latitude")
plt.ylabel('Max Temperature')
plt.savefig("CityLatvsMaxTemp.png")
plt.show()
```


![png](output_4_0.png)



```python
plt.scatter(humidity_list, latitude_list, facecolors="green", edgecolors="black", linewidth=1, marker='o', alpha=0.8)
plt.title('City Latitude vs. Humidity')
plt.xlabel("Latitude")
plt.ylabel('Humidity')
plt.savefig("CityLatvsHumidity.png")
plt.show()
```


![png](output_5_0.png)



```python
plt.scatter(cloudiness_list, latitude_list, facecolors="yellow", edgecolors="black", linewidth=1, marker='o', alpha=0.8)
plt.title('City Latitude vs. Cloudiness')
plt.xlabel("Latitude")
plt.ylabel('Cloudiness (%)')
plt.savefig("CityLatvsCloudiness.png")
plt.show()
```


![png](output_6_0.png)



```python
plt.scatter(wind_speed_list, latitude_list, facecolors="orange", edgecolors="black", linewidth=1, marker='o', alpha=0.8)
plt.title('City Latitude vs. Wind Speed')
plt.xlabel("Latitude")
plt.ylabel('Wind Speed (mph)')
plt.savefig("CityLatvsWindSpeed.png")
plt.show()
```


![png](output_7_0.png)



```python
dictionary_df.to_csv("WeatherPy.csv", encoding='utf-8', index=False)
```
