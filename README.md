### Source 

```
The main 'geoname' table has the following fields :
---------------------------------------------------
geonameid         : integer id of record in geonames database
name              : name of geographical point (utf8) varchar(200)
asciiname         : name of geographical point in plain ascii characters, varchar(200)
alternatenames    : alternatenames, comma separated, ascii names automatically transliterated, convenience attribute from alternatename table, varchar(10000)
latitude          : latitude in decimal degrees (wgs84)
longitude         : longitude in decimal degrees (wgs84)
feature class     : see http://www.geonames.org/export/codes.html, char(1)
feature code      : see http://www.geonames.org/export/codes.html, varchar(10)
country code      : ISO-3166 2-letter country code, 2 characters
cc2               : alternate country codes, comma separated, ISO-3166 2-letter country code, 200 characters
admin1 code       : fipscode (subject to change to iso code), see exceptions below, see file admin1Codes.txt for display names of this code; varchar(20)
admin2 code       : code for the second administrative division, a county in the US, see file admin2Codes.txt; varchar(80) 
admin3 code       : code for third level administrative division, varchar(20)
admin4 code       : code for fourth level administrative division, varchar(20)
population        : bigint (8 byte int) 
elevation         : in meters, integer
dem               : digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.
timezone          : the iana timezone id (see file timeZone.txt) varchar(40)
modification date : date of last modification in yyyy-MM-dd format# GEO-LOCATION-INFO
```

Sample:
Last updated:  Tue Jul 7 01:07:12 UTC 2020

*cities500.csv*
```
geonameid,name,asciiname,alternatenames,latitude,longitude,feature class,feature code,country code,cc2,admin1 code,admin2 code,admin3 code,admin4 code,population,elevation,dem,timezone,modification date
3038999,Soldeu,Soldeu,,42.576879999999996,1.6676900000000001,P,PPL,AD,,02,,,,602,,1832,Europe/Andorra,2017-11-06
3039154,El Tarter,El Tarter,"Ehl Tarter,Эл Тартер",42.57952,1.65362,P,PPL,AD,,02,,,,1052,,1721,Europe/Andorra,2012-11-03
3039163,Sant Julià de Lòria,Sant Julia de Loria,"San Julia,San Julià,Sant Julia de Loria,Sant Julià de Lòria,Sant-Zhulija-de-Lorija,sheng hu li ya-de luo li ya,Сант-Жулия-де-Лория,サン・ジュリア・デ・ロリア教区,圣胡利娅-德洛里亚,圣胡利娅－德洛里亚",42.46372,1.49129,P,PPLA,AD,,06,,,,8022,,921,Europe/Andorra,2013-11-23
3039604,Pas de la Casa,Pas de la Casa,"Pas de la Kasa,Пас де ла Каса",42.542770000000004,1.7336099999999999,P,PPL,AD,,03,,,,2363,2050.0,2106,Europe/Andorra,2008-06-09
3039678,Ordino,Ordino,"Ordino,ao er di nuo,orudino jiao qu,Ордино,オルディノ教区,奥尔迪诺",42.55623,1.53319,P,PPLA,AD,,05,,,,3066,,1296,Europe/Andorra,2018-10-26
3040051,les Escaldes,les Escaldes,"Ehskal'des-Ehndzhordani,Escaldes,Escaldes-Engordany,Les Escaldes,esukarudesu=engorudani jiao qu,lai sai si ka er de-en ge er da,Эскальдес-Энджордани,エスカルデス＝エンゴルダニ教区,萊塞斯卡爾德-恩戈爾達,萊塞斯卡爾德－恩戈爾達",42.507290000000005,1.53414,P,PPLA,AD,,08,,,,15853,,1033,Europe/Andorra,2008-10-15
3040132,la Massana,la Massana,"La Macana,La Massana,La Maçana,La-Massana,la Massana,ma sa na,Ла-Массана,ラ・マサナ教区,马萨纳",42.544990000000006,1.51483,P,PPLA,AD,,04,,,,7211,,1245,Europe/Andorra,2008-10-15
3040141,l'Aldosa,l'Aldosa,,42.54391,1.5228899999999999,P,PPL,AD,,04,,,,594,,1296,Europe/Andorra,2007-04-29
3040686,Encamp,Encamp,"Ehnkam,Encamp,en kan pu,enkanpu jiao qu,Энкам,エンカンプ教区,恩坎普",42.53474,1.5801399999999999,P,PPLA,AD,,03,,,,11223,,1257,Europe/Andorra,2018-10-26
```
