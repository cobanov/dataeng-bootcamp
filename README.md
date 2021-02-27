# Data Engineering Masterclass

<p align="center"> <img src="https://pbs.twimg.com/profile_images/1341352412540530688/EJfGb11W_400x400.jpg"> </img></p>

Bu Repo [Data Engineering Masterclass (DEMC–201)](https://datamasterclass.zeministanbul.ist) eğitiminde verilen derslerin içeriklerini ve notlarını içermektedir.

**Tanım:** Data Engineering Masterclass (DEMC–201) veri odaklı teknolojik ürün geliştirme ekiplerinin veri mühendisliği ihtiyaçları gözetilerek hazırlanmış bir uzmanlık sınıfıdır. Bu uzmanlık sınıfı, data engineering alanında uzun yıllar çalışmış, deneyim sahibi yazılım geliştiriciler, veri mühendisleri, veri bilimcileri ve sistem mühendisleri tarafından hazırlanmıştır.

## Contributors

- Mert Çobanov
- Çağrı Köz

## İçindekiler

| Topic           | Day                                                                         |
| --------------- | --------------------------------------------------------------------------- |
| Data Collection | [Link](https://github.com/cobanov/dataeng-bootcamp#modül-1-data-collection) |
| Data Cleaning   | [Link](https://github.com/cobanov/dataeng-bootcamp#modül-2-data-cleaning)   |

| Files              | Link                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------ |
| Webscraping Script | [.py](https://github.com/cobanov/dataeng-bootcamp/blob/main/homeworks/extractFromVatan.py) |
| AWK Cheatsheet     | [PDF](https://github.com/cobanov/dataeng-bootcamp/blob/main/additional/AWK.pdf)            |

# Modül-1: Data Collection

**İçerik:** API'lar, loglama, sensory data, web scraping.

**Anahtar sözcükler:** JSON, XML, HTTP, HTML, DOM, grep, RegExp.

**Araçlar:** Postman, log4j, python-logging, BeautifulSoup, Jsoup, Selenium

<!-- <details><summary><b>Show Day 1
</b></summary> -->

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

### Keywords:

- **POSTMAN:** API’ları paylaşmak, test etmek, dokümante etmek, monitör etmek için kullanılır. En öne çıkan özelliği tüm bunlar için çok kullanışlı bir arayüz sunmasıdır.
- **Log4j:** Java uygulamalarında kullanılacak loglama kütüphanesidir.
- **python-logging:** Log4j'in python versiyonu
- **BeautifulSoup:** BeautifulSoup, HTML veya XML dosyalarını işlemek için oluşturulmuş bir kütüphanedir.
- **Jsoup:** BS4'un java versiyonu
- **Selenium:** Selenium, bilgisayarınıza yükleyeceğiniz bir driver yardımı ile ekrana chrome, firefox gibi bir tarayıcı açarak, gerçek bir insan gibi istediğiniz tüm işlemleri programlama dili yardımıyla çalıştırmanızı sağlayan bir araçtır.

### End of the first day!

</details>

<!-- <details><summary><b>Show Day 2
</b></summary> -->

## HTTP

“http”, bilginin sunucudan kullanıcıya nasıl ve ne şekilde aktarılacağını gösteren protokoldür. İnternet ağında sunucular ve kullanıcılar arasında nasıl bir veri alışverişi olacağı hakkında kurallar vardır. Bu düzeni sağlayan protokol de HTTP’dir.internet sitesine girmek için adres çubuğuna sitenin adresini yazdığınız vakit HTTP ile sunucuya bir istek gönderilir ve sunucu bu isteğe cevap verdiği vakit internet sitesinin verileri size gelir.

## 🏢 Restful Mimarisi

RESTful servisler veri iletiminde farklı HTTP metotlarını kullanmaktadır. Yapılan HTTP request’i için çağrılan URL ile beraber HTTP method bilgisi bahsi geçen 4 metottan biri olarak seçilir ve sunucu yapılan talebin kayıt üzerine nasıl etki edeceğini buna göre belirler.

**GET:** Veri listeleme - veri görüntülemek için kullanılır.

**POST:** Veri eklemek için kullanılır.

### Diğer Metodlar

- **PUT:** Veriyi Güncelleme isteği olarak kullanılır.
- **PATCH:** Verinin sadece bir parçasını güncellemek için kullanılır. Örneğin bir issue'nun durumunun aktiften çözüldü haline getirilmesi.
- **DELETE:** Veriyi silmek için kullanılır.
- **OPTIONS:** Bir  api urline Options isteği yapıldığında o url in hangi istekleri kabul ettiği bilgisi verilir.

[httpbin.org](http://httpbin.org) sitesinden bu denemeler yapılabilir

## HTTP Status kodları

Kodlara linkten ulaşılabilir. [https://www.argenova.com.tr/http-durum-ve-hata-kodlari](https://www.argenova.com.tr/http-durum-ve-hata-kodlari)

### En sık karşılaşılan hata kodları

- **HTTP 200 (OK):** yanıtın başarılı olduğunu gösterir. Yani, istemci ile sunucu arasındaki iletişim herhangi bir hata olmadan sorunsuz bir şekilde yürütülmüştür.
- **HTTP 404 (Not Found):** istenen kaynağın sunucu tarafından bulunamayacağı anlamına gelir. Bu, geçici bir aksaklıktan kaynaklanıyor olabilir ve gelecekte başka bir istekte bulunulursa kaynak kullanılabilir olabilir. Çoğunlukla, 404'e götüren bağlantılara genellikle bozuk bağlantılar denir.
- **HTTP 502 (Bad Gateway):** sunucunun proxy olarak hareket ederken istekte bulunurken sunucudan geçersiz bir yanıt aldığını gösterir.

## 🥌 CURL

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

ipify.org

[https://api.ipify.org?format=json&param=2](https://api.ipify.org/?format=json&param=2)

### URL içerisindeki özel karakterler

- **"?":** "sorgu parametreleri" olarak adlandırılır. Sunucu, bu ek bilgilere dinamik olarak cevap verebilir ve göreceğiniz sayfayı bu parametrelere göre oluşturabilir. Bu, sayfadaki bir alana otomatik olarak yazılmış bir bilgi veya bir arama motorundaki arama sorgunuz olabilir.
- **"%":** "Escaping" olarak adlandırılan bu işlem, URL'deki boşluk karakterinin soruna yol açmaması için alternatif bir biçime dönüştürülmesidir. Örneğin + yazdığınızda bu karakter, %3F ile değiştirilir.
- **"=":** anahtar-değer çiftlerini temsil eder. Anahtar-değer çiftine bir örnek, sayfa=4 olabilir. Burada "sayfa" anahtar, "4" ise değerdir.

## 🚀 GREP

Elimizdeki loglarda buradan terminal ekranında hızlıca sorgularımız getirebiliriz. Logların güzel şekilde tutulması işimizi kolaylaştırıyor. Pipe ile çok daha etkin kullanım yöntemleri mevcut.

grep "42.236.10.125" \* —color | wc -lw

### 📚 Ders Örnekleri:

grep "GET" \* —color

grep "42.236.10.125" \* —color | wc -lw

grep "mozilla" \* —color

## 🌲 DOM

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

## 🐍 Python Web Scraping

### Logging

**Kaynak**: [https://medium.com/@umut.boz/python-logging-a8fdd36fee7](https://medium.com/@umut.boz/python-logging-a8fdd36fee7)

Loglama, bir sistemdeki hareketliliği kaydetmek için kullanılan yapıdır. Python standart kütüphanesi içinde loglama için çok güçlü bir kütüphane barındırır. Bu kütüphane ile geliştirdiğimiz programlarda hata ayıklamak aynı zamanda ifadeleri yazdırmak için loglama kullanabiliriz.

### Requests

**Kaynak**: [https://medium.com/python/python-requests-modülü-4af79ebdb8c8](https://medium.com/python/python-requests-mod%C3%BCl%C3%BC-4af79ebdb8c8)

Python, standart modüllerinin yanında harici yüzlerce kullanışlı modül ile birlikte çok güçlü bir dil. Bu gücü veren harika modüller var bunlardan biri de **Requests modülü.**

Bu modül ile web üzerindeki isteklerinizi yöneteceksiniz. Mesela bu modül ile API entpointlerine PUT, DELETE, POST gibi istekler atabilirsiniz.

### BeautifulSoup4

**Kaynak**: [https://medium.com/@nuriyavuz2.71/python-beautifulsoup-modülü-689ef499ee16](https://medium.com/@nuriyavuz2.71/python-beautifulsoup-mod%C3%BCl%C3%BC-689ef499ee16)

BeautifulSoup, HTML veya XML dosyalarını işlemek için oluşturulmuş güçlü ve hızlı bir kütüphanedir.

Bu modül ile bir kaynak içerisindeki HTML kodlarını parse edip,botlar yazabiliriz.

### Selenium

**Kaynak**: [https://www.sinanerdinc.com/python-selenium-modulu-kullanimi-1](https://www.sinanerdinc.com/python-selenium-modulu-kullanimi-1)

Selenium, bilgisayarınıza yükleyeceğiniz bir driver yardımı ile ekrana chrome, firefox gibi bir tarayıcı açarak, gerçek bir insan gibi istediğiniz tüm işlemleri programlama dili yardımıyla çalıştırmanızı sağlayan bir araçtır.

**Homework:** Vatan bilgisayardaki ürünlerin görsellerin veya isimleri ile ücretlerini scrap edebilirsin.

**Ödev Linki:** [https://github.com/cobanov/dataeng-bootcamp/blob/main/homeworks/scraping_homework.py](https://github.com/cobanov/dataeng-bootcamp/blob/main/homeworks/scraping_homework.py)

### 🔗 **GISTLER:**

- **BS4**: [https://gist.github.com/sirin/695abacaa207ad7af20f18c946d19858](https://gist.github.com/sirin/695abacaa207ad7af20f18c946d19858)
- **Selenium**: [https://gist.github.com/sirin/0e1491163b8f485a476e0991ad228b86](https://gist.github.com/sirin/0e1491163b8f485a476e0991ad228b86)
</details>

---

# Modül-2: Data Cleaning

**İçerik:** Parsing, Duplicate Elimination, Ensuring Quality: Validity-Accuracy-Completeness, Statistical Analysis, Unix-Linux Terminal

**Anahtar sözcükler:** Bash, GNU Awk, GNU sed, jq, CSV files, JSON

**Araçlar:** Shell(s), Excel, R
<!-- 
<details><summary><b>Show Day 3
</b></summary> -->
# Modul 2 - Day 3

## **Modül-2: Data Cleaning**

**İçerik:** Parsing, Duplicate Elimination, Ensuring Quality: Validity-Accuracy-Completeness, Statistical Analysis, Unix-Linux Terminal

**Anahtar sözcükler:** Bash, GNU Awk, GNU sed, jq, CSV files, JSON

**Araçlar:** Shell(s), Excel, R

# Data Quality

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

### 1000 karakter uzunluğundan fazla olan satırlar

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

netflix datasetinde country birden fazla film cekmıs yonetmenler vs.

csv ve tsv formatlarını ekle

json örnek sitesi:

<!-- </details> -->

---

# Modül-3: Data Storage

**İçerik:** SQL, Relational Databases, Document Databases, Time Series Databases, Graph Databases, Key-value Stores, Data Lakes

**Anahtar sözcükler:** SQL Query, Index, Database normalization, Database optimization, Designing Data Infrastructure

**Araçlar:** MySQL, MariaDB, PostgreSQL, Redis, MongoDB, Neo4J

<!-- <details><summary><b>Show Day 5
</b></summary> -->
# Modul 3 - Day 1

## Veritabanları (Databases)

Veri tabanları birbirleriyle ilişkili bilgilerin depolandığı alanlardır. Bilgi artışıyla birlikte bilgisayarda bilgi depolama ve bilgiye erişim konularında yeni yöntemlere ihtiyaç duyulmuştur. Veri tabanları; büyük miktardaki bilgileri depolamada geleneksel yöntem olan ‘‘dosya-işlem sistemine’’ alternatif olarak geliştirilmiştir.

### İlişkisel Veritabanları (Relational Databases)

**MySQL:** Çoklu iş parçacıklı (multi-threaded), çok kullanıcılı (multi-user), hızlı ve sağlam (robust) bir veri tabanı yönetim sistemidir.

**PostgreSQL**, veritabanları için ilişkisel modeli kullanan ve [SQL](https://tr.wikipedia.org/wiki/SQL) standart sorgu dilini destekleyen bir [veritabanı yönetim sistemidir](https://tr.wikipedia.org/wiki/Veritaban%C4%B1_y%C3%B6netim_sistemi). PostgreSQL aynı zamanda iyi performans veren, güvenli ve geniş özellikleri olan bir [Veri Tabanı Yönetim Sistemi](https://tr.wikipedia.org/wiki/Veri_Taban%C4%B1_Y%C3%B6netim_Sistemi)'dir. PostgreSQL ücretsiz ve açık kodludur.

**MariaDB** [ilişkisel veritabanı sistemi](https://tr.wikipedia.org/wiki/%C4%B0li%C5%9Fkisel_veri_taban%C4%B1_y%C3%B6netim_sistemi) olan [MySQL](https://tr.wikipedia.org/wiki/MySQL)'in kaynak kodundan türemiş, [GNU Genel Kamu Lisansı](https://tr.wikipedia.org/wiki/GNU_Genel_Kamu_Lisans%C4%B1) altında dağıtılarak ücretsiz olarak kullanılabilen, geliştirilmesi ve bakımı topluluk tarafından sürdürülen veritabanıdır. MySQL, önde gelen [açık kaynaklı](https://tr.wikipedia.org/wiki/A%C3%A7%C4%B1k_kaynak) yazılım sistemi olarak ticari bir şirket olan [Oracle](https://tr.wikipedia.org/wiki/Oracle) tarafından satın alındıktan sonra MySQL'in ilk geliştiricileri tarafından Monty AB çatısı altında yine açık kaynak olarak MariaDB adıyla yola devam edeceği duyurulmuş ve oldukça ilgi görmüştür.

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

**\*Kaynak**: [http://www.ilterismutlu.com/yatay-vs-dikey-olceklenebilirlik-horizontally-vs-vertically-scalable-scalability/](http://www.ilterismutlu.com/yatay-vs-dikey-olceklenebilirlik-horizontally-vs-vertically-scalable-scalability/)\*

**Dikey Ölçeklenebilirlik Nedir ?**

Sistemin/Veritabanının Dikeyde ölçeklenebilir olması (dikey ölçeklenebilirlik, vertically scalable, scale up); bir tane çok güçlü aynı zamanda pahalı bir makine/donanım kullanılmasıdır. Dikey Ölçeklenebilir sistemlerde donanım kısıtları mevcuttur. Örneğin mevcut sisteminizin CPU frekansını 5 ghz yapamazsınız veya 1 tb ram yapamazsınız.

Yatay ölçeklenebilirlikte yüzlerce, binlerce makinelik server (sunucu) ağı kurulabilir. Yatay ölçeklenebilirliğin yönetimi dikey ölçeklenebilirliğe göre daha zordur.Sonuçta onlarca veya yüzlerce makinayı yönetmek, tabi ki tek bir makinayı yönetmekten daha zordur.

**Yatay Ölçeklenebilirlik Nedir ?**

Sistemin/Veritabanının Yatayda ölçeklenebilir olması (horizontally scalable, scale out); ucuz ve çok sayıda makinenin aynı anda kullanılması anlamına gelir. Yatay ölçeklenebilirlik sayesinde yedeklilik de performans artışı da sağlanabilir.

## ACID

**\*Kaynak:** [https://medium.com/cloud-and-servers/acid-nedir-53f729f2bbb2](https://medium.com/cloud-and-servers/acid-nedir-53f729f2bbb2)\*

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

**Consistency(Tutarlılık) :** Transaction işlemi sonucunda veritabanındaki verinin geçerli durumunun, bir sonraki geçerli duruma geçmesidir. Özetle Transaction tam anlamı ile gerçekleşinceye kadar (constraints, cascades, triggers) işlemden etkilenen verilerin değerlerinin bir önceki geçerli değeri vermesidir.

**Isolation:** Aynı anda aynı veri üzerinde birden fazla Transaction değiştirme gereksinimi olabilir. Transaction’ların birbirlerinin işlemlerinden etkilenmemesi için işlemler Seri olarak yapılması gerekir. Transaction sırasında ilgili ve etkilenecek veri setleri kilitlenir. Taki işlem başarılı ve başarısız olarak sonuç dönünceye kadar.

**Durability(Dayanıklılık):** Transaction sırasında fiziksel veya işlemsel bir hata olması durumunda sistemin kendisini bir önceki geçerli veri durumuna döndürebilme kabiliyetidir.

### **Veritabanı Normalleştirmesi**

**\*Kaynak:** [https://www.lifeacode.com/sql-dersleri/rdbms-nedir.html](https://www.lifeacode.com/sql-dersleri/rdbms-nedir.html)\*

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

**\*Kaynak:** [https://www.beyaz.net/tr/guvenlik/makaleler/onbellege_alma_caching_nedir.html](https://www.beyaz.net/tr/guvenlik/makaleler/onbellege_alma_caching_nedir.html)\*

Önbellek, geçici bir veri alt kümesini depolayan yüksek hızlı veri depolama katmanıdır. Önbelleğe alma, daha önce alınan veya hesaplanan verinin verimli bir şekilde yeniden kullanılmasını sağlar. Önbellekleme yöntemi ile ilgili verilerin sonraki süreçte talep edildiğinde, verilere birincil depolama konumundan erişildiği için daha yüksek bir performans elde edilir.

Bir önbellekteki veriler genellikle RAM gibi donanımlarlarda saklanır ve veriye erişmek için bir yazılım üzerinden bağlantı kurulması gerekebilir. Önbelleğe alma işleminin amacı altta bulunan yavaş depolama katmanına erişme gereksinimini mimumuma indirerek veri erişim performansını arttırmaktır.

**Önbelleğe Alma Sisteminin Faydaları:** Uygulama performansı arttırılır.Veritabanı maliyeti düşürülür.Arka uçtaki yük azaltılır.Tahmin edilebilir performans sağlanır.Veritabanı bağlantı noktaları ortadan kaldırılır.Okuma verimini arttırır.

**Veritabanı (Database) Önbelleğe Alma**

Web uygulamasında kullanılan veritabanının hız ve verimlilik performansı, web uygulamasının performansı için büyük bir etkendir. Veritabanının önbelleğe alınması, uygulama performansını etkileyen arka uç veritabanlarından veri alışveriş sonucu doğacak gecikmelerin azaltılmasını sağlar.

<!-- </details> -->
