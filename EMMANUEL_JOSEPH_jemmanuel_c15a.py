#!/usr/bin/env python
# coding: utf-8

# # Emmanuel Joseph
# #cohort 15 Data Analytics Project 1
# #Timezone converter

# In[1]:


# Name : Doris Akpan
# Cohort : 1.4
#Track: Software Engr
# In[2]:


'''
Loading dataset with timezone/countrieslist and offset from my computer to jupyter notebook.

Please note that before loading this dataset, I have already cleaned it using excel. 
At the cleaning stage, I removed the slash in between continuents,countries and cities, and I took only the continents
and cities e.g AfricaLagos
Then I noticed that 7 continent with city names having the same offsets were duplicated which I removed. 
This reduced my data rows from 588 to 581

The lines removed as per excel numbering is as follows
No 61 AmericaBuenos_Aires duplicated number 87
No 62 AmericaCatamarca duplicated in number 92
No 64 AmericaCordoba duplicated in number 98
No 65 AmericaJujuy duplicated in number 140
No 67 AmericaMendoza duplicated in number 158
No 128 AmericaIndianapolis duplicated in number 136
No 142 AmericaLouisville duplicated in number 149
7 duplicates removed.

'''

#df = pd.read_csv('C:/Users/ICT/Desktop/Project_docs/timezones_Detailed_588_Countries.csv')


# In[3]:


#printing my dataframe

#print(df)


# In[4]:


#I converted the timezone(continent+city) column to a list

#continentAndC = list(df['timezone'])


# In[5]:


#printing continentAndC list
#continentAndC


# In[6]:


#checking the length of new created list to confirm no data is lost

#len (continentAndC)


# In[7]:


#I manually copied the converted continentAndC list and created a new list using copy and paste to enable anyone with my script be able to use it.

continentAndCity = ['AfricaAbidjan',
'AfricaAccra',
 'AfricaAddis_Ababa',
 'AfricaAlgiers',
 'AfricaAsmara',
 'AfricaAsmera',
 'AfricaBamako',
 'AfricaBangui',
 'AfricaBanjul',
 'AfricaBissau',
 'AfricaBlantyre',
 'AfricaBrazzaville',
 'AfricaBujumbura',
 'AfricaCairo',
 'AfricaCasablanca',
 'AfricaCeuta',
 'AfricaConakry',
 'AfricaDakar',
 'AfricaDar_es_Salaam',
 'AfricaDjibouti',
 'AfricaDouala',
 'AfricaEl_Aaiun',
 'AfricaFreetown',
 'AfricaGaborone',
 'AfricaHarare',
 'AfricaJohannesburg',
 'AfricaJuba',
 'AfricaKampala',
 'AfricaKhartoum',
 'AfricaKigali',
 'AfricaKinshasa',
 'AfricaLagos',
 'AfricaLibreville',
 'AfricaLome',
 'AfricaLuanda',
 'AfricaLubumbashi',
 'AfricaLusaka',
 'AfricaMalabo',
 'AfricaMaputo',
 'AfricaMaseru',
 'AfricaMbabane',
 'AfricaMogadishu',
 'AfricaMonrovia',
 'AfricaNairobi',
 'AfricaNdjamena',
 'AfricaNiamey',
 'AfricaNouakchott',
 'AfricaOuagadougou',
 'AfricaPorto-Novo',
 'AfricaSao_Tome',
 'AfricaTimbuktu',
 'AfricaTripoli',
 'AfricaTunis',
 'AfricaWindhoek',
 'AmericaAdak',
 'AmericaAnchorage',
 'AmericaAnguilla',
 'AmericaAntigua',
 'AmericaAraguaina',
 'AmericaBuenos_Aires',
 'AmericaCatamarca',
 'AmericaComodRivadavia',
 'AmericaCordoba',
 'AmericaJujuy',
 'AmericaLa_Rioja',
 'AmericaMendoza',
 'AmericaRio_Gallegos',
 'AmericaSalta',
 'AmericaSan_Juan',
 'AmericaSan_Luis',
 'AmericaTucuman',
 'AmericaUshuaia',
 'AmericaAruba',
 'AmericaAsuncion',
 'AmericaAtikokan',
 'AmericaAtka',
 'AmericaBahia',
 'AmericaBahia_Banderas',
 'AmericaBarbados',
 'AmericaBelem',
 'AmericaBelize',
 'AmericaBlanc-Sablon',
 'AmericaBoa_Vista',
 'AmericaBogota',
 'AmericaBoise',
 'AmericaCambridge_Bay',
 'AmericaCampo_Grande',
 'AmericaCancun',
 'AmericaCaracas',
 'AmericaCayenne',
 'AmericaCayman',
 'AmericaChicago',
 'AmericaChihuahua',
 'AmericaCoral_Harbour',
 'AmericaCosta_Rica',
 'AmericaCreston',
 'AmericaCuiaba',
 'AmericaCuracao',
 'AmericaDanmarkshavn',
 'AmericaDawson',
 'AmericaDawson_Creek',
 'AmericaDenver',
 'AmericaDetroit',
 'AmericaDominica',
 'AmericaEdmonton',
 'AmericaEirunepe',
 'AmericaEl_Salvador',
 'AmericaEnsenada',
 'AmericaFort_Nelson',
 'AmericaFort_Wayne',
 'AmericaFortaleza',
 'AmericaGlace_Bay',
 'AmericaGodthab',
 'AmericaGoose_Bay',
 'AmericaGrand_Turk',
 'AmericaGrenada',
 'AmericaGuadeloupe',
 'AmericaGuatemala',
 'AmericaGuayaquil',
 'AmericaGuyana',
 'AmericaHalifax',
 'AmericaHavana',
 'AmericaHermosillo',
 'AmericaIndianapolis',
 'AmericaKnox',
 'AmericaMarengo',
 'AmericaPetersburg',
 'AmericaTell_City',
 'AmericaVevay',
 'AmericaVincennes',
 'AmericaWinamac',
 'AmericaInuvik',
 'AmericaIqaluit',
 'AmericaJamaica',
 'AmericaJuneau',
 'AmericaLouisville',
 'AmericaMonticello',
 'AmericaKnox_IN',
 'AmericaKralendijk',
 'AmericaLa_Paz',
 'AmericaLima',
 'AmericaLos_Angeles',
 'AmericaLower_Princes',
 'AmericaMaceio',
 'AmericaManagua',
 'AmericaManaus',
 'AmericaMarigot',
 'AmericaMartinique',
 'AmericaMatamoros',
 'AmericaMazatlan',
 'AmericaMenominee',
 'AmericaMerida',
 'AmericaMetlakatla',
 'AmericaMexico_City',
 'AmericaMiquelon',
 'AmericaMoncton',
 'AmericaMonterrey',
 'AmericaMontevideo',
 'AmericaMontreal',
 'AmericaMontserrat',
 'AmericaNassau',
 'AmericaNew_York',
 'AmericaNipigon',
 'AmericaNome',
 'AmericaNoronha',
 'AmericaBeulah',
 'AmericaCenter',
 'AmericaNew_Salem',
 'AmericaOjinaga',
 'AmericaPanama',
 'AmericaPangnirtung',
 'AmericaParamaribo',
 'AmericaPhoenix',
 'AmericaPort-au-Prince',
 'AmericaPort_of_Spain',
 'AmericaPorto_Acre',
 'AmericaPorto_Velho',
 'AmericaPuerto_Rico',
 'AmericaRainy_River',
 'AmericaRankin_Inlet',
 'AmericaRecife',
 'AmericaRegina',
 'AmericaResolute',
 'AmericaRio_Branco',
 'AmericaRosario',
 'AmericaSanta_Isabel',
 'AmericaSantarem',
 'AmericaSantiago',
 'AmericaSanto_Domingo',
 'AmericaSao_Paulo',
 'AmericaScoresbysund',
 'AmericaShiprock',
 'AmericaSitka',
 'AmericaSt_Barthelemy',
 'AmericaSt_Johns',
 'AmericaSt_Kitts',
 'AmericaSt_Lucia',
 'AmericaSt_Thomas',
 'AmericaSt_Vincent',
 'AmericaSwift_Current',
 'AmericaTegucigalpa',
 'AmericaThule',
 'AmericaThunder_Bay',
 'AmericaTijuana',
 'AmericaToronto',
 'AmericaTortola',
 'AmericaVancouver',
 'AmericaVirgin',
 'AmericaWhitehorse',
 'AmericaWinnipeg',
 'AmericaYakutat',
 'AmericaYellowknife',
 'AntarcticaCasey',
 'AntarcticaDavis',
 'AntarcticaDumontDUrville',
 'AntarcticaMacquarie',
 'AntarcticaMawson',
 'AntarcticaMcMurdo',
 'AntarcticaPalmer',
 'AntarcticaRothera',
 'AntarcticaSouth_Pole',
 'AntarcticaSyowa',
 'AntarcticaTroll',
 'AntarcticaVostok',
 'ArcticLongyearbyen',
 'AsiaAden',
 'AsiaAlmaty',
 'AsiaAmman',
 'AsiaAnadyr',
 'AsiaAqtau',
 'AsiaAqtobe',
 'AsiaAshgabat',
 'AsiaAshkhabad',
 'AsiaBaghdad',
 'AsiaBahrain',
 'AsiaBaku',
 'AsiaBangkok',
 'AsiaBeirut',
 'AsiaBishkek',
 'AsiaBrunei',
 'AsiaCalcutta',
 'AsiaChita',
 'AsiaChoibalsan',
 'AsiaChongqing',
 'AsiaChungking',
 'AsiaColombo',
 'AsiaDacca',
 'AsiaDamascus',
 'AsiaDhaka',
 'AsiaDili',
 'AsiaDubai',
 'AsiaDushanbe',
 'AsiaGaza',
 'AsiaHarbin',
 'AsiaHebron',
 'AsiaHo_Chi_Minh',
 'AsiaHong_Kong',
 'AsiaHovd',
 'AsiaIrkutsk',
 'AsiaIstanbul',
 'AsiaJakarta',
 'AsiaJayapura',
 'AsiaJerusalem',
 'AsiaKabul',
 'AsiaKamchatka',
 'AsiaKarachi',
 'AsiaKashgar',
 'AsiaKathmandu',
 'AsiaKatmandu',
 'AsiaKhandyga',
 'AsiaKolkata',
 'AsiaKrasnoyarsk',
 'AsiaKuala_Lumpur',
 'AsiaKuching',
 'AsiaKuwait',
 'AsiaMacao',
 'AsiaMacau',
 'AsiaMagadan',
 'AsiaMakassar',
 'AsiaManila',
 'AsiaMuscat',
 'AsiaNicosia',
 'AsiaNovokuznetsk',
 'AsiaNovosibirsk',
 'AsiaOmsk',
 'AsiaOral',
 'AsiaPhnom_Penh',
 'AsiaPontianak',
 'AsiaPyongyang',
 'AsiaQatar',
 'AsiaQyzylorda',
 'AsiaRangoon',
 'AsiaRiyadh',
 'AsiaRiyadh87',
 'AsiaRiyadh88',
 'AsiaRiyadh89',
 'AsiaSaigon',
 'AsiaSakhalin',
 'AsiaSamarkand',
 'AsiaSeoul',
 'AsiaShanghai',
 'AsiaSingapore',
 'AsiaSrednekolymsk',
 'AsiaTaipei',
 'AsiaTashkent',
 'AsiaTbilisi',
 'AsiaTehran',
 'AsiaTel_Aviv',
 'AsiaThimbu',
 'AsiaThimphu',
 'AsiaTokyo',
 'AsiaUjung_Pandang',
 'AsiaUlaanbaatar',
 'AsiaUlan_Bator',
 'AsiaUrumqi',
 'AsiaVientiane',
 'AsiaVladivostok',
 'AsiaYakutsk',
 'AsiaYekaterinburg',
 'AsiaYerevan',
 'AtlanticAzores',
 'AtlanticBermuda',
 'AtlanticCanary',
 'AtlanticCape_Verde',
 'AtlanticFaeroe',
 'AtlanticFaroe',
 'AtlanticJan_Mayen',
 'AtlanticMadeira',
 'AtlanticReykjavik',
 'AtlanticSouth_Georgia',
 'AtlanticSt_Helena',
 'AtlanticStanley',
 'AustraliaACT',
 'AustraliaAdelaide',
 'AustraliaBrisbane',
 'AustraliaBroken_Hill',
 'AustraliaCanberra',
 'AustraliaCurrie',
 'AustraliaDarwin',
 'AustraliaEucla',
 'AustraliaHobart',
 'AustraliaLHI',
 'AustraliaLindeman',
 'AustraliaLord_Howe',
 'AustraliaMelbourne',
 'AustraliaNSW',
 'AustraliaNorth',
 'AustraliaPerth',
 'AustraliaQueensland',
 'AustraliaSouth',
 'AustraliaSydney',
 'AustraliaTasmania',
 'AustraliaVictoria',
 'AustraliaWest',
 'AustraliaYancowinna',
 'BrazilAcre',
 'BrazilDeNoronha',
 'BrazilEast',
 'BrazilWest',
 'CET',
 'CST6CDT',
 'CanadaAtlantic',
 'CanadaCentral',
 'CanadaEast-Saskatchewan',
 'CanadaEastern',
 'CanadaMountain',
 'CanadaNewfoundland',
 'CanadaPacific',
 'CanadaSaskatchewan',
 'CanadaYukon',
 'ChileContinental',
 'ChileEasterIsland',
 'Cuba',
 'EET',
 'EST',
 'EST5EDT',
 'Egypt',
 'Eire',
 'EtcGMT',
 'EtcGMT+0',
 'EtcGMT+1',
 'EtcGMT+10',
 'EtcGMT+11',
 'EtcGMT+12',
 'EtcGMT+2',
 'EtcGMT+3',
 'EtcGMT+4',
 'EtcGMT+5',
 'EtcGMT+6',
 'EtcGMT+7',
 'EtcGMT+8',
 'EtcGMT+9',
 'EtcGMT-0',
 'EtcGMT-1',
 'EtcGMT-10',
 'EtcGMT-11',
 'EtcGMT-12',
 'EtcGMT-13',
 'EtcGMT-14',
 'EtcGMT-2',
 'EtcGMT-3',
 'EtcGMT-4',
 'EtcGMT-5',
 'EtcGMT-6',
 'EtcGMT-7',
 'EtcGMT-8',
 'EtcGMT-9',
 'EtcGMT0',
 'EtcGreenwich',
 'EtcUCT',
 'EtcUTC',
 'EtcUniversal',
 'EtcZulu',
 'EuropeAmsterdam',
 'EuropeAndorra',
 'EuropeAthens',
 'EuropeBelfast',
 'EuropeBelgrade',
 'EuropeBerlin',
 'EuropeBratislava',
 'EuropeBrussels',
 'EuropeBucharest',
 'EuropeBudapest',
 'EuropeBusingen',
 'EuropeChisinau',
 'EuropeCopenhagen',
 'EuropeDublin',
 'EuropeGibraltar',
 'EuropeGuernsey',
 'EuropeHelsinki',
 'EuropeIsle_of_Man',
 'EuropeIstanbul',
 'EuropeJersey',
 'EuropeKaliningrad',
 'EuropeKiev',
 'EuropeLisbon',
 'EuropeLjubljana',
 'EuropeLondon',
 'EuropeLuxembourg',
 'EuropeMadrid',
 'EuropeMalta',
 'EuropeMariehamn',
 'EuropeMinsk',
 'EuropeMonaco',
 'EuropeMoscow',
 'EuropeNicosia',
 'EuropeOslo',
 'EuropeParis',
 'EuropePodgorica',
 'EuropePrague',
 'EuropeRiga',
 'EuropeRome',
 'EuropeSamara',
 'EuropeSan_Marino',
 'EuropeSarajevo',
 'EuropeSimferopol',
 'EuropeSkopje',
 'EuropeSofia',
 'EuropeStockholm',
 'EuropeTallinn',
 'EuropeTirane',
 'EuropeTiraspol',
 'EuropeUzhgorod',
 'EuropeVaduz',
 'EuropeVatican',
 'EuropeVienna',
 'EuropeVilnius',
 'EuropeVolgograd',
 'EuropeWarsaw',
 'EuropeZagreb',
 'EuropeZaporozhye',
 'EuropeZurich',
 'Factory',
 'GB',
 'GB-Eire',
 'GMT',
 'GMT+0',
 'GMT-0',
 'GMT0',
 'Greenwich',
 'HST',
 'Hongkong',
 'Iceland',
 'IndianAntananarivo',
 'IndianChagos',
 'IndianChristmas',
 'IndianCocos',
 'IndianComoro',
 'IndianKerguelen',
 'IndianMahe',
 'IndianMaldives',
 'IndianMauritius',
 'IndianMayotte',
 'IndianReunion',
 'Iran',
 'Israel',
 'Jamaica',
 'Japan',
 'Kwajalein',
 'Libya',
 'MET',
 'MST',
 'MST7MDT',
 'MexicoBajaNorte',
 'MexicoBajaSur',
 'MexicoGeneral',
 'MideastRiyadh87',
 'MideastRiyadh88',
 'MideastRiyadh89',
 'NZ',
 'NZ-CHAT',
 'Navajo',
 'PRC',
 'PST8PDT',
 'PacificApia',
 'PacificAuckland',
 'PacificBougainville',
 'PacificChatham',
 'PacificChuuk',
 'PacificEaster',
 'PacificEfate',
 'PacificEnderbury',
 'PacificFakaofo',
 'PacificFiji',
 'PacificFunafuti',
 'PacificGalapagos',
 'PacificGambier',
 'PacificGuadalcanal',
 'PacificGuam',
 'PacificHonolulu',
 'PacificJohnston',
 'PacificKiritimati',
 'PacificKosrae',
 'PacificKwajalein',
 'PacificMajuro',
 'PacificMarquesas',
 'PacificMidway',
 'PacificNauru',
 'PacificNiue',
 'PacificNorfolk',
 'PacificNoumea',
 'PacificPago_Pago',
 'PacificPalau',
 'PacificPitcairn',
 'PacificPonape',
 'PacificPort_Moresby',
 'PacificRarotonga',
 'PacificSaipan',
 'PacificSamoa',
 'PacificTahiti',
 'PacificTarawa',
 'PacificTongatapu',
 'PacificTruk',
 'PacificWake',
 'PacificWallis',
 'PacificYap',
 'Poland',
 'Portugal',
 'ROC',
 'ROK',
 'Singapore',
 'Turkey',
 'UCT',
 'USAlaska',
 'USAleutian',
 'USArizona',
 'USCentral',
 'USEast-Indiana',
 'USEastern',
 'USHawaii',
 'USIndiana-Starke',
 'USMichigan',
 'USMountain',
 'USPacific',
 'USPacific-New',
 'USSamoa',
 'UTC',
 'Universal',
 'W-SU',
 'WET',
 'Zulu']


# In[8]:


#printing my manually created list to confirm they are in order.
continentAndCity


# In[9]:


#checking the length to be sure no data is loss


# In[10]:


#I converted the offset column header of the dataframe to a list

#offsetL = list(df ['offset'])


# In[11]:


#printing the newly converted list offsetL

#offsetL


# In[12]:


#I manually copied the converted offsetL list and created a new list usig copy and paste to enable anyone with my script be able to use it.

offsetList = [0,
 0,
 10800,
 3600,
 10800,
 10800,
 0,
 3600,
 0,
 0,
 7200,
 3600,
 7200,
 7200,
 0,
 3600,
 0,
 0,
 10800,
 10800,
 3600,
 0,
 0,
 7200,
 7200,
 7200,
 10800,
 10800,
 10800,
 7200,
 3600,
 3600,
 3600,
 0,
 3600,
 7200,
 7200,
 3600,
 7200,
 7200,
 7200,
 10800,
 0,
 10800,
 3600,
 3600,
 0,
 0,
 3600,
 0,
 0,
 7200,
 3600,
 3600,
 -36000,
 -32400,
 -14400,
 -14400,
 -10800,
 -10800,
 -10800,
 -10800,
 -10800,
 -10800,
 -10800,
 -10800,
 -10800,
 -10800,
 -10800,
 -10800,
 -10800,
 -10800,
 -14400,
 -10800,
 -18000,
 -36000,
 -10800,
 -21600,
 -14400,
 -10800,
 -21600,
 -14400,
 -14400,
 -18000,
 -25200,
 -25200,
 -14400,
 -18000,
 -16200,
 -10800,
 -18000,
 -21600,
 -25200,
 -18000,
 -21600,
 -25200,
 -14400,
 -14400,
 0,
 -28800,
 -25200,
 -25200,
 -18000,
 -14400,
 -25200,
 -18000,
 -21600,
 -28800,
 -25200,
 -18000,
 -10800,
 -14400,
 -10800,
 -14400,
 -14400,
 -14400,
 -14400,
 -21600,
 -18000,
 -14400,
 -14400,
 -18000,
 -25200,
 -18000,
 -21600,
 -18000,
 -18000,
 -21600,
 -18000,
 -18000,
 -18000,
 -25200,
 -18000,
 -18000,
 -32400,
 -18000,
 -18000,
 -21600,
 -14400,
 -14400,
 -18000,
 -28800,
 -14400,
 -10800,
 -21600,
 -14400,
 -14400,
 -14400,
 -21600,
 -25200,
 -21600,
 -21600,
 -28800,
 -21600,
 -10800,
 -14400,
 -21600,
 -10800,
 -18000,
 -14400,
 -18000,
 -18000,
 -18000,
 -32400,
 -7200,
 -21600,
 -21600,
 -21600,
 -25200,
 -18000,
 -18000,
 -10800,
 -25200,
 -18000,
 -14400,
 -18000,
 -14400,
 -14400,
 -21600,
 -21600,
 -10800,
 -21600,
 -21600,
 -18000,
 -10800,
 -28800,
 -10800,
 -10800,
 -14400,
 -10800,
 -3600,
 -25200,
 -32400,
 -14400,
 -12600,
 -14400,
 -14400,
 -14400,
 -14400,
 -21600,
 -21600,
 -14400,
 -18000,
 -28800,
 -18000,
 -14400,
 -28800,
 -14400,
 -28800,
 -21600,
 -32400,
 -25200,
 28800,
 25200,
 36000,
 39600,
 18000,
 43200,
 -10800,
 -10800,
 43200,
 10800,
 0,
 21600,
 3600,
 10800,
 21600,
 7200,
 43200,
 18000,
 18000,
 18000,
 18000,
 10800,
 10800,
 14400,
 25200,
 7200,
 21600,
 28800,
 19800,
 28800,
 28800,
 28800,
 28800,
 19800,
 21600,
 7200,
 21600,
 32400,
 14400,
 18000,
 7200,
 28800,
 7200,
 25200,
 28800,
 25200,
 28800,
 7200,
 25200,
 32400,
 7200,
 16200,
 43200,
 18000,
 21600,
 20700,
 20700,
 32400,
 19800,
 25200,
 28800,
 28800,
 10800,
 28800,
 28800,
 36000,
 28800,
 28800,
 14400,
 7200,
 25200,
 21600,
 21600,
 18000,
 25200,
 25200,
 30600,
 10800,
 21600,
 23400,
 10800,
 10800,
 10800,
 10800,
 25200,
 36000,
 18000,
 32400,
 28800,
 28800,
 39600,
 28800,
 18000,
 14400,
 12600,
 7200,
 21600,
 21600,
 32400,
 28800,
 28800,
 28800,
 21600,
 25200,
 36000,
 32400,
 18000,
 14400,
 -3600,
 -14400,
 0,
 -3600,
 0,
 0,
 3600,
 0,
 0,
 -7200,
 0,
 -10800,
 36000,
 34200,
 36000,
 34200,
 36000,
 36000,
 34200,
 31500,
 36000,
 37800,
 36000,
 37800,
 36000,
 36000,
 34200,
 28800,
 36000,
 34200,
 36000,
 36000,
 36000,
 28800,
 34200,
 -18000,
 -7200,
 -10800,
 -14400,
 3600,
 -21600,
 -14400,
 -21600,
 -21600,
 -18000,
 -25200,
 -12600,
 -28800,
 -21600,
 -28800,
 -10800,
 -18000,
 -18000,
 7200,
 -18000,
 -18000,
 7200,
 0,
 0,
 0,
 -3600,
 -36000,
 -39600,
 -43200,
 -7200,
 -10800,
 -14400,
 -18000,
 -21600,
 -25200,
 -28800,
 -32400,
 0,
 3600,
 36000,
 39600,
 43200,
 46800,
 50400,
 7200,
 10800,
 14400,
 18000,
 21600,
 25200,
 28800,
 32400,
 0,
 0,
 0,
 0,
 0,
 0,
 3600,
 3600,
 7200,
 0,
 3600,
 3600,
 3600,
 3600,
 7200,
 3600,
 3600,
 7200,
 3600,
 0,
 3600,
 0,
 7200,
 0,
 7200,
 0,
 7200,
 7200,
 0,
 3600,
 0,
 3600,
 3600,
 3600,
 7200,
 10800,
 3600,
 10800,
 7200,
 3600,
 3600,
 3600,
 3600,
 7200,
 3600,
 14400,
 3600,
 3600,
 7200,
 3600,
 7200,
 3600,
 7200,
 3600,
 7200,
 7200,
 3600,
 3600,
 3600,
 7200,
 10800,
 3600,
 3600,
 7200,
 3600,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 -36000,
 28800,
 0,
 10800,
 21600,
 25200,
 23400,
 10800,
 18000,
 14400,
 18000,
 14400,
 10800,
 14400,
 12600,
 7200,
 -18000,
 32400,
 43200,
 7200,
 3600,
 -25200,
 -25200,
 -28800,
 -25200,
 -21600,
 0,
 0,
 0,
 43200,
 45900,
 0,
 0,
 0,
 46800,
 43200,
 39600,
 45900,
 36000,
 -18000,
 39600,
 46800,
 46800,
 43200,
 43200,
 -21600,
 -32400,
 39600,
 36000,
 -36000,
 -36000,
 50400,
 39600,
 43200,
 43200,
 -34200,
 -39600,
 43200,
 -39600,
 39600,
 39600,
 -39600,
 32400,
 -28800,
 39600,
 36000,
 -36000,
 36000,
 -39600,
 -36000,
 43200,
 46800,
 36000,
 43200,
 43200,
 36000,
 3600,
 0,
 28800,
 32400,
 28800,
 7200,
 0,
 -32400,
 -36000,
 -25200,
 -21600,
 -18000,
 -18000,
 -36000,
 -21600,
 -18000,
 -25200,
 -28800,
 -28800,
 -39600,
 0,
 0,
 10800,
 0,
 0]


# In[13]:


#converting offsetList to UTC/GMT timezone

convertedTime = [] #An empty list that would have the timezone in UTC
hoursConversion = 3600
for countryTime in offsetList:
    if  countryTime > 0 or countryTime < 0:
        countryTimeList = countryTime/hoursConversion
        convertedTime.append(countryTimeList)
    else:
        convertedTime.append(countryTime)
        
convertedTime #printing the new convertedTime list


# In[14]:


#checking to confirm the length is intact


# In[15]:


#converting continentAndCity and convertedTime lists into a dictionary

continentAndCity
convertedTime

continentAndTimeDict = dict(zip(continentAndCity, convertedTime))

continentAndTimeDict #printing the continentAndTimeDict dictionary


# In[16]:


#checking the length to be sure no data is loss


# In[ ]:





# In[17]:


'''
Loading Bootcamp scheduler dataset into jupyter notebook.

Please note that before loading this dataset, I have already cleaned and prepared it with excel.
Since I was going to use the dictionary method, I collapsed the bootcamp date and time column in a separate column called Bootcamp_Date_Time.
While I collapsed the cohort, program and topic columns in another separate column called Cohort_Program_Topic. 
Making it a total of 2 columns in the csv file.
The Bootcamp_Date_Time formed the key while Cohort_Program_Topic formed the value of the dictionary.

While cleaning the data in excel, I noticed a conflict of bootcamp date and time which I manually corrected.
My observations were:
1. Two classes usually hold each day by 6am and 10am.
2. From 21th July to 30th September, 2022 the bootcamp times are 6am and 10am for cohort 14 & 15 respectively for 
the 24 class days out of 28 days.
3. But for 7th July 2022, I observed that Cohort 14 Data analytics and Cohort 14 Data science/ML have identical bootcamp
date and time of 6am. Because of this identical date and time issues, the entire 28 bootcamp class days could not be 
captured in the dictionary which I created to hold both Bootcamp_Date_Time and Cohort_Program_Topic which got me stucked.
4. In order for me to get passed this stage, I normalized the bootcamp date such that 2 classes will not hold at the
same time of 6am and only cohort 14 class alone does not hold for the entire day. Rather one cohort class for 6am while the other cohort class at 10am just like the other 24 class days.
5. Similar date conflict occured on 8th July, 2022 for cohort 15 data analytics and cohort 15 data science/ML which I handled using the same method

'''
#df2 = pd.read_csv('C:/Users/ICT/Desktop/Project_docs/cleaned_bootcampSchedule.csv')


# In[18]:


#printing the loaded data scheduler
#df2


# In[19]:


#I converted Bootcamp_Date_Time column to list

#dateT = list(df2['Bootcamp_Date_Time'])
#dateT


# In[20]:


#I manually copied the converted dateT list and created a new list usig copy and paste to enable anyone with my script be able to use it.

dateTime = ['2022-07-07 06:00',
 '2022-07-07 10:00',
 '2022-07-08 06:00',
 '2022-07-08 10:00',
 '2022-07-21 06:00',
 '2022-07-21 10:00',
 '2022-07-22 06:00',
 '2022-07-22 10:00',
 '2022-08-04 06:00',
 '2022-08-04 10:00',
 '2022-08-05 06:00',
 '2022-08-05 10:00',
 '2022-08-18 06:00',
 '2022-08-18 10:00',
 '2022-08-19 06:00',
 '2022-08-19 10:00',
 '2022-09-01 06:00',
 '2022-09-01 10:00',
 '2022-09-02 06:00',
 '2022-09-02 10:00',
 '2022-09-15 06:00',
 '2022-09-15 10:00',
 '2022-09-16 06:00',
 '2022-09-16 10:00',
 '2022-09-29 06:00',
 '2022-09-29 10:00',
 '2022-09-30 06:00',
 '2022-09-30 10:00']


# In[21]:


# printing the list I just created manually

dateTime


# In[ ]:





# In[ ]:





# In[22]:


#I converted the Cohort_Program_Topic column in the bootcamp scheduler data to a list

#Cohort_Prog_TopicD = list(df2['Cohort_Program_Topic'])
#Cohort_Prog_TopicD


# In[ ]:





# In[23]:


# I manually copied the converted Cohort_Prog_TopicD list using copy and paste and then created a new list to enable any user to be able to use my script

Cohort_Prog_TopicDict = ['Cohort 14 Data Analytics Python Variables',
 'Cohort 15 Data Science/ML Data Cleaning',
 'Cohort 14 Data Science/ML Python Variables',
 'Cohort 15 Data Analytics Data Visualization Project 1',
 'Cohort 14 Data Analytics Python Container',
 'Cohort 15 Data Science/ML Data Transformation',
 'Cohort 14 Data Science/ML Python Container',
 'Cohort 15 Data Analytics Data Visualization Project 2',
 'Cohort 14 Data Analytics Python Container II',
 'Cohort 15 Data Science/ML Data Transformation II',
 'Cohort 14 Data Science/ML Python Container II',
 'Cohort 15 Data Analytics Data Visualization Project 3',
 'Cohort 14 Data Analytics Python Functions',
 'Cohort 15 Data Science/ML Feature Selection',
 'Cohort 14 Data Science/ML Python Functions',
 'Cohort 15 Data Analytics Data Visualization Project 4',
 'Cohort 14 Data Analytics Python Functions',
 'Cohort 15 Data Science/ML Feature Selection II',
 'Cohort 14 Data Science/ML Python Functions II',
 'Cohort 15 Data Analytics Data Visualization Project 5',
 'Cohort 14 Data Analytics Python Pandas I',
 'Cohort 15 Data Science/ML Supervised Learning Intro',
 'Cohort 14 Data Science/ML Python Pandas I',
 'Cohort 15 Data Analytics Data Visualization Project 6',
 'Cohort 14 Data Analytics Python Pandas II',
 'Cohort 15 Data Science/ML Unsupervised Learning Intro',
 'Cohort 14 Data Science/ML Python Pandas II',
 'Cohort 15 Data Analytics Data Visualization Project 7']


# In[24]:


#printing newly created Cohort_Prog_TopicDict dictionary

Cohort_Prog_TopicDict


# In[25]:


#checking the length to confirm there is no data loss


# In[26]:


#Converting both date_time and cohort_program_topic lists to dictionary
dateTime
Cohort_Prog_TopicDict

dateTime_cohortProgDict = dict(zip(dateTime, Cohort_Prog_TopicDict))
dateTime_cohortProgDict


# In[27]:


#len(dateTime_cohortProgDict)


# # TIME ZONE CONVERSION

# # TIME ZONE CONVERSION

# In[28]:


#TIME ZONE CONVERSION
'''

1. This timezone converter converts any given date and time in EST timezone to the user's chosen local time.
Does not matter if the date and time is not within any bootcamp schedule date and time.

2. If the inputed date and time falls within the bootcamp schedule date and time, the user will be notified of 
of the cohort, program and topic that is scheduled in the inputed time.

3. If the inputed local region is wrong, the code will notify the user and advise user to input correct continent+City
and if the date and time format is wrong, there will be an error.

'''

#Importing datetime, timezone and timedelta library

import datetime
from datetime import datetime

import pytz

from datetime import time

from datetime import timedelta

continentAndTimeDict #Dictionary for continents and timezones in universal time.
dateTime_cohortProgDict #Dictionary for date,time,cohort, program and topic

#user input varialbe for continent+city
continentCity = input('Enter name of continent+city or city: ')

#user input varialbe for bootcamp date and time
sourceTime = input('Enter bootcamp date and time in EST using the format yyyy-mm-dd hh:mm ')
y = 0

#This code checks if items in continenties and cities are present in the the dictionary holding continent and time.
#It also checks if user source date and time entered is present in the dictionary holding date and time
if continentCity in continentAndTimeDict.keys() and sourceTime in dateTime_cohortProgDict.keys():
    y = continentAndTimeDict[continentCity]
    classes = dateTime_cohortProgDict[sourceTime]
    
    #timezone conversion
    UTC = y+5
    EST = datetime.strptime(sourceTime,'%Y-%m-%d %H:%M')
    localTime = (EST + timedelta(hours=UTC)).strftime('%Y-%m-%d %H:%M')
    strTime = str(localTime)
    
    #print user specified time, continent+city entered and converted local time of the user if data is entered correctly
    print (f'{sourceTime}EST in {continentCity} local time is {strTime}')
    
    #printing the bootcamp class that will hold based on the user time if program time and date is entered correctly
    print (f'The class is for {classes}')
    
    #my trade mark
    print('***THANKS FOR USING EMJOE TIMEZONE CONVERTER***')
    
# This will print if continent+City name entered by the user is not in continentAndTimeDict dictionary
elif continentCity not in continentAndTimeDict.keys():
    print ('wrong continent+City name entered. Please refer to continentAndTimeDict and enter correct continent+City ')
    
    print ('***TRY AGAIN***')

# This code prints the user specified time and convert to his/her local time even if entered time and date is not in dateTime_cohortProgDict    
else:
    y = continentAndTimeDict[continentCity]
    UTC = y+5
    EST = datetime.strptime(sourceTime,'%Y-%m-%d %H:%M')
    localTime = (EST + timedelta(hours=UTC)).strftime('%Y-%m-%d %H:%M')
    strTime = str(localTime)
    
    #printing source time, continent+City and converted time in user local time
    print (f'{sourceTime}EST in {continentCity} local time is {strTime}')
    
    #This will print if date and time entered is not in the bootcamp schedule
    print ('You do not have any class at this time. Enter your valid class date and time in EST to view your class')
    #print('You have entered an invalid details. Please use the correct date format yyyy-mm-dd hh:mm and continent+city format')

    #my trade mark
    print('***THANKS FOR USING EMJOE TIMEZONE CONVERTER***')


# In[ ]:





# In[ ]:


'''
some test samples

AustraliaSouth
AfricaLagos
Cuba
USMountain
Libya
Israel
Japan
Factory
AustraliaSouth
Egypt
EET
AsiaManila




2022-07-22 10:00
2022-08-18 10:00
2022-09-15 10:00
2022-08-05 06:00
2022-09-16 10:00
'''


# In[ ]:




