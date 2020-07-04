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
Last updated:  Sat Jul 4 19:08:43 UTC 2020

*cities15000.csv*
```
geonameid,name,asciiname,alternatenames,latitude,longitude,feature class,feature code,country code,cc2,admin1 code,admin2 code,admin3 code,admin4 code,population,elevation,dem,timezone,modification date
3040051,les Escaldes,les Escaldes,"Ehskal'des-Ehndzhordani,Escaldes,Escaldes-Engordany,Les Escaldes,esukarudesu=engorudani jiao qu,lai sai si ka er de-en ge er da,Эскальдес-Энджордани,エスカルデス＝エンゴルダニ教区,萊塞斯卡爾德-恩戈爾達,萊塞斯卡爾德－恩戈爾達",42.507290000000005,1.53414,P,PPLA,AD,,08,,,,15853,,1033,Europe/Andorra,2008-10-15
3041563,Andorra la Vella,Andorra la Vella,"ALV,Ando-la-Vyey,Andora,Andora la Vela,Andora la Velja,Andora lja Vehl'ja,Andoro Malnova,Andorra,Andorra Tuan,Andorra a Vella,Andorra la Biella,Andorra la Vella,Andorra la Vielha,Andorra-a-Velha,Andorra-la-Vel'ja,Andorra-la-Vielye,Andorre-la-Vieille,Andò-la-Vyèy,Andòrra la Vièlha,an dao er cheng,andolalabeya,andwra la fyla,Ανδόρρα,Андора ла Веля,Андора ла Веља,Андора ля Вэлья,Андорра-ла-Велья,אנדורה לה וולה,أندورا لا فيلا,አንዶራ ላ ቬላ,アンドラ・ラ・ヴェリャ,安道爾城,안도라라베야",42.50779,1.52109,P,PPLC,AD,,07,,,,20430,,1037,Europe/Andorra,2020-03-03
290594,Umm Al Quwain City,Umm Al Quwain City,"Oumm al Qaiwain,Oumm al Qaïwaïn,Um al Kawain,Um al Quweim,Umm Al Quwain City,Umm al Qaiwain,Umm al Qawain,Umm al Qaywayn,Umm al-Quwain,Umm-ehl'-Kajvajn,Yumul al Quwain,am alqywyn,mdynt am alqywyn,Умм-эль-Кайвайн,أم القيوين,مدينة ام القيوين",25.564729999999997,55.55517,P,PPLA,AE,,07,,,,62747,,2,Asia/Dubai,2019-10-24
291074,Ras Al Khaimah City,Ras Al Khaimah City,"Julfa,Khaimah,RAK City,RKT,Ra's al Khaymah,Ra's al-Chaima,Ras Al Khaimah City,Ras al Khaimah,Ras al-Khaimah,Ras el Khaimah,Ras el Khaïmah,Ras el-Kheima,Ras-ehl'-Khajma,Ra’s al Khaymah,Ra’s al-Chaima,mdynt ras alkhymt,ras alkhymt,Рас-эль-Хайма,رأس الخيمة,مدينة رأس الخيمة",25.78953,55.9432,P,PPLA,AE,,05,,,,351943,,2,Asia/Dubai,2019-09-09
291580,Zayed City,Zayed City,"Bid' Zayed,Bid’ Zayed,Madinat Za'id,Madinat Zayid,Madīnat Zāyid,Madīnat Zā’id,Zayed City,mdynt zayd,مدينة زايد",23.65416,53.70522,P,PPL,AE,,01,103,,,63482,,124,Asia/Dubai,2019-10-24
291696,Khawr Fakkān,Khawr Fakkan,"Fakkan,Fakkān,Khawr Fakkan,Khawr Fakkān,Khawr al Fakkan,Khawr al Fakkān,Khor Fakhan,Khor Fakkan,Khor Fakkan City,Khor Fakkān,Khor al Fakhan,Khor al Fakkan,Khor al Fākhān,Khor'fakkan,Khor-Fakkan,Khorfakan,Khorfakhan,Port Khor Fakkan,mdynt khwr fkan,Хор-Факкан,مدينة خور فكان",25.33132,56.34199,P,PPL,AE,,06,,,,40677,,20,Asia/Dubai,2020-06-10
292223,Dubai,Dubai,"DXB,Dabei,Dibai,Dibay,Doubayi,Dubae,Dubai,Dubai City,Dubai emiraat,Dubaija,Dubaj,Dubajo,Dubajus,Dubay,Dubayy,Dubaï,Dubái,Dúbæ,Ehmirat Dubaj,Fort Dabei,Ntoumpai,dby,dbyy,di bai,dobai,du bai,duba'i,dubai,dubay,dubi,dwbyy,tupai,Ντουμπάι,Дубаи,Дубай,Эмірат Дубай,Դուբայի Էմիրություն,דובאי,דוביי,دبئی,دبى,دبي,دبی,دوبەی,دۇبائى,दुबई,দুবাই,துபை,దుబాయ్,ದುಬೈ,ദുബായ്,ดูไบ,დუბაი,ドバイ,杜拜,迪拜,두바이",25.07725,55.30927,P,PPLA,AE,,03,,,,2956587,,24,Asia/Dubai,2019-08-28
292231,Dibba Al-Fujairah,Dibba Al-Fujairah,"Al-Fujairah,BYB,Dibba Al-Fujairah,dba alfjyrt,دبا الفجيرة",25.59246,56.261759999999995,P,PPL,AE,,04,,,,30000,,16,Asia/Dubai,2014-08-12
292239,Dibba Al-Hisn,Dibba Al-Hisn,"BYB,Daba,Daba al-Hisn,Dabā,Dabā al-Ḥiṣn,Diba,Diba al Hisn,Dibah,Dibba,Dibba Al'-Khisn,Dibba Al-Hisn,Dibbah,Dibā,Dībā al Ḩişn,Hisn Diba,Husn Dibba,Дибба Аль-Хисн,Ḩişn Dibā",25.61955,56.272909999999996,P,PPL,AE,,04,,,,26395,,4,Asia/Dubai,2014-04-21
```
