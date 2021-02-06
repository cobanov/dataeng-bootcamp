# Day 1

## **Modül-1: Data Collection**

**İçerik:** API'lar, loglama, sensory data, web scraping.

**Anahtar sözcükler:** JSON, XML, HTTP, HTML, DOM, grep, RegExp.

**Araçlar:** Postman, log4j, python-logging, BeautifulSoup, Jsoup, Selenium

# Data Toplama

Information retrieval, web-scraping, alınan API dataları bunlara örnektir.

## **API**

İki sistemin arasında nasıl konusacağını belirleyen bir yapıdır. Belirli spesifik tipte akış ve veri sunar. Belirli bir rate içerisinde olmaktadır. Belirli sorgulara karşı belirli bir data parçası geçmektedir, tüm sistemin veri akışını sağlamak için değildir.

> Farklı formatlarda dönüşü olabilir. **.xml** veya **json** olabilir. JSON oldukça popüler, şu an genel akım json üzerinden geçiyor.

Sensörler ufak bilgisayarlar denilebilir, genellikle amaca yönelik sadece görevini yapan pil ömrü yüksek olan mini cihazlardır. Üzerindeki datayı merkeze alınarak kullanılabilir. _Aslında **edgedeki** cihazlardan bahsediliyor._

## **Web Scraping**

Görece API'ye göre verinin elde edilmesi daha zor. Veri genellikle dağınık biçimde web'de bulunur, veri toplama prosesi kullanıcının bu rotaları tanımlayarak gerçekleştirmesiyle sağlanır. Dezavantajı ise belirli bir protokolun olmaması, **_challenging but fun!_**

Değişikliklerde call denilen bir sistem kullanılabilir. İki taraf için yüklü bir sistem olduğundan dolayı istenilen bir yöntem değildir. Bir websitesi için yazılan scraping scriptleri her gün değişmez bu yüzden büyük bir problem yaratmayacaktır. Subscribe yönteminde webhook gibi yöntemler kullanılabilir fakat karşı tarafın da sizi tanıyor olması gerek.

## Loglama

Genellikle problemler belirli bir zaman diliminden itibaren veya geçmişten gelir. Anlık sorunları ve sistemin ne yaptığını en ince detayın kadar görmek için **loglama** kullanılır.

> **Pro Tip:** Her satırın loglanmasının anlamı yoktur. Oldukça dikkat dağıtıcı ve kullanışsız olmaya başlamaktadır. Bunun için loglamanın seviyeleri vardır.

### Loglamanın seviyeleri

Low level, critical, warning, info gibi seviyeler vardır.

- **Debug:** Sorunların teşhisi için debugging gibi düşünebiliriz. Ayrıntılı bilgilere ihtiyacımız vardır.
- **Info:** Beklenen çıktılarımızdır.
- **Warning:** Yazılım hala çalışıyordur ama uyarı çanları çalmaktadır.
- **Error:** Yazılım ciddi bir sorunla karşılaştı ve görevini yerine getiremedi.
- **Critical**: Programın işlevini yerine getiremeyecek bir sorunla karşılaşmasıdır.

> **Pro Tip:** _grep_ komutuyla dosyaların içerisindeki belirli kelimeyi arar. _(e.g. 2 şubat tarihinde bir problem oldu ve onun bulunması için kullanılabilir.)_

### Loglama yaparken:

- **Timestamp:** Tarih, zaman damgası bulunması ve ne zaman olduğuna dair bilgi vermesi açısından önemlidir.
- **Logging Level:** Hatanın derecesi, nedeni veya olayın ne olduğuna dair seviyenin belirtilmesi gerekmektedir.
- **API Bilgisi:** Sensor ID, hangi fonksiyon, genel bilgiler
- **Logun içeriği:** value, logun içeriği json, plain text, xml olabilir.

Logların tek büyük bir dosyada açmak giderek büyüyen dosyadan dolayı mantıklı değildir. Databasede tablo olarak saklanabilir böyle bir durumda select süresi uzamaktadır. Sistemi optimize edebilmek için aktif olanlar veya olmayanlar yahut arşivlenmiş gibi farklı parçalara bölmek zaman açısından yararlı olacaktır.

Güncel datayı optimize tutmak için düşünülmesi gerekmektedir. Bunun için **Hadoop** gibi özelleşmiş sistemler bulunmaktadır. Temelde depolanan ve güncel olarak kullanılan iki parçaya bölmek mantıklı olacaktır.

### Keywords:

- **POSTMAN:** API isteği yapmak için kullanılan bir tooldur.
- **Log4j:**
- **python-logging:**
- **BeautifulSoup:**
- **Jsoup:**
- **Selenium:**

# End of the first day!
