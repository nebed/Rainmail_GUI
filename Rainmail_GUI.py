#-*-coding:utf8;-*-
from tkinter import *

countrycodes = [ 'AD','AE','AF','AG','AL','AM','AO','AQ','AR','AS','AT','AU','AZ','BA','BB','BD','BE','BF','BG','BH','BI','BJ','BN','BO','BQ','BR','BS','BT','BW','BY','BZ','CA','CC','CD','CF','CG','CH','CI','CK','CL','CM','CN','CO','CR','CV','CW','CX','CY','CZ','DE','DJ','DK','DM','DO','DZ','EC','EE','EG','ER','ES','ET','FI','FJ','FM','FR','GA','GB','GD','GE','GG','GH','GM','GN','GQ','GR','GS','GT','GU','GW','GY','HM','HN','HR','HT','HU','ID','IE','IL','IN','IQ','IS','IT','JE','JM','JO','JP','KE','KG','KH','KI','KM','KN','KR','KW','KZ','LA','LB','LC','LI','LK','LR','LS','LT','LU','LV','LY','MA','MC','MD','ME','MG','MH','MK','ML','MM','MN','MP','MR','MT','MU','MV','MW','MX','MY','MZ','NA','NC','NE','NF','NG','NI','NL','NO','NP','NR','NU','NZ','OM','PA','PE','PF','PG','PH','PK','PL','PM','PN','PT','PW','PY','QA','RO','RS','RU','RW','SA','SB','SC','SE','SG','SH','SI','SK','SL','SM','SN','SO','SR','ST','SV','SX','SZ','TD','TF','TG','TH','TJ','TK','TL','TM','TN','TO','TR','TT','TV','TZ','UA','UG','UM','US','UY','UZ','VA','VC','VE','VN','VU','WF','WS','YE','ZA','ZM','ZW']
countries = { 
	'AD':'Andorra',
        'AE':'United Arab Emirates',
	'AF':'Afghanistan',
   	'AG':'Antigua and Barbuda',
   	'AL':'Albania',
   	'AM':'Armenia',
   	'AO':'Angola',
   	'AQ':'Antarctica',
   	'AR':'Argentina',
   	'AS':'American Samoa',
   	'AT':'Austria',
   	'AU':'Australia',
   	'AZ':'Azerbaijan',
   	'BA':'Bosnia and Herzegovina',
   	'BB':'Barbados',
   	'BD':'Bangladesh',
   	'BE':'Belgium',
   	'BF':'Burkina Faso',
   	'BG':'Bulgaria',
   	'BH':'Bahrain',
   	'BI':'Burundi',
   	'BJ':'Benin',
   	'BN':'Brunei',
   	'BO':'Bolivia',
	'BQ':'Caribbean Netherlands',
	'BR':'Brazil',
	'BS':'The Bahamas',
	'BT':'Bhutan',
	'BW':'Botswana',
	'BY':'Belarus',
	'BZ':'Belize',
	'CA':'Canada',
	'CC':'Cocos (Keeling) Islands',
	'CD':'Democratic Republic of the Congo',
	'CF':'Central African Republic',
	'CG':'Republic of the Congo',
	'CH':'Switzerland',
	'CI':'Cote d\'Ivoire',
	'CK':'Cook Islands',
	'CL':'Chile',
	'CM':'Cameroon',
	'CN':'China',
	'CO':'Colombia',
	'CR':'Costa Rica',
	'CV':'Cape Verde',
	'CW':'Curacao',
	'CX':'Christmas Island',
	'CY':'Cyprus',
	'CZ':'Czechia',
	'DE':'Germany',
	'DJ':'Djibouti',
	'DK':'Denmark',
	'DM':'Dominica',
	'DO':'Dominican Republic',
	'DZ':'Algeria',
	'EC':'Ecuador',
	'EE':'Estonia',
	'EG':'Egypt',
	'ER':'Eritrea',
	'ES':'Spain',
	'ET':'Ethiopia',
	'FI':'Finland',
	'FJ':'Fiji',
	'FM':'Federated States of Micronesia',
	'FR':'France',
	'GA':'Gabon',
	'GB':'United Kingdom',
	'GD':'Grenada',
	'GE':'Georgia',
	'GG':'Guernsey',
	'GH':'Ghana',
	'GM':'The Gambia',
	'GN':'Guinea',
	'GQ':'Equatorial Guinea',
	'GR':'Greece',
	'GS':'South Georgia and the South Sandwich Islands',
	'GT':'Guatemala',
	'GU':'Guam',
	'GW':'Guinea-Bissau',
	'GY':'Guyana',
	'HM':'Heard Island and McDonald Islands',
	'HN':'Honduras',
	'HR':'Croatia',
	'HT':'Haiti',
	'HU':'Hungary',
	'ID':'Indonesia',
	'IE':'Ireland',
	'IL':'Israel',
	'IN':'India',
	'IQ':'Iraq',
	'IS':'Iceland',
	'IT':'Italy',
	'JE':'Jersey',
	'JM':'Jamaica',
	'JO':'Jordan',
	'JP':'Japan',
	'KE':'Kenya',
	'KG':'Kyrgyzstan',
	'KH':'Cambodia',
	'KI':'Kiribati',
	'KM':'Comoros',
	'KN':'Saint Kitts and Nevis',
	'KR':'South Korea',
	'KW':'Kuwait',
	'KZ':'Kazakhstan',
	'LA':'Laos',
	'LB':'Lebanon',
	'LC':'Saint Lucia',
	'LI':'Liechtenstein',
	'LK':'Sri Lanka',
	'LR':'Liberia',
	'LS':'Lesotho',
	'LT':'Lithuania',
	'LU':'Luxembourg',
	'LV':'Latvia',
	'LY':'Libya',
	'MA':'Morocco',
	'MC':'Monaco',
	'MD':'Moldova',
	'ME':'Montenegro',
	'MG':'Madagascar',
	'MH':'Marshall Islands',
	'MK':'Macedonia (FYROM)',
	'ML':'Mali',
	'MM':'Myanmar (Burma)',
	'MN':'Mongolia',
	'MP':'Northern Mariana Islands',
	'MR':'Mauritania',
	'MT':'Malta',
	'MU':'Mauritius',
	'MV':'Maldives',
	'MW':'Malawi',
	'MX':'Mexico',
	'MY':'Malaysia',
	'MZ':'Mozambique',
	'NA':'Namibia',
	'NC':'New Caledonia',
	'NE':'Niger',
	'NF':'Norfolk Island',
	'NG':'Nigeria',
	'NI':'Nicaragua',
	'NL':'Netherlands',
	'NO':'Norway',
	'NP':'Nepal',
	'NR':'Nauru',
	'NU':'Niue',
	'NZ':'New Zealand',
	'OM':'Oman',
	'PA':'Panama',
	'PE':'Peru',
	'PF':'French Polynesia',
	'PG':'Papua New Guinea',
	'PH':'Philippines',
	'PK':'Pakistan',
	'PL':'Poland',
	'PM':'Saint Pierre and Miquelon',
	'PN':'Pitcairn Islands',
	'PT':'Portugal',
	'PW':'Palau',
	'PY':'Paraguay',
	'QA':'Qatar',
	'RO':'Romania',
	'RS':'Serbia',
	'RU':'Russia',
	'RW':'Rwanda',
	'SA':'Saudi Arabia',
	'SB':'Solomon Islands',
	'SC':'Seychelles',
	'SE':'Sweden',
	'SG':'Singapore',
	'SH':'Saint Helena, Ascension and Tristan da Cunha',
	'SI':'Slovenia',
	'SK':'Slovakia',
	'SL':'Sierra Leone',
	'SM':'San Marino',
	'SN':'Senegal',
	'SO':'Somalia',
	'SR':'Suriname',
	'ST':'Sao Tome and Principe',
	'SV':'El Salvador',
	'SX':'Sint Maarten',
	'SZ':'Swaziland',
	'TD':'Chad',
	'TF':'French Southern and Antarctic Lands',
	'TG':'Togo',
	'TH':'Thailand',
	'TJ':'Tajikistan',
	'TK':'Tokelau',
	'TL':'Timor-Leste',
	'TM':'Turkmenistan',
	'TN':'Tunisia',
	'TO':'Tonga',
	'TR':'Turkey',
	'TT':'Trinidad and Tobago',
	'TV':'Tuvalu',
	'TZ':'Tanzania',
	'UA':'Ukraine',
	'UG':'Uganda',
	'UM':'United States Minor Outlying Islands',
	'US':'United States',
	'UY':'Uruguay',
	'UZ':'Uzbekistan',
	'VA':'Vatican City',
	'VC':'Saint Vincent and the Grenadines',
	'VE':'Venezuela',
	'VN':'Vietnam',
	'VU':'Vanuatu',
	'WF':'Wallis and Futuna',
	'WS':'Samoa',
	'YE':'Yemen',
	'ZA':'South Africa',
	'ZM':'Zambia',
	'ZW':'Zimbabwe',

}

def choose_country():
	choose_country = Toplevel(rainmail)
	choose_country.title('Choose Country')
	choose_country.geometry('100x100')
	choose_country.attributes('-topmost', 'true')
	label_country = Label(choose_country, text='Enter Two letter Country Code and Press Enter')
	label_country.place(x=80,y=100)
	enter_country = Entry(choose_county, command=country_validate)
	enter_country.place(x=80,y=60)

def country_validate():
	search_country = enter_country.get()
	chosen_country = str(search_country).upper()
	if (len(chosen_country) != 2):
		messagebox.showinfo(title='Info', message='It Must Be Two Characters Only')
	elif (chosen_country in countrycodes) and (len(chosen_country) == 2):
		messagebox.showinfo(title='Info', message='You Have Chosen Search Country as: %s' %(countries[chosen_country]))
		choose_country.destroy()
	else:
		messagebox.showinfo(title='Info', message='You have not Chosen a Searchable Country')


def choose_keyword():
	choose_keyword = Toplevel(rainmail)
	choose_keyword.title('Choose Keyword')
	choose_keyword.geometry('100x100')
	choose_keyword.attributes('-topmost', 'true')
	label_keyword = Label(choose_keyword, text='Enter Keyword and Press Enter')
	label_keyword.place(x=80,y=100)
	enter_keyword = Entry(choose_keyword, command=keyword_validate)
	enter_keyword.place(x=80,y=60)

def keyword_validate():
	search_keyword = enter_keyword.get()
	chosen_keyword = str(search_keyword)
	if (len(chosen_keyword) > 0):
		messagebox.showinfo(title='Info', message='You Have Chosen to Search: %s' %(chosen_keyword))
		choose_keyword.destroy()
	else:
		messagebox.showinfo(title='Info', message='You Have Not Input Anything')

	
	
def express_gui():
	express = Toplevel(rainmail)
	express.title('Express Mode')
	express.geometry('500x400')
	values_to_set = Menubutton(express, text='Values to Set', relief=RAISED)
	values_to_set.place(x=250,y=400)
	values_to_set_menu = Menu(values_to_set, tearoff=0)
	values_to_set_menu.add_command = (label='Choose What to Search', command=choose_keyword)
	values_to_set_menu.add_command = (label='Choose Country to Search', command=choose_country)
	
	
	google_search_url_default = 'https://www.google.' + chosen_country.lower() + '/search?hl=en'
	use_own_ip_default = True
	continue_last_scrape_default = False
	sel_browser_default = 'chrome'
	manual_captcha_solving_default = 'False'
	scrape_method_default = 'selenium'
	search_engines_default = ['google']
	print_results_default = 'summarize'
	num_results_per_page_default = 10
	num_workers_default = 1
	num_pages_for_keyword_default = 20
	maximum_workers_default = 20
	keywords = [ chosen_keyword ] 
	sleeping_ranges_default = {
		1:  (1, 2),
		5:  (2, 4),
		30: (10, 20),
		127: (30, 50),
	}
	google_sleeping_ranges_default = {
		1:  (2, 3),
		5:  (3, 5),
		30: (10, 20),
		127: (30, 50),
	}

	config = {
		'keywords':keywords,
		'google_search_url':google_search_url_default, 
		'use_own_ip':use_own_ip_default, 
		'continue_last_scrape':continue_last_scrape_default,
		'sel_bowser':sel_browser_default, 
		'manual_captcha_solving':manual_captcha_solving_default,
		'scrape_method':scrape_method_default,
		'search_engines':search_engines_default,
		'print_results':print_results_default,
		'num_results_per_page':num_results_per_page_default,
		'num_workers':num_workers_default,
		'num_pages_for_keyword':num_pages_for_keyword_default,
		'maximum_workers':maximum_workers_default,
		'search_offset':2,
		'sleeping_ranges':sleeping_ranges_default,
		'google_sleeping_ranges':google_sleeping_ranges_default

		}
	
	

	return config
	
def start_search(config):
	urls_to_process = deque()
	try:
		search = scrape_with_config(config)
	except GoogleSearchError as e:
		print(e)

	for serp in search.serps:
		print(serp)

		for link in serp.links:
			print(link)
			retrieved_url = str(link)
			end = len(retrieved_url) -1
			urls_to_process.append(retrieved_url[25:end])
	return urls_to_process

#funtion to extract email addresses from web pages

def process_urls(urls_to_process):

	processed_urls = set()  # a set of urls that have already been crawled
	emails = set()  # a set of extracted emails

	while len(urls_to_process) > 0:  # process urls one by one until we exhaust the queue

		url = urls_to_process.popleft()  # move next url from the queue to the set of processed urls
		processed_urls.add(url)
		parts = urlsplit(url)    # extract base url to resolve relative links
		base_url = "{0.scheme}://{0.netloc}".format(parts)
		path = url[:url.rfind('/')+1] if '/' in parts.path else url
		print("Processing %s" % url)
		try:
			response = requests.get(url)
		except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
		# ignore pages with errors
			continue

		new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))   # extract all email addresses and add them into a set
		emails.update(new_emails)
		soup = BeautifulSoup(response.text)     # create a beutiful soup for the html document

		for anchor in soup.find_all("a"):
			link = anchor.attrs["href"] if "href" in anchor.attrs else ''  # extract link url from the anchor

			if link.startswith('/'):   # resolve relative links
				link = base_url + link

			elif not link.startswith('http'):
				link = path + link

			if not link in urls_to_process and not link in processed_urls:   # add the new url to the queue if it was not enqueued nor processed yet
				urls_to_process.append(link)
	f = open('Rainmails.txt','w')    #indicate name of output file to write emails
	#sys.stdout = f
	#path= '/home/Desktop'  #for linux
	f.write(emails) 
	f.close()
	
	return emails
    

def prompt_gui():
	rainmail = Tk()
	rainmail.title('Rainmail GUI')
	rainmail.geometry('500x400')
	menubar = Menu(root)
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label='Exit', command=rainmail.quit)
	menubar.add_cascade(label='File', menu=filemenu)
	options = Menu(menubar, tearoff=0)
	options.add_command(label='Express Mode', command=express_gui)
	options.add_seperator()
	options.add_command(label='Normal Mode', command=user_gui)
	menubar.add_cascade(label='Select Mode', menu=options)
    
    
    
    
    
