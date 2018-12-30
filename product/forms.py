from django import forms

from .models import Product

CITIES = (
    ('adana', 'ADANA'),
    ('adiyaman', 'ADIYAMAN'),
    ('afyon', 'AFYON'),
    ('ağri', 'AĞRI'),
    ('aksaray', 'AKSARAY'),
    ('amasya', 'AMASYA'),
    ('ankara', 'ANKARA'),
    ('antalya', 'ANTALYA'),
    ('ardahan', 'ARDAHAN'),
    ('artvi̇n', 'ARTVİN'),
    ('aydin', 'AYDIN'),
    ('balikesi̇r', 'BALIKESİR'),
    ('bartin', 'BARTIN'),
    ('batman', 'BATMAN'),
    ('bayburt', 'BAYBURT'),
    ('bi̇leci̇k', 'BİLECİK'),
    ('bi̇ngöl', 'BİNGÖL'),
    ('bi̇tli̇s', 'BİTLİS'),
    ('bolu', 'BOLU'),
    ('burdur', 'BURDUR'),
    ('bursa', 'BURSA'),
    ('çanakkale', 'ÇANAKKALE'),
    ('çankiri', 'ÇANKIRI'),
    ('çorum', 'ÇORUM'),
    ('deni̇zli̇', 'DENİZLİ'),
    ('di̇yarbakir', 'DİYARBAKIR'),
    ('düzce', 'DÜZCE'),
    ('edi̇rne', 'EDİRNE'),
    ('elaziğ', 'ELAZIĞ'),
    ('erzi̇ncan', 'ERZİNCAN'),
    ('erzurum', 'ERZURUM'),
    ('eski̇şehi̇r', 'ESKİŞEHİR'),
    ('gazi̇antep', 'GAZİANTEP'),
    ('gi̇resun', 'GİRESUN'),
    ('gümüşhane', 'GÜMÜŞHANE'),
    ('hakkari̇', 'HAKKARİ'),
    ('hatay', 'HATAY'),
    ('iğdir', 'IĞDIR'),
    ('isparta', 'ISPARTA'),
    ('i̇stanbul', 'İSTANBUL'),
    ('i̇zmi̇r', 'İZMİR'),
    ('kahramanmaraş', 'KAHRAMANMARAŞ'),
    ('karabük', 'KARABÜK'),
    ('karaman', 'KARAMAN'),
    ('kars', 'KARS'),
    ('kastamonu', 'KASTAMONU'),
    ('kayseri̇', 'KAYSERİ'),
    ('kirikkale', 'KIRIKKALE'),
    ('kirklareli̇', 'KIRKLARELİ'),
    ('kirşehi̇r', 'KIRŞEHİR'),
    ('ki̇li̇s', 'KİLİS'),
    ('kocaeli̇', 'KOCAELİ'),
    ('konya', 'KONYA'),
    ('kütahya', 'KÜTAHYA'),
    ('malatya', 'MALATYA'),
    ('mani̇sa', 'MANİSA'),
    ('mardi̇n', 'MARDİN'),
    ('mersin','MERSİN'),
    ('muğla', 'MUĞLA'),
    ('muş', 'MUŞ'),
    ('nevşehi̇r', 'NEVŞEHİR'),
    ('ni̇ğde', 'NİĞDE'),
    ('ordu', 'ORDU'),
    ('osmani̇ye', 'OSMANİYE'),
    ('ri̇ze', 'RİZE'),
    ('sakarya', 'SAKARYA'),
    ('samsun', 'SAMSUN'),
    ('si̇i̇rt', 'SİİRT'),
    ('si̇nop', 'SİNOP'),
    ('si̇vas', 'SİVAS'),
    ('şanliurfa', 'ŞANLIURFA'),
    ('şirnak', 'ŞIRNAK'),
    ('teki̇rdağ', 'TEKİRDAĞ'),
    ('tokat', 'TOKAT'),
    ('trabzon', 'TRABZON'),
    ('tunceli̇', 'TUNCELİ'),
    ('uşak', 'UŞAK'),
    ('van', 'VAN'),
    ('yalova', 'YALOVA'),
    ('yozgat', 'YOZGAT'),
    ('zonguldak', 'ZONGULDAK'))

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
        'productname', 'quantity', 'location', 'bread_date', 'harvest_date', 'product_content', 'price', 'product_photo')
        widgets = {
            'bread_date': forms.DateInput(attrs={'type': 'date'}),
            'harvest_date': forms.DateInput(attrs={'type': 'date'}),
            'location': forms.Select(choices=CITIES)
        }

