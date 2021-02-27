# Data Engineering Masterclass

<p align="center"> <img src="https://pbs.twimg.com/profile_images/1341352412540530688/EJfGb11W_400x400.jpg"> </img></p>

Bu Repo [Data Engineering Masterclass (DEMC–201)](https://datamasterclass.zeministanbul.ist) eğitiminde verilen derslerin içeriklerini ve notlarını içermektedir.

**Tanım:** Data Engineering Masterclass (DEMC–201) veri odaklı teknolojik ürün geliştirme ekiplerinin veri mühendisliği ihtiyaçları gözetilerek hazırlanmış bir uzmanlık sınıfıdır. Bu uzmanlık sınıfı, data engineering alanında uzun yıllar çalışmış, deneyim sahibi yazılım geliştiriciler, veri mühendisleri, veri bilimcileri ve sistem mühendisleri tarafından hazırlanmıştır.

## Contributors

- Yasar Celep
- Çağrı Köz

## İçindekiler

<!-- TOC -->

- [Data Engineering Masterclass](#data-engineering-masterclass)
    - [Contributors](#contributors)
    - [İçindekiler](#i%CC%87%C3%A7indekiler)
- [Modül-1: Data Collection](#mod%C3%BCl-1-data-collection)
    - [Data Toplama](#data-toplama)
    - [API](#api)
    - [**Web Scraping**](#web-scraping)
    - [Loglama](#loglama)
        - [Loglamanın seviyeleri](#loglaman%C4%B1n-seviyeleri)
        - [Loglama yaparken:](#loglama-yaparken)
    - [Keywords:](#keywords)
    - [HTTP](#http)
    - [Restful Mimarisi](#restful-mimarisi)
        - [Diğer Metodlar](#di%C4%9Fer-metodlar)
    - [HTTP Status kodları](#http-status-kodlar%C4%B1)
        - [En sık karşılaşılan hata kodları](#en-s%C4%B1k-kar%C5%9F%C4%B1la%C5%9F%C4%B1lan-hata-kodlar%C4%B1)
    - [CURL](#curl)
        - [**Basit Curl Command Sözdizimi**](#basit-curl-command-s%C3%B6zdizimi)
        - [Derste kullanılan örnekler](#derste-kullan%C4%B1lan-%C3%B6rnekler)
        - [URL içerisindeki özel karakterler](#url-i%C3%A7erisindeki-%C3%B6zel-karakterler)
    - [GREP](#grep)
        - [Ders Örnekleri](#ders-%C3%B6rnekleri)
    - [DOM](#dom)
    - [Python Web Scraping](#python-web-scraping)
    - [Logging](#logging)
    - [Requests](#requests)
    - [BeautifulSoup4](#beautifulsoup4)
    - [Selenium](#selenium)
        - [**GISTLER**](#gistler)
- [Modül-2: Data Cleaning](#mod%C3%BCl-2-data-cleaning)
    - [Data Quality](#data-quality)
    - [AWK](#awk)
        - [En uzun satır](#en-uzun-sat%C4%B1r)
        - [".awk" uzantılı bir dosya olusturarak](#awk-uzant%C4%B1l%C4%B1-bir-dosya-olusturarak)
        - [karakter uzunluğundan fazla olan satırlar](#karakter-uzunlu%C4%9Fundan-fazla-olan-sat%C4%B1rlar)
        - [Şubat ayında kaç log düşmüş?](#%C5%9Fubat-ay%C4%B1nda-ka%C3%A7-log-d%C3%BC%C5%9Fm%C3%BC%C5%9F)
        - [HTTP Kodlarında analiz](#http-kodlar%C4%B1nda-analiz)
        - [IP Count](#ip-count)
    - [Mozilla ve Chrome Sayısı](#mozilla-ve-chrome-say%C4%B1s%C4%B1)
- [Modül-3: Data Storage](#mod%C3%BCl-3-data-storage)
    - [Veritabanları Databases](#veritabanlar%C4%B1-databases)
        - [İlişkisel Veritabanları Relational Databases](#i%CC%87li%C5%9Fkisel-veritabanlar%C4%B1-relational-databases)
        - [Key, Primary Key, Unique Key ve Foreign Key Tanımlamaları Constrains](#key-primary-key-unique-key-ve-foreign-key-tan%C4%B1mlamalar%C4%B1-constrains)
        - [**Primary Key Constraint**](#primary-key-constraint)
        - [**Unique Constraint**](#unique-constraint)
        - [**Foreign Key Constraint**](#foreign-key-constraint)
        - [**Default Constraint**](#default-constraint)
        - [**Check Constraint**](#check-constraint)
        - [**Query**](#query)
        - [**SQL**](#sql)
        - [**SQL Index**](#sql-index)
        - [Yatay ve Dikey Ölçeklenebilirlik:](#yatay-ve-dikey-%C3%B6l%C3%A7eklenebilirlik)
    - [ACID](#acid)
    - [Veritabanı Normalleştirmesi](#veritaban%C4%B1-normalle%C5%9Ftirmesi)
    - [Database Türleri](#database-t%C3%BCrleri)
    - [Database Caching](#database-caching)
        - [Veritabanı Database Önbelleğe Alma](#veritaban%C4%B1-database-%C3%B6nbelle%C4%9Fe-alma)
- [Module 4 - Day 1](#module-4---day-1)
    - [Socket](#socket)
        - [Python Socket Ornegi](#python-socket-ornegi)
    - [FTP File Transfer Protocol](#ftp-file-transfer-protocol)
        - [FTP RFC959 → https://tools.ietf.org/html/rfc959](#ftp-rfc959-%E2%86%92-httpstoolsietforghtmlrfc959)
    - [OSI Modeli](#osi-modeli)
    - [IETFInternet Engineering Task Force](#ietfinternet-engineering-task-force)
        - [HTTP RFC2616 → https://tools.ietf.org/html/rfc2616](#http-rfc2616-%E2%86%92-httpstoolsietforghtmlrfc2616)
    - [IP Internet Protocol](#ip-internet-protocol)
        - [URL RFC1738 → https://tools.ietf.org/html/rfc1738](#url-rfc1738-%E2%86%92-httpstoolsietforghtmlrfc1738)
    - [Further Reading](#further-reading)
    - [TCP Transmission Control Protocol](#tcp-transmission-control-protocol)
    - [SSH Güvenli Kabuk](#ssh-g%C3%BCvenli-kabuk)
    - [SFTP](#sftp)
        - [SSH ile SFTP Kullanımı](#ssh-ile-sftp-kullan%C4%B1m%C4%B1)
        - [SFTP Komutları](#sftp-komutlar%C4%B1)
    - [SCP](#scp)
        - [**SCP Nasıl Kurulur?**](#scp-nas%C4%B1l-kurulur)
        - [SCP Parameterleri Nelerdir?](#scp-parameterleri-nelerdir)
        - [**SCP ile Dosya Transferi Nasıl Yapılır?**](#scp-ile-dosya-transferi-nas%C4%B1l-yap%C4%B1l%C4%B1r)
    - [SOAP](#soap)
        - [Bir SOAP mesajının yapısı](#bir-soap-mesaj%C4%B1n%C4%B1n-yap%C4%B1s%C4%B1)
    - [Keywords, Tools:](#keywords-tools)

<!-- /TOC -->

# Modül-1: Data Collection

**İçerik:** API'lar, loglama, sensory data, web scraping.

**Anahtar sözcükler:** JSON, XML, HTTP, HTML, DOM, grep, RegExp.

**Araçlar:** Postman, log4j, python-logging, BeautifulSoup, Jsoup, Selenium

## Data Toplama

Information retrieval, web-scraping, alınan API dataları bunlara örnektir.

## API

İki sistemin arasında nasıl konusacağını belirleyen bir yapıdır. Belirli spesifik tipte akış ve veri sunar. Belirli bir rate içerisinde olmaktadır. Belirli sorgulara karşı belirli bir data parçası geçmektedir, tüm sistemin veri akışını sağlamak için değildir.

Farklı formatlarda dönüşü olabilir. **.xml** veya **json** olabilir. JSON oldukça popüler, şu an genel akım json üzerinden çalışıyor.

Sensörlere ufak bilgisayarlar denilebilir, genellikle amaca yönelik sadece görevini yapan pil ömrü yüksek olan mini cihazlardır. Üzerindeki datayı merkeze alınarak kullanılır. _Aslında **edgedeki** cihazlardan bahsediliyor._

## **Web Scraping**

Görece API'ye göre verinin elde edilmesi daha zordur. Veri genellikle dağınık biçimde web'de bulunur, veri toplama prosesi kullanıcının bu rotaları tanımlayarak gerçekleştirmesiyle sağlanır. Dezavantajı ise belirli bir protokolun olmaması, **_challenging but fun!_**

Değişikliklerde call denilen bir sistem kullanılabilir. İki taraf için yüklü bir sistem olduğundan dolayı istenilen bir yöntem değildir. Bir websitesi için yazılan scraping scriptleri her gün değişmez bu yüzden büyük bir problem yaratmayacaktır. Subscribe yönteminde webhook gibi yöntemler kullanılabilir fakat karşı tarafın da sizi tanıyor olması gerek.

## Loglama

Genellikle problemler belirli bir zaman diliminden itibaren veya geçmişten gelir. Anlık sorunları ve sistemin ne yaptığını en ince detayın kadar görmek için **loglama** kullanılır.

**Pro Tip:** Her satırın loglanmasının anlamı yoktur. Bu yöntem oldukça dikkat dağıtıcı ve kullanışsız olabilir. Bunun için loglamanın seviyeleri vardır.

### Loglamanın seviyeleri

Low level, critical, warning, info gibi seviyeler vardır.

- **Debug:** Sorunların teşhisi için debugging gibi düşünebiliriz. Ayrıntılı bilgilere ihtiyacımız vardır.
- **Info:** Beklenen çıktılarımızdır.
- **Warning:** Yazılım hala çalışıyordur ama uyarı çanları çalmaktadır.
- **Error:** Yazılım ciddi bir sorunla karşılaştı ve görevini yerine getiremedi.
- **Critical**: Programın işlevini yerine getiremeyecek bir sorunla karşılaşmasıdır.

**Pro Tip:** _grep_ komutuyla dosyaların içerisindeki belirli kelimeyi arar. _(e.g. 2 şubat tarihinde bir problem oldu ve onun bulunması için kullanılabilir.)_

### Loglama yaparken:

- **Timestamp:** Tarih, zaman damgası bulunması ve ne zaman olduğuna dair bilgi vermesi açısından önemlidir.
- **Logging Level:** Hatanın derecesi, nedeni veya olayın ne olduğuna dair seviyenin belirtilmesi gerekmektedir.
- **API Bilgisi:** Sensor ID, hangi fonksiyon, genel bilgiler içermelidir.
- **Logun içeriği:** value, logun içeriği json, plain text, xml olabilir.

Logları tek büyük bir dosyada depolamak giderek büyüyen bir dosya olacağından dolayı mantıklı değildir. Databasede tablo olarak saklanabilir böyle bir durumda select süresi giderek uzayacaktır. Sistemi optimize edebilmek için aktif olanlar veya olmayanlar yahut arşivlenmiş gibi farklı parçalara bölmek zaman açısından yararlı olacaktır.

Bu gibi büyük çaplı verilerde hızlı işlemler yapabilmek için **Hadoop** gibi özelleşmiş sistemler bulunmaktadır. Temelde depolanan ve güncel olarak kullanılan iki parçaya bölmek mantıklı olacaktır.

## Keywords:

- **POSTMAN:** API’ları paylaşmak, test etmek, dokümante etmek, monitör etmek için kullanılır. En öne çıkan özelliği tüm bunlar için çok kullanışlı bir arayüz sunmasıdır.
- **Log4j:** Java uygulamalarında kullanılacak loglama kütüphanesidir.
- **python-logging:** Log4j'in python versiyonu
- **BeautifulSoup:** BeautifulSoup, HTML veya XML dosyalarını işlemek için oluşturulmuş bir kütüphanedir.
- **Jsoup:** BS4'un java versiyonu
- **Selenium:** Selenium, bilgisayarınıza yükleyeceğiniz bir driver yardımı ile ekrana chrome, firefox gibi bir tarayıcı açarak, gerçek bir insan gibi istediğiniz tüm işlemleri programlama dili yardımıyla çalıştırmanızı sağlayan bir araçtır.

## HTTP

“http”, bilginin sunucudan kullanıcıya nasıl ve ne şekilde aktarılacağını gösteren protokoldür. İnternet ağında sunucular ve kullanıcılar arasında nasıl bir veri alışverişi olacağı hakkında kurallar vardır. Bu düzeni sağlayan protokol de HTTP’dir.internet sitesine girmek için adres çubuğuna sitenin adresini yazdığınız vakit HTTP ile sunucuya bir istek gönderilir ve sunucu bu isteğe cevap verdiği vakit internet sitesinin verileri size gelir.

## Restful Mimarisi

RESTful servisler veri iletiminde farklı HTTP metotlarını kullanmaktadır. Yapılan HTTP request’i için çağrılan URL ile beraber HTTP method bilgisi bahsi geçen 4 metottan biri olarak seçilir ve sunucu yapılan talebin kayıt üzerine nasıl etki edeceğini buna göre belirler.

- **GET:** Veri listeleme - veri görüntülemek için kullanılır.

- **POST:** Veri eklemek için kullanılır.

### Diğer Metodlar

- **PUT:** Veriyi Güncelleme isteği olarak kullanılır.
- **PATCH:** Verinin sadece bir parçasını güncellemek için kullanılır. Örneğin bir issue'nun durumunun aktiften çözüldü haline getirilmesi.
- **DELETE:** Veriyi silmek için kullanılır.
- **OPTIONS:** Bir  api urline Options isteği yapıldığında o url in hangi istekleri kabul ettiği bilgisi verilir.

> [httpbin.org](http://httpbin.org) sitesinden bu denemeler yapılabilir

## HTTP Status kodları

Kodlara linkten ulaşılabilir. [https://www.argenova.com.tr/http-durum-ve-hata-kodlari](https://www.argenova.com.tr/http-durum-ve-hata-kodlari)

### En sık karşılaşılan hata kodları

- **HTTP 200 (OK):** yanıtın başarılı olduğunu gösterir. Yani, istemci ile sunucu arasındaki iletişim herhangi bir hata olmadan sorunsuz bir şekilde yürütülmüştür.
- **HTTP 404 (Not Found):** istenen kaynağın sunucu tarafından bulunamayacağı anlamına gelir. Bu, geçici bir aksaklıktan kaynaklanıyor olabilir ve gelecekte başka bir istekte bulunulursa kaynak kullanılabilir olabilir. Çoğunlukla, 404'e götüren bağlantılara genellikle bozuk bağlantılar denir.
- **HTTP 502 (Bad Gateway):** sunucunun proxy olarak hareket ederken istekte bulunurken sunucudan geçersiz bir yanıt aldığını gösterir.

## CURL

Çoğu Unix bazlı sistemde mevcut olan bir komuttur ve “Client URL”nin kısaltılmışıdır. Curl komutları URL’lerin bağlanabilirliğini kontrol etmek ve veri transferi için harika bir araç olarak kullanılmak için üretilmiştir.

### **Basit Curl Command Sözdizimi**

Hadi Curl komutlarını nasıl kullanacağımızı öğrenelim. Curl’ün basit sözdizimi böyledir:

```
curl [OPTIONS] [URL]
```

Curl’ün en basit kullanımı bir sayfanın içeriklerini göstermektir. Aşağıdaki örnek testalanadi.com’un ana sayfasının içeriklerini gösterecektir:

```
curl testalanadi.com
```

### Derste kullanılan örnekler

```jsx
curl -x GET "http://httpbin.org/get" -H "accept: application/json"
```

> [ipify.org ](https://api.ipify.org/?format=json&param=2)

### URL içerisindeki özel karakterler

- **"?":** "sorgu parametreleri" olarak adlandırılır. Sunucu, bu ek bilgilere dinamik olarak cevap verebilir ve göreceğiniz sayfayı bu parametrelere göre oluşturabilir. Bu, sayfadaki bir alana otomatik olarak yazılmış bir bilgi veya bir arama motorundaki arama sorgunuz olabilir.
- **"%":** "Escaping" olarak adlandırılan bu işlem, URL'deki boşluk karakterinin soruna yol açmaması için alternatif bir biçime dönüştürülmesidir. Örneğin + yazdığınızda bu karakter, %3F ile değiştirilir.
- **"=":** anahtar-değer çiftlerini temsil eder. Anahtar-değer çiftine bir örnek, sayfa=4 olabilir. Burada "sayfa" anahtar, "4" ise değerdir.

## GREP

Elimizdeki loglarda buradan terminal ekranında hızlıca sorgularımız getirebiliriz. Logların güzel şekilde tutulması işimizi kolaylaştırıyor. Pipe ile çok daha etkin kullanım yöntemleri mevcut.

`grep "42.236.10.125" \* —color | wc -lw`

### Ders Örnekleri

` grep "GET" \* —color`

`grep "42.236.10.125" \* —color | wc -lw`

` grep "mozilla" \* —color`

## DOM

HTML için kullanılan doküman nesne modelidir. HTML Elementlerini objeler olarak, HTML elementlerinin tüm özelliklerini, HTML elementlerine erişmek için metotları, tüm HTML elementleri için olayları tanımlar. Diğer bir deyişle HTML DOM yeni elementler eklemek, elementleri değiştirmek veya silmek için kullanılır.

![https://biltektasarim.com/biltek3/dosyalar/kcfinder/images/transparent_dom.png](https://biltektasarim.com/biltek3/dosyalar/kcfinder/images/transparent_dom.png)

```html
<html>
  <head>
    <title></title>
    <style></style>
  </head>
  <body>
    <div>
      <p>Cobanov</p>
    </div>
  </body>
</html>
```

## Python Web Scraping

## Logging

**Kaynak**: [https://medium.com/@umut.boz/python-logging-a8fdd36fee7](https://medium.com/@umut.boz/python-logging-a8fdd36fee7)

Loglama, bir sistemdeki hareketliliği kaydetmek için kullanılan yapıdır. Python standart kütüphanesi içinde loglama için çok güçlü bir kütüphane barındırır. Bu kütüphane ile geliştirdiğimiz programlarda hata ayıklamak aynı zamanda ifadeleri yazdırmak için loglama kullanabiliriz.

## Requests

**Kaynak**: [https://medium.com/python/python-requests-modülü-4af79ebdb8c8](https://medium.com/python/python-requests-mod%C3%BCl%C3%BC-4af79ebdb8c8)

Python, standart modüllerinin yanında harici yüzlerce kullanışlı modül ile birlikte çok güçlü bir dil. Bu gücü veren harika modüller var bunlardan biri de **Requests modülü.**

Bu modül ile web üzerindeki isteklerinizi yöneteceksiniz. Mesela bu modül ile API entpointlerine PUT, DELETE, POST gibi istekler atabilirsiniz.

## BeautifulSoup4

**Kaynak**: [https://medium.com/@nuriyavuz2.71/python-beautifulsoup-modülü-689ef499ee16](https://medium.com/@nuriyavuz2.71/python-beautifulsoup-mod%C3%BCl%C3%BC-689ef499ee16)

BeautifulSoup, HTML veya XML dosyalarını işlemek için oluşturulmuş güçlü ve hızlı bir kütüphanedir.

Bu modül ile bir kaynak içerisindeki HTML kodlarını parse edip,botlar yazabiliriz.

## Selenium

**Kaynak**: [https://www.sinanerdinc.com/python-selenium-modulu-kullanimi-1](https://www.sinanerdinc.com/python-selenium-modulu-kullanimi-1)

Selenium, bilgisayarınıza yükleyeceğiniz bir driver yardımı ile ekrana chrome, firefox gibi bir tarayıcı açarak, gerçek bir insan gibi istediğiniz tüm işlemleri programlama dili yardımıyla çalıştırmanızı sağlayan bir araçtır.

**Homework:** Vatan bilgisayardaki ürünlerin görsellerin veya isimleri ile ücretlerini scrap edebilirsin.

**Ödev Linki:** [https://github.com/cobanov/dataeng-bootcamp/blob/main/homeworks/scraping_homework.py](https://github.com/cobanov/dataeng-bootcamp/blob/main/homeworks/scraping_homework.py)

### **GISTLER**

- **BS4**: [https://gist.github.com/sirin/695abacaa207ad7af20f18c946d19858](https://gist.github.com/sirin/695abacaa207ad7af20f18c946d19858)
- **Selenium**: [https://gist.github.com/sirin/0e1491163b8f485a476e0991ad228b86](https://gist.github.com/sirin/0e1491163b8f485a476e0991ad228b86)
</details>

---

# Modül-2: Data Cleaning

**İçerik:** Parsing, Duplicate Elimination, Ensuring Quality: Validity-Accuracy-Completeness, Statistical Analysis, Unix-Linux Terminal

**Anahtar sözcükler:** Bash, GNU Awk, GNU sed, jq, CSV files, JSON

**Araçlar:** Shell(s), Excel, R

## Data Quality

**Kaynak:** [https://smartbridge.com/data-done-right-6-dimensions-of-data-quality/](https://smartbridge.com/data-done-right-6-dimensions-of-data-quality/)

1. **Completeness (Tamlık):** Verinin kendi içinde bütünlüğünü temsil eder. (e.g. eksik veri olmaması.)
2. **Consistency (Tutarlılık):** Veri kümeleri arasız tutarsızlık, imbalanced durumlarının olmaması.
3. **Confirmity (Uygunluk):** Her datanın olması gereken formatta tutulması, kolonların veritipleri uygun olmalıdır. (e.g. tarih verisinin tarih formatında olması, ağırlığın integer olması)
4. **Accuracy (Doğruluk):** Verilerin gerçek dünya nesnesini veya açıklanan bir olayı doğru şekilde yansıttığı derecedir.
5. **Integrity (Bütünlük):** Birbirine ilişkili olan iki veri arasında tutarlılık olup olmaması.
6. **Timeliness(Zamanlılık):** Zamanlılık, bilginin beklendiğinde ve ihtiyaç duyulduğunda mevcut olup olmadığını belirtir. Verilerin güncelliği çok önemlidir.

**CrispDM:** Cross-industry standard process for data mining Not AL foto ekle

**Kaynak:** [https://www.proglobalbusinesssolutions.com/six-steps-in-crisp-dm-the-standard-data-mining-process/](https://www.proglobalbusinesssolutions.com/six-steps-in-crisp-dm-the-standard-data-mining-process/)

awk ve gnu-sed not al

```bash
brew install awk;
brew install gnu-sed;
```

```bash
cat access-log-2.txt | grep robots.txt | wc -l
```

## AWK

```bash
awk '/^42/ {print $0}' access-log-2.txt | wc -l
# 547
```

slash regex'in başı ve sonu

filtre kısmı default işlem print 0'dır

### En uzun satır

```bash
awk '{if (length($0) > max) max=length($0)} END {print max}' access.log.2.txt
```

### ".awk" uzantılı bir dosya olusturarak

```bash
awk -f script.awk file-name.txt
```

### karakter uzunluğundan fazla olan satırlar

```bash
awk 'length($0) > 1000' file-name.txt | wc -l
```

$0

$1, $2, $3 sırasıyla boşlukla ayrıldıktan sonraki alanlar

log dosyasında her token bir bölümü ifade ediyor

tail: son 10 satır

head: ilk 10 satır

-n flag ile satır sayısı belirlenebilir

### Şubat ayında kaç log düşmüş?

herhangi bir yerde feb yazabilir bakacağımız yer 4. tokende feb yazmalı

```bash
awk '$4 ~ /Feb/' file-name.txt | wc- l
```

### HTTP Kodlarında analiz

```bash
awk '$9 ~ /200/' file-name.txt | wc -l
```

### IP Count

```bash
{
	freq[$1]++
}

END {
	for (word in freq)
		printf "%d\t%s\n", freq[word],  word
}
```

```bash
awk '{print $12}' file-name.txt | uniq ;
# Cozulecek awk '{print $12}' file-name.txt | awk '{split($0, a, "/")}' | uniq
```

## Mozilla ve Chrome Sayısı

```bash
awk '{print $12}' file-name.txt | grep 'Chrome' | wc -l
```

# Modül-3: Data Storage

**İçerik:** SQL, Relational Databases, Document Databases, Time Series Databases, Graph Databases, Key-value Stores, Data Lakes

**Anahtar sözcükler:** SQL Query, Index, Database normalization, Database optimization, Designing Data Infrastructure

**Araçlar:** MySQL, MariaDB, PostgreSQL, Redis, MongoDB, Neo4J

## Veritabanları (Databases)

Veri tabanları birbirleriyle ilişkili bilgilerin depolandığı alanlardır. Bilgi artışıyla birlikte bilgisayarda bilgi depolama ve bilgiye erişim konularında yeni yöntemlere ihtiyaç duyulmuştur. Veri tabanları; büyük miktardaki bilgileri depolamada geleneksel yöntem olan ‘‘dosya-işlem sistemine’’ alternatif olarak geliştirilmiştir.

### İlişkisel Veritabanları (Relational Databases)

- **MySQL:** Çoklu iş parçacıklı (multi-threaded), çok kullanıcılı (multi-user), hızlı ve sağlam (robust) bir veri tabanı yönetim sistemidir.

- **PostgreSQL**, veritabanları için ilişkisel modeli kullanan ve [SQL](https://tr.wikipedia.org/wiki/SQL) standart sorgu dilini destekleyen bir [veritabanı yönetim sistemidir](https://tr.wikipedia.org/wiki/Veritaban%C4%B1_y%C3%B6netim_sistemi). PostgreSQL aynı zamanda iyi performans veren, güvenli ve geniş özellikleri olan bir [Veri Tabanı Yönetim Sistemi](https://tr.wikipedia.org/wiki/Veri_Taban%C4%B1_Y%C3%B6netim_Sistemi)'dir. PostgreSQL ücretsiz ve açık kodludur.

- **MariaDB** [ilişkisel veritabanı sistemi](https://tr.wikipedia.org/wiki/%C4%B0li%C5%9Fkisel_veri_taban%C4%B1_y%C3%B6netim_sistemi) olan [MySQL](https://tr.wikipedia.org/wiki/MySQL)'in kaynak kodundan türemiş, [GNU Genel Kamu Lisansı](https://tr.wikipedia.org/wiki/GNU_Genel_Kamu_Lisans%C4%B1) altında dağıtılarak ücretsiz olarak kullanılabilen, geliştirilmesi ve bakımı topluluk tarafından sürdürülen veritabanıdır. MySQL, önde gelen [açık kaynaklı](https://tr.wikipedia.org/wiki/A%C3%A7%C4%B1k_kaynak) yazılım sistemi olarak ticari bir şirket olan [Oracle](https://tr.wikipedia.org/wiki/Oracle) tarafından satın alındıktan sonra MySQL'in ilk geliştiricileri tarafından Monty AB çatısı altında yine açık kaynak olarak MariaDB adıyla yola devam edeceği duyurulmuş ve oldukça ilgi görmüştür.

### Key, Primary Key, Unique Key ve Foreign Key Tanımlamaları (Constrains)

**_Kaynak_**: [\*https://ceaksan.com/tr/primary-unique-foreign-key](https://ceaksan.com/tr/primary-unique-foreign-key),\* [https://medium.com/gokhanyavas/constraints-kullanımı-26bb89dbcd2b](https://medium.com/gokhanyavas/constraints-kullan%C4%B1m%C4%B1-26bb89dbcd2b)

**Key (anahtar)** veri tabanı içeriğinde, bir veya daha fazla alanın bir satırı nitelemesi amacıyla tanımlanması olarak özetlenebilir. Bir anahtar farklı amaçlar doğrultusunda kullanılabilecek **Unique Key(Tekil Anahtar), Primary Key(Birincil Anahtar)** ve **Foreign Key (Yabancı Anahtar)** gibi özel bir tip ile tanımlanabilir.

1. Primary Key Constraint
2. Unique Constraint
3. Foreign Key Constraint
4. Default Constraint
5. Check Constraint

### **Primary Key Constraint**

Birincil anahtar kısıtlayıcısıdır. Her tabloda bir adet bulunabilir. Girilen her değerin farklı olması anlamına gelmektedir. Yani eşsiz kayıtlar tutmakta kullanılır. Bu alanlar NULL değere sahip olamazlar. Genelde otomatik artan sayılar için kullanılırlar. Otomatik arttırma **Identity** komutuyla gerçekleştirilir. **Identity** komutundan sonra işlemin kaçtan başlayacağı ve kaçar kaçar artacağı belirtilir. Identity(1,1) 1'den başlayacağını ve 1'er 1'er artacağını gösterir.

### **Unique Constraint**

Tablodaki bir sütünün benzersiz olmasını istediğimiz durumlarda kullanırız. Örnek vermek gerekirse, T.C Kimlik numaraları, Banka Hesap Numaraları gibi vs. Primary key den farkı ise Unique key bir tabloda birden fazla olmasıdır, primary key ise tabloda sadece 1 adet olabilir. Unique olarak tanımlanmış bir alan NULL olabilir. Değeri NULL’dan farklı olacak olursa kesinlikle daha önce girilen değerlerden farklı olmak zorundadır.

### **Foreign Key Constraint**

Yabancıl Anahtar anlamına gelen bu kısıtlayıcı tabloları ilişkilendirme de kullanılır. Yabancıl anahtar ile kısıtlanan tablodaki sütun diğer tablodaki sütun ile kısıtlanmış olur. Kod tarafında eşleştirme işlemi aşağıdaki biçimde yapılır;

### **Default Constraint**

Varsayılan kısıtlayıcı demektir. Tablodaki herhangi bir alan için girilmesi gereken değerin atanmasıdır. INSERT komutu için geçerlidir. Örnek olarak bir kayıt eklendiğinde, kaydın eklenme zamanını default olarak belirtebiliriz.

### **Check Constraint**

Kontrol Kısıtlayıcısı anlamına gelmektedir. Yani istediğimiz biçime göre verilerin girilmesini sağlar. Örneğin T.C Kimlik NO alanına 11 karakterin girilmesini sağlayabiliriz.

### **Query**

Türkçe karşılığı “sorgu” olan Query, basitçe, bilgi için yapılan bir istektir.

### **SQL**

_(İngilizce "Structured Query Language", Türkçe: Yapılandırılmış Sorgu Dili)_ verileri yönetmek ve tasarlamak için kullanılan bir dildir. SQL, kendisi bir programlama dili olmamasına rağmen birçok kişi tarafından programlama dili olarak bilinir. SQL herhangi bir veri tabanı ortamında kullanılan bir alt dildir. SQL ile yalnızca veri tabanı üzerinde işlem yapılabilir; veritabanlarında bulunan sistemlere bilgi ekleme, bilgi değiştirme, bilgi çıkarma ve bilgi sorgulama için kullanılmaktadır. Özellikle de ilişkisel veritabanı sistemleri üzerinde yoğun olarak kullanılmaktadır. SQL'e özgü cümleler kullanarak veri tabanına kayıt eklenebilir, olan kayıtlar değiştirilebilir, silinebilir ve bu kayıtlardan listeler oluşturulabilir.

### **SQL Index**

SQL indekslemenin amacı işlenen verinin daha az veri okunarak sorgu sonucunun daha kısa zamanda getirilmesini sağlamaktır. Indeksleme kullanarak tablonun tamamını okumaktansa oluşturacağımız indeks key i aracılığı ile okumak istediğimiz kayıda ulaşabilmemiz daha hızlı bir şekilde mümkün olacaktır. Bu sayede tamamlanması saatler süren sorgunun uygun indeksler kullanılarak saniyeler içinde getirilmesini sağlayabiliriz. _Kaynak: [https://medium.com/fullstackturkiye/sql-indexing-nedir-nasıl-çalışır-588be1f43029](https://medium.com/fullstackturkiye/sql-indexing-nedir-nas%C4%B1l-%C3%A7al%C4%B1%C5%9F%C4%B1r-588be1f43029)_

### Yatay ve Dikey Ölçeklenebilirlik:

**Kaynak**: [http://www.ilterismutlu.com/yatay-vs-dikey-olceklenebilirlik-horizontally-vs-vertically-scalable-scalability/](http://www.ilterismutlu.com/yatay-vs-dikey-olceklenebilirlik-horizontally-vs-vertically-scalable-scalability/)

**Dikey Ölçeklenebilirlik Nedir ?**

Sistemin/Veritabanının Dikeyde ölçeklenebilir olması (dikey ölçeklenebilirlik, vertically scalable, scale up); bir tane çok güçlü aynı zamanda pahalı bir makine/donanım kullanılmasıdır. Dikey Ölçeklenebilir sistemlerde donanım kısıtları mevcuttur. Örneğin mevcut sisteminizin CPU frekansını 5 ghz yapamazsınız veya 1 tb ram yapamazsınız.

Yatay ölçeklenebilirlikte yüzlerce, binlerce makinelik server (sunucu) ağı kurulabilir. Yatay ölçeklenebilirliğin yönetimi dikey ölçeklenebilirliğe göre daha zordur.Sonuçta onlarca veya yüzlerce makinayı yönetmek, tabi ki tek bir makinayı yönetmekten daha zordur.

**Yatay Ölçeklenebilirlik Nedir ?**

Sistemin/Veritabanının Yatayda ölçeklenebilir olması (horizontally scalable, scale out); ucuz ve çok sayıda makinenin aynı anda kullanılması anlamına gelir. Yatay ölçeklenebilirlik sayesinde yedeklilik de performans artışı da sağlanabilir.

## ACID

**Kaynak:** [https://medium.com/cloud-and-servers/acid-nedir-53f729f2bbb2](https://medium.com/cloud-and-servers/acid-nedir-53f729f2bbb2)\*

ACID, ilişkisel veritabanlarındaki Transaction için tanımlanmış özellik setidir.

Transaction için olarak verilen örnek bir banka hesabından başka bir banka hesabına paranın transfer edilmesi olarak anlatılabilir. Burada 2 hesap gönderici ve alıcının hesabı üzerinde mantıksal bir operasyon gerçekleştiriliyor. Bu işleme **_Transaction_** deniyor.

Bu transaction başarılı bir şekilde gerçekleşebilmesi için ACID ilkelerine uyması gerekmektedir.

- Atomicity
- Consistency
- Isolation
- Durability

**Atomicity:** Transaction işlemini bir bütün olarak görür. İşlem sırasında birden fazla veritabanı/tablodaki verinin güncellenmesi gerçekleşiyor ise tüm bunların hepsi birden başarılı olacaktır veya başarısız olacaktır

- Veritabanları erişilemez olabilir.
- Network problemi olabilir.
- Herhangi bir hata oluşabilir.

Bu durumda işlem geçersiz sayılacaktır.

**Consistency(Tutarlılık):** Transaction işlemi sonucunda veritabanındaki verinin geçerli durumunun, bir sonraki geçerli duruma geçmesidir. Özetle Transaction tam anlamı ile gerçekleşinceye kadar (constraints, cascades, triggers) işlemden etkilenen verilerin değerlerinin bir önceki geçerli değeri vermesidir.

**Isolation:** Aynı anda aynı veri üzerinde birden fazla Transaction değiştirme gereksinimi olabilir. Transaction’ların birbirlerinin işlemlerinden etkilenmemesi için işlemler Seri olarak yapılması gerekir. Transaction sırasında ilgili ve etkilenecek veri setleri kilitlenir. Taki işlem başarılı ve başarısız olarak sonuç dönünceye kadar.

**Durability(Dayanıklılık):** Transaction sırasında fiziksel veya işlemsel bir hata olması durumunda sistemin kendisini bir önceki geçerli veri durumuna döndürebilme kabiliyetidir.

## Veritabanı Normalleştirmesi

**Kaynak:** [https://www.lifeacode.com/sql-dersleri/rdbms-nedir.html](https://www.lifeacode.com/sql-dersleri/rdbms-nedir.html)\*

Veritabanı normalleştirmesi, bir veritabanında verileri verimli bir şekilde düzenleme işlemidir. Bu normalleşme sürecinin iki nedeni var

- Yedekli verileri ortadan kaldırmak, örneğin aynı verileri birden fazla tabloda saklamak.
- Veri bağımlılıklarının sağlanması mantıklı.

Her iki sebep de, bir veri tabanının tükettiği alanı azalttığı ve verilerin mantıksal olarak depolanmasını sağladığı için değerli hedeflerdir.

**Normalizasyon,** iyi bir veritabanı yapısı oluşturmanızda size yardımcı olan bir dizi kılavuzdan oluşur.

Normalizasyon kuralları normal formlara ayrılır; Bir formu, bir veritabanı yapısının biçimi veya biçimi olarak düşünün. Normal formların amacı, veritabanı yapısını organize etmektir, böylece ilk normal formun kurallarına, sonra ikinci normal forma ve son olarak üçüncü normal forma uygundur.

Daha fazla almak ve dördüncü normal forma, beşinci normal forma ve benzerlerine gitmek sizin seçiminizdir, ama genel olarak, üçüncü normal form fazlasıyla yeterlidir.

- İlk Normal Form (1NF)
- İkinci Normal Form (2NF)
- Üçüncü Normal Form (3NF)

## Database Türleri

![https://www.tutorialspoint.com/assets/questions/images/113180-1532341943.jpg](https://www.tutorialspoint.com/assets/questions/images/113180-1532341943.jpg)

## Database Caching

**Kaynak:** [https://www.beyaz.net/tr/guvenlik/makaleler/onbellege_alma_caching_nedir.html](https://www.beyaz.net/tr/guvenlik/makaleler/onbellege_alma_caching_nedir.html)\*

Önbellek, geçici bir veri alt kümesini depolayan yüksek hızlı veri depolama katmanıdır. Önbelleğe alma, daha önce alınan veya hesaplanan verinin verimli bir şekilde yeniden kullanılmasını sağlar. Önbellekleme yöntemi ile ilgili verilerin sonraki süreçte talep edildiğinde, verilere birincil depolama konumundan erişildiği için daha yüksek bir performans elde edilir.

Bir önbellekteki veriler genellikle RAM gibi donanımlarlarda saklanır ve veriye erişmek için bir yazılım üzerinden bağlantı kurulması gerekebilir. Önbelleğe alma işleminin amacı altta bulunan yavaş depolama katmanına erişme gereksinimini mimumuma indirerek veri erişim performansını arttırmaktır.

**Önbelleğe Alma Sisteminin Faydaları:** Uygulama performansı arttırılır.Veritabanı maliyeti düşürülür.Arka uçtaki yük azaltılır.Tahmin edilebilir performans sağlanır.Veritabanı bağlantı noktaları ortadan kaldırılır.Okuma verimini arttırır.

### Veritabanı (Database) Önbelleğe Alma

Web uygulamasında kullanılan veritabanının hız ve verimlilik performansı, web uygulamasının performansı için büyük bir etkendir. Veritabanının önbelleğe alınması, uygulama performansını etkileyen arka uç veritabanlarından veri alışveriş sonucu doğacak gecikmelerin azaltılmasını sağlar.

# Module 4 - Day 1

## Socket

**Soket**, [TCP/IP](https://tr.wikipedia.org/wiki/TCP/IP)'de, [veri](https://tr.wikipedia.org/wiki/Veri) iletişimi için gereken iki bilgi olan [IP adresi](https://tr.wikipedia.org/wiki/IP_adresi) ve [port](https://tr.wikipedia.org/wiki/Port) numarasının yan yana yazılmasıyla oluşan [iletişim](https://tr.wikipedia.org/wiki/%C4%B0leti%C5%9Fim_protokol%C3%BC) kanalıdır. Örneğin, **192.168.1.1** makinesine **23** numaralı porttan yapılmış olan bir bağlantı **192.168.1.1:23** şeklinde yazılır.

Aynı zamanda, [programlamada](https://tr.wikipedia.org/wiki/Programlama) bir makineye bağlantı açıldığında buna "**soket açma**" denir. Bir soket açılınca, sistem programcıya IP adresi ve port numarasını verdiği için bu isimlendirme ortaya çıkmıştır.

Uygulama servisi olan bilgisayarlar başlangıçta soketleri dinlemeyi kurarlar. İletişim halindeki sistemler arasında bir bağlantı kurulduğunda, her bir bağlantı için bir soket oluşturulur. İşletim sistemi gelen IP paketlerini soket adresine göre uygun uygulama veya servise yönlendir

### Python Socket Ornegi

[Kaynak](https://realpython.com/python-sockets/)

**echo-server.py**

```python
#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
```

**echo-client.py**

```
#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
```

## FTP (File Transfer Protocol)

Kaynak: [https://tr.wikipedia.org/wiki/Dosya_aktarım_iletişim_kuralı](https://tr.wikipedia.org/wiki/Dosya_aktar%C4%B1m_ileti%C5%9Fim_kural%C4%B1)

**Dosya aktarım iletişim kuralı**, ([İngilizce](https://tr.wikipedia.org/wiki/%C4%B0ngilizce): **F**ile **T**ransfer **P**rotocol; **FTP**), bir [veri](https://tr.wikipedia.org/wiki/Veri) yığınının - [ASCII](https://tr.wikipedia.org/wiki/ASCII), [EBCDIC](https://tr.wikipedia.org/wiki/EBCDIC), ve binary- bir uç aygıttan diğerine iletimi için kullanılmaktadır.

Bir [dosyayı](https://tr.wikipedia.org/wiki/Dosya) [FTP](https://tr.wikipedia.org/wiki/FTP) kullanarak başka bir [TCP/IP](https://tr.wikipedia.org/wiki/TCP/IP) ağı üzerindeki kullanıcıya yollamak için o ağdaki bilgisayarda geçerli bir kullanıcı ismi ve şifresi gerekmektedir. Birçok FTP sunucusu, kullanıcı ismi ve parola olmadan erişim için "anonim FTP" (anonymous FTP) desteği verir, bu kullanım için kullanıcı adı olarak anonymous parola olarak ise bir [e-mail](https://tr.wikipedia.org/wiki/E-mail) adresi girilmesi gerekmektedir ([Internet Explorer](https://tr.wikipedia.org/wiki/Internet_Explorer), e-mail olarak IEuser@ girer).

FTP, dosya transferi ve komut transferi için değişik [portlar](https://tr.wikipedia.org/wiki/Port) kullanır. Varsayılan konfigürasyonda, komut transferi (yani sisteme giriş, klasör değiştirme, dosya adı değiştirme veya "dosya yolluyorum" komutları) için kullanılan port numarası 21'dir. Dosyalar indirilir veya gönderilirken ise o an boş olan bir port numarası kullanılır.

### FTP RFC959 → [https://tools.ietf.org/html/rfc959](https://tools.ietf.org/html/rfc959)

## OSI Modeli

**Kaynak:** [https://tr.wikipedia.org/wiki/OSI_modeli](https://tr.wikipedia.org/wiki/OSI_modeli)

**Open Systems Interconnection** (**OSI**) modeli ISO ([International Organization for Standardization](https://tr.wikipedia.org/wiki/International_Organization_for_Standardization)) tarafından geliştirimiştir. Bu modelle, ağ farkındalığına sahip cihazlarda çalışan uygulamaların birbirleriyle nasıl iletişim kuracakları tanımlanır.[[1]](https://tr.wikipedia.org/wiki/OSI_modeli#cite_note-a1-1)

İlk OSI standartları 1970'lerin sonlarında ve 1980’lerin başlarında ISO’nun TC 97 ([Technical Committee 97](https://tr.wikipedia.org/w/index.php?title=Technical_Committee_97&action=edit&redlink=1)), Enformasyon İşlemesi tarafından ortaya çıkartılmıştır.[[2]](https://tr.wikipedia.org/wiki/OSI_modeli#cite_note-a3-2) [ISO](<https://tr.wikipedia.org/wiki/ISO_(standart)>), son OSI standardını 1984’te çıkartmıştır.[[3]](https://tr.wikipedia.org/wiki/OSI_modeli#cite_note-a4-3) Bu model kısa sürede kabul görerek yaygınlaşmış ve ağ işlemleri için bir kılavuz olmuştur.

**Open Systems Interconnection** (**OSI**) modeli ISO ([International Organization for Standardization](https://tr.wikipedia.org/wiki/International_Organization_for_Standardization)) tarafından geliştirimiştir. Bu modelle, ağ farkındalığına sahip cihazlarda çalışan uygulamaların birbirleriyle nasıl iletişim kuracakları tanımlanır.[[1]](https://tr.wikipedia.org/wiki/OSI_modeli#cite_note-a1-1)

İlk OSI standartları 1970'lerin sonlarında ve 1980’lerin başlarında ISO’nun TC 97 ([Technical Committee 97](https://tr.wikipedia.org/w/index.php?title=Technical_Committee_97&action=edit&redlink=1)), Enformasyon İşlemesi tarafından ortaya çıkartılmıştır.[[2]](https://tr.wikipedia.org/wiki/OSI_modeli#cite_note-a3-2) [ISO](<https://tr.wikipedia.org/wiki/ISO_(standart)>), son OSI standardını 1984’te çıkartmıştır.[[3]](https://tr.wikipedia.org/wiki/OSI_modeli#cite_note-a4-3) Bu model kısa sürede kabul görerek yaygınlaşmış ve ağ işlemleri için bir kılavuz olmuştur.

![https://upload.wikimedia.org/wikipedia/tr/5/55/OSI_HUN.gif](https://upload.wikimedia.org/wikipedia/tr/5/55/OSI_HUN.gif)

## IETF(Internet Engineering Task Force)

**Kaynak:** [https://tr.wikipedia.org/wiki/İnternet_Mühendisliği_Görev_Gücü](https://tr.wikipedia.org/wiki/%C4%B0nternet_M%C3%BChendisli%C4%9Fi_G%C3%B6rev_G%C3%BCc%C3%BC)

İnternet Mühendisliği Görev Grubu (İng. İngilizce: Internet Engineering Task Force (İngilizce: IETF), İnternet protokollerini geliştiren ve standartlaştıran, resmî statüsü olmayan bir gruptur. IETF'nin çalışmaları ve ürettiği dokümanlar İnternet üzerinden herkese açıktır. Çalışma gruplarına ve toplantılarına katılım için herhangi bir kısıtlama bulunmamaktadır. Toplantılar, genellikle İnternet üzerinden tartışma grupları aracılığıyla sanal olarak yapılmaktadır.

> **RFC Yorumlar İçin Talep** (Orijinal adı: Request For Comments, RFC), TCP/IP nin tanımlanmasında kullanılan standart numaralara sahip dokümanlardır.

### HTTP RFC2616 → [https://tools.ietf.org/html/rfc2616](https://tools.ietf.org/html/rfc2616)

## IP (Internet Protocol)

**Kaynak:** [https://tr.wikipedia.org/wiki/Internet_Protocol](https://tr.wikipedia.org/wiki/Internet_Protocol)

Internet Protocol (IP) ağ sınırları boyunca datagramların geçişi için internet protokolü takımında temel iletişim protokolüdür. Yönlendirme işlevi sayesinde internetin çalışmasını sağlamaktadır. IP, paket teslim görevini paket başlıklarındaki IP adreslerine dayalı olarak kaynak adresten hedef adrese doğru gerçekleştirir. Bu amaçla, IP veri teslim edilecek kapsülleyen bir paket yapıları tanımlamaktadır. Aynı zamanda adresleme yöntemlerini tanımlayan bu metot kaynak ve hedef bilgileri ile diyagramı etiketlemek için kullanılır. IP, 1974 yılında Vint Cerf ve Bob Kahn tarafından orijinal iletim kontrol programında bağlantısız bir datagram hizmeti olarak tanıtıldı. İnternet protokolü paketi bu nedenle sık sık TCP/IP gibi ifade edilir. IP'nin ilk büyük versiyonu İnternet Protokolü Sürüm 4'tür. IPv4 internette baskın olan bir protokoldür. Protokolün halefi ise İnternet Protokolü Sürüm 6 (IPv6)'dır.

### URL RFC1738 → [https://tools.ietf.org/html/rfc1738](https://tools.ietf.org/html/rfc1738)

## Further Reading

**40 maps that explain the internet →** [https://www.vox.com/a/internet-maps](https://www.vox.com/a/internet-maps)

**Türkiye' de İnternet' in 25. Yılı Belgeseli →** [https://www.youtube.com/watch?v=AEXWn-NsmXY](https://www.youtube.com/watch?v=AEXWn-NsmXY)

## TCP (Transmission Control Protocol)

**Kaynak:** [https://tr.wikipedia.org/wiki/TCP](https://tr.wikipedia.org/wiki/TCP)

**TCP (Transmission Control Protocol)**, [TCP/IP protokol takımının](https://tr.wikipedia.org/wiki/TCP/IP_protokol_tak%C4%B1m%C4%B1) aktarım katmanı [protokollerinden](https://tr.wikipedia.org/wiki/Protokol) birisidir. Gelişmiş bilgisayar ağlarında paket anahtarlamalı bilgisayar iletişiminde kayıpsız veri gönderimi sağlayabilmek için TCP protokolü yazılmıştır. [HTTP](https://tr.wikipedia.org/wiki/HTTP), [HTTPS](https://tr.wikipedia.org/wiki/HTTPS), [POP3](https://tr.wikipedia.org/wiki/POP3), [SSH](https://tr.wikipedia.org/wiki/SSH), [SMTP](https://tr.wikipedia.org/wiki/SMTP), [Telnet](https://tr.wikipedia.org/wiki/Telnet) ve [FTP](https://tr.wikipedia.org/wiki/FTP) gibi internet'in kullanıcı açısından en popüler protokollerinin veri iletimi TCP vasıtasıyla yapılır.

## SSH Güvenli Kabuk

**Güvenli Kabuk** (**SSH**), ağ hizmetlerinin güvenli olmayan bir ağ üzerinde güvenli şekilde çalıştırılması için kullanılan bir [kriptografik](https://tr.wikipedia.org/wiki/Kriptografi) [ağ protokolüdür](https://tr.wikipedia.org/wiki/%C4%B0leti%C5%9Fim_protokol%C3%BC).[[1]](https://tr.wikipedia.org/wiki/G%C3%BCvenli_kabuk#cite_note-rfc4251-1) En iyi bilinen örnek uygulaması bilgisayar sistemlerine uzaktan [oturum açmak](https://tr.wikipedia.org/wiki/Oturum_a%C3%A7ma) için olandır.

SSH, bir [SSH istemcisini](https://tr.wikipedia.org/w/index.php?title=SSH_istemcisi&action=edit&redlink=1) bir [SSH sunucusuna](https://tr.wikipedia.org/w/index.php?title=SSH_sunucusu&action=edit&redlink=1) bağlayarak [istemci-sunucu](https://tr.wikipedia.org/wiki/%C4%B0stemci-sunucu) mimarisi çerçevesinde güvenli olmayan bir ağ üzerinde [güvenli kanal](https://tr.wikipedia.org/w/index.php?title=Secure_channel&action=edit&redlink=1) sağlar.[[2]](https://tr.wikipedia.org/wiki/G%C3%BCvenli_kabuk#cite_note-rfc4252-2) Yaygın uygulamalar arasında uzaktan [komut satırı](https://tr.wikipedia.org/wiki/Komut_sat%C4%B1r%C4%B1) [girişi](https://tr.wikipedia.org/wiki/Oturum_a%C3%A7ma) ve uzaktan komut çalıştırma bulunur, ama herhangi bir ağ hizmeti de SSH ile güvenceye alınabilir. Protokol belirtimi [SSH-1](https://tr.wikipedia.org/wiki/G%C3%BCvenli_kabuk#S%C3%BCr%C3%BCm_1.x) ve [SSH-2](https://tr.wikipedia.org/wiki/G%C3%BCvenli_kabuk#S%C3%BCr%C3%BCm_2.x) olarak adlandırılan iki ana sürüm arasında ayrım yapar

```bash
# Asagidaki sekilde baglanti saglanabilir

SSH root@ip
```

## SFTP

Secure FTP (Güvenli Dosya Taşıma Protokolü), yani SFTP, [SSH](https://tr.wikipedia.org/wiki/SSH) kullanarak dosya transferi yapan bir dosya aktarım protokolüdür. [SSH](https://tr.wikipedia.org/wiki/SSH)'ın sağladığı güvenlik özellikleri, [FTP](https://tr.wikipedia.org/wiki/FTP)'den farklı olarak SFTP'yi güvenli hale getirir. [FTP](https://tr.wikipedia.org/wiki/FTP)'nin [RSA](https://tr.wikipedia.org/w/index.php?title=RSA&action=edit&redlink=1) ile güçlendirilmiş halidir. [TCP](https://tr.wikipedia.org/wiki/TCP) üzerinden çalışır.

### SSH ile SFTP Kullanımı

SFTP ile dosya transferi yapabilmek için bir SFTP istemcisine sahip olmak gereklidir. Neredeyse bütün [Linux](https://tr.wikipedia.org/wiki/Linux) dağıtımlarında bir SFTP istemcisi ön tanımlı olarak bulunur. [Windows](https://tr.wikipedia.org/wiki/Microsoft_Windows) işletim sistemlerinde bir SFTP istemcisi edinerek kurmak gerekir.

### SFTP Komutları

- Host ile bağlantı kurma: $sftp

  host_adi

- Oturum açma: $sftp

  kullanici_adi@host_adi

- help: Yardım komutudur. sftp ile kullanılabilecek komutların ve bu komutların işlevlerinin listesini verir.
- put: Host bilgisayara dosya kopyalar.

sftp> put kaynak_dosya_konumu (hedef_konum)

- get: Host bilgisayardan istemci bilgisayara dosya kopyalar.

sftp> get kaynak_dosya_konumu (hedef_konum)

- cd: Host bilgisayarda dizin değiştirme komutu. ([Linux](https://tr.wikipedia.org/wiki/Linux) işletim sistemindeki cd komutunun aynısı.)
- lcd: İstemci bilgisayarda dizin değiştirme komutu.
- rm: Host bilgisayarda dosya silme.
- rmdir: Host bilgisayarda dizin silme.
- chmod: Dosyalara ait kullanıcı izinlerini değiştirmenizi sağlar.

sftp> chmod izin_kodu dosya_konumu

- ls: Host bilgisayarda dizin içeriğini listeleme.
- lls: İstemci bilgisayarda dizin içeriğini listeleme.
- rename: Host bilgisayarda dosya adı değiştirme.

sftp> rename eski_isim yeni_isim

- mkdir: Host bilgisayarda dizin oluşturma.
- lmkdir: İstemci bilgisayada dizin oluşturma.
- Oturum kapatma ve SFTP'den çıkma:sftp> exit sftp> quit sftp>

## SCP

**Kaynak:** [https://www.hosting.com.tr/bilgi-bankasi/scp-nedir/](https://www.hosting.com.tr/bilgi-bankasi/scp-nedir/)

SCP, açılımı Secure Copy Protocol olan ve Güvenli Kopyalama Protokolü anlamına gelen, iki farklı Linux tabanlı bilgisayar veya sunucu arasındaki dosya aktarım aracıdır. FTP alternatifi olarak düşünülebilir. Secure Copy , SSH Protokolünü kullandığı için güvenli bağlantı sağlamaktadır

### **SCP Nasıl Kurulur?**

Linux tabanlı cihazlarda SCP ekli olarak gelmemektedir. Sadece OpenSSH-Client’in kurulu olduğu sistemlerde SCP eklidir.

Aşağıdaki komutlarla SCP Arasını kolayca kurabilirsiniz.

```
root# apt-get install openssh-client -y  (#Debian/Ubuntu)

root# yum install openssh-client -y    (#RHEL/CentOS/Fedora)
```

### SCP Parameterleri Nelerdir?

- p : Hedef dizindeki port bilgilerini girmek için kullanılır.
- q : Transer sırasında gösterilen yüzdelik oranı kapatır ancak işlemi sonlandırmaz, sadece arayüzde göstermez.
- r : Dosyaları kopyalamak için kullanılır.
- C : Transfer sırasında dosyaları sıkıştırarak kopyalama hızını artırır.
- i : Ortak anahtar kimlik doğrulaması veya özel anahtar (ssh key) dosyasını kullanmak için kullanılır.
- l : Bant genişliğini (Bandwidth) limitlendirmek için kullanılabilir. Kbit/s.
- v : Hata ayıklama raporlarını görüntülemek için kullanılır.
- c : Veri transferi sırasında şifreleme yöntemini “-c blowfish cipher” şeklinde değiştirir.

### **SCP ile Dosya Transferi Nasıl Yapılır?**

SCP ile dosya transfer etmek çok kolay! Birkaç örnekle transferin nasıl gerçekleştiğini anlatacağım.

Alt örnekteki komutu kullanarak hedef bilgisayar veya sunucudaki **/bilgi** dizini içerisine **mesaj.txt** adlı dosyayı transfer edebiliriz. Komutu kullandıktan sonra karşı bilgisayar veya sunucunun şifresini isteyecektir.

```
root# scp mesaj.txt root@85.66.123.145:/bilgi/
```

Alt örnekteki komutu kullanarak hedef bilgisayar veya sunucudaki  \***\* **/bilgi/mesaj.txt\*\* adlı dosyayı bulunduğumuz dizine transfer edebiliriz.

```
root# scp root@85.66.123.145:/bilgi/mesaj.txt  .
```

Alt örnekte hedef bilgisayar veya sunucudaki  **/bilgi/mesaj.txt** adlı dosyayı, kendi bilgisayar veya sunucumuzdaki **/bilgi/admin/** dizinine kopyalamak.

**root#** `scp root@5.5.5.5.5:/bilgi/mesaj.txt /bilgi/admin/`

## SOAP

**Kaynak:** [https://tr.wikipedia.org/wiki/SOAP](https://tr.wikipedia.org/wiki/SOAP)

SOAP (Simple Object Access Protocol - Basit Nesne Erişim Protokolü), Service-oriented Architecture felsefesini pratiğe uyarlayan iki interface'den biridir. Üzerinde bulunan Universal Description Discovery and Integration (UDDI) ile birlikte hizmet yönelimli mimarinin pratikte kullanılmasını mümkün kılar.

### Bir SOAP mesajının yapısı

- **Envelope:** Bütün SOAP mesajlarının içinde olduğu elemandır. SOAP mesajına ilişkin XML belgesinin root elemanı olmak zorundadır. Envelope elemanı içinde Body veya Header gibi elemanlar bulunur. Envelope elemanının içinde her zaman bir Body elemanı vardır fakat Header elemanı olmak zorunda değildir. SOAP mimarisine göre eğer Envelope elemanı içinde Header elemanı varsa bu eleman Envelope elemanının içindeki ilk eleman olmalıdır. Soap kullanan mimarilerde kesinlikle erişim protokolü olarak TCP kullanılmalıdır
- **Header :** SOAP mesajlarındaki Header elemanını HTML standartlarında bulunan <Head></Head> etiketlerine benzetebiliriz. Header bölümü metot çağrımı ile doğrudan ilişkili değildir. Header bölümü ile meta-data dediğimizi bilgiler gönderilir.
- **Body:** Body elemanı SOAP mesajının en önemli kısmını oluşturur. Body bölümünde web metodunun adı ve metodun parametrik bilgileri XML formatında gönderilir. Cevap mesajında ise metodun geri dönüş değeri Body bölgesine eklenir. Metodun parametrik yapısının bu şekilde XML formatında yazılmasına SOAP Serialization denir. Son olarak hata mesajlarında ise Body bölümünde hatanın adı ve tanımı gibi bilgiler bulunur.

## Keywords, Tools:

- rsync
- WSDL dosyasi
- jq json
- json blob.com
- telnet
- tracerout

  [https://curl.trillworks.com/](https://curl.trillworks.com/) curl converter
